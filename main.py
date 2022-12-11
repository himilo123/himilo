import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('sm.csv')

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport",
         "content": "width=device-width, initial-scale=1.0, maximum-scale=2, minimum-scale=0.5"}
    ],
)


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Himilo-Solutions", className="display-4"),
        html.Hr(),
        html.P(
            "Facbook Post Statistics", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Impressions", href="/", active="exact"),
                dbc.NavLink("People_Reached", href="/page-1", active="exact"),
                dbc.NavLink("Engagements", href="/page-2", active="exact"),
                dbc.NavLink("Shares", href="/page-3", active="exact"),
                dbc.NavLink("Likes", href="/page-4", active="exact"),
                dbc.NavLink("Comments", href="/page-5", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Social Media ',style={'textAlign':'center'},xs=12, sm=12, md=12, lg=4, xl=4),
                dcc.Graph(id='bargraph',figure=px.bar(df, barmode='group', x='Publish-time',
                         y='Impressions',color='Description'))
                ]
    elif pathname == "/page-1":
        return [
            html.H1('Social Media',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Publish-time',
                                    y='People_Reached', color='Description'))
                ]
    elif pathname == "/page-2":
        return [
                html.H1('Social Media ',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Publish-time',
                         y='Engagements',color = 'Description'))
                ]

    elif pathname == "/page-3":
        return [
            html.H1('Social Media ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Publish-time',
                    y='Shares', color='Description'))
        ]
    elif pathname == "/page-4":
        return [
            html.H1('Social Media ',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Publish-time',
                    y='Likes', color='Description'))
        ]
    elif pathname == "/page-5":
        return [
            html.H1('Social Media ',
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
