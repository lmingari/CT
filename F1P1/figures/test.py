import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'author':  ['1st','2nd','3rd','other'], 
    'author3': ['1st+2nd+3rd','1st+2nd+3rd','1st+2nd+3rd',None],
    'author2': ['1st+2nd','1st+2nd',None,None],
    'author1': ['1st',None,None,None],
    'pubs':   [4,7,2,5]
    })

print(df)

fig = px.sunburst(df, path=['author1','author2','author3','author'], values='pubs')


#data = dict(
#    character = ['1st author','2nd author','3rd author','other','1st+2nd author'],
#    parent    = ["", "", "", "","1st author"],
#    value     = [4, 7, 2, 5,11])
#
#fig = px.sunburst(
#    data,
#    names='character',
#    parents='parent',
#    values='value',
#)
fig.show()
