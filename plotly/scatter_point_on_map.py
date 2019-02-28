import numpy as np
# from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
# print (__version__) # requires version >= 1.9.0

#Always run this the command before at the start of notebook
init_notebook_mode(connected=True)
import plotly.graph_objs as go

x=np.array([2, 5, 8, 0, 2, -8, 4, 3, 1])
y=np.array([2, 5, 8, 0, 2, -8, 4, 3, 1])


data = [go.Scatter(x=x,y=y)]
fig = go.Figure(
        data=data,layout=go.Layout(
            title='Offline Plotly Testing',width=800,height=500,
            xaxis=dict(title='X-axis'),
            yaxis=dict(title='Y-axis')))


plot(fig,show_link = False)




# import plotly.graph_objs as go

# # mapbox_access_token = 'ADD_YOUR_TOKEN_HERE'
#
# data = [
#     go.Scattermapbox(
#         lat=['45.5017'],
#         lon=['-73.5673'],
#         mode='markers',
#         marker=dict(
#             size=14
#         ),
#         text=['Montreal'],
#     )
# ]
#
# layout = go.Layout(
#     autosize=True,
#     hovermode='closest',
#     mapbox=dict(
#         # accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=45,
#             lon=-73
#         ),
#         pitch=0,
#         zoom=5
#     ),
# )
#
# fig = dict(data=data, layout=layout)
#
# py.iplot(fig, filename='Montreal Mapbox')