from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from api.models import *
# Include the `fusioncharts.py` file that contains functions to embed the charts.

from .fusioncharts import FusionCharts

def myFirstChart(request):
# Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  dataSource = OrderedDict()

# The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  chartConfig["caption"] = "Hopitaux avec un service de qualité"
  chartConfig["subCaption"] = "En étoiles s=star"
  chartConfig["xAxisName"] = "Hopitaux"
  chartConfig["yAxisName"] = "Nombre d'étoiles (S)"
  chartConfig["numberSuffix"] = "S"
  chartConfig["theme"] = "candy"

  dataSource["chart"] = chartConfig
  dataSource["data"] = []

 # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
# Insert the data into the `dataSource['data']` list.
  for key in Pharma.objects.all():
      data = {}
      data['label'] = key.name
      data['value'] = key.vote
      dataSource['data'].append(data)

# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
  column2D = FusionCharts("column2d", "myFirstChart", "800", "500", "myFirstchart-container", "json", dataSource)
  return render(request, 'chart.html', {
    'output': column2D.render()
})