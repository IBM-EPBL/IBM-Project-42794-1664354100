IMPORT THE DATASET
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os
import collections
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
!pip3 install openpyxl
Requirement already satisfied: openpyxl in c:\users\vicky reddy\anaconda3\lib\site-packages (3.0.9)
Requirement already satisfied: et-xmlfile in c:\users\vicky reddy\anaconda3\lib\site-packages (from openpyxl) (1.1.0)
## loading dataset
df=pd.read_csv('weather.csv')
df.head()
366 Days	MinTemp	MaxTemp	Rainfall	Evaporation	Sunshine	WindGustDir	WindGustSpeed	WindDir9am	WindDir3pm	...	Humidity3pm	Pressure9am	Pressure3pm	Cloud9am	Cloud3pm	Temp9am	Temp3pm	RainToday	RISK_MM	RainTomorrow
0	1	8.0	24.3	0.0	3.4	6.3	NW	30.0	SW	NW	...	29	1019.7	1015.0	7	7	14.4	23.6	No	3.6	Yes
1	2	14.0	26.9	3.6	4.4	9.7	ENE	39.0	E	W	...	36	1012.4	1008.4	5	3	17.5	25.7	Yes	3.6	Yes
2	3	13.7	23.4	3.6	5.8	3.3	NW	85.0	N	NNE	...	69	1009.5	1007.2	8	7	15.4	20.2	Yes	39.8	Yes
3	4	13.3	15.5	39.8	7.2	9.1	NW	54.0	WNW	W	...	56	1005.5	1007.0	2	7	13.5	14.1	Yes	2.8	Yes
4	5	7.6	16.1	2.8	5.6	10.6	SSE	50.0	SSE	ESE	...	49	1018.3	1018.5	7	7	11.1	15.4	Yes	0.0	No
5 rows × 23 columns

dfa=pd.read_csv('rainfall in india 1901-2015.csv')
dfa.head()
SUBDIVISION	YEAR	JAN	FEB	MAR	APR	MAY	JUN	JUL	AUG	SEP	OCT	NOV	DEC	ANNUAL	Jan-Feb	Mar-May	Jun-Sep	Oct-Dec
0	ANDAMAN & NICOBAR ISLANDS	1901	49.2	87.1	29.2	2.3	528.8	517.5	365.1	481.1	332.6	388.5	558.2	33.6	3373.2	136.3	560.3	1696.3	980.3
1	ANDAMAN & NICOBAR ISLANDS	1902	0.0	159.8	12.2	0.0	446.1	537.1	228.9	753.7	666.2	197.2	359.0	160.5	3520.7	159.8	458.3	2185.9	716.7
2	ANDAMAN & NICOBAR ISLANDS	1903	12.7	144.0	0.0	1.0	235.1	479.9	728.4	326.7	339.0	181.2	284.4	225.0	2957.4	156.7	236.1	1874.0	690.6
3	ANDAMAN & NICOBAR ISLANDS	1904	9.4	14.7	0.0	202.4	304.5	495.1	502.0	160.1	820.4	222.2	308.7	40.1	3079.6	24.1	506.9	1977.6	571.0
4	ANDAMAN & NICOBAR ISLANDS	1905	1.3	0.0	3.3	26.9	279.5	628.7	368.7	330.5	297.0	260.7	25.4	344.7	2566.7	1.3	309.7	1624.9	630.8
dfb=pd.read_csv('District wise rainfall normal.csv')
dfb.head()
STATE_UT_NAME	DISTRICT	JAN	FEB	MAR	APR	MAY	JUN	JUL	AUG	SEP	OCT	NOV	DEC	ANNUAL	Jan-Feb	Mar-May	Jun-Sep	Oct-Dec
0	ANDAMAN And NICOBAR ISLANDS	NICOBAR	107.3	57.9	65.2	117.0	358.5	295.5	285.0	271.9	354.8	326.0	315.2	250.9	2805.2	165.2	540.7	1207.2	892.1
1	ANDAMAN And NICOBAR ISLANDS	SOUTH ANDAMAN	43.7	26.0	18.6	90.5	374.4	457.2	421.3	423.1	455.6	301.2	275.8	128.3	3015.7	69.7	483.5	1757.2	705.3
2	ANDAMAN And NICOBAR ISLANDS	N & M ANDAMAN	32.7	15.9	8.6	53.4	343.6	503.3	465.4	460.9	454.8	276.1	198.6	100.0	2913.3	48.6	405.6	1884.4	574.7
3	ARUNACHAL PRADESH	LOHIT	42.2	80.8	176.4	358.5	306.4	447.0	660.1	427.8	313.6	167.1	34.1	29.8	3043.8	123.0	841.3	1848.5	231.0
4	ARUNACHAL PRADESH	EAST SIANG	33.3	79.5	105.9	216.5	323.0	738.3	990.9	711.2	568.0	206.9	29.5	31.7	4034.7	112.8	645.4	3008.4	268.1