from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver


class Coach(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='使用者')
    name = models.CharField(max_length=10, help_text='教練姓名')
    gender_list = [('M', '男'), ('F', '女'), ('O', '其他')]
    gender = models.CharField(db_column='性別', default='M', choices=gender_list, max_length=2)
    school = models.CharField(max_length=30, help_text='所屬學校')
    phone = models.CharField(max_length=10, help_text='聯絡電話')
    mail = models.EmailField(help_text='電子郵件')
    avatar = models.ImageField(upload_to='uploads/coach/', blank=True, null=True)
    
    # Metadata
    class Meta:
        ordering = ['name']
        db_table = 'tb_coach'
        unique_together = ['name', 'gender', 'phone']

    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        return ''

    # Methods
    def __str__(self):
        return self.name
    

class Athlete(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='使用者')
    name = models.CharField(max_length=10, help_text='運動員姓名')
    gender_list = [('M', '男'), ('F', '女'), ('O', '其他')]
    gender = models.CharField(db_column='性別', default='M', choices=gender_list, max_length=2)
    name = models.CharField(max_length=10, help_text='運動員姓名')
    coach = models.ManyToManyField(Coach, through='Coach_Athlete', through_fields=('athlete', 'coach'), related_name='athletes', help_text='教練')
    school = models.CharField(max_length=30, help_text='所屬學校')
    phone = models.CharField(max_length=10, help_text='聯絡電話')
    mail = models.EmailField(max_length=50, help_text='電子郵件')
    guardian = models.CharField(max_length=10, help_text='監護人 (姓名/稱謂)')
    emr_phone = models.CharField(max_length=10, help_text='緊急聯絡電話')
    address = models.CharField(max_length=50, help_text='地址')
    birth = models.DateField(help_text='生日')
    avatar = models.ImageField(upload_to='uploads/athlete/', blank=True, null=True)
    
                                 
    # Metadata
    class Meta:
        ordering = ['name']
        db_table = 'tb_athlete'
        unique_together = ['name', 'gender', 'phone']
    
    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        return ''

    # Methods
    def __str__(self):
        """String for representing the Athlete object (in Admin site etc.)."""
        return self.name


class Coach_Athlete(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='coach_athlete_relationships')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='athlete_coach_relationships')
    start_date = models.DateField()
    
    def __str__(self):
        return f'{self.coach} -> {self.athlete} at {self.start_date}'
    
    class Meta:
        db_table = 'tb_coach_athlete'
        unique_together = ('athlete', 'coach')
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Athlete'))