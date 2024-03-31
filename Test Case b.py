from datetime import date
from Assignment2 import Exhibition, SpecialEvent, EventType, ArtLocation

# Test case for the opening of a new exhibition or event at the museum
def new_exhibition_event():
    # Creating and opening a new exhibition
    new_exhibition = Exhibition("EX003", date(2024, 7, 1), date(2024, 7, 31), ArtLocation.EXHIBITION_HALL, 30)
    print("New exhibition opened at the museum:")
    print(new_exhibition)

    # Creating and opening a new special event
    new_event = SpecialEvent("E012", EventType.MUSICAL_CONCERT, date(2024, 8, 1), date(2024, 8, 3), 150, eventLoc = 'OUTDOORS')
    print("New special event opened at the museum:")
    print(new_event)

# Calling the test function
new_exhibition_event()
