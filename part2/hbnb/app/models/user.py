import re
from app.models.base_model import BaseModel

class User(BaseModel): #inherit from BaseModel
    def __init__(self, first_name, last_name, email, is_admin=False): # Add constructor parameters
        super().__init__() # Call parent's constructor first!
        self.first_name = first_name # Set the first_name attribute
        self.last_name = last_name # Set the last_name attribute
        self.email = email # Set the email attribute
        self.is_admin = is_admin # Set the is_admin attribute
        self.validate() # Validate the object   

    def validate(self):
        """Validate user attributes"""
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("First name is required and must be 50 characters or less")
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("Last name is required and must be 50 characters or less")
        if not self.email or not self.valid_email(self.email):
            raise ValueError("Valid email is required")

    @staticmethod # Static Method is independent of the class object it only takes email as parameter
    def valid_email(email): # Check if email format is valid
        """Check if email format is valid"""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None