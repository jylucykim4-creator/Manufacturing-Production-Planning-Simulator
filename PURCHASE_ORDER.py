# Purchase Order Generator

bom = {
    "Plastic Housing": 1,
    "PCB": 1,
    "Microcontroller": 1,
    "RF Module": 1,
    "LCD Display": 1,
    "Button": 5,
    "Battery": 2,
    "Battery Contact": 2
}

production_quantity = 10

inventory = {
    "Plastic Housing": 15,
    "PCB": 8,
    "Microcontroller": 12,
    "RF Module": 10,
    "LCD Display": 6,
    "Button": 60,
    "Battery": 15,
    "Battery Contact": 25
}

print("=" * 50)
print("PURCHASE ORDER")
print("=" * 50)

total_items = 0

for component, quantity_per_unit in bom.items():
    required = quantity_per_unit * production_quantity
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)

    if shortage > 0:
        print(f"{component}: {shortage} units")
        total_items += shortage

print("-" * 50)
print(f"Total units to purchase: {total_items}")
print("=" * 50)

