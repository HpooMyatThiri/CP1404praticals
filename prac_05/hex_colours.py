PALETTE = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "Alice Blue": "#f0f8ff",
    "Alizarin Crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "Antique White": "#faebd7",
    "Apricot": "#fbceb1"
}

print(PALETTE)

while True:
    try:
        chosen_color = input("Enter your preferred color>>> ").title().replace(" ", "")
        if chosen_color == "":
            break
        color_hex_code = PALETTE[chosen_color]
        print(f"The color code for {chosen_color} is {color_hex_code}")
    except KeyError:
        print("Invalid color name")
