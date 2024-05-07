from importlib.metadata import files
import pandas as pd # type: ignore
import numpy as np # type: ignore
import streamlit as st # type: ignore
import altair as alt
df2 = pd.read_csv('Data/Soil contamination.csv')
df2
df2.rename(columns={'TIME': 'COUNTRIES'}, inplace=True)
df2 = df2.set_index('COUNTRIES')
df2.at['European Union - 28 countries (2013-2020)', '2020'] = 530610000.0
average = (47 + 65) / 2
average = round(average)
df2.at['Malta', '2012'] = average
df2.at['Malta', '2014'] = average
df2.at['Malta', '2016'] = average
df2.at['Malta', '2020'] = average
df2.at['Norway', '2010'] = 3920.0
df2.at['United Kingdom', '2020'] = 62009410.0
average_her = (df2.at['Bosnia and Herzegovina', '2012'] + df2.at['Bosnia and Herzegovina', '2014'] + df2.at['Bosnia and Herzegovina', '2016'] + df2.at['Bosnia and Herzegovina', '2018'] + df2.at['Bosnia and Herzegovina', '2020']) / 5
average_her = round(average_her)
df2.at['Bosnia and Herzegovina', '2010'] = average_her
df2.at['Montenegro', '2010'] = 101918.0
df2 = df2.drop('Albania')
df2.at['Kosovo*', '2010'] = 1045.0
df2.at['Kosovo*', '2012'] = 1045.0
df2
df2.columns
df2['2020']
df2_new = pd.melt(df2, id_vars=['2020'], var_name='Year', value_name='Soil contamination in tonnes')
print("Long Format DataFrame:")
print(df2_new)
df2_new.to_csv('Data/clean_Soil_contamination.csv')
df2_subset = df2.iloc[2:]
df2_subset
st.bar_chart(df2_subset['2020'])
st.bar_chart(df2_subset['2010'])