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

				dcc.Tab(children= tab_single, label= 'Single Request'),
				dcc.Tab(children= tab_batch, label= 'Batch request')
			]
		),

	])
])