
from django.db import models
from user_data.models import UserProfile

class DailyTrainRecord(models.Model):
    # Fields
    athlete = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='daily_train_record', help_text='運動員')
    date = models.DateField(help_text='訓練日期')
    # 以田徑選手為例
    distance = models.FloatField(help_text='跑步距離 (公里)')
    time = models.TimeField(help_text='跑步時間')
    description = models.TextField(max_length=255, help_text='訓練描述')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    # Metadata
    class Meta:
        ordering = ['-athlete', '-date']

    # Methods
    def __str__(self):
        return f"{self.athlete.name} - {self.date}"
    
    
class RaceRecord(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    athlete = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='race_record', help_text='運動員')
    date = models.DateField(help_text='比賽日期')
    race_name = models.CharField(max_length=10, help_text='比賽名稱')
    description = models.TextField(max_length=255, help_text='比賽描述')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Metadata
    class Meta:
        ordering = ['-athlete', '-date']

    # Methods
    def __str__(self):
        """String for representing the Race object (in Admin site etc.)."""
        return f"{self.athlete.name} - {self.race_name} ({self.date})"


class HurtRecord(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    athlete = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hurt_records', help_text='運動員')
    date = models.DateField(help_text='受傷日期')
    injury_type = models.CharField(max_length=10, help_text='受傷部位')
    description = models.TextField(max_length=255, help_text='受傷描述')
    injure_date = models.DateField(help_text='受傷日期')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Metadata
    class Meta:
        ordering = ['-athlete', 'date']

    # Methods
    def __str__(self):
        """String for representing the Hurt object (in Admin site etc.)."""
        return f"{self.athlete.name} - {self.type} ({self.date})"
    
    
class BasicInfo(models.Model):
    athlete = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='basic_info', help_text='運動員')
    age = models.SmallIntegerField(help_text='年齡')
    height = models.FloatField(help_text='身高')
    weight = models.FloatField(help_text='體重')
    BMI = models.FloatField(help_text='BMI')
    musule_mass = models.FloatField(help_text='肌肉量')
    body_fat = models.FloatField(help_text='體脂率')
    test_date = models.DateField(help_text='測試日期')
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Metadata
    class Meta:
        ordering = ['-athlete']

    # Methods
    def __str__(self):
        return f"{self.athlete.name} - {self.age} (建於: {self.created_at}, 更新: {self.updated_at})"


class PhysicalTest(models.Model):
    athlete = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='physical_test', help_text='運動員')
    
    vertical_jump = models.FloatField(help_text='垂直跳 (cm)', blank=True, null=True)
    agility = models.FloatField(help_text='敏捷性 (秒)', blank=True, null=True)
    grip_strength = models.FloatField(help_text='握力', blank=True, null=True)
    sprint_30m = models.FloatField(help_text='30M衝刺', blank=True, null=True)
    back_muscle_strength = models.FloatField(help_text='背肌力', blank=True, null=True)
    aerobic_fitness = models.FloatField(help_text='有氧適能', blank=True, null=True)
            
    test_date = models.DateField(help_text='測試日期')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Metadata
    class Meta:
        ordering = ['-athlete', 'test_date']

    # Methods
    def __str__(self):
        return f"{self.athlete.name} - {self.test_date}"