'''
This module queries the SQLite database to determine whether seats are available for a given event. The function `check_event()` takes an event name as input, performs a database lookup to find the corresponding event record, and calculates the number of available seats by subtracting the booked seats from the total seats. It returns both the event details and the number of available seats, which can be used by the main assistant logic to decide whether to proceed with booking or to recommend alternative events.
'''


import sqlite3

def check_event(event_name):

    conn = sqlite3.connect("database/events.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM events WHERE name LIKE ?",('%'+event_name+'%',)
    )

    event = cursor.fetchone()

    if event is None:
        return None

    total = event[5]
    booked = event[6]

    available = total - booked

    return event, available