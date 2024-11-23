from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', help_text='使用者', primary_key=True)
    gender = models.CharField(choices=[('M', '男'), ('F', '女'), ('O', '其他')], max_length=1, default='M')
    name = models.CharField(max_length=10, help_text='姓名', null=True)
    # identity = models.CharField(choices=[('Ath', '運動員'), ('Coach', '教練')], max_length=5, default='Ath')
    school = models.CharField(max_length=30, help_text='所屬學校', null=True)
    linking = models.ManyToManyField('self', through='LinkInformation', through_fields=('link_A', 'link_B'))
    phone = models.CharField(max_length=10, help_text='聯絡電話', null=True)
    # mail = models.EmailField(max_length=50, help_text='電子郵件', null=True)
    guardian = models.CharField(max_length=10, help_text='監護人 (姓名/稱謂)', null=True)
    emr_phone = models.CharField(max_length=10, help_text='緊急聯絡電話', null=True)
    address = models.CharField(max_length=50, help_text='地址', null=True)
    birth = models.DateField(help_text='生日', null=True)
    avatar = models.ImageField(upload_to='uploads/profilePic/', blank=True, null=True)
    
                                 
    # Metadata
    class Meta:
        ordering = ['name']
        db_table = 'tb_user_profile'
        unique_together = ['name', 'gender', 'birth', 'school']
    
    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        return ''

    # Methods
    def __str__(self):
        """String for representing the Athlete object (in Admin site etc.)."""
        return self.name


class LinkInformation(models.Model):
    link_A = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='link_A')
    link_B = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='link_B')
    start_date = models.DateField()
    
    def __str__(self):
        return f'{self.link_A.name} <-> {self.link_B.name} at {self.start_date}'
    
    class Meta:
        db_table = 'tb_link_information'
        unique_together = ('link_A', 'link_B')