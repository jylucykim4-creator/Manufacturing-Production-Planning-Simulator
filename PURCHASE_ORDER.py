# Purchase Order Generator

shortages = {
    "PCB": 2,
    "LCD Display": 4,
    "Battery": 5,
    "Microcontroller": 0,
    "RF Module": 0
}

print("=" * 40)
print("PURCHASE ORDER")
print("=" * 40)

total_items = 0

for component, quantity in shortages.items():
    if quantity > 0:
        print(f"{component}: {quantity} units")
        total_items += quantity

print("-" * 40)
print(f"Total units to purchase: {total_items}")
print("=" * 40)
