import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
  __name__,
  external_stylesheets=[dbc.themes.FLATLY],
  meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
  ]
)
server = app.server
app.config.suppress_callback_exceptions = True
