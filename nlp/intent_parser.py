'''
This module analyzes the user's text command and extracts structured information required for booking an event. The function `parse_intent()` takes the raw text input, identifies the event type (e.g., photography workshop, dance show) and the number of tickets requested. It uses simple keyword matching to determine the event and looks for any digits in the text to determine the ticket quantity. The output is a dictionary containing the parsed intent information that can be used by other parts of the assistant to check availability and make bookings.
'''
def parse_intent(text):

    text = text.lower()

    tickets = 1

    # detect number of tickets
    for word in text.split():
        if word.isdigit():
            tickets = int(word)

    # detect event name
    if "photography" in text:
        event = "Photography Workshop"

    elif "dance" in text:
        event = "Dance Show"

    elif "music" in text:
        event = "Music Concert"

    elif "ai" in text:
        event = "AI Seminar"

    elif "yoga" in text:
        event = "Yoga Session"

    else:
        event = "Photography Workshop"

    return {
        "event": event,
        "tickets": tickets
    }
