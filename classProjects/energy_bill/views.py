from django.shortcuts import render
from . import services

# Create your views here.

from django.shortcuts import render

# Create your views here.

def energy(request):
     return render (request, 'energy_bill/energy_form.html')
 
def bill_calculate_result(request):
    if request.method == 'POST':
        energy_use = int(request.POST.get('kwh'))
    
        result = services.bill_calculate(energy_use)
        context = {
            'result': result,
        }
    
        return render (request, 'energy_bill/result.html', context)
 
 