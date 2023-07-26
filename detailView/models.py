from django.db import models
from base.models import BaseModel

# Create your models here.

class Contact(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Career(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cv = models.FileField(upload_to="cv")

    def __str__(self):
        return self.name


# interested Choices

interested_choices = (
    ("Skin-Care", "Skincare"),
    ("Hair-Care", "Haircare"),
    ("Eye-Care", "Eyecare"),
    ("cleanser", "Cleanser"),
    ("professional-care", "Professional Care"),
    ("Sun-Care", "Suncare"),
)

# types of products

types_of_products = (
    ("natural", "Natural"),
    ("organic", "Organic"),
    ("chemical-free", "Chemical Free"),
    ("vegan-friendly", "Vegan Friendly"),
    ("paraben-free", "Paraben Free"),
)

# planing to choose

planing_to_choose = (
    ("within-a-month", "Within a month"),
    ("one-to-six-month", "One to six months"),
    ("just-inquiring", "Just inquiring"),
)

class LevelManufacturing(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_num = models.IntegerField()
    interested_in = models.CharField(
        max_length=100, 
        choices=interested_choices,
        default="skincare"
    )
    types_of_products = models.CharField(
        max_length=100,
        choices=types_of_products,
        default="Natural"
    )
    planning_to_choose = models.CharField(
        max_length=100,
        choices=planing_to_choose,
        default="within_a_month"
    )
    message = models.TextField()

    def __str__(self) -> str:
        return self.interested_in

