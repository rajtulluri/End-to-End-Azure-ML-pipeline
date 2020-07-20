import dash
import dash_core_components as dcc
import dash_html_components as html

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


tab_single = html.Div(children= [
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