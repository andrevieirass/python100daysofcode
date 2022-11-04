# List 
# fruits = [item1, item2]
states_of_usa = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Print whole list
print(states_of_usa)

print("\n##########\n")

# Print index/offset
print(states_of_usa[0])
print(states_of_usa[9])
print(states_of_usa[-1])
print(states_of_usa[-10])

print("\n##########\n")

# Edit index value
states_of_usa[1] = "Pencilvania"

print(states_of_usa)

print("\n##########\n")

# Add a value to the end of the list
states_of_usa.append("São Paulo")

print(states_of_usa)

print("\n##########\n")

# Add a list to the list
states_of_usa.extend(["Bahia", "Manaus"])

print(states_of_usa)
