"""Practice with generating dictionaries using basic syntax!"""

# Basic syntax, generating a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

# Adding an element
ice_cream["mint"] = 3
print(ice_cream)

# Removing elements, use pop function
ice_cream.pop("mint")
print(ice_cream)

# Access an element
ice_cream["chocolate"]
print(ice_cream["chocolate"])

# Modify an element (update)
ice_cream["vanilla"] = 10
# OR
ice_cream["vanilla"] += 2

# Length of dictionary
len(ice_cream)
print(len(ice_cream))

# Check "if" key in dictionary
print("chocolate" in ice_cream)
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint!")


# Bump up student's grade to an A+ if their grade is an A
# Otherwise, give student an A as their grade
def grade_bump(gradebook: dict[str, str], student: str) -> None:
    """Bump up a student's grade!"""
    if gradebook[student] == "A":
        gradebook[student] = "A+"
    else:
        gradebook[student] = "A"


grades: dict[str, str] = {"Addison": "A", "Weston": "B+"}
grade_bump(grades, "Addison")
print(grades)
grade_bump(grades, "Weston")
print(grades)
