import dash_bootstrap_components as dbc
import dash_html_components as html

def make_header():
  return dbc.Nav(
    html.A(
      "Dashboard",
      href="/",
      className="navbar-brand col-sm-3 col-md-2 mr-0"
    ),
    className="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow"
  )
