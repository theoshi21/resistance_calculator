bandDigit = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9",
}

def bandnumber():
    while(True):
        bandnum = int(input("Please input how many bands your resistor are [4/5/6]: "))
        if bandnum == 4 or bandnum == 5 or bandnum == 6:
            return bandnum
        else:
            print("Invalid input, try again.")

def bandcolors():
    bandcolors = []
    number = bandnumber()
    for x in range(number-2):
        while(True):
            usercolor = input(f"Band {x+1}: ")
            if usercolor in bandDigit.keys():
                bandcolors.append(usercolor)
                break
            else:
                print("Invalid color, try again.")
    return bandcolors

def banddigit():
    banddigits = []
    for colors in bandcolors():
        for key, value in bandDigit.items():
            if key == colors:
                banddigits.append(value)
    final_digit = "".join(banddigits)
    return final_digit

