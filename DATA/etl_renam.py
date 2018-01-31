import pandas as pd

df = pd.read_csv('renam_2018_01_30.csv.gz')		# use dtypes for efficient memory usage + dateparser straight into time
# without any specs, 2.4 Gb
# float64:	Vivienda ID, Humedad Interior, Humedad Exterior, Co2, Ruido
# object:	Temperatura Interior,Temperatura Exterior,Pm10,Pm25,Potencia,Energia,Measured At,fecha                   ,
df['fecha']=[ma.split() for ma in df['Measured At']]
ddf['fecha']=['-'.join(f[0].split('-')[::-1]) for f in df['fecha']]

print(df.fecha.describe())				# count        6137478
print(df.fecha.min(),df.fecha.max())	# ('2015-11-26', '2018-01-27')	2 años y 2 meses