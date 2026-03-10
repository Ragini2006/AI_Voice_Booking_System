'''
If an event is fully booked, this module recommends alternative events from the same category that still have available seats. The function `recommend()` takes a category as input, queries the database for events in that category, and filters the results to include only those events that have available seats. It returns a list of up to three recommended events, which can be presented to the user as alternatives when their desired event is not available.
'''


import sqlite3

def recommend(category):

    conn = sqlite3.connect("database/events.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name,date,time,total_seats,booked_seats FROM events WHERE category=?",
        (category,)
    )

    events = cursor.fetchall()

    suggestions = []

    for e in events:
        available = e[3]-e[4]

        if available > 0:
            suggestions.append(e)

    return suggestions[:3]