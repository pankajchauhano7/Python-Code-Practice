
def min_notes(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    note_count = {}

    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            note_count[denom] = count
            amount -= denom * count

    return note_count
# Example usage
amount = 3768
result = min_notes(amount)
print("Denomination count for amount", amount, "is:", result)
