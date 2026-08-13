# Bill of Materials (BOM) for an iClicker-inspired classroom response device

bom = {
    "Response Device": {
        "Plastic Housing": 1,
        "PCB": 1,
        "Microcontroller": 1,
        "RF Module": 1,
        "LCD Display": 1,
        "Button": 5,
        "Battery": 2,
        "Battery Contact": 2
    }
}

# Production plan
production_quantity = 10

# Current inventory
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

print(f"Material requirements for {production_quantity} response devices:\n")

for component, quantity in bom["Response Device"].items():
    required = quantity * production_quantity
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)

    print(f"{component}")
    print(f"  Required: {required}")
    print(f"  Available: {available}")
    print(f"  Shortage: {shortage}\n")
