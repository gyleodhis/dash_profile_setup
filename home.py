from dash import dash,html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG],
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server
app.title = 'Dennis'

app.layout = html.Div(className='container-fluid',children=[
	html.Div(className='navbar navbar-expand-lg navbar-dark bg-primary',children=[
		html.A('Dennis Profile',className='navbar-brand'),
		html.Button(className='navbar-toggler',type='button', **{'data-bs-toggle': 'collapse','data-bs-target':'#navbarColor01',
                    'aria-controls':'navbarColor01','aria-expanded':'false','aria-label':'Toggle navigation'},children=[
                    html.Span(className='navbar-toggler-icon')]),
		html.Div(className='collapse navbar-collapse',id='navbarColor01',children=[
			html.Ul(className='navbar-nav me-auto',children=[
				html.Li(className='nav-item',children=[
					html.A('Home',className='nav-link active',href='#')]),
				html.Li(className='nav-item',children=[
					html.A('About',className='nav-link',href='#')])
				]
				),
			html.Form(className='d-flex',children=[
				dcc.Input(className='form-control me-sm-2',type='text',placeholder='Search'),
				html.Button('Search',className='btn btn-secondary my-2 my-sm-0',type='submit')])
			])
		]),
	html.Div(className='horizontalgap',style={'height':'10px'}),
	html.Div(className='row',children=[
		html.Div(className='card text-white bg-success col-md-3',children=[
			html.Div('Data Science',className='card-header'),
			html.Div(className='card-body',children=[
				html.H4('Machine Learning',className='card-title'),
				html.P('ML engineer from Kenya',className='card-text')])]),
		html.Div(className='card text-white bg-danger col-md-3',children=[
			html.Div('Data Visualization',className='card-header'),
			html.Div(className='card-body',children=[
				html.H4('Creating Data Visuals',className='card-title'),
				html.P('Visualization expert',className='card-text')])]),
		html.Div(className='card text-white bg-warning col-md-3',children=[
			html.Div('Qlik Sense',className='card-header'),
			html.Div(className='card-body',children=[
				html.H4('Qlik Expert',className='card-title'),
				html.P('Building dashboards',className='card-text')])]),
		html.Div(className='card text-white bg-success col-md-3',children=[
			html.Div('Power BI',className='card-header'),
			html.Div(className='card-body',children=[
				html.H4('Power BI Expert',className='card-title'),
				html.P('Power BI expert',className='card-text')])])]),
	html.Div(className='horizontalgap',style={'height':'10px'}),
	html.Div(className='row',children=[
		html.Div(className='col-md-6 card',children=[
		html.Div('First Dahboard Here',className='card-header'),
		html.Div(className='card-body',children=[
			html.H4('Put dashboard here')])
		]),
		html.Div(className='col-md-6 card',children=[
		html.Div('Second Dahboard Here',className='card-header'),
		html.Div(className='card-body',children=[
			html.H4('Put dashboard here')])
		]),
		html.Div(className='col-md-6 card',children=[
		html.Div('Third Dahboard Here',className='card-header'),
		html.Div(className='card-body',children=[
			html.H4('Put dashboard here')])
		]),
		html.Div(className='col-md-6 card',children=[
		html.Div('Fourth Dahboard Here',className='card-header'),
		html.Div(className='card-body',children=[
			html.H4('Put dashboard here')])
		])
		])
	])

if __name__ == '__main__':
    app.run_server(debug=True,port=3031)