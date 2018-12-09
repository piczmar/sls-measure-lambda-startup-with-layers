import plotly.plotly as py
import plotly.graph_objs as go
# import plotly.figure_factory as FF
#
# import numpy as np
# import pandas as pd
#
# df = pd.read_csv('sample-data.csv')
#
# sample_data_table = FF.create_table(df.head())
# py.offline.plot(sample_data_table)
#
#

import plotly
import plotly.graph_objs as go
import pandas as pd
import plotly.figure_factory as FF

df = pd.read_csv('sample-data.csv')
sample_data_table = FF.create_table(df.head())

# plotly.offline.plot({
#   "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#   "layout": go.Layout(title="hello world")
# }, auto_open=True)


plotly.offline.plot(sample_data_table)


trace1 = go.Scatter(
    x=df['x'], y=df['logx'], # Data
    mode='lines', name='logx' # Additional options
)
trace2 = go.Scatter(x=df['x'], y=df['sinx'], mode='lines', name='sinx' )
trace3 = go.Scatter(x=df['x'], y=df['cosx'], mode='lines', name='cosx')

layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
plotly.offline.plot(fig, filename='simple-plot-from-csv.html')