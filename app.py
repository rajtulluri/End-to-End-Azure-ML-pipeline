import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import urllib
from Layouts.layout import layout_main
from Layouts.tab1_layout import tab_single, Columns
from Layouts.tab2_layout import tab_batch
import json
import base64
import datetime
import io
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets= external_stylesheets)
server = app.server
app.layout = layout_main


"""
Utility functions
"""

def correct_input(features):
	"""
	Builds entire data row as per the dataset by filling in
	some columns.

	parameter:
		features: List, input list of data

	returns:
		features: List, output list with insertions
	"""
	features.insert(2,0)
	features.insert(4,0)
	features.append('?')

	return features

def build_packet(features):
	"""
	Builds packet and requests with data passed using assigned URL and API key.

	parameters:
		features: List, input list of data

	returns:
		req: Request object
	"""

	data= {
		"Inputs":{
			"input1":{
				"ColumnNames":[
					"age", "workclass", "fnlwgt", "education",
				    "education-num", "marital-status", "occupation",
				    "relationship", "race", "sex", "capital-gain",
				    "capital-loss", "hours-per-week", "native-country", "income"
				],
				"Values":[features]
			}
		},
		"GlobalParameters":{}
	}
	body = str.encode(json.dumps(data))

	url = "https://ussouthcentral.services.azureml.net/workspaces/d3987bf891554ed48a30ee0cb1e4ac01/services/60cb1919f8fc466f8ef1030352807ac0/execute?api-version=2.0&details=true "
	api_key = "C36R9Tj6f6oueqtZasbgFO+SX4MZHIts7bYKaaPrqaNpZzCEyWyBOty1FDNCsnIFXP6FkD/h23TuGTVr6ej1Tw=="
	headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

	req = urllib.request.Request(url, body, headers)

	return req

def post_request(request):
	"""
	Post request created earlier.

	parameters:
		request: Request object

	returns:
		result: result from request
	"""

	try:
		response = urllib.request.urlopen(request)
		result = response.read()
		result = json.loads(result)["Results"]["output1"]["value"]["Values"]
		return "Salary category predicted: {}".format(result[0][0])

	except urllib.error.HTTPError as error:
		print("The request failed with status code: " + str(error.code))
		print(error.info())
		print(json.loads(error.read()))
		return json.loads(error.read())

"""
Callback functions
"""


@app.callback(
	Output('output-text','children'),
	[Input('submit', 'n_clicks')],
	[State('input_{}'.format(col), 'value') for col in Columns if col not in ["fnlwgt","education-num"]]

)
def model_prediction(clicks, *features):
	"""
	Requests API for single predictions and reverts with predicted output.

	paramters:
		n_clicks: int, number of clicks on button

		*features: List of arguments, input data from html components
	"""

	features = correct_input([x for x in features])
	request = build_packet(features)

	response = post_request(request)

	return response


@app.callback(
	Output('uploaded-file', 'children'),
    [Input('upload-data', 'contents')]
)
def update_output(str_contents):
	"""
	Read uploaded file data into a dataframe.

	parameters: 
		list_of_contents: String, file contents in a string format

	returns:
		dataTab: data table object, to view dataset with predicted value.
	"""
	string = str_contents.split(',')[1]
	decoded = base64.b64decode(string)
	df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
	df['predicted_label'] = ""
	print('Here')
	for ind,row in df.iterrows():
		row.income= '?'
		request = build_packet(list(row.values[:-1]))
		response = post_request(request)
		df.loc[ind, 'predicted_label'] = response

	return [
		dash_table.DataTable(
			id= 'table',
			columns= [{"name":x, 'id':x} for x in (df.columns)],
			data= df.to_dict('records')
		)
	]



"""
Main code
"""


if __name__ == '__main__':

	app.title = 'ML API app'
	app.config.suppress_callback_exceptions = True
	server.config.suppress_callback_exceptions = True
	app.run_server(debug=True, host= '127.0.0.1',port=5000)
