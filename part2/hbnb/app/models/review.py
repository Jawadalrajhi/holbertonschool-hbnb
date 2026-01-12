from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.validate()
    def validate(self):
        """Validate review attributes"""
        if not self.text:
            raise ValueError("Review text is required")
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5")