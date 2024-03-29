from dash import html
import os

profile_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Profile')
                ]),
                html.Div(className='col-sm-6',children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('My Profile', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid',children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-3', children=[
                    # Profile Image
                    html.Div(className='card card-primary card-outline', children=[
                        html.Div(className='card-body box-profile', children=[
                            html.Div(className='text-center', children=[
                                html.Img(className='profile-user-img img-fluid img-circle', src='assets/img/denis.jpg',
                                         alt='Profile picture')
                            ]),
                            html.H3('Denis Kevogo', className='profile-username text-center'),
                            html.P('Data Leader - Smart International', className='text-muted text-center'),
                            html.Ul(className='list-group list-group-unbordered mb-3', children=[
                                html.Li(className='list-group-item', children=[
                                    html.B('Twitter'),
                                    html.A('300', className='float-right')
                                ]),
                                html.Li(className='list-group-item', children=[
                                    html.B('LinkedIn'),
                                    html.A('+1000', className='float-right')
                                ]),
                                html.Li(className='list-group-item', children=[
                                    html.B('Github'),
                                    html.A('12', className='float-right')
                                ])
                            ]),
                        ]) # card body
                    ]), #card
                    # About Me Box
                    html.Div(className='card card-primary', children=[
                        html.Div(className='card-header', children=[
                            html.H3('About Me', className='card-title')
                        ]),
                    # card-header
                        html.Div(className='card-body',children=[
                            html.Strong(children=[
                                html.I(className='fas fa-book mr-1'), ' Education'
                            ]),
                            html.P('B.S. in Acturial Science - Maseno University',
                                   className='text-muted'),
                            html.Hr(),
                            html.Strong(children=[
                                html.I(className='fas fa-map-marker-alt mr-1'), ' Location'
                            ]),
                            html.P('Nairobi, Kenya',
                                   className='text-muted'),
                            html.Hr(),
                            html.Strong(children=[
                                html.I(className='fas fa-pencil-alt mr-1'), ' Skills'
                            ]),
                            html.P(className='text-muted', children=[
                                html.Span('Data Science ', className='tag tag-success'),
                                html.Span('Machine Learning ', className='tag tag-success'),
                                html.Span('Data Engineering ', className='tag tag-success'),
                                html.Span('Apache Spark ', className='tag tag-success'),
                                html.Span('ETL ', className='tag tag-info'),
                                html.Span('Big Data ', className='tag tag-success'),
                                html.Span('Python ', className='tag tag-info'),
                                html.Span('Qlik Sense ', className='tag tag-info')
                            ]),
                            html.Hr(),
                            html.Strong(children=[
                                html.I(className='fas fa-envelope-open-text mr-1'), ' Contact'
                            ]),
                            html.P(className='text-muted', children=[
                                html.Span('denniskevogo2017@gmail.com ', className='tag tag-info')
                            ])
                        ]) #card-body
                    ]) #Card
                ]), #Col-md-3
                html.Div(className='col-md-9',children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header p-2',children=[
                            html.Ul(className='nav nav-pills',children=[
                                html.Li(className='nav-item',children=[
                                    html.A('Activity', className='nav-link active',href='#activity', **{'data-toggle': 'tab'})
                                ])
                            ])
                        ]),
                        html.Div(className='card-body',children=[
                            html.Div(className='tab-content', children=[
                                html.Div(className='active tab-pane', id="activity", children=[
                                    # Posts
                                    html.Div(className='post', children=[
                                        html.Div(className='user-block', children=[
                                            html.Img(className='img-circle img-bordered-sm', src='assets/img/kenya.png', alt='image'),
                                            html.Span(className='username', children=[
                                                html.A('Machine Learning on Kenyan Marriage',
                                                       href='https://nbviewer.jupyter.org/github/gyleodhis/Modelling-Mariage-Issues-in-Kenya-Using-Random-Forest/blob/master/random-forest.ipynb', target='_blank'),
                                                html.A(className='float-right btn-tool', href='#', children=[
                                                    html.I(className='fas fa-minus')
                                                ])
                                            ]),
                                            html.Span('Shared publicly on 15th March 2019', className='description')
                                        ]),
                                        html.P('In this project I seek to model features that contribute to extra marital '
                                               'affairs in Kenya and why couples engage in extra marital affairs.')
                                    ]),
                                    html.Div(className='post clearfix', children=[
                                        html.Div(className='user-block', children=[
                                            html.Img(className='img-circle img-bordered-sm', src='assets/img/movie.jpg', alt='movie image'),
                                            html.Span(className='username', children=[
                                                html.A('Apache Spark Movie Recommender System',
                                                       href='https://nbviewer.jupyter.org/github/gyleodhis/apacheSpark-Recommender-System/blob/master/main.ipynb', target='_blank'),
                                                html.A(className='float-right btn-tool', href='#', children=[
                                                    html.I(className='fas fa-minus')
                                                ])
                                            ]),
                                            html.Span('Shared publicly on 27th March 2019', className='description')
                                        ]),
                                        html.P('A simple collaborative filtering based recommender system in PySpark '
                                               'using the ALS method to recommend movies to the users')
                                    ]),
                                    html.Div(className='post', children=[
                                        html.Div(className='user-block', children=[
                                            html.Img(className='img-circle img-bordered-sm', src='assets/img/nasa.jpg', alt='nasa image'),
                                            html.Span(className='username', children=[
                                                html.A('Server Log Analysis With Apache Spark',
                                                       href='https://nbviewer.jupyter.org/github/gyleodhis/log-analysis/blob/master/logs.ipynb', target='_blank'),
                                                html.A(className='float-right btn-tool', href='#', children=[
                                                    html.I(className='fas fa-minus')
                                                ])
                                            ]),
                                            html.Span('Shared publicly on 28th July 2020', className='description')
                                        ]),
                                        html.P('Server logs contain a lot of information, but due to its nature and '
                                               'vastness its rarely analysed. This code I analyze two months NASA logs '
                                               'to find insights such us: intruition detection, daily requests per host, '
                                               'Hosts that return 404, top error end points and sites leading on forbided requests.')
                                    ]),
                                    html.Div(className='post', children=[
                                        html.Div(className='user-block', children=[
                                            html.Img(className='img-circle img-bordered-sm', src='assets/img/loan.jpg', alt='bank image'),
                                            html.Span(className='username', children=[
                                                html.A('Potential of Defaulting a loan by a customer',
                                                       href='https://nbviewer.jupyter.org/github/gyleodhis/Loan-defaulting-prediction/blob/master/Predicting%20Loan%20defaulting.ipynb', target='_blank'),
                                                html.A(className='float-right btn-tool', href='#', children=[
                                                    html.I(className='fas fa-minus')
                                                ])
                                            ]),
                                            html.Span('Shared publicly on 22nd April 2020', className='description')
                                        ]),
                                        html.P('Can we train a model to help us predict whether a loan applicant has the '
                                               'possibility of defaulting our loan as a bank or SME and what are the red '
                                               'flags that we should always look at when considering loan issuance.')
                                    ]),
                                    html.Div(className='post', children=[
                                        html.Div(className='user-block', children=[
                                            html.Img(className='img-circle img-bordered-sm', src='assets/img/afcon.jpg', alt='afcon image'),
                                            html.Span(className='username', children=[
                                                html.A('2019 African Cup of Nations',
                                                       href='https://nbviewer.jupyter.org/github/gyleodhis/afcon2019/blob/master/Afcon2019.ipynb', target='_blank'),
                                                html.A(className='float-right btn-tool', href='#', children=[
                                                    html.I(className='fas fa-minus')
                                                ])
                                            ]),
                                            html.Span('Shared publicly on 24th June 2020', className='description')
                                        ]),
                                        html.P('In this code I streamed 44K tweets about the AFCON2019 from twitter live as it '
                                               'was twitted. I did not have any goal in mind just trying to find what twitter '
                                               'users were talking about.')
                                    ]),
                                    html.Div(className='post', children=[
                                        html.Div(className='user-block', children=[
                                            html.Img(className='img-circle img-bordered-sm', src='assets/img/kenya.png', alt='image'),
                                            html.Span(className='username', children=[
                                                html.A('2019 Mental Health Bill',
                                                       href='https://nbviewer.jupyter.org/github/gyleodhis/mental-Health/blob/master/%23MentalHealthBIllKenya.ipynb', target='_blank'),
                                                html.A(className='float-right btn-tool', href='#', children=[
                                                    html.I(className='fas fa-minus')
                                                ])
                                            ]),
                                            html.Span('Shared publicly on 19th May 2019', className='description')
                                        ]),
                                        html.P('Just a lazy afternoon mining tweets concerning the then tabled mental '
                                               'health bill tabled to Kenyan parliament after Several dull incidences '
                                               'in relation to mental health. '
                                               'The bill was meant to make mental health act more protective of the most '
                                               'vulnerable; women and youth. The analysis below is how kenyans reacted '
                                               'to it on twitter.')
                                    ])])
                        ])
                    ])
                ])
            ])
            ])
        ])
    ])])