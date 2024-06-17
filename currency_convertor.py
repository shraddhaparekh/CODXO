pip install forex-python

from forex_python.convertor import CurrencyRates

c = CurrencyRates()

amount = 100 

source_currency ="USD"
target_currency ="INR"

converted_amount = c.convert(source_currency,target_currency, amount)

print(f"{amount} {source_currency} is equal to {converted_amount} {target_currency}.")
