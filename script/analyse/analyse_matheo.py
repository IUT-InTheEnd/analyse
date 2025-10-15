import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("./cleaned_dataset/clean_genres.csv")
df = df.dropna(subset=['genre_title'])
df['#tracks'] = df['#tracks'].fillna(0)
df['genre_parent_id'] = df['genre_parent_id'].fillna(0).astype(int)

milieu = {'genre_id': 'root','genre_title': 'Hierarchy of genres of music','genre_parent_id': np.nan,'#tracks': 0}
df = pd.concat([pd.DataFrame([milieu]), df], ignore_index=True)
df['genre_parent_id'] = df['genre_parent_id'].replace(0, 'root')

graph = px.sunburst(
    df,
    ids="genre_id",
    names="genre_title",
    parents="genre_parent_id",
    values="#tracks",
    color="#tracks",
    color_continuous_scale="YlGn",
    title="Hierarchy of genres of music with their tracks",
)
graph.update_traces(textinfo="label+value",texttemplate="%{label}",hovertemplate="<b>%{label}</b><br>%{value} tracks<br>",maxdepth=3)
graph.update_layout(margin=dict(t=50, l=0, r=0, b=0))
graph.show()