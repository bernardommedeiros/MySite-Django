def get_condition(imc):
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

    return condition;