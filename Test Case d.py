from Assignment2 import Ticket, ArtLocation, TicketType

# Function to display payment receipts for purchasing tickets
def display_payment_receipts(tickets):
    total_bill = 0.0
    print("Payment Receipts:")
    print("=================")
    for ticket in tickets:
        print(ticket)
        total_bill += ticket.get_Price()
    print("-----------------")
    print(f"Total Bill: {total_bill:.2f} AED")
    print("=================")

# Example usage
tickets = [
    Ticket("T001", "Roudha Ahli", "V01703", 66.15, 0.0, TicketType.SPECIAL_EVENT, ArtLocation.OUTDOOR_SPACE),
    Ticket("TGA001", "Tour Group A", "TGA00A", 787.5, 0.5, TicketType.TOUR, ArtLocation.EXHIBITION_HALL)
]

display_payment_receipts(tickets)
