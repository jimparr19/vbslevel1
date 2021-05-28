import dash_table
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_table.Format import Format
import dash_table.FormatTemplate as FormatTemplate


def get_recommendation_layout(tasted_table, table, weights_table):
    recommendation_layout = [
        dbc.Row(
            children=[
                html.P('Personalised ranking of beers available at Beer52:'),
                dbc.Col(
                    dash_table.DataTable(
                        id='table',
                        style_cell={
                            'whiteSpace': 'normal',
                            'height': 'auto',
                        },
                        columns=[{'id': 'Style', 'name': 'Style'},
                                 {'id': 'Category', 'name': 'Category'},
                                 {'id': 'utility', 'name': 'utility', 'type': 'numeric', 'format': Format(precision=2)},
                                 {'id': 'tasted', 'name': 'tasted'},
                                 {'id': 'ABVAvg', 'name': 'ABVAvg', 'type': 'numeric',
                                  'format': FormatTemplate.percentage(1)},
                                 {'id': 'IBUAvg', 'name': 'IBUAvg', 'type': 'numeric', 'format': Format(precision=2)},
                                 {'id': 'SRMAvg', 'name': 'SRMAvg', 'type': 'numeric', 'format': Format(precision=2)},
                                 {'id': 'ADF(%)', 'name': 'ADF(%)', 'type': 'numeric',
                                  'format': FormatTemplate.percentage(1)},
                                 {'id': 'FGAvg', 'name': 'FGAvg', 'type': 'numeric', 'format': Format(precision=4)},
                                 {'id': 'RelativeBitterness', 'name': 'RelativeBitterness', 'type': 'numeric',
                                  'format': Format(precision=2)},
                                 {'id': 'Link', 'name': 'Link', 'type': 'text', 'presentation': 'markdown'}
                                 ],
                        data=table.to_dict('records'),
                        style_cell_conditional=[
                            {
                                'if': {'column_id': 'Style'},
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

                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} lt 4'
                                },
                                'backgroundColor': '#E8D77D',
                                'color': '#E8D77D',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 4 && {SRMAvg} lt 5'
                                },
                                'backgroundColor': '#DCB332',
                                'color': '#DCB332',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 5 && {SRMAvg} lt 7'
                                },
                                'backgroundColor': '#D6A531',
                                'color': '#D6A531',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 7 && {SRMAvg} lt 9'
                                },
                                'backgroundColor': '#C98B28',
                                'color': '#C98B28',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 9 && {SRMAvg} lt 13'
                                },
                                'backgroundColor': '#BC752C',
                                'color': '#BC752C',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 13 && {SRMAvg} lt 17'
                                },
                                'backgroundColor': '#A85629',
                                'color': '#A85629',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 17 && {SRMAvg} lt 22'
                                },
                                'backgroundColor': '#994320',
                                'color': '#994320',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 22 && {SRMAvg} lt 27'
                                },
                                'backgroundColor': '#812C1E',
                                'color': '#812C1E',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 27 && {SRMAvg} lt 34'
                                },
                                'backgroundColor': '#671F12',
                                'color': '#671F12',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 34 && {SRMAvg} lt 44'
                                },
                                'backgroundColor': '#4D0D0F',
                                'color': '#4D0D0F',
                            },
                            {
                                'if': {
                                    'column_id': 'SRMAvg',
                                    'filter_query': '{SRMAvg} ge 44'
                                },
                                'backgroundColor': '#2C0E0F',
                                'color': '#2C0E0F',
                            }
                        ],
                        css=[
                            {
                                'selector': 'table',
                                'rule': 'width: 100%;'
                            }
                        ],
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
                        data=weights_table.to_dict('records'),
                        css=[
                            {
                                'selector': 'table',
                                'rule': 'width: 100%;'
                            }
                        ],
                    ), md=12
                )
            ]
        )
    ]
    return recommendation_layout
