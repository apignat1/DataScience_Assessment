import pandas as pd
# Scrape wiki and create pandas df with tables
url = "https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll"
df_list = pd.read_html(url)
century_20 = df_list[1]
century_21 = df_list[2]
merged = pd.concat(frames)
# Remove linked reference within square brackets, which are found after some numbers in death toll
merged.iloc[:,1]=merged.iloc[:,1].str.split("[", expand=True)[0]
# Transform number+ to number
merged.iloc[:,1]=merged.iloc[:,1].str.split("+", expand=True)[0]
# Remove commas
merged.iloc[:,1]=merged.iloc[:,1].str.replace(',','')
# Take average for ranges
import numpy as np
import math
temp=merged.iloc[:,1].str.split("–", expand=True).to_numpy()
tempf=temp.astype(float)
for i in range(len(tempf[:,0])):
  if math.isnan(tempf[i,1])==False:
    tempf[i,0] = (tempf[i,0]+tempf[i,1])/2
merged.iloc[:,1]=pd.Series(tempf[:,0])
# Save dataframe in drive (then download and upload to github)
merged.to_csv('/content/drive/My Drive/merged_dataframe.csv', index=False)
