import yfinance as yf #for fetching company financial data
import pandas as pd #for handling data
import matplotlib.pyplot as plt #for ploting graphs
#now input data
ticker = input("Enter stock ticker (e.g AAPL for apple, TCS.NS for TCS India):")
company=yf.Ticker(ticker)#give access to all data about company
#print(company)
#Get financial data like totla revenue or net income
income_stmt = company.financials.T #transpose so years come as rows
print(income_stmt)
revenue = income_stmt['Total Revenue']
net_income = income_stmt['Net Income']
#print revenue and net income
print(f"\nRevenue Data for {ticker}:\n")
print(revenue)
print(f"\nNet Income Data\n")
print(f"{net_income}")
#Calculate revenue Growth (to show company performance is chaninging over time)
growth = ((revenue.iloc[0] - revenue.iloc[1]) / revenue.iloc[1]) * 100 #iloc stands for (interger location) iloc[0] is most recent year
#iloc[-1] oldest year -1 means last
print(f"\n Revenue Growth Over Years:{growth:.2f}%") #Show percentage growth in revenue from the oldest year to most recent year

#plot the data graphs 
plt.figure(figsize=(10,5))
plt.plot(revenue.index, revenue.values/1e9, marker='o', label='Revenue (in Billions)') # divide by 1e9 to conver in billons
plt.plot(net_income.index, net_income.values/1e9, marker='s', label='Net Income (in Billons)')
plt.title(f"{ticker} Revenue & income Trend")
plt.xlabel('Year')
plt.ylabel('USD (Billons)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{ticker}_trend.png")
plt.show()

