"""
Layout file for the server.
Contains HTML layout for the app file to render.
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from Layouts.tab2_layout import tab_batch
from Layouts.tab1_layout import tab_single
import dash_table

"""
Main layout variable
"""

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