from django.db import models
from django.contrib.auth.models import User # ??? is this right ???

class Listings(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='listing_images/', blank=True, default='auction_images/default/default.svg')
    created_at = models.DateField()
    updated_at - models.DateField()
    start_time = models.DateField()
    end_time = models.DateField()

    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)


class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True)


class Bids(models.Model):
    amount = models.IntegerField()
    bid_time = models.DateField()
    winning_bid = models.BooleanField()

    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)