"""
Test script for HBnB models
Run from the hbnb directory: python -m tests.test_models
"""
import sys
sys.path.insert(0, '.')

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def test_user_creation():
    """Test User class"""
    print("Testing User creation...")
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False
    assert user.id is not None
    print(f"  ✅ User created with ID: {user.id}")
    return user

def test_amenity_creation():
    """Test Amenity class"""
    print("Testing Amenity creation...")
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print(f"  ✅ Amenity created: {amenity.name}")
    return amenity

def test_place_creation(owner):
    """Test Place class with relationships"""
    print("Testing Place creation...")
    place = Place(
        title="Cozy Apartment",
        description="A nice place to stay",
        price=100,
        latitude=37.7749,
        longitude=-122.4194,
        owner=owner
    )
    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert place.owner == owner
    print(f"  ✅ Place created: {place.title}")
    return place

def test_review_creation(place, user):
    """Test Review class"""
    print("Testing Review creation...")
    review = Review(text="Great stay!", rating=5, place=place, user=user)
    assert review.text == "Great stay!"
    assert review.rating == 5
    print(f"  ✅ Review created with rating: {review.rating}")
    return review

def test_relationships(place, review, amenity):
    """Test relationships between models"""
    print("Testing relationships...")
    place.add_review(review)
    place.add_amenity(amenity)
    assert len(place.reviews) == 1
    assert len(place.amenities) == 1
    assert place.reviews[0].text == "Great stay!"
    print(f"  ✅ Place has {len(place.reviews)} review(s) and {len(place.amenities)} amenity(ies)")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("HBnB Model Tests")
    print("="*50 + "\n")
    
    # Run tests
    user = test_user_creation()
    amenity = test_amenity_creation()
    place = test_place_creation(user)
    review = test_review_creation(place, user)
    test_relationships(place, review, amenity)
    
    print("\n" + "="*50)
    print("All tests passed! ✅")
    print("="*50 + "\n")
