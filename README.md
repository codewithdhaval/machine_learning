#### Numpy  
     Numpy is a numperical processing library that can efficiently handle large data sets stored as arrays  
     Numpy allows to perform operation that is broadcasted to every single number on the array
     
#### Pandas  
     It is build on top of Numpy array.  
     A series is basic building block of Pandas.    
     It holds an array of information organized by index.    
     It can have a Named Index.
           
##### DataFrames  
     Multiple series that share same index  
     Tabular data format  
        Missing Data  
        Some forecasting libraries cannot work with missing data.     
         1. Replace missing data with NaN  
         2. Drop missing data  
         3. Fill missing data with some value  

#### StatsModel  
    statsmodel has lot of useful statistical test build in.  

#### Time Series has trends.  
    Upward, Horizontal or Downward.  
    Repeating Trends - Seasonality.  
     Cyclical trends with no set repetition.  

##### ETS model - Error-Trend-Seasonality    
    Exponential Smoothing  
    Trend Methods Model  
    ETS Decomposition
      
#### Holt-Winters Model

#### Errors  
       Mean Absolute Error - Forecast won't alert if the forecast was really off for a few points.
       Mean Squared Error - Larger Error ar noted more than MAE, making MSE more popular.   
       Root Mean Square Error - Take square root of MSE.  

#### AR(Auto Regression) Model  
    Forecast using linear combination of past values. Regression of variable against itself.  
    Run against a set of lagged values of order p.  

### Prophet
    TODO    
    