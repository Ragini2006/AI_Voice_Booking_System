'''
This module updates the database when a user successfully books an event
'''
import sqlite3
import random

def book_ticket(event_id,tickets):

    conn = sqlite3.connect("database/events.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT total_seats,booked_seats FROM events WHERE id=?",
        (event_id,)
    )

    total,booked = cursor.fetchone()
# prevents overbooking by checking if the requested number of tickets exceeds the available seats before updating the database. If the booking request cannot be fulfilled, it returns None, allowing the main assistant logic to handle the situation appropriately.
    if booked + tickets > total:
        return None

    new_booked = booked + tickets

    cursor.execute(
        "UPDATE events SET booked_seats=? WHERE id=?",
        (new_booked,event_id)
    )

    conn.commit()
# generates unique booking reference number for each successful booking
    booking_ref = "BOOK-" + str(random.randint(10000,99999))

    conn.close()

    return booking_ref