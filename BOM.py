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

production_quantity = 10

print(f"Materials required for {production_quantity} response devices:")

for component, quantity in bom["Response Device"].items():
    required_quantity = quantity * production_quantity
    print(f"{component}: {required_quantity}")
