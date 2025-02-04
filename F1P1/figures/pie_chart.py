import plotly.graph_objects as go

labels = ['1st author','2nd author','3rd author','other']
values = [4, 7, 2, 5]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

#fig.write_image("fig1.svg")
