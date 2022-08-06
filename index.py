# import dash
from dash import dash,html, dcc
from charts import *
from _datetime import datetime as dt
#import my_functions as mf
from about import profile_page
#from covid import covid_vax_page
#from climate import carbon_page
# import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
# from climate_data import fig_top_emitter_by_year,emission_by_continent

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server
app.title = 'Kevogo'

app.layout = html.Div(className='wrapper hold-transition sidebar-mini layout-navbar-fixed', children=[
    dcc.Location(id='url', refresh=False),
    html.Div(className="main-header navbar navbar-expand navbar-dark",
        # Left navbar links
        children=[
            html.Ul(className="navbar-nav",
                    children=[
                        html.Li(className='nav-item',
                                children=[
                                    html.A(className='nav-link', href='#', **{'data-bs-toggle': 'collapse','data-bs-target':'#navbarColor01',
                                                                              'aria-controls':'navbarColor01','aria-expanded':'true','aria-label':'Toggle navigation'}, role='button',
                                           children=[html.I(className='fas fa-bars')])
                                ]),
                        html.Li(className='nav-item d-sm-inline-block',
                                children=[
                                    html.A('Home', className='nav-link', href='/')
                                ]),
                        html.Li(className='nav-item d-sm-inline-block',
                                children=[
                                    html.A('Profile', className='nav-link', href='/profile')
                                ])
                    ]),
            html.Form(className='form-inline ml-3', children=[
                html.Div(
                    className='input-group input-group-sm', children=[
                        dcc.Input(className='form-control form-control-navbar', type='search',
                                  placeholder='Search'),
                        html.Div(className='input-group-append',
                                 children=[
                                     html.Button(className='btn btn-navbar', type='submit',
                                                 children=html.I(className='fas fa-search'))
                                 ])
                    ])
            ])
        ]),
    # Main Sidebar Container
    html.Aside(className='main-sidebar sidebar-dark-primary elevation-4',
               # Logo container
               children=[
                   html.Div(className='sidebar',
                            children=[
                                html.Div(className='user-panel mt-3 pb-3 mb-3 d-flex',
                                         children=[
                                             html.Div(className='image',
                                                      children=[
                                                          html.Img(className='img-circle elevation-2', alt='Dennis',
                                                                   src='assets/img/denis.jpg')
                                                      ]),
                                             html.Div(className='info',
                                                      children=[
                                                          html.A('Dennis', className='d-block',
                                                                 href='#',
                                                                 target='_blank')
                                                      ])
                                         ]),
                                # Sidebar Menu
                                html.Div(className='mt-2',
                                         children=[
                                             html.Ul(className='nav nav-pills nav-sidebar flex-column', role='menu',
                                                     **{'data-widget': 'treeview', 'data-accordion': 'false'},
                                                     children=[
                                                         html.Li(className='nav-item has-treeview menu-open',
                                                                 children=[
                                                                     html.A(className='nav-link active', href='/',
                                                                            children=[
                                                                                html.I(
                                                                                    className='nav-icon fas fa-globe-africa text-success'),
                                                                                html.P(children=['Home'])
                                                                            ])
                                                                 ])
                                                     ])
                                         ])
                            ])
               ]),
    # Content Wrapper. Contains page content
    html.Div(className='content-wrapper',
             # Content Header (Page header)
             children=[
                 html.Div(id='page-content')
             ]),
    html.Footer(className='main-footer', children=[
        html.Strong('Dennis Kevogo')
    ])
])

