from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_stock_data, create_candlestick_chart

def index(request):
    return render(request, 'stock_dashboard/index.html')

def get_stock_data_view(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        period = request.POST.get('period')
        data, info = get_stock_data(ticker, period)
        chart_json = create_candlestick_chart(data)
        return JsonResponse({
            'chart': chart_json,
            'info': {
                'name': info['longName'],
                'price': data['Close'].iloc[-1],
                'change': f"{(data['Close'].iloc[-1] - data['Open'].iloc[0]) / data['Open'].iloc[0] * 100:.2f}%",
                'volume': int(data['Volume'].mean())
            }
        })