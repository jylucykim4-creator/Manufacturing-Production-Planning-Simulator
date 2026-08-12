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

print("Bill of Materials:")
for component, quantity in bom["Response Device"].items():
    print(f"{component}: {quantity}")
