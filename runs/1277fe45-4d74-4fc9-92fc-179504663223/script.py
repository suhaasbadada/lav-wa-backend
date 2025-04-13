import plotly.graph_objects as go
fig = go.Figure(data=[go.Surface(z=[[1,2],[3,4]])])
fig.write_html('chart.html')