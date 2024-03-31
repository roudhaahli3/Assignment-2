from datetime import date
from Assignment2 import Artwork, ArtLocation

# Test case for the addition of new art to the museum
def add_art_to_museum():
    # Create a new artwork object
    new_artwork1 = Artwork("The Starry Night", "Vincent van Gogh", date(1889, 6, 1), "Iconic painting",
                          ArtLocation.PERMANENT_GALLERY)
    new_artwork2 = Artwork("The Crystal Palace", "Joseph Paxton", date(1851, 1, 1), "Glass and iron structure",
                          ArtLocation.OUTDOOR_SPACE)

    # Confirming
    print("New artwork added to the museum:")
    print(new_artwork1)
    print(new_artwork2)


# Run the test
add_art_to_museum()
