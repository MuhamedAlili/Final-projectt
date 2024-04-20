from django.shortcuts import render

CONVERSION_RATES = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
}

def convert_currency(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        
        converted_amount = amount * (CONVERSION_RATES[to_currency] / CONVERSION_RATES[from_currency])
        
        return render(request, 'currency_converter/result.html', {
            'amount': amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'converted_amount': converted_amount,
        })
    else:
        return render(request, 'currency_converter/converter.html', {'currencies': CONVERSION_RATES.keys()})
