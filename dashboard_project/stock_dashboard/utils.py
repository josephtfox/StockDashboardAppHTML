import yfinance as yf
import plotly.graph_objs as go
import json
import plotly

def get_stock_data(ticker, period="1mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist, stock.info

def create_candlestick_chart(data):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
    fig.update_layout(title="Stock Price", xaxis_title="Date", yaxis_title="Price")
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)