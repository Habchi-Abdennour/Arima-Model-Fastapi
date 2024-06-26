import uvicorn
from fastapi import FastAPI
import requests
from class_arima import TimeSeriesAnalysis

app = FastAPI()


@app.get("/")
def main():
    dates = ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01',
         '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01',
         '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01',
         '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01',
         '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01',
         '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01']

    ordered = [45, 22, 80, 30, 70, 100, 90, 115, 150, 120, 200, 175,
           200, 250, 100, 120, 30, 50, 100, 75, 250, 150, 205, 175]
    return {'dates':dates,'ordered':ordered}




@app.get("/predict")
def read_root(url:str,value:int):
    read=requests.get(url)
    format=read.json()
    dates=format['dates']
    ordered=format['ordered']
    tsa = TimeSeriesAnalysis(dates, ordered)
    tsa.preprocess_data()
    predictions = tsa.make_predictions(value)

    return {'dates': predictions.index.strftime('%Y-%m-%d').tolist(), 'ordered': predictions.tolist()}



