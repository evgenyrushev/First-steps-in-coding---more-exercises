price_skumria = float(input())
price_caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = price_skumria * 1.6
safrid_price = price_caca * 1.8
midi_price = 7.50

ordered_palamud = palamud_price * palamud_kg
ordered_safrid = safrid_price * safrid_kg
ordered_midi = midi_kg * midi_price

total_sum = (ordered_midi + ordered_safrid + ordered_palamud)

print(f'{total_sum:.2f}')
