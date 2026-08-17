# Bill of Materials 
# iClicker-inspired classroom response device

BOM = {
    "Plastic Housing": 1,
    "PCB": 1,
    "Microcontroller": 1,
    "RF Module": 1,
    "LCD Display": 1,
    "Button": 5,
    "Battery": 2,
    "Battery Contact": 2
}


def calculate_material_requirements(production_quantity):
    """Calculate the materials required for a given production quantity."""

    requirements = {}

    for component, quantity_per_unit in BOM.items():
        requirements[component] = quantity_per_unit * production_quantity

    return requirements


if __name__ == "__main__":
    production_quantity = 10

    requirements = calculate_material_requirements(production_quantity)

    print(f"Materials required for {production_quantity} response devices:")

    for component, quantity in requirements.items():
        print(f"{component}: {quantity}")

