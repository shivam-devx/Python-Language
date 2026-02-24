# a for loop inside another for loop
# useful for working with grids, matrices, or combinations
# outer loop runs first, and for each iteration of outer loop, inner loop run completely
# commonly used in pattern printing

# Example

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

print("\n")

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()

print("\n")
# a while loop inside another while loop
# useful for repeatead tasks with conditions
# must update both outer and inner loop counters to avoid infinite loops
# often used in simulations or multi-level conditions

# Example

i = 1
while i <= 3:          # outer loop
    j = 1
    while j <= 2:      # inner loop
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print("\n")

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