covid_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Covid 19 Tracker: ' + str(dt.date(dt.now())))
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Covid', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-3', children=[
                ]),
                html.Div(className='col-md-12', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-info', children=[
                                html.Div(className='inner', children=[
                                    html.H4('New Cases')
                                ]),
                                html.A('Africa: %s' %round(func_continent()['new_cases'].sum()), className='small-box-footer', href='#'),
                                # html.A(func_continent()['new_cases'].sum(), className='small-box-footer', href='#')
                                html.A('Worldwide: %s' % round(df_covid_data['new_cases'].sum()),className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4('Positivity Rate')
                                ]),
                                html.Div(className='icon', children=[
                                    html.I(className='ion ion-bars')
                                ]),
                                html.A('Africa: %s' %round(func_continent()['positive_rate'].mean(), 2), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s' % round(df_covid_data['positive_rate'].mean(),2),className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4('Total Death')
                                ]),
                                html.Div(className='icon', children=[
                                    html.I(className='ion ion-pie-graph')
                                ]),
                                html.A('Africa: %s' %round(func_continent()['new_deaths'].sum()), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s' % round(df_covid_data['new_deaths'].sum()),className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-warning', children=[
                                html.Div(className='inner', children=[
                                    html.H5('Patients in ICU')
                                ]),
                                html.Div(className='icon', children=[
                                    html.I(className='ion ion-bag')
                                ]),
                                html.A('Africa: %s' %round(func_continent()['icu_patients'].sum()), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s' % round(df_covid_data['icu_patients'].sum()),className='small-box-footer', href='#')
                            ])
                        ])
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('N. America', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent()['new_cases'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('New Cases Today')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((round(
                                                    func_continent()['new_cases'].sum() / df_global_data[
                                                        'new_cases'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar(), config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='asia', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent('Asia')['new_cases'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('Asia New Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((round(
                                                    func_continent('Asia')['new_cases'].sum() / df_global_data[
                                                        'new_cases'].sum(),
                                                    2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar('Asia'), config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='europe', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent('Europe')['new_cases'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('Europe New Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((round(
                                                    func_continent('Europe')['new_cases'].sum() / df_global_data[
                                                        'new_cases'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar('Europe'), config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='namerica', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent('North America')['new_cases'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('N. America New Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((round(
                                                    func_continent('North America')['new_cases'].sum() / df_global_data[
                                                        'new_cases'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar('North America'), config=config)
                                    ])])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top Countries in Vaccinations', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_vax', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia_vax',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe_vax',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('N.America', className='nav-link',
                                                                                      href='#namerica_vax',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent()['new_vaccinations'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('New Vaccinations Today')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str(
                                                    (round(func_continent()['new_vaccinations'].sum() / df_global_data[
                                                        'new_vaccinations'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % to the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie(),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent('Asia')['new_vaccinations'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('Asia New Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent('Asia')['new_vaccinations'].sum() / df_global_data[
                                                        'new_vaccinations'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie('Asia'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent('Europe')['new_vaccinations'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('Europe New Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent('Europe')['new_vaccinations'].sum() / df_global_data[
                                                        'new_vaccinations'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie('Europe'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(func_continent('North America')['new_vaccinations'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('N. America New Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent('North America')['new_vaccinations'].sum() /
                                                    df_global_data['new_vaccinations'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph',
                                                  figure=fig_pie('North America'),config=config)
                                    ])
                                ])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Positivity Rate', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_pst_rate', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia_pst_rate',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe_pst_rate',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('N.America', className='nav-link',
                                                                                      href='#namerica_pst_rate',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    (func_continent()['positive_rate'].dropna(how='any').mean()) * 100,
                                                    2),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((round(
                                                    func_continent()['positive_rate'].sum() / df_global_data[
                                                        'positive_rate'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel(),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round((func_continent('Asia')['positive_rate'].dropna(
                                                    how='any').mean()) * 100,2),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((round(
                                                    func_continent('Asia')['positive_rate'].sum() / df_global_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel('Asia'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round((func_continent('Europe')['positive_rate'].dropna(
                                                    how='any').mean()) * 100,2),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((round(
                                                    func_continent('Europe')['positive_rate'].sum() / df_global_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel('Europe'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round((func_continent('North America')['positive_rate'].dropna(
                                                    how='any').mean()) * 100,2),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((round(
                                                    func_continent('North America')['positive_rate'].sum() /
                                                    df_global_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph',
                                                  figure=fig_funnel('North America'),
                                                  config=config)
                                    ])
                                ]),
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Vaccinations Per 100 Persons', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_vax_100', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia_vax_100',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe_vax_100',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('N.America', className='nav-link',
                                                                                      href='#namerica_vax_100',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    func_continent()['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Avg Vaccination Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent()['people_vaccinated_per_hundred'].sum() /
                                                    df_global_data[
                                                        'people_vaccinated_per_hundred'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-down')
                                            ]),
                                            html.Span('Africas % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel_vaccine(),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    func_continent('Asia')['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('Asia Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent('Asia')['people_vaccinated_per_hundred'].sum() /
                                                    df_global_data[
                                                        'people_vaccinated_per_hundred'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_funnel_vaccine('Asia'), config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    func_continent('Europe')['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('Europe Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent('Europe')['people_vaccinated_per_hundred'].sum() /
                                                    df_global_data[
                                                        'people_vaccinated_per_hundred'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_funnel_vaccine('Europe'), config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    func_continent('North America')[
                                                        'people_vaccinated_per_hundred'].dropna(how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('N. America Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    func_continent('North America')[
                                                        'people_vaccinated_per_hundred'].sum() / df_global_data[
                                                        'people_vaccinated_per_hundred'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_funnel_vaccine('North America'),
                                                  config=config)
                                    ])
                                ])
                            ]),
                        ])
                    ])
                ])
            ])
        ])
    ])

])



@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return covid_page
    elif pathname == '/profile':
        return profile_page


if __name__ == '__main__':
    app.run_server(port=3000)
