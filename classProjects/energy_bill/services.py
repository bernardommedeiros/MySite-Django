def bill_calculate(energy_use):
    if energy_use <= 100:
        result = energy_use * 0.50
    elif energy_use <= 200:
        result = (100 * 0.50) + ((energy_use - 100) * 0.75)
    else:
        result = (100 * 0.50) + (100 * 0.75) + ((energy_use - 200) * 1.00)

    return energy_use;