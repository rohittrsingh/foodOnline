from .models import *
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)    
def create_profile_reciever(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('profile created')
    
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('User updated successfully')
        except:
            #create user profile if it doesn't exist
            UserProfile.objects.create(user=instance)
            print('profile created')


@receiver(pre_save, sender=User)
def pre_save_profile_reciever(sender, instance, **kwargs):
    print(instance.username, 'is being saved')


#post_save.connect(post_save_create_profile_reciever, sender=User)