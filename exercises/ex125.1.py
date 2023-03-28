liters = float(input("Enter liters: "))

def convert(liters):
    liters_local = liters
    cubic_meters = liters_local * 1000
    return cubic_meters

cm = convert(liters)
print(f"{liters} liters is equal to {cm} cubic meters.")
