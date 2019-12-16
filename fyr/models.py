from django.db import models
from django.utils import timezone
from django.db.models import Case, CharField, Value, When
# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    description = models.TextField()
    formation_date = models.DateField('Band formation')
    #founder = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class BandMembers(models.Model):
#     band = models.ForeignKey(Band, on_delete=models.CASCADE)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     membership_start = models.DateTimeField(default=timezone.now())
#     membership_end = models.DateTimeField(null=True, blank=True)
#
#
# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     real_name = models.CharField(max_length=100)
#     birthday = models.DateTimeField()


class Address(models.Model):
    house_apt_unit_no = models.CharField(max_length=20)
    descriptor = models.CharField(null=True, max_length=100)
    street_no = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_prov = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.street_no} {self.street}, {self.city}"

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_start = models.DateField('Event Date', null=True)
    duration_description = models.CharField(max_length=100, null=True)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True, blank=True)
    bands = models.ManyToManyField('Band')

    def __str__(self):
        return self.name

    #This doesn't work/ do anything. #TODO figure out why
    # def label_country_nicknames(cls):
    #     qs = cls.annotate_country = Event.objects.annotate(country_code=Case(
    #         When(venue__address__country__in=["South Africa", "SA", "United States"],
    #              then=Value("Saffer")),
    #         When(Q(venue__address__country="United States") | Q(venue__address__country="Canada"),
    #              then= Value("Northerica")),
    #         default=Value("REST of WORLD"),
    #         output_field=CharField(),))
    #     return qs

class BandImage(models.Model):
    band = models.ForeignKey(Band, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return f"{self.band.name}| Image -{str(self.pk)}"