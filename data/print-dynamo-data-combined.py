from datetime import datetime

import pandas as pd
import plotly
import plotly.graph_objs as go

no_layer_cold = 'no-layer-cold.txt'
layer_cold = 'layer-cold.txt'
no_layer = 'no-layer.txt'
layer = 'layer.txt'


def dateparse(time_in_millis):
  return datetime.fromtimestamp(float(time_in_millis) / 1000.0)


no_layer_cold_df = pd.read_csv(no_layer_cold, delim_whitespace=True,
                               parse_dates=[1], date_parser=dateparse,
                               index_col=False, names=['Duration', 'Timestamp'],
                               header=None)
no_layer_cold_df.sort_values(by=['Timestamp'], inplace=True)

layer_cold_df = pd.read_csv(layer_cold, delim_whitespace=True, parse_dates=[1],
                            date_parser=dateparse, index_col=False,
                            names=['Duration', 'Timestamp'], header=None)
layer_cold_df.sort_values(by=['Timestamp'], inplace=True)

no_layer_df = pd.read_csv(no_layer, delim_whitespace=True, parse_dates=[1],
                          date_parser=dateparse, index_col=False,
                          names=['Duration', 'Timestamp'], header=None)
no_layer_df.sort_values(by=['Timestamp'], inplace=True)

layer_df = pd.read_csv(layer, delim_whitespace=True, parse_dates=[1],
                       date_parser=dateparse, index_col=False,
                       names=['Duration', 'Timestamp'], header=None)
layer_df.sort_values(by=['Timestamp'], inplace=True)

# sample_data_table = FF.create_table(no_layer_cold_df.head())
# plotly.offline.plot(sample_data_table)

trace_no_layer_cold = go.Scatter(
    x=no_layer_cold_df['Timestamp'], y=no_layer_cold_df['Duration'],
    mode='markers', name='No layer (cold)'
)
trace_layer_cold = go.Scatter(
    x=layer_cold_df['Timestamp'], y=layer_cold_df['Duration'],
    mode='markers', name='Layer (cold)'
)

trace_no_layer = go.Scatter(
    x=no_layer_df['Timestamp'], y=layer_cold_df['Duration'],
    mode='markers', name='No layer'
)

trace_layer = go.Scatter(
    x=layer_df['Timestamp'], y=layer_cold_df['Duration'],
    mode='markers', name='Layer'
)

layout = go.Layout(title='Comparing Lambda startup times',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(
  data=[trace_no_layer_cold, trace_layer_cold, trace_no_layer, trace_layer],
  layout=layout)
plotly.offline.plot(fig, filename='dynamodb-data.html')

