from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x): return x.value

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A'][1:]
years = map(getvalue, sheet['A'][1:])
x = list(years)

sheet1 = wb['Data']
sheet1['B'][1:]
relations = map(getvalue, sheet1['B'][1:])
y = list(relations)

pyplot.plot(x, y, label="Метка")
pyplot.show()

sheet2 = wb['Data']
sheet2['C'][1:]
activity = map(getvalue, sheet2['C'][1:])
z = list(activity)

pyplot.plot(x, z, label="Метка")
pyplot.show()