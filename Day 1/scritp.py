# Create empty lists for left and right values
leftarray = []
rightarray = []
distances = []

# Open and read the input.txt file
with open('input.txt', 'r') as file:
    for line in file:
        # Split each line by space, convert to integers and append to respective lists
        left, right = map(int, line.split())
        leftarray.append(left)
        rightarray.append(right)

# Sort both arrays
leftarray.sort()
rightarray.sort()

# Loop through both lists, calculate the absolute difference, and add to distances list
for left, right in zip(leftarray, rightarray):
    distances.append(abs(left - right))

# Calculate the total sum of the distances list
total_distance = sum(distances)

# Print the sorted arrays, distances list, and the total sum
print("Sorted leftarray:", leftarray)
print("Sorted rightarray:", rightarray)
print("Distances:", distances)
print("Total distance:", total_distance)
