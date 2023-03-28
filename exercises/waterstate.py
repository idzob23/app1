def water_state(temp):
    if temp >= 100:
        return "Gas"
    elif 0 < temp < 100:
        return "Liquid"
    else:
        return "Solid"
