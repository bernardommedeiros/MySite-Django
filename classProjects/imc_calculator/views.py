from django.shortcuts import render

# Create your views here.
def form_imc(request):
    return render (request, 'imc_calculator/calculator.html')
    
def imc_calculate(request):
    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        imc = peso / (altura * altura)
        
        if imc < 18.5:
            condition = 'abaixo do peso ideal'
        elif imc >= 18.5 and imc <= 24.9:
            condition = 'com o peso ideal'
        elif imc >= 25 and imc <= 29.9:
            condition = 'acima do peso ideal'
        elif imc >= 30 and imc <= 34.9:
            condition = 'com Obesidade Grau 1'
        elif imc >= 35 and imc <= 39.9:
            condition = 'com Obesidade Grau 2'
        else:
            condition = 'com Obesidade Mórbida'
            
        context = {
            'peso': peso,
            'altura': altura,
            'imc': imc,
            'condition': condition
        }
        
        return render(request, 'imc_calculator/result.html', context)