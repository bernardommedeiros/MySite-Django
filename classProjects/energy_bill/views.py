from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def energy(request):
     return render (request, 'energy_bill/energy_form.html')
 
def bill_calculate(request):
    
    energy_use = int(request.POST.get('kwh'))
    
    if energy_use <= 100:
        result = energy_use * 0.50
    elif energy_use <= 200:
        result = (100 * 0.50) + ((energy_use - 100) * 0.75)
    else:
        result = (100 * 0.50) + (100 * 0.75) + ((energy_use - 200) * 1.00)
        
    context = {
        'result': result,
    }

    
    
    return render (request, 'energy_bill/result.html', context)
 
 