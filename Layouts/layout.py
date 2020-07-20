import dash
import dash_core_components as dcc
import dash_html_components as html
from Layouts.tab2_layout import tab_batch
from Layouts.tab1_layout import tab_single
import dash_table

Columns= [
	"age", "workclass", "fnlwgt", "education",
    "education-num", "marital-status", "occupation",
    "relationship", "race", "sex", "capital-gain",
    "capital-loss", "hours-per-week", "native-country"
]

Types= [
	'number', 'text', 'number', 'text',
	'number', 'text', 'text', 'text',
	'text', 'text', 'number', 'number',
	'number', 'text'
]

layout_main = html.Div(children= [
	html.Center(children=[
		dcc.Tabs(
			id= 'tab-select',
			children= [

				dcc.Tab(children= [

					html.Div(children= [
						html.Center(children=[

							html.H3("Enter details for a prediction"),

							html.Br(),

							html.Div(children= [

								html.Div(children= [
									html.H6('Enter data - {}'.format(col)),

									dcc.Input(
										id= 'input_{}'.format(col),
										type= typ,
										placeholder= 'input {}'.format(col),
									),

									html.Br(),
									html.Br()
								])
								for typ,col in zip(Types,Columns)
								if col not in ["fnlwgt","education-num"]
							]),

							html.Div(children= [
								html.Button('Submit', id= 'submit', n_clicks= 0)
							]),

							html.Br(),

							html.H6('Output from the classifier'),

							html.H5(id= 'output-text', style= {'whieSpace':'pre-line'})
						])
					])

				], label= 'Single Request'),
				dcc.Tab(children= [
					html.Div(children= [
						html.Center(children=[
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

							    html.Div(id= 'uploaded-file')
							])
						])
					])
				], label= 'Batch request')
			]
		),

	])
])