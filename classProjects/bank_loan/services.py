def loan_calculate(value, tax, parcels):
    montante = value
    i = 0
    while i < parcels:
        montante *= (1 + tax)
        i += 1

    monthly_payment = montante / parcels
    monthly_payment_str = f"{monthly_payment:.2f}"
    return monthly_payment_str