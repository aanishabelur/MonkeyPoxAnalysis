# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 12:45:32 2022

@author: belura
"""

import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import matplotlib.pyplot as plt

pox = pd.read_csv("Development/latest.csv", parse_dates=['Date'])

colsToKeep = ['ID', 'Date','Status', 'Country', 'Symptoms', 'Hospitalised', 'Travel History',
       'Travel from']

pox = pox[colsToKeep]
pox['Date'] = pox['Date'].dt.date

pox=pox.fillna("n.a.")


# pox.columns
# del pox['ID']
# del pox['Location']
# del pox['City']
# del pox['Age']
# del pox['Gender']
# del pox['Date']
# del pox['Date_onset']
# del pox['Date_hospitalisation']
# del pox['Isolated (Y/N/NA)']
# del pox['Date_isolation']
# del pox['Outcome']
# del pox['Contact_comment']
# del pox['Contact_ID']
# del pox['Contact_location']
# del pox['Travel_history_entry']
# del pox['Travel_history_start']
# del pox['Travel_history_location']
# del pox['Genomics_Metadata']
# del pox['Confirmation_method']
# del pox['Source']
# del pox['Source_II']
# del pox['Date_entry']
# del pox['Date_last_modified']
# del pox['Source_III']
# del pox['Country_ISO3']
# del pox['Country_ISO4']
# del pox['Symptoms1']

# pox=pox.dropna(how='all')

st.title("Monkey Pox Cases")
st.write("Cases reported below have been tracked since May'22")

country = list(pox['Country'].unique())
status = list(pox['Status'].unique())
travel = list(pox['Travel History'].unique())
symptoms = list(pox['Symptoms'].unique())
hosp = list(pox['Hospitalised'].unique())

picked_country = st.sidebar.multiselect("Pick country",country)
picked_status = st.sidebar.multiselect("Status",status)
picked_travel = st.sidebar.multiselect("Travel history", travel)
picked_symptoms = st.sidebar.multiselect("Pick reported symptom", symptoms)
picked_hosp = st.sidebar.multiselect("Hospitalised", hosp)

countCases = pox.groupby(['Date']).count()
countCountries = pox.groupby(['Country']).count()
countDayCountries = pox.groupby(['Country','Date']).count()
countDayCountries = pox.groupby(['Country','Date']).count()



# st.write(picked_country)
if len(picked_country)==0:
    filterDF = pox
else:
    filterDF = pox[pox['Country'].isin(picked_country)]

if len(picked_travel)==0:
    filterDF = filterDF
else:
    filterDF = filterDF[filterDF['Travel History'].isin(picked_travel)]

if len(picked_status)==0:
    filterDF = filterDF
else:
    filterDF = filterDF[filterDF['Status'].isin(picked_status)]

if len(picked_symptoms)==0:
    filterDF = filterDF
else:
    filterDF = filterDF[filterDF['Symptoms'].isin(picked_symptoms)]

if len(picked_hosp)==0:
    filterDF = filterDF
else:
    filterDF = filterDF[filterDF['Hospitalised'].isin(picked_hosp)]

numRows = 3
numCols = 1
plt.plot(numRows, numCols)

#graph1
plt.plot(numRows, numCols, 1)
fig1 = px.line(countCases, title= 'Daily Addition of Cases')
st.plotly_chart(fig1)

#graph2
plt.plot(numRows, numCols, 2)
fig2 = px.bar(filterDF, x='Country', color='Symptoms', title= 'Dominant symptoms')
st.plotly_chart(fig2)

#graph3
plt.plot(numRows, numCols, 3)
fig3 = px.bar(filterDF, x='Hospitalised', color='Symptoms', title= 'Hospitalisation Tally', barmode='group')
st.plotly_chart(fig3)
