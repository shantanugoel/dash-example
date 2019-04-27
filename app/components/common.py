import dash_html_components as html
import dash_bootstrap_components as dbc

def make_header():
    return dbc.NavbarSimple(
      brand="My Dashboard",
      brand_href="/",
      color="primary",
      dark=True,
    )
