# Using dictionary to replace swtich method in other languages

day = 1

def mon():
    return "Monday"

swticher = {
    0: "Sunday",
    1: mon,
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

day_name = swticher.get(day, 'Unknown')()
print(day_name)