from datetime import datetime

import pandas as pd
import plotly
import plotly.figure_factory as FF
import plotly.graph_objs as go

src = 'no-layer-cold.txt'


def dateparse(time_in_millis):
  return datetime.fromtimestamp(float(time_in_millis) / 1000.0)


df = pd.read_csv(src, delim_whitespace=True, parse_dates=[1],
                 date_parser=dateparse, index_col=False,
                 names=['Duration', 'Timestamp'], header=None)

df.sort_values(by=['Timestamp'], inplace=True)
print(df.columns.tolist())

sample_data_table = FF.create_table(df.head())
plotly.offline.plot(sample_data_table)

trace1 = go.Scatter(
    x=df['Timestamp'], y=df['Duration'],
    mode='lines', name='No layer (cold)'
)

layout = go.Layout(title='Lambda startup times',
                   plot_bgcolor='rgb(230, 230,230)')
fig = go.Figure(data=[trace1], layout=layout)
plotly.offline.plot(fig, filename='dynamodb-data.html')
