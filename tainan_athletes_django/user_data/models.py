from django.contrib.auth.models import User, Group
from django.db import models
from django.core.files import File

import os
from io import BytesIO
from PIL import Image
# from rest_framework.response import Response

class UserProfile(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', help_text='使用者', primary_key=True, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='profile', help_text='使用者群組')
    gender = models.CharField(choices=[('M', '男'), ('F', '女'), ('O', '其他')], max_length=1, default='M')
    name = models.CharField(max_length=10, help_text='姓名', null=True)
    email = models.EmailField(help_text='電子郵件', blank=True, null=True)
    school = models.CharField(max_length=30, help_text='所屬學校/單位', null=True)
    linking = models.ManyToManyField('self', through='LinkInformation', through_fields=('link_A', 'link_B'), symmetrical=True)
    phone = models.CharField(max_length=10, help_text='聯絡電話', null=True)
    guardian = models.CharField(max_length=10, help_text='監護人 (姓名/稱謂)', blank=True, null=True)
    emr_phone = models.CharField(max_length=10, help_text='緊急聯絡電話', blank=True, null=True)
    address = models.CharField(max_length=50, help_text='地址', blank=True, null=True)
    birth = models.DateField(help_text='生日', blank=True, null=True)
    avatar = models.ImageField(upload_to='uploads/profilePic/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/profilePic/thumbnail', blank=True, null=True)
    
                                 
    # Metadata
    class Meta:
        ordering = ['name']
        db_table = 'tb_user_profile'
        unique_together = ['name', 'gender', 'birth', 'school']
    
    def save(self, *args, **kwargs):
        # 檢查是否為管理員
        if self.group.name == 'Admin':
            self.user.is_staff = True
            self.user.save()
        
        # 新增對應群組
        self.user.groups.clear()
        self.group.user_set.add(self.user)
        
        # 刪除舊頭像/縮圖
        old_avatar = UserProfile.objects.get(pk=self.pk).avatar
        if old_avatar and old_avatar != self.avatar:
            if self.thumbnail:
                thumbnail_path = self.thumbnail.path
                if os.path.exists(thumbnail_path): os.remove(thumbnail_path)
                self.thumbnail.delete(save=False)
                
            avatar_path = old_avatar.path
            if os.path.exists(avatar_path): os.remove(avatar_path)
        
        # 新增頭像縮圖
        if self.avatar and not self.thumbnail:
            self.thumbnail = self.make_thumbnail(self.avatar, self.user.username)
        
        super().save()

    # 製作縮圖
    def make_thumbnail(self, image, name, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name = name+".jpeg")
        
        return thumbnail

    
    def __str__(self):
        """String for representing the Athlete object (in Admin site etc.)."""
        return f"{self.name} ({self.user.username})"


class LinkInformation(models.Model):
    link_A = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='link_A')
    link_B = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='link_B')
    start_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.link_A.name} <-> {self.link_B.name}'
    
    def save(self, *args, **kwargs):
        if self.link_A == self.link_B:
            raise ValueError('You cannot link a user to itself.')
        
        if self.link_A.group.name == self.link_B.group.name and self.link_A.group.name != 'admin':
            raise ValueError('You cannot link two users in the same group.')
        
        if self.link_A.group.name == 'Admin' or self.link_B.group.name == 'Admin':
            raise ValueError('You cannot link an admin.')
        
        if self.link_A not in self.link_B.linking.all():
            return self.link_B.linking.add(self.link_A)
        
        return super().save()
    
    class Meta:
        db_table = 'tb_link_information'
        unique_together = ('link_A', 'link_B')