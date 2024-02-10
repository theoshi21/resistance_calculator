tolerance_val = {
    "red": 0.01,
    "orange": 0.02,
    "green": 0.005,
    "blue": 0.0025,
    "violet": 0.001,
    "gold": 0.05,
    "silver": 0.10
}

tolerance_percent ={
    "red": "1%",
    "orange": "2%",
    "green": "0.5%",
    "blue": "0.25%",
    "violet": "0.1%",
    "gold": "5%",
    "silver": "10%"
}

def tolerance_calc(multiplied):
    tolerance_color = input("Tolerance color: ")
    for key, value in tolerance_val.items():
        if key == tolerance_color:
            tolerance = round(float(multiplied * value),2)
            for color, percent in tolerance_percent.items():
                if color == tolerance_color:
                    print(f"Tolerance (+-{percent}): +-{tolerance}")

            print(f"Plus Tolerance: {round(float(multiplied)+float(tolerance),2)}")
            print(f"Minus Tolerance: {round(float(multiplied)-float(tolerance),2)}")
            return tolerance


