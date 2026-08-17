# Purchase Order Generation

from bom import calculate_material_requirements

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

suppliers = {
    "Plastic Housing": "ABC Plastics",
    "PCB": "ElectroParts Inc.",
    "Microcontroller": "MicroTech",
    "RF Module": "Wireless Components",
    "LCD Display": "DisplayWorks",
    "Button": "Switch Supply Co.",
    "Battery": "PowerCell",
    "Battery Contact": "Metal Components"
}

unit_cost = {
    "Plastic Housing": 2.50,
    "PCB": 8.00,
    "Microcontroller": 4.00,
    "RF Module": 3.50,
    "LCD Display": 6.00,
    "Button": 0.50,
    "Battery": 1.50,
    "Battery Contact": 0.30
}

requirements = calculate_material_requirements(production_quantity)

total_cost = 0

print("=" * 60)
print("PURCHASE ORDER")
print("=" * 60)

for component, required in requirements.items():
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)

    if shortage > 0:
        cost = shortage * unit_cost[component]
        total_cost += cost

        print(f"\nComponent: {component}")
        print(f"Supplier: {suppliers[component]}")
        print(f"Order Quantity: {shortage}")
        print(f"Unit Cost: ${unit_cost[component]:.2f}")
        print(f"Total Cost: ${cost:.2f}")
        print("Status: Pending")

print("\n" + "=" * 60)
print(f"TOTAL PURCHASE ORDER VALUE: ${total_cost:.2f}")
print("=" * 60)
