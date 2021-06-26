#importing the data
from list_crypto import crypto_list

#importing the libraries for data collection
import pandas_datareader.data as pdr
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#importing the libraries for the calculations
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, discrete_allocation
from pypfopt import expected_returns
from pypfopt.cla import CLA
#from pypfopt.plotting import Plotting #CHECK THIS ONE LATER! IT HAS A PROBLEM
from matplotlib.ticker import FuncFormatter

#testing some shit
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage


#creating the needed variables
end = datetime.today()
start = datetime(end.year,end.month,end.day-15)#set how much you wanna go back here.
#we have already imported our crypto list so no need for initialization
first_df=pdr.DataReader("SNX-USD","yahoo",start,end)#we'll be joining the other df's to this one
first_df=first_df[["Adj Close"]]
first_df.columns=["SNX"]
failed_cryptos=[]


#we create a dataframe with all the prices and dates of the cryptos inside it.
for crypto in crypto_list:
    try:
        df = pdr.DataReader(f"{crypto}-USD","yahoo",start,end)
        df = df[["Adj Close"]]
        df.columns=[crypto]
        first_df = first_df.join(df)
        print(f"{crypto} added!")
    except:
        failed_cryptos.append(crypto)
        print(f"{crypto} failed")

rdf = first_df #ready_df == rdf

#We give data about the failed cryptos here.
print(f"Failed to capture {len(failed_cryptos)}\n{failed_cryptos}")


#We start doing the portfolio calculations here.
"""
I've tried different functions and arguments from the 
pyportfolioopt library  and it still doesn't give results that make sense without errors.
This could either be because of how volatile the crypto market is or there is a problem
with the data extraction.
"""
#Not allowing the shorting of cryptos give ridicilous results with any of the risk_models.
#My computer cannot handle data more than a year ago. You'll have to find a solution.
"""
mu = mean_historical_return(rdf) #Annualized Return.
sv = CovarianceShrinkage(rdf).ledoit_wolf()  #Sample variance of the portfolio.
ef = EfficientFrontier(mu, sv)
weights = ef.max_sharpe()
c_weights = ef.clean_weights() #Don't really understand this part. Don't forget to look over it again.
print(weights)
print(c_weights)
"""
rdf.to_excel(r'C:\Users\F\PycharmProjects\RemoteTraining\fifteen_days_df.xlsx')

mu = mean_historical_return(rdf) #Annualized Return.
sv = CovarianceShrinkage(rdf).ledoit_wolf()  #Sample variance of the portfolio.
ef = EfficientFrontier(mu, sv, weight_bounds=(0,1))
weights = ef.max_sharpe() #incase if you want the exact weights.
c_weights = ef.clean_weights()
print(c_weights)











