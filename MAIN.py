# iClicker Manufacturing Planning System
# Main program

from bom import calculate_material_requirements
from mrp import inventory, unit_cost
from purchase_order import suppliers

production_quantity = 10

requirements = calculate_material_requirements(production_quantity)

total_procurement_cost = 0

print("=" * 60)
print("iCLICKER MANUFACTURING PLANNING SYSTEM")
print("=" * 60)

print(f"\nProduction Quantity: {production_quantity} units\n")

print("MATERIAL REQUIREMENTS")
print("-" * 60)

for component, required in requirements.items():
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)

    print(
        f"{component}: "
        f"Required={required}, "
        f"Available={available}, "
        f"Shortage={shortage}"
    )

print("\nPURCHASE REQUIREMENTS")
print("-" * 60)

for component, required in requirements.items():
    available = inventory.get(component, 0)
    shortage = max(required - available, 0)

    if shortage > 0:
        cost = shortage * unit_cost[component]
        total_procurement_cost += cost

        print(
            f"{component}: "
            f"Order {shortage} units "
            f"from {suppliers[component]} "
            f"(${cost:.2f})"
        )

print("\n" + "=" * 60)
print(f"TOTAL PROCUREMENT COST: ${total_procurement_cost:.2f}")
print("=" * 60)
