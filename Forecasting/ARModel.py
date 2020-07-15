import pandas as pd
from statsmodels.tsa.ar_model import  AR, ARResults


def AR_Forecast() -> None:
    df = pd.read_csv("./uspopulation.csv", parse_dates=True, index_col='DATE')
    df.asfreq('MS')
    train = df.iloc[:84]
    test = df.iloc[84:]
    model = AR(train['PopEst'])
    #ic is very important parameter for fitting AR model.
    # One has to choose the value that best fits the model
    ARFit = model.fit(ic='t-stat')
    print(ARFit.params)
    start = len(train)
    end = len(train) + len(test) - 1
    predictions = ARFit.predict(start=start, end=end)
    test.plot(legend=True, label='Test')
    predictions.plot(legend=True, label='Predictions', figsize=(12, 8))


if __name__ == '__main__':
    AR_Forecast()