"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key --looking up
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update/ reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Demonstrations of dictionary literals
schools = {}  # same as dict()

# Alternatively, initialize key-value pair
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}

# What happens when a key does not exist?
# print(schools['UNCC'])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")