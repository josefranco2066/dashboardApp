import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
        ],
        brand="MIO Dash",
        color="primary",
        dark=True,
    )
    return navbar