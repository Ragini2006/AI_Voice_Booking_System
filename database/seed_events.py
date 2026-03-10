import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
category TEXT,
date TEXT,
time TEXT,
total_seats INTEGER,
booked_seats INTEGER,
description TEXT
)
""")

events = [

("Photography Workshop","Workshop","2025-06-10","17:00",20,5,"Learn photography basics"),
("Dance Show","Entertainment","2025-06-10","19:00",40,10,"Classical dance performance"),
("Music Concert","Entertainment","2025-06-11","18:00",50,20,"Live music night"),
("AI Seminar","Tech","2025-06-12","11:00",30,12,"Introduction to AI"),
("Startup Meetup","Business","2025-06-12","16:00",25,5,"Networking event"),
("Yoga Session","Health","2025-06-13","07:00",20,8,"Morning yoga class"),
("Coding Bootcamp","Tech","2025-06-13","10:00",35,15,"Learn Python coding"),
("Photography Advanced","Workshop","2025-06-14","17:00",20,18,"Advanced photography"),
("Art Exhibition","Art","2025-06-14","15:00",50,25,"Local artists showcase"),
("Cooking Workshop","Workshop","2025-06-15","11:00",20,10,"Learn cooking"),
("Dance Workshop","Entertainment","2025-06-15","16:00",30,15,"Learn dance basics"),
("Music Jam","Entertainment","2025-06-16","18:00",40,30,"Open mic music jam"),
("AI Workshop","Tech","2025-06-16","10:00",25,5,"Hands-on AI workshop"),
("Meditation Session","Health","2025-06-17","08:00",20,10,"Guided meditation"),
("Startup Pitch","Business","2025-06-17","14:00",35,20,"Startup pitch event")

]

cursor.executemany("""
INSERT INTO events
(name,category,date,time,total_seats,booked_seats,description)
VALUES (?,?,?,?,?,?,?)
""",events)

conn.commit()
conn.close()

print("Events seeded successfully")