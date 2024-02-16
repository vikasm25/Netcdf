import pandas as pd
import numpy as np
import netCDF4 as nc
import os

file2=pd.read_excel("C:/Users/Dr. Asif Qureshi/Desktop/Name_lat.xlsx")
#print(file2)

dir= "E:/RCP_DATA/DEPOSITIONS/TOTAL_DEP/RCP85/"
list_file=os.listdir(dir)
print(list_file)
i=0
df = pd.DataFrame()
for fi in list_file:
    
    file=dir+fi
    data=nc.Dataset(file)
    # print(data)
    
    lat=data['lat'][:]
    lat=lat.tolist()

    lon=data['lon'][:]
    lon=lon.tolist()

    a=lat.index(-10)
    # print(a)


    model_v=[]
    for id in range(0,len(file2)):
        
        in_lat=file2['Lat'][id]
        in_long=file2['Long'][id]


        nc_lon=np.arange(-178.125,180,3.75)
        nc_lat=np.arange(88.125,-90,-3.75)
        y=lat.index(in_lat)
        x=lon.index(in_long)

        value=np.average(data['__xarray_dataarray_variable__'][0,0,y,x])  
        model_v.append(value)
    
    temp=model_v
    df.insert(i,fi[-14:-10],temp)
    i=i+1
    

        
# print(df)
df.insert(0,"park",file2['Name '])
df.insert(1,"lat",file2['Lat'])
df.insert(2,"Log",file2['Long'])
#data2=pd.DataFrame({'Lat':file2['Lat'],'Long':file2['Long'],'Model Conc':model_v})
df.to_excel("D:/OneDrive - IIT Hyderabad/RCP85.xlsx",index=None)



