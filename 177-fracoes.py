# Frações

from fractions import Fraction

frac1 = Fraction(1, 4)

print(f"Fração: {frac1}")
print(f"Fração: {frac1.numerator}")
print(f"Fração: {frac1.denominator}")

frac2 = Fraction(5, 8)
print(f"Fração: {frac2}")
print(f"Numerador: {frac2.numerator}")
print(f"Denominador: {frac2.denominator}")

frac3 = Fraction(frac1) + Fraction(frac2)
print(f"Fração: {frac3}")
print(f"Numerador: {frac3.numerator}")
print(f"Denominador: {frac3.denominator}")

print(f"Soma das Frações: {frac3}")