# Material Requirements Planning (MRP)

from bom import BOM, calculate_material_requirements

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

total_procurement_cost = 0

print("=" * 50)
print(f"MRP PLAN FOR {production_quantity} RESPONSE DEVICES")
print("=" * 50)

for component, required in requirements.items():
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)
    recommended_order = shortage
    cost = recommended_order * unit_cost[component]

    total_procurement_cost += cost

    print(f"\n{component}")
    print(f"  Required: {required}")
    print(f"  Available: {available}")
    print(f"  Shortage: {shortage}")
    print(f"  Recommended Order: {recommended_order}")
    print(f"  Procurement Cost: ${cost:.2f}")

print("\n" + "=" * 50)
print(f"TOTAL PROCUREMENT COST: ${total_procurement_cost:.2f}")
print("=" * 50)

