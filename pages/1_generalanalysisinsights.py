from importlib.metadata import files
import pandas as pd # type: ignore
import numpy as np # type: ignore
import statistics
import streamlit as st # type: ignore
import altair as alt
df1 = pd.read_csv('Data/Total waste.csv')
df1
df1 = df1.drop(36)
df1 = df1.drop(38)
df1 = df1.reset_index(drop=True)
df1
# Replacing missing values with mean of the row values
df1.at[1, '2020'] = 2620400000

df1average_uk = (df1.at[32, '2010'] + df1.at[32, '2012'] + df1.at[32, '2014'] + df1.at[32, '2016'] + df1.at[32, '2018']) / 5
df1average_uk = round(df1average_uk)
print('Average uk is:', df1average_uk)
df1.at[32, '2020'] = df1average_uk
df1.at[29, '2006'] = df1average_uk
df1.at[30, '2006'] = df1average_uk

df1average_bosnia = (df1.at[33, '2012'] + df1.at[33, '2014'] + df1.at[33, '2016'] + df1.at[33, '2018'] + df1.at[33, '2020']) / 5
df1average_bosnia = round(df1average_bosnia)
print('Average bosnia is:', df1average_bosnia)
df1.at[33, '2010'] = df1average_bosnia
df1.at[33, '2004'] = df1average_bosnia
df1.at[33, '2006'] = df1average_bosnia
df1.at[36, '2004'] = df1average_bosnia
df1.at[36, '2006'] = df1average_bosnia
df1.at[36, '2008'] = df1average_bosnia
df1.at[33, '2008'] = df1average_bosnia
df1.at[30, '2004'] = df1average_bosnia
df1average_montenegro = (df1.at[34, '2012'] + df1.at[34, '2014'] + df1.at[34, '2016'] + df1.at[34, '2018'] + df1.at[34, '2020']) / 5
df1average_montenegro = round(df1average_montenegro)
print('Average montenegro is:', df1average_montenegro)
df1.at[34, '2010'] = df1average_montenegro
df1.at[34, '2004'] = df1average_montenegro
df1.at[34, '2006'] = df1average_montenegro
df1.at[34, '2008'] = df1average_montenegro

df1average_kosovo = (df1.at[37, '2012'] + df1.at[37, '2014'] + df1.at[37, '2016'] + df1.at[37, '2018'] + df1.at[37, '2020']) / 5
df1average_kosovo = round(df1average_kosovo)
print('Average kosovo is:', df1average_kosovo)
df1.at[37, '2010'] = df1average_kosovo
df1.at[37, '2004'] = df1average_kosovo
df1.at[37, '2006'] = df1average_kosovo
df1.at[37, '2008'] = df1average_kosovo
df1.at[35, '2004'] = df1average_kosovo
df1.at[35, '2006'] = df1average_kosovo
df1average_kosovo
df1.columns
df1['TIME']
# Melt the DataFrame to convert from wide to long format
df1_new = pd.melt(df1, id_vars=['TIME'], var_name='Year', value_name='Total waste in tonnes')

# Display the long format DataFrame
print("Long Format DataFrame:")
print(df1_new)
df1_new.to_csv('Data/clean_total_waste.csv')
df1_subset = df1.iloc[2:]
# Bar plot showing waste values for specific countries
#st.dataframe(df1_subset)
df1_subset
chart = pd.DataFrame(df1_new)
#d = {
    #alt.Chart(chart)
    #.mark_circle()
    #.encode(x="TIME", y="Year", size="Total waste in tonnes", color="c", tooltip=["TIME", "Year", "Total waste in tonnes"])
#}
df1_new
Countries, Year = st.columns(2)

st.bar_chart(df1_new['TIME'])
st.bar_chart(df1_new['Year'])
