TYPES = [
    {
        "id": 1,
        "name": "Ring",
        "price": 1
    },
    {
        "id": 2,
        "name": "Earring",
        "price": 2
    },
    {
        "id": 3,
        "name": "Necklace",
        "price": 4
    }
]

def get_all_types():
    """This function gets all types
    """
    return TYPES

def get_single_type(id):
    """This function finds a single type item
    """
    # Variable to hold the found type, if it exists
    requested_type = None

    # Iterate the TYPES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for type in TYPES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if type["id"] == id:
            requested_type = type

    return requested_type
