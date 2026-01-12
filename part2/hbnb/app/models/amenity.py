from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__() # Call parent's constructor first!   
        self.name = name # Set the name attribute
        self.validate() # Validate the object

    def validate(self): # Validate the object
        """Validate amenity attributes"""
        if not self.name or len(self.name) > 50:
            raise ValueError("Amenity name is required and must be 50 characters or less")
