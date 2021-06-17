import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

logo_image = '/assets/img/ml4b.png'

preference_data = {'preferences': [], 'tasted': []}

nav_links = dbc.Row(
    children=[
            dbc.Col(dbc.NavLink("Shuffle", id='shuffle-link', href="#", className='nav_link')),
    ],
    id='nav-items',
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=logo_image, height="34px", className='ml-2')),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(nav_links, id="navbar-collapse", navbar=True),
    ],
    color='#fff'
)

main_layout = html.Div(
    children=[
        dcc.Location(
            id='url',
            refresh=False
        ),
        navbar,
        dbc.Container(
            children=[],
            id='page_content',
            className="mt-4",
        ),
        html.Div(
            id='hidden_data',
            style={'display': 'none'}
        ),
        html.Div(
            id='preference_data',
            style={'display': 'none'}
        )
    ]
)
