from django.db import models
from home.models import *
# Create your models here.
DAY_CHOICE = {
    'sunday': 'Sunday',
    'monday': 'Monday',
    'tuesday': 'Tuesday',
    'wednesday': 'Wednesday',
    'thursday': 'Thursday',
    'friday': 'Friday',
    'saturday': 'saturday',
}


class Shedule(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    day = models.CharField(choices=DAY_CHOICE, default='sunday', max_length=500)

    shift1_course = models.CharField(max_length=500, blank=True, null=True, verbose_name='Course Name')
    shift1_room = models.CharField(max_length=500, blank=True, null=True, verbose_name='Romm no.')
    shift1_faculty = models.CharField(max_length=500, blank=True, null=True, verbose_name='Faculty details')

    shift2_course = models.CharField(max_length=500, blank=True, null=True, verbose_name='Course Name')
    shift2_room = models.CharField(max_length=500, blank=True, null=True, verbose_name='Romm no.')
    shift2_faculty = models.CharField(max_length=500, blank=True, null=True, verbose_name='Faculty details')

    shift3_course = models.CharField(max_length=500, blank=True, null=True, verbose_name='Course Name')
    shift3_room = models.CharField(max_length=500, blank=True, null=True, verbose_name='Romm no.')
    shift3_faculty = models.CharField(max_length=500, blank=True, null=True, verbose_name='Faculty details')

    shift4_course = models.CharField(max_length=500, blank=True, null=True, verbose_name='Course Name')
    shift4_room = models.CharField(max_length=500, blank=True, null=True, verbose_name='Romm no.')
    shift4_faculty = models.CharField(max_length=500, blank=True, null=True, verbose_name='Faculty details')

    shift5_course = models.CharField(max_length=500, blank=True, null=True, verbose_name='Course Name')
    shift5_room = models.CharField(max_length=500, blank=True, null=True, verbose_name='Romm no.')
    shift5_faculty = models.CharField(max_length=500, blank=True, null=True, verbose_name='Faculty details')

    shift6_course = models.CharField(max_length=500, blank=True, null=True, verbose_name='Course Name')
    shift6_room = models.CharField(max_length=500, blank=True, null=True, verbose_name='Romm no.')
    shift6_faculty = models.CharField(max_length=500, blank=True, null=True, verbose_name='Faculty details')

    def __str__(self):
        return f"{self.day}: {self.department.name}"