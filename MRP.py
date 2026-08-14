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

total_procurement_cost = 0

print("=" * 50)
print(f"MRP PLAN FOR {production_quantity} RESPONSE DEVICES")
print("=" * 50)

for component, quantity_per_unit in bom.items():
    required = quantity_per_unit * production_quantity
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
    print(f"  Unit Cost: ${unit_cost[component]:.2f}")
    print(f"  Procurement Cost: ${cost:.2f}")

print("\n" + "=" * 50)
print(f"TOTAL PROCUREMENT COST: ${total_procurement_cost:.2f}")
print("=" * 50)

