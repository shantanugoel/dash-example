import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

def make_sidebar():
  return dbc.Nav(
    html.Div(
      "Link",
      className="sidebar-sticky"
    ),
    className="col-md-2 d-none d-md-block bg-light sidebar",
  )
