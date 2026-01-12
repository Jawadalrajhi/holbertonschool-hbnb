from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews  attributes to store relationships like a container
        self.amenities = []  # List to store related amenities attributes to store relationships like a container
        self.validate()

    def validate(self):
        """Validate place attributes"""
        if not self.title or len(self.title) > 100:
            raise ValueError("Title is required and must be 100 characters or less")
        if self.price <= 0:
            raise ValueError("Price must be a positive value")
        if not (-90 <= self.latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= self.longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")

    def add_review(self, review): # Add a review to the place
        """Add a review to the place"""
        self.reviews.append(review) # Add the review to the reviews list

    def add_amenity(self, amenity): # Add an amenity to the place
        """Add an amenity to the place"""
        self.amenities.append(amenity) # Add the amenity to the amenities list