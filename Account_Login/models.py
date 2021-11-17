from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=50, null=True, blank=True)
    Last_Name = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.CharField(max_length=10, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    pic = models.ImageField(upload_to='Profile_pic', blank=True, null=True)

    def __str__(self):
        return self.First_Name

    class Meta:
        db_table = 'auth_profile'


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(instance,**kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
