from django.shortcuts import render
from . import services
from .models import imcCalc

# Create your views here.
def form_imc(request):
    return render (request, 'imc_calculator/calculator.html')
    
def imc_calculate(request):
    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        imc = peso / (altura * altura)
        
        condition = services.get_condition(imc) 
        
        imcCalc.objects.create(
            peso=peso,
            altura=altura,
            imc=imc,
            condicao=condition
        )  

        context = {
            'peso': peso,
            'altura': altura,
            'imc': imc,
            'condition': condition
        }
        
        return render(request, 'imc_calculator/result.html', context)

