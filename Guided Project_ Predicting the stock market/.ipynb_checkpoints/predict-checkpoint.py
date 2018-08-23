import pandas as pd
from datetime import datetime

df=pd.read_csv('sphist.csv')
df['Date']=pd.to_datetime(df['Date'])
df_sorted=df.sort_values(by='Date', ascending=True)


# Generate the average price for last 5, 30, 365 days, ratio of 5/365, std of 5, std of 365, ratio std5/std365
# Generate the average price for last 5, 30, 365 days, 
# ratio of 5/365, std of 5, std of 365, ratio std5/std365

df['day_5']=df['Close'].rolling(5).mean().shift(1)
df['day_365']=df['Close'].rolling(365).mean().shift(1)
df['day_30']=df['Close'].rolling(30).mean().shift(1)
df['ratio_p/y']=df['day_5']/df['day_365']
df['std_5']=df['Close'].rolling(5).std().shift(1)
df['std_365']=df['Close'].rolling(365).std().shift(1)
df['std_ratio']=df['std_5']/df['std_365']


# Generate more Indicators using Volume:
# Three more indicators with Volume
df['vol_5']=df['Volume'].rolling(5).mean().shift(1)
df['vol_365']=df['Volume'].rolling(365).mean().shift(1)
df['vol_ratio']=df['vol_5']/df['vol_365']


df['Year']=df['Date'].dt.year
# Ratio between lowest value of last year and current price
lowest_yr=[]
for index, row in df.iterrows():   
    lastyr=row['Year']-1
    lowest=df[df['Year']==lastyr]['Close'].min()
    lowest_yr.append(lowest)

df['lowest']=lowest_yr
df['last_low_ratio']=df['Close']/df['lowest']

## Train models with different indicators:
# Define error metric: Mean Absolute Error:
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

target=train['Close']
features=['day_5','day_365','ratio_p/y','std_ratio','vol_5','vol_ratio','day_30']

model=LinearRegression()
model.fit(train[features],target)

predictions=model.predict(test[features])
mae=mean_absolute_error(predictions,test['Close'])
print(mae)


# Plot the predictions againt the true value
import matplotlib.pyplot as plt
%matplotlib inline

predictions_Series=pd.Series(predictions,index=test.index)
pred_df=pd.DataFrame({'predictions':predictions_Series,'Date':test.Date})


ax1=pred_df.plot(x='Date',y='predictions')
test.plot(x='Date',y='Close',color='red',ax=ax1)
#plt.xlim(['2014','2015'])
plt.show()
