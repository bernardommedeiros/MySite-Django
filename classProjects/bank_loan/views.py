from django.shortcuts import render
from . import services

# Create your views here.

def loan(request):
     return render(request, 'bank_loan/loan_form.html')

def loan_calculate_result(request):
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        tax = float(request.POST.get('tax')) / 100
        parcels = int(request.POST.get('parcels'))

        monthly_payment = services.loan_calculate(value, tax, parcels)

        context = {
            'monthly_payment': monthly_payment
        }

        return render(request, 'bank_loan/result.html', context)