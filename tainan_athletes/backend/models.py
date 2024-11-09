from django.db import models
from django.urls import reverse
import uuid

class Athlete(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    unique_id = models.UUIDField(help_text='運動員id', primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=10, help_text='運動員姓名')
    coach = models.ForeignKey('Coach', on_delete=models.CASCADE)
    school = models.CharField(max_length=30, help_text='所屬學校')
    phone = models.CharField(max_length=10, help_text='聯絡電話')
    mail = models.EmailField(max_length=50, help_text='電子郵件')
    guardian = models.CharField(max_length=10, help_text='監護人 (姓名/稱謂)')
    emr_phone = models.CharField(max_length=10, help_text='緊急聯絡電話')
    address = models.CharField(max_length=50, help_text='地址')
    birth = models.DateField(help_text='生日')
                                 
    # Metadata
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Athlete."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the Athlete object (in Admin site etc.)."""
        return self.name


class Coach(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    unique_id = models.UUIDField(help_text='教練id', primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=10, help_text='教練姓名')
    school = models.CharField(max_length=30, help_text='所屬學校')
    phone = models.CharField(max_length=10, help_text='聯絡電話')
    mail = models.EmailField(max_length=50, help_text='電子郵件')
    
    # Metadata
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Coach."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the Coach object (in Admin site etc.)."""
        return self.name
    

class HurtRecord(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    athlete_id = models.ForeignKey(Athlete, on_delete=models.CASCADE, help_text='運動員id')
    date = models.DateField(help_text='受傷日期')
    type = models.CharField(max_length=10, help_text='受傷部位')
    description = models.CharField(max_length=50, help_text='受傷描述')
    
    # Metadata
    class Meta:
        ordering = ['-athlete_id', 'date']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Hurt."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the Hurt object (in Admin site etc.)."""
        return self.name

    
class RaceRecord(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    athlete_id = models.ForeignKey(Athlete, on_delete=models.CASCADE, help_text='運動員id')
    date = models.DateField(help_text='比賽日期')
    race_name = models.CharField(max_length=10, help_text='比賽名稱')
    description = models.CharField(max_length=50, help_text='比賽描述')
    
    # Metadata
    class Meta:
        ordering = ['-athlete_id', 'date']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Race."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the Race object (in Admin site etc.)."""
        return self.name
    
class DailyTrainRecord(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    athlete_id = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    date = models.DateField(help_text='訓練日期')
    # 以田徑選手為例
    distance = models.FloatField(help_text='跑步距離 (公里)')
    time = models.TimeField(help_text='跑步時間')
    description = models.CharField(max_length=50, help_text='訓練描述')
    
    
    # Metadata
    class Meta:
        ordering = ['-athlete_id', 'date']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Race."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the Race object (in Admin site etc.)."""
        return self.name