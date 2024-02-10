multiplier = {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 10000,
    "green": 100000,
    "blue": 1000000,
    "gold": 0.1,
    "silver": 0.01,
}

def multiplier_calc(final_digit):
    multiplier_color = input("Multiplier color: ")
    for key, value in multiplier.items():
        if key == multiplier_color:
            multiplied = round((float(final_digit)*float(value)),2)
            print(f"Multiplier: {final_digit} x {value} ohms = {multiplied}")
            return multiplied
