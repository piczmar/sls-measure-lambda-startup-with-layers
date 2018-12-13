import pandas as pd
import plotly as py
import plotly.graph_objs as go

no_layer_cold = 'nolayer-cold.txt'
layer_cold = 'layer-cold.txt'
no_layer = 'nolayer-hot.txt'
layer = 'layer-hot.txt'

no_layer_cold_df = pd.read_csv(no_layer_cold, delim_whitespace=True,
                               names=['Duration', 'Timestamp'], header=None)
layer_cold_df = pd.read_csv(layer_cold, delim_whitespace=True,
                            names=['Duration', 'Timestamp'], header=None)
no_layer_df = pd.read_csv(no_layer, delim_whitespace=True,
                          names=['Duration', 'Timestamp'], header=None)
layer_df = pd.read_csv(layer, delim_whitespace=True,
                       names=['Duration', 'Timestamp'], header=None)

no_layer_cold_duration = no_layer_cold_df['Duration'].values.tolist()
no_layer_hot_duration = no_layer_df['Duration'].values.tolist()
layer_cold_duration = layer_cold_df['Duration'].values.tolist()
layer_hot_duration = layer_df['Duration'].values.tolist()

trace_nol_cold = go.Box(
    y=no_layer_cold_duration,
    name='No Layer (cold)',
    boxpoints='all',
    jitter=0.3,
    marker=dict(
        color='rgb(214,12,140)',
    ),
)
trace_nol_hot = go.Box(
    y=no_layer_hot_duration,
    name='No Layer (hot)',
    boxpoints='all',
    jitter=0.3,
    marker=dict(
        color='rgb(0,12,140)',
    ),
)
trace_l_cold = go.Box(
    y=layer_cold_duration,
    name='Layer (cold)',
    boxpoints='all',
    jitter=0.3,
    marker=dict(
        color='rgb(225,0,0)',
    ),
)
trace_l_hot = go.Box(
    y=layer_hot_duration,
    name='Layer (hot)',
    boxpoints='all',
    jitter=0.3,
    marker=dict(
        color='rgb(0,0,255)',
    ),
)
layout = go.Layout(
    width=1000,
    yaxis=dict(
        title='Comparing Lambda startup times',
        zeroline=False
    ),
)

data = [trace_nol_cold, trace_nol_hot, trace_l_cold, trace_l_hot]
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='boxes-plot.html')
