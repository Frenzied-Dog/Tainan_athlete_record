from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import UserProfile


# 創建User時，給預設Group:Athlete，自動創建UserProfile
@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Athlete'))
        UserProfile.objects.create(
            user=instance,
            name=instance.username,
        )
        # print('Profile created!')