import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll"
df_list = pd.read_html(url)
century_20 = df_list[1]
century_21 = df_list[2]
