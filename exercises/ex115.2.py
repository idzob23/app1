# The function we wrote in exercise 1 returned 9.7.
# Change the function so this time it returns
# Max: 9.7, Min: 9.2
# where 9.7 is the maximum and 9.2 is the minimum.


def get_min_max():
    grades = [9.6, 9.2, 9.7]
    maxgrade_local = max(grades)
    mingrade_local = min(grades)
    return f"Max: {maxgrade_local}, Min: {mingrade_local}"

print(get_min_max())
