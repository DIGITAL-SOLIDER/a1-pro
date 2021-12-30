import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("csvpro.csv")

sdf = df.loc[df["student_id"]=="TRL_xsl"]

mean = sdf.groupby(["level","student_id"],as_index=False)["attempt"].mean()

fig = px.scatter(mean,x="student_id", y="level", color="attempt", size="attempt")
fig.show()