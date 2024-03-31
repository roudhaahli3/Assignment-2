from enum import Enum

class EventType(Enum):
    '''class to represent the ENUM for the SpecialEvent different purposes'''
    FUNDRAISING = 1
    MUSICAL_CONCERT = 2
    LIGHT_SHOW = 3

class ArtLocation(Enum):
    '''class to represent the ENUM for the Artwork locations that can be used in the ticked and Exhibition'''
    PERMANENT_GALLERY = 1
    EXHIBITION_HALL = 2
    OUTDOOR_SPACE = 3

class  TicketType(Enum):
    '''class to represent the ENUM for the Ticket's type'''
    EXHIBITION = 1
    SPECIAL_EVENT = 2
    TOUR = 3

class Visitor:
    '''class to represent the museum's visitors'''
    #Initializing the constructor
    def __init__(self, visitorName, visitorID, visitorAge, nationalID):
        self._visitorName = visitorName
        self._visitorID = visitorID
        self._visitorAge = visitorAge
        self._nationalID = nationalID
        self._tours = []  # List to store associated tours (composition)
        self._special_events = []  # List to store associated special events (composition)
        self._tickets = []  # List to store associated tickets (composition)

    # Setter and getter methods for visitorName
    def set_VisitorName(self, visitorName):
        self._visitorName = visitorName

    def get_VisitorName(self):
        return self._visitorName

    # Setter and getter methods for visitorID
    def setVisitorID(self, visitorID):
        self._visitorID = visitorID

    def getVisitorID(self):
        return self._visitorID

    # Setter and getter methods for visitorAge
    def set_VisitorAge(self, visitorAge):
        self._visitorAge = visitorAge

    def get_VisitorAge(self):
        return self._visitorAge

    # Setter and getter methods for nationalID
    def set_NationalID(self, nationalID):
         self._nationalID = nationalID

    def get_NationalID(self):
        return self._nationalID

    def add_tour(self, tour):
        '''adding a tour to the visitor's list of tours'''
        if len(self._tours) < 40:
            self._tours.append(tour)
        else:
            print("Maximum number of tours reached.")

    def remove_tour(self, tour):
        ''' removing a tour from the visitor's list of tours'''
        if tour in self._tours:
            self._tours.remove(tour)

    def add_special_event(self, special_event):
        '''adding a special event to the visitor's list of special events'''
        self._special_events.append(special_event)

    def remove_special_event(self, special_event):
        '''removing a special event from the visitor's list of special events'''
        if special_event in self._special_events:
            self._special_events.remove(special_event)

    def add_ticket(self, ticket):
        '''adding a ticket to the visitor's list of tickets'''
        if len(self._tickets) == 0:
            self._tickets.append(ticket)
        else:
            print("Visitor can have only one ticket.")

    def remove_ticket(self, ticket):
        '''removing a ticket from the visitor's list of tickets'''
        if ticket in self._tickets:
            self._tickets.remove(ticket)

    #string representation of the Visitor object
    def __str__(self):
        return f"Visitor Name: {self._visitorName}, Visitor ID: {self._visitorID}, Age: {self._visitorAge}, National ID: {self._nationalID}"

class Ticket:
    '''class to represent the tickets'''
    #Intializing the constructor
    def __init__(self, ticketid, visitorName, visitorID, price, discount, type, location):
        self._ticketid = ticketid
        self._visitorName = visitorName
        self._visitorID = visitorID
        self._price = price
        self._discount = discount
        self._type = type
        self._location = location

    # Setter and getter methods for ticketid
    def set_Ticketid(self, ticketid):
        self._ticketid = ticketid

    def get_Ticketid(self):
        return self._ticketid

    # Setter and getter methods for visitorName
    def set_VisitorName(self, visitorName):
        self._visitorName = visitorName

    def get_VisitorName(self):
        return self._visitorName

    # Setter and getter methods for visitorID
    def set_VisitorID(self, visitorID):
        self._visitorID = visitorID

    def get_VisitorID(self):
        return self._visitorID

    # Setter and getter methods for ticket price
    def set_Price(self, price):
        self._price = price

    def get_Price(self):
        return self._price

    # Setter and getter methods for discount
    def set_Discount(self, discount):
        self._discount = discount

    def get_Discount(self):
        return self._discount

    # Setter and getter methods for ticket type
    def set_Type(self, type):
        self._type = type

    def get_Type(self):
        return self._type

    # Setter and getter methods for ticket location
    def set_Location(self, location):
        self._location = location

    def get_Location(self):
        return self._location

    # string representation of the Ticket object
    def __str__(self):
        return f"Ticket ID: {self._ticketid}, Visitor Name: {self._visitorName}, Visitor ID: {self._visitorID}, Price: {self._price}, Discount: {self._discount}, Ticket Type: {self._type.name}, Location: {self._location.name}"

class Tour:
    '''class to represent the tours'''
    #Initializing the constructor
    def __init__(self, tourid, tourDate, numofvisitors, guide):
        self._tourid = tourid
        self._tourDate = tourDate
        self._numofvisitors = numofvisitors
        self._guide = guide

    # Setter and getter methods for tourid
    def set_Tourid(self, tourid):
        self._tourid = tourid

    def get_Tourid(self):
        return self._tourid

    # Setter and getter methods for tourDate
    def set_TourDate(self, tourDate):
        self._tourDate = tourDate

    def get_TourDate(self):
        return self._tourDate

    # Setter and getter methods for numofvisitors
    def set_Numofvisitors(self, numofvisitors):
        self._numofvisitors = numofvisitors

    def get_Numofvisitors(self):
        return self._numofvisitors

    # Setter and getter methods for the tour guide
    def set_Guide(self, guide):
        self._guide = guide

    def get_Guide(self):
        return self._guide

    # string representation of the Tour object
    def __str__(self):
        return f"Tour ID: {self._tourid}, Tour Date: {self._tourDate}, Number of Visitors: {self._numofvisitors}, Tour Guide: {self._guide}"

class SpecialEvent:
    '''class to represent the SpecialEvent'''
    # Initializing the constructor
    def __init__(self, eventid, eventType, startDate, endDate, numofvisitors, eventLoc):
        self._eventid = eventid
        self._eventType = eventType
        self._startDate = startDate
        self._endDate = endDate
        self._numofvisitors = numofvisitors
        self._eventLoc = eventLoc

    # Setter and getter methods for the eventid
    def set_Eventid(self, eventid):
        self._eventid = eventid

    def get_Eventid(self):
        return self._eventid

    # Setter and getter methods for the eventType
    def set_EventType(self, eventType):
        self._eventType = eventType

    def get_EventType(self):
        return self._eventType

    # Setter and getter methods for startDate
    def set_StartDate(self, startDate):
        self._startDate = startDate

    def get_StartDate(self):
        return self._startDate

    # Setter and getter methods for endDate
    def set_EndDate(self, endDate):
        self._endDate = endDate

    def get_EndDate(self):
        return self._endDate

    # Setter and getter methods for eventLoc
    def set_EventLoc(self, eventLoc):
        self._eventLoc = eventLoc

    def get_EventLoc(self):
        return self._eventLoc

    # string representation of the SpecialEvent object
    def __str__(self):
        return f"Event ID: {self._eventid}, Event Type: {self._eventType.name}, Start Date: {self._startDate}, End Date: {self._endDate}, Number of Visitors: {self._numofvisitors}, Event Location: {self._eventLoc}"

class Artwork:
    '''class to represent the different artworks in the museum'''
    def __init__(self, title, artist, creationDate, historicalSignificance, artloc):
        self._title = title
        self._artist = artist
        self._creationDate = creationDate
        self._historicalSignificance = historicalSignificance
        self._artloc = artloc

    # Setter and getter methods for title
    def set_Title(self, title):
        self._title = title

    def get_StartDate(self):
        return self._title

    # Setter and getter methods for artist
    def set_Artist(self, artist):
        self._artist = artist

    def get_Artist(self):
        return self._artist

    # Setter and getter methods for creationDate
    def set_CreationDate(self, creationDate):
        self._creationDate = creationDate

    def get_CreationDate(self):
        return self._creationDate

    # Setter and getter methods for historicalSignificance
    def set_HistoricalSignificance(self, historicalSignificance):
        self._historicalSignificance = historicalSignificance

    def get_HistoricalSignificance(self):
        return self._historicalSignificance

    # Setter and getter methods for artLoc
    def set_Artloc(self, artloc):
        self._artloc = artloc

    def get_Artloc(self):
        return self._artloc

    # string representation of the Artwork object
    def __str__(self):
        return f"Artwork Title: {self._title}, Artist: {self._artist}, Creation Date: {self._creationDate}, Historical Significance: {self._historicalSignificance}, Art Location: {self._artloc.name}"

class Exhibition:
    '''class to represent the Exhibition'''
    def __init__(self, exhibid, startDate, endDate, loc, numofartworks):
        self._exhibid = exhibid
        self._startDate = startDate
        self._endDate = endDate
        self._loc = loc
        self._numofartworks = numofartworks

    # Setter and getter methods for exhibid
    def set_Exhibid(self, exhibid):
        self._artloc = exhibid

    def get_Exhibid(self):
        return self._exhibid

    # Setter and getter methods for startDate
    def set_StartDate(self, startDate):
        self._startDate = startDate

    def get_StartDate(self):
        return self._startDate

    # Setter and getter methods for endDate
    def set_EndDate(self, endDate):
         self._endDate = endDate

    def get_EndDate(self):
        return self._endDate

    # Setter and getter methods for location
    def set_Loc(self, loc):
        self._loc = loc

    def get_loc(self):
        return self._loc

    # Setter and getter methods for numofartworks
    def set_Numofartworks(self, numofartworks):
        self._numofartworks = numofartworks

    def get_Numofartworks(self):
        return self._numofartworks

    # string representation of the Exhibition object
    def __str__(self):
        return f"Exhibition ID: {self._exhibid}, Start Date: {self._startDate}, End Date: {self._endDate}, Location: {self._loc.name}, Number of Artworks: {self._numofartworks}"