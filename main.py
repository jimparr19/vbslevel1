import dash

from config import THEME

app = dash.Dash(__name__, external_stylesheets=[THEME])
app.title = 'VBSPBL'
app.config.suppress_callback_exceptions = True
