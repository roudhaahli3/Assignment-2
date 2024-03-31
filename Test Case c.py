from datetime import date
from Assignment2 import Ticket, EventType, ArtLocation, Tour, TicketType

# Function to calculate the ticket price based on age and event type given in the instructions
def calculate_ticket_price(age, event_type):
    ticket_price = 0.0
    # Calculate ticket price based on age and event type
    if age >= 18 and age <= 60:
        ticket_price = 63.0
        if event_type != TicketType.TOUR:
            ticket_price += ticket_price * 0.05  # Adding 5% VAT
    elif age < 18 or age >= 60:
        ticket_price = 0.0  # Free ticket for children below 18 and seniors above 60
    return ticket_price

# Test case for the purchase of tickets by an individual or tour group for an event
def purchase_tickets():
    ticket1 = Ticket("T001", "Roudha Ahli", "V01703", calculate_ticket_price(19, TicketType.SPECIAL_EVENT), 0.0, TicketType.SPECIAL_EVENT, ArtLocation.OUTDOOR_SPACE)
    print("Ticket purchased:")
    print(ticket1)

    # Tour group ticket purchase with a 50% discount
    num_of_visitors = 25
    per_person = calculate_ticket_price(30, TicketType.TOUR)
    total_price = num_of_visitors * per_person  # Total price for all visitors
    discounted_price = total_price * 0.5  # 50% discount
    tourgroup_ticket = Ticket("TGA001", "Tour Group A", "TGA00A", discounted_price, 0.5, TicketType.TOUR,
                              ArtLocation.EXHIBITION_HALL)
    print("Tour group ticket purchased:")
    print(tourgroup_ticket)

# Tour details
def tour_details():
    # Tour details
    tour_details = Tour("TR001", date(2024, 4, 15), 25, "James Bond")
    print("Tour details:")
    print(tour_details)

# Calling the test functions
purchase_tickets()
tour_details()

