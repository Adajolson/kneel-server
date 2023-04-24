import sqlite3
import json
from models import Metal

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

# def get_all_metals():
#     """This function gets all metals
#     """
#     return METALS

def get_all_metals():
    # Open a connection to the database
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM metals m
        """)

        # Initialize an empty list to hold all metal representations
        metals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an metal instance from the current row.
            # Note that the database fields are specified in
            # exact metal of the parameters defined in the
            # metal class above.
            metal = Metal(row['id'], row['metal'], row['price'])

            metals.append(metal.__dict__)

    return metals

# Function with a single parameter
# def get_single_metal(id):
#     """This function finds a single metal item
#     """
#     # Variable to hold the found metal, if it exists
#     requested_metal = None

#     # Iterate the METALS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for metal in METALS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if metal["id"] == id:
#             requested_metal = metal

#     return requested_metal

def get_single_metal(id):
    """function that gets a single metal"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM metals m
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an metal instance from the current row
        metal = Metal(data['id'], data['metal'], data['price'])

        return metal.__dict__

def update_metal(id, new_metal):
    """This function updates an metal dictionary using SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
