from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    WORK_TYPE_CHOICES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES)

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    works = models.ManyToManyField(Work)

# Signal to create an Artist object after user registration
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    if created:
        artist = Artist.objects.create(user=instance, name=instance.username)

        # Add some dummy works for the artist
        Work.objects.create(link='https://www.youtube.com/artist1', work_type='YT')
        Work.objects.create(link='https://www.instagram.com/artist1', work_type='IG')
        Work.objects.create(link='https://www.example.com/artist1', work_type='OT')

        artist.works.add(*Work.objects.all())

@receiver(post_save, sender=User)
def save_artist(sender, instance, **kwargs):
    instance.artist.save()
