from django.db import models
from django.contrib.auth.models import User  ### ??? is this right ???
from django.utils.timezone import now
### IMPORTANT thing to discuss later as a group is timezone. Does Django save everything in UTC? Do we have to set that manually? I think everything datetime related in the db should be in UTC, if that's not the django default for some reason.

from listings.constants import PRODUCT_CONDITION, CATEGORIES


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, choices=CATEGORIES)
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
    is_active = models.BooleanField(default=True)
    starting_price = models.DecimalField(max_digits=9, decimal_places=2)
    ending_price = models.DecimalField(max_digits=9, decimal_places=2)
    # winning_bidder = models.ForeignKey(User, related_name='won_auction', blank=True, null=True, on_delete=models.SET("deleted"))
    ### I think winning_bidder should associated via winning bid

    def __str__(self):
        return self.name

    def has_started(self):
        return self.start_time > now ### I'm assuming both are UTC, but I don't know if this is true

    def has_ended(self):
        return self.end_time < now ### I'm assuming both are UTC, but I don't know if this is true

    def get_all_bids(self):
        all_bids = Bid.objects.filter(listing_id=self).order_by('amount').order_by('bid_time')
        return all_bids

    def get_current_price(self):
        last_bid = Bid.objects.filter(listing_id=self).order_by('amount').order_by('bid_time').last()
        if last_bid:
            return last_bid.amount
        else:
            return self.starting_price

    def remaining_time(self):
        # is there a good library/pre-written function for this?
        pass

    def get_winning_bid(self):
        if self.is_active:
            # If expired
            if self.has_ended():
                # Define winner
                highest_bid = Bid.objects.filter(listing_id=self).order_by('-amount').order_by('bid_time').first()
                ### wow, is '-amount' the indicating desc order? damn, that's good to know
                if highest_bid:
                    self.winning_bidder = highest_bid.bid_user
                    self.ending_price = highest_bid.amount
                self.is_active = False
                self.save()


class Bid(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    bid_time = models.DateTimeField()
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_winning_bid = models.BooleanField()

    def __str__(self):
        return f"{self.bid_user} : {self.amount}"
