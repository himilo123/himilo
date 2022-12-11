import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('data.csv')

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)


# styling the sidebar
SIDEBAR_STYLE1 = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
SIDEBAR_STYLE2 = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE1 = {
    "margin-left": "18rem",
    "margin-right": "18rem",
    "padding": "2rem 1rem",
}

CONTENT_STYLE2 = {
    "margin-right": "18rem",
    "margin-left": "2rem",
    "padding": "2rem 1rem",
}


sidebar1 = html.Div(
    [
        html.H6("Himilo Solutions  ", className="display-12",xs=12, sm=12, md=12, lg=4, xl=4),

        html.H6("himilo@hotmail.com", className="display-12",xs=12, sm=12, md=12, lg=4, xl=4),

        html.H6("+252634220384", className="display-12",xs=12, sm=12, md=12, lg=4, xl=4),
        html.Hr(),
        html.P(
            "Eelections in Udub Era ", className="lead",xs=12, sm=12, md=12, lg=4, xl=4
        ),
        dbc.Nav(
            [
                dbc.NavLink("2003_Presidential_Elections", href="/", active="exact",xs=12, sm=12, md=12, lg=4, xl=4),
                dbc.NavLink("2005_Parliamentary_Elections", href="/page-1", active="exact",xs=12, sm=12, md=12, lg=4, xl=4),
                dbc.NavLink("2010_Presidential_Elections", href="/page-2", active="exact",xs=12, sm=12, md=12, lg=4, xl=4),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE1,
)
sidebar2 = html.Div(
    [
        html.H6("Himilo Solutions  ", className="display-12",xs=12, sm=12, md=12, lg=4, xl=4),

        html.H6("himilo@hotmail.com", className="display-12",xs=12, sm=12, md=12, lg=4, xl=4),

        html.H6("+252634220384", className="display-12",xs=12, sm=12, md=12, lg=4, xl=4),
        html.Hr(),
        html.P(
            "Eelections in Wadani Era", className="lead",xs=12, sm=12, md=12, lg=4, xl=4
        ),
        dbc.Nav(
            [
                dbc.NavLink("2017_Presidential_Elections", href="/page-3", active="exact",xs=12, sm=12, md=12, lg=4, xl=4),
                dbc.NavLink("2021_Parliamentary_Elections", href="/page-4", active="exact",xs=12, sm=12, md=12, lg=4, xl=4),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE2,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE1,xs=12, sm=12, md=12, lg=4, xl=4)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar1,sidebar2,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H3('Somaliland Elections ',
                        style={'textAlign':'center'}),

                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Regions',
                         y=['Ucid2003','Kulmiye2003','Udub2003']))
                ]
    elif pathname == "/page-1":
        return [
            html.H1('Somaliland Elections ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Regions',
                                    y=['Ucid2005', 'Kulmiye2005', 'Udub2005']))
                ]
    elif pathname == "/page-2":
        return [
            html.H1('Somaliland Elections ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Regions',
                                    y=['Ucid2010', 'Kulmiye2010', 'Udub2010']))
                ]

    elif pathname == "/page-3":
        return [
            html.H1('Somaliland Elections  ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Regions',
                                    y=['Ucid2017', 'Kulmiye2017', 'Wadani2017']))
        ]
    elif pathname == "/page-4":
        return [
            html.H1('Somaliland Elections  ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Regions',
                                    y=['Ucid2021', 'Kulmiye2021', 'Wadani2021']))

        ]
    elif pathname == "/page-5":
        return [
            html.H1('Somaliland Elections  ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Publish-time',
                    y='Comments', color='Description'))
        ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


app.run(host='0.0.0.0')

server = app.server
