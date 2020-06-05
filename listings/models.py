from django.db import models
from django.contrib.auth.models import User  # ??? is this right ???

from listings.constants import PRODUCT_CONDITION, CATEGORIES


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(choices=CATEGORIES)
    condition = models.PositiveSmallIntegerField(choices=PRODUCT_CONDITION)
    description = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='listing_images/', blank=True, default='auction_images/default/default.svg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    starting_price = models.DecimalField(decimal_places=2)
    ending_price = models.DecimalField(decimal_places=2)
    winning_bidder = models.ForeignKey(User, related_name='won_auction', blank=True, null=True)

    def __str__(self):
        return self.name

    def has_started(self):
        pass

    def get_current_price(self):
        pass

    def has_ended(self):
        pass

    def remaining_minutes(self):
        pass


class Bid(models.Model):
    amount = models.IntegerField()
    bid_time = models.DateField()
    winning_bid = models.BooleanField()
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bid_user} : {self.amount}"
