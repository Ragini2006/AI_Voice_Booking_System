'''
Main entry  point for AI voice vooking assistant. Listens for user commands, processes intents, checks event availability, books tickets, and provides responses.   
'''
from speech.speech_to_text import transcribe
from speech.text_to_speech import speak

from nlp.intent_parser import parse_intent
from booking.check_availability import check_event
from booking.book_event import book_ticket
from booking.recommend_events import recommend


print("🎙️ AI Event Booking Voice Assistant Started")
print("Say 'stop' anytime to exit.\n")


while True:

    print("🎤 Listening...")
# Capture voice and convert to text
    text, lang = transcribe()
    if "ki" in text or "cheyyi" in text or "tickets" in text and "book" not in text: 
        lang = "te" # detect Hindi words 
    elif "ke" in text or "karo" in text: 
        lang = "hi"
    else:
        lang = "en"

    if text == "":
        continue

    print("User said:", text)
    print("Detected language:", lang)

    command = text.lower().strip()
     # stop commands
    if command in ["stop", "exit", "quit", "close"]: 
        print("Assistant stopped.") 
        speak("Assistant stopped", lang) 
        break
#extract booking intent from text
    intent = parse_intent(text)

    event_name = intent["event"]
    tickets = intent["tickets"]
# check database from event availability and book if possible, else recommend alternatives
    result = check_event(event_name)

    if result is None:

        response = "Sorry, I could not find that event."

    else:

        event, available = result

        if available >= tickets:

            ref = book_ticket(event[0], tickets)

            response = (
                f"Booking confirmed for {event_name}. "
                f"{tickets} tickets booked. "
                f"Reference number {ref}."
            )

        else:

            suggestions = recommend(event[1])

            if suggestions:

                alt = suggestions[0]

                response = (
                    f"Sorry, {event_name} is full. "
                    f"You can try {alt[0]} on {alt[1]} at {alt[2]}."
                )

            else:

                response = "Sorry, the event is full and no alternatives are available."

    print("Assistant:", response)
#convert response text to speech
    speak(response, lang)

    print("\n-----------------------------------\n")
