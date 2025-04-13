import plotly.express as px
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])
fig.write_html('chart.html')