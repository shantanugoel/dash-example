import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1
import config

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(1, id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
      return app1.layout
    elif pathname == '/':
      return app.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(host=config.HOST_IP,
                   port=config.PORT,
                   debug=config.DEBUG_FLAG)
