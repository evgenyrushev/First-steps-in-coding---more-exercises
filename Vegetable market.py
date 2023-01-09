price_per_kg_veg = float(input())
price_per_kg_fru = float(input())
total_kg_veg = int(input())
total_kg_fru = int(input())

total_income = price_per_kg_fru * total_kg_fru + price_per_kg_veg * total_kg_veg

in_eur = total_income / 1.94

print(f'{in_eur:.2f}')
