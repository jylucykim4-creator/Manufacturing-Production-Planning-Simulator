# Material Requirements Planning (MRP)

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

print(f"MRP for {production_quantity} response devices:\n")

for component, quantity_per_unit in bom.items():
    required = quantity_per_unit * production_quantity
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)

    print(f"{component}:")
    print(f"  Required: {required}")
    print(f"  Available: {available}")
    print(f"  Shortage: {shortage}")
    print()

