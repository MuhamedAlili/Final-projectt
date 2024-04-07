from django.shortcuts import render
import sys
from django.shortcuts import render
import requests
sys.setrecursionlimit(1500)

def convert(request):
    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = float(request.POST.get('amount'))

        # Make API request to fetch exchange rate
        api_url = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={from_currency}&vs_currencies={to_currency}')
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            conversion_rate = data[from_currency.lower()][to_currency.lower()]
            converted_amount = float(amount) * conversion_rate
        data = response.json()
        rate = float(data['data']['rates'][to_currency])

        converted_amount = amount * rate

        return render(request, 'convertapp/convert.html', {'converted_amount': converted_amount})

    return render(request, 'convertapp/convert.html')

