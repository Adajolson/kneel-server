METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 405
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 782
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1470
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 1997
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 3638
    }
]

def get_all_metals():
    """This function gets all metals
    """
    return METALS

# Function with a single parameter
def get_single_metal(id):
    """This function finds a single metal item
    """
    # Variable to hold the found metal, if it exists
    requested_metal = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for metal in METALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal
