import dash
import dash_core_components as dcc
import dash_html_components as html

tab_batch = html.Div(children= [
	html.Center(children=[
		html.H3('Submit file for prediction'),

		html.Br(),

		html.Div(children= [
			dcc.Upload(
		        id= 'upload-data',
		        children= html.Div([
		            'Drag and Drop or ',
		            html.A('Select Files')
		        ]),
		        style={
		            'width': '80%',
		            'height': '60px',
		            'lineHeight': '60px',
		            'borderWidth': '1px',
		            'borderStyle': 'dashed',
		            'borderRadius': '5px',
		            'textAlign': 'center',
		            'margin': '10px'
		        }
		    ),

		    html.Br(),

		    html.H6('Uploaded dataset is shown below, along with the predicted output as a column'),

		    html.Div(id= 'uploaded-file')
		])
	])
])