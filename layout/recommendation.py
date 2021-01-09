import dash_table
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_table.Format import Format
import dash_table.FormatTemplate as FormatTemplate


def get_recommendation_layout(tasted_table, table, weights_table):
    recommendation_layout = [
        dbc.Row(
            children=[
                html.P('Utility:'),
                dbc.Col(
                    dash_table.DataTable(
                        id='table',
                        columns=[{'id': 'beer', 'name': 'beer'},
                                 {'id': 'style', 'name': 'style'},
                                 {'id': 'utility', 'name': 'utility', 'type': 'numeric', 'format': Format(precision=2)},
                                 {'id': 'tasted', 'name': 'tasted'},
                                 {'id': 'abv', 'name': 'abv', 'type': 'numeric',
                                  'format': FormatTemplate.percentage(1)},
                                 {'id': 'hoppy', 'name': 'hoppy', 'type': 'numeric'},
                                 {'id': 'malty', 'name': 'malty', 'type': 'numeric'},
                                 {'id': 'sour', 'name': 'sour', 'type': 'numeric'},
                                 {'id': 'floral', 'name': 'floral', 'type': 'numeric'},
                                 {'id': 'fruit', 'name': 'fruit', 'type': 'numeric'},
                                 {'id': 'sweet', 'name': 'sweet', 'type': 'numeric'},
                                 {'id': 'smooth', 'name': 'smooth', 'type': 'numeric'},
                                 {'id': 'bitter', 'name': 'bitter', 'type': 'numeric'},
                                 {'id': 'buy', 'name': 'beer52', 'type': 'text', 'presentation': 'markdown'}
                                 ],
                        data=table.to_dict('records'),
                        style_cell_conditional=[
                            {
                                'if': {'column_id': 'beer'},
                                'textAlign': 'left',
                            },
                        ],
                        style_data_conditional=[
                            {
                                'if': {
                                    'column_id': 'tasted',
                                    'filter_query': '{tasted} eq "yes"'
                                },
                                'backgroundColor': '#E9ECEF',
                                'fontWeight': 'bold',

                            }
                        ]
                    ), md=12
                )
            ],
            className='mb-3'
        ),
        dbc.Row(
            children=[
                html.P('Preference weights:'),
                dbc.Col(
                    dash_table.DataTable(
                        id='weight',
                        columns=[{'id': col, 'name': col, 'type': 'numeric', 'format': Format(precision=2)} for col in
                                 weights_table.columns],
                        data=weights_table.to_dict('records')
                    ), md=12
                )
            ]
        )
    ]
    return recommendation_layout
