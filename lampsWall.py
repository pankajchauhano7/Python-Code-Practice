arr = [1, 0, 0, 1, 0, 0, 0, 1]
n = 4  # total number of lamps allowed

def is_lit(arr, i):
    return (i > 0 and arr[i-1] == 1) or arr[i] == 1 or (i < len(arr)-1 and arr[i+1] == 1)

def place_lamps(arr, n):
    existing_lamps = arr.count(1)
    remaining = n - existing_lamps

    i = 0
    while i < len(arr) and remaining > 0:
        if arr[i] == 0 and not is_lit(arr, i):
            arr[i] = 1  # Place a lamp
            remaining -= 1
        i += 1

    return arr

final_arr = place_lamps(arr[:], n)  # Use arr[:] to avoid changing original
print("Final arrangement:", final_arr)

# Check if all lit
all_lit = all(is_lit(final_arr, i) for i in range(len(final_arr)) if final_arr[i] == 0)
print("All spaces lit:", all_lit)
