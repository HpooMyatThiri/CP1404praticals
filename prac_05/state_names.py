"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


# TODO: Format the dictionary code according to PEP 8 conventions
STATE_CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(STATE_CODE_TO_NAME)

while True:
    try:
        entered_code = input("Enter state code: ").upper()
        if entered_code == "":
            break

        state_full_name = STATE_CODE_TO_NAME[entered_code]
        print(f"{entered_code} corresponds to {state_full_name}")

    except KeyError:
        print("Invalid state code")

for state_code, full_name in STATE_CODE_TO_NAME.items():
    print("{:3} corresponds to {}".format(state_code, full_name))
