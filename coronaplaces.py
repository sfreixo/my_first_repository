import os 
from exif import Image
from PIL import Image as Pilmage
import pandas as pd
import folium
import base64

def gps_file(img_path):
    with open (img_path, 'rb') as src:
        img=Image(src)
        if img.has_exif:
            latitude, longitude, hora = img.gps_latitude, img.gps_longitude, img.datetime_original
        else:
            latitude = longitude = hora = None
    return(latitude, longitude, hora)

def convertir_longlat(dato, signo='+'):    
    dato = dato.replace('(', '').replace(')','')        
    grados, minutos, segundos = [float(i) for i in dato.split(',')]    
    grados_conv = grados + minutos / 60 + segundos / 3600
    if signo == '-':
        grados_conv *=  -1
    return grados_conv

nombres = []
latitudes = []
longitudes = []
horas = []
path = "C:/Users/RAMON SANTIAGO/Documents/Fotos/lugares/"

for base, dirs, files in os.walk(path):
    for file in files:
        nombres.append(file)           
        latitude, longitude, hora = gps_file(path+file)
        latitudes.append(str(latitude))
        longitudes.append(str(longitude))
        horas.append(hora)

dic_df =  {'fichero':nombres, 'longitud':longitudes, 'latitud':latitudes, 'hora':horas}
df = pd.DataFrame(dic_df)

df['longap'] = df["longitud"].apply(convertir_longlat, args = '-')
df['latap'] =  df["latitud"].apply(convertir_longlat)


display(df)
