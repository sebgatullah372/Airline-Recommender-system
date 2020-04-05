# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:04:03 2020

@author: Arnob
"""

import pandas as pd
import numpy as np 

airline_last_travel = input();
data = pd.read_csv('airline.csv')
data_m = data.dropna(subset= ['overall_rating'])
#data_n = data.isnull().sum()
#print(data_m.head())
data_new = data_m.groupby('airline_name')['overall_rating'].mean().sort_values(ascending=False)

data_cnt = data_m.groupby('airline_name')['overall_rating'].count().sort_values(ascending=False)
data_mean_count = pd.DataFrame(data_m.groupby('airline_name')['overall_rating'].mean())
data_mean_count['rating_count'] = pd.DataFrame(data_m.groupby('airline_name')['overall_rating'].count())
airline_user_rating = data_m.pivot_table(index = 'author', columns = 'airline_name', values = 'overall_rating')
airline_user_rating = airline_user_rating[airline_user_rating.get(airline_last_travel).notnull()]
airline_user_rating = airline_user_rating.dropna(axis = 'columns', thresh = 2 )
airline_last_travel_ratings = airline_user_rating[airline_last_travel]
airline_like_airline_last_travel = airline_user_rating.corrwith(airline_last_travel_ratings)
airline_like_airline_last_travel = airline_like_airline_last_travel.dropna()
corr_airline_last_travel = pd.DataFrame(airline_like_airline_last_travel, columns=['Correlation'])
corr_airline_last_travel.dropna()
corr_airline_last_travel = corr_airline_last_travel.sort_values('Correlation', ascending=False)
corr_airline_last_travel = corr_airline_last_travel.join(data_mean_count['rating_count'])
corr_airline_last_travel=corr_airline_last_travel[corr_airline_last_travel ['rating_count']>500].sort_values('Correlation', ascending=False)


print(corr_airline_last_travel)