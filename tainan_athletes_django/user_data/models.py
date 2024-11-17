from django.contrib.auth.models import User
from django.db import models

class Athlete(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='使用者')
    name = models.CharField(max_length=10, help_text='運動員姓名')
    coach = models.ForeignKey('Coach', on_delete=models.CASCADE)
    school = models.CharField(max_length=30, help_text='所屬學校')
    phone = models.CharField(max_length=10, help_text='聯絡電話')
    mail = models.EmailField(max_length=50, help_text='電子郵件')
    guardian = models.CharField(max_length=10, help_text='監護人 (姓名/稱謂)')
    emr_phone = models.CharField(max_length=10, help_text='緊急聯絡電話')
    address = models.CharField(max_length=50, help_text='地址')
    birth = models.DateField(help_text='生日')
    image = models.ImageField(upload_to='uploads/athlete/', blank=True, null=True)
    
                                 
    # Metadata
    class Meta:
        ordering = ['name']
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    # Methods
    def __str__(self):
        """String for representing the Athlete object (in Admin site etc.)."""
        return self.name


class Coach(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='使用者')
    name = models.CharField(max_length=10, help_text='教練姓名')
    school = models.CharField(max_length=30, help_text='所屬學校')
    phone = models.CharField(max_length=10, help_text='聯絡電話')
    mail = models.EmailField(help_text='電子郵件')
    image = models.ImageField(upload_to='uploads/coach/', blank=True, null=True)
    
    # Metadata
    class Meta:
        ordering = ['name']

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    # Methods
    def __str__(self):
        return self.name
    
    