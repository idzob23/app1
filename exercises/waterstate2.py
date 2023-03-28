minT = 0
maxT = 100
def water_state(temp):
    if temp >= maxT:
        return "Gas"
    elif minT < temp < maxT:
        return "Liquid"
    else:
        return "Solid"
