import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1
from components.header import make_header
from components.sidebar import make_sidebar
import config

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        make_header(),
        html.Div(
            dbc.Row(
                [
                    make_sidebar(),
                    html.Main(
                        html.Div(id='page-content',
                                 className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"),
                        className="col-md-9 ml-sm-auto col-lg-10 px-4",
                    )
                ]
            ),
            className="container-fluid",
        ),
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
      return app1.layout
    elif pathname == '/':
      return "Hello!\n" * 10000
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(host=config.HOST_IP,
                   port=config.PORT,
                   debug=config.DEBUG_FLAG)
