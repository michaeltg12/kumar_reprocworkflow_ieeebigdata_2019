import plotly
import plotly.io as plio
import plotly.graph_objs as go
import pandas as pd

dqrdata = pd.read_csv("radflux_dqr_reproc_per_year.txt", index_col=0)

traceslist = dqrdata.columns.tolist()
numinstruments = len(dqrdata.index)
dqrcount = dqrdata.sum(axis=1)

print(traceslist)
print(dqrdata.index)

#print(dqrdata.index)

# Create a function that will create as many traces for us as we need
def tracing(column):
   trace = go.Bar(
         x = dqrdata.index,
         y = dqrdata[column],
         # Parameters above specify what you would see if hover on any column
         name = column,
		 text=dqrdata[column][dqrdata.index],
		 #text=column,
         #text=dqrdata[column][dqrdata.index],
         textposition='auto',
         hoverinfo="x+y")
   return trace
# Create data
data = []
# Fill out data with our traces
#for i in range(len(traceslist)):
for i in range(len(traceslist)-1):
   eachtrace = tracing(traceslist[i])
   data.append(eachtrace)
# Optional: create layout
layout = go.Layout(
      # Set title to plot
      title = "Data Quality Reports for RADFLUX Instruments",
      font = dict(size=36, color="#330000"),
	  xaxis = dict(title = "Year", nticks=len(dqrdata.index), ticktext=list(dqrdata.index), tickvals=list(dqrdata.index), titlefont=dict(size=48, color="#330000")),
	  yaxis = dict(title = "Number of DQRs", titlefont=dict(size=48, color="#330000")),
	  paper_bgcolor='rgb(255,255,255)', # background color
	  plot_bgcolor='rgb(255,255,255)', # background color
      # Choose one of the barmode below and comment another
      barmode="stack",
      #barmode="group"
      )
# Create figure with all we need to plot
fig = go.Figure(data=data, layout=layout)
# Use offline plot without connection to plotly site
plotly.offline.plot(fig, filename='radflux_reproc_by_year.html')

#plio.write_image(fig, file="sorted_dqr_by_instrument_20.png")

print(dqrdata.iloc[1,:])
print(dqrdata.iloc[2,:])
dqrdata.fillna(0)
print(dqrdata.iloc[2,:])
print("Number of instruments: %d"%(numinstruments))
