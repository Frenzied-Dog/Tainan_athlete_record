
from django.db import models
from user_data.models import Athlete

class DailyTrainRecord(models.Model):
    # Fields
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='daily_train_record', help_text='運動員')
    date = models.DateField(help_text='訓練日期')
    # 以田徑選手為例
    distance = models.FloatField(help_text='跑步距離 (公里)')
    time = models.TimeField(help_text='跑步時間')
    description = models.TextField(max_length=255, help_text='訓練描述')
    
    
    # Metadata
    class Meta:
        ordering = ['-athlete', '-date']

    # Methods
    def __str__(self):
        return f"{self.athlete.name} - {self.date}"
    
    
class RaceRecord(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='race_record', help_text='運動員')
    date = models.DateField(help_text='比賽日期')
    race_name = models.CharField(max_length=10, help_text='比賽名稱')
    description = models.TextField(max_length=255, help_text='比賽描述')
    
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
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='hurt_records', help_text='運動員')
    date = models.DateField(help_text='受傷日期')
    type = models.CharField(max_length=10, help_text='受傷部位')
    description = models.TextField(max_length=255, help_text='受傷描述')
    
    # Metadata
    class Meta:
        ordering = ['-athlete', 'date']

    # Methods
    def __str__(self):
        """String for representing the Hurt object (in Admin site etc.)."""
        return f"{self.athlete.name} - {self.type} ({self.date})"