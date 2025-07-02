from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.id}. {self.name}"
    

class Batch(models.Model):
    depertment = models.ForeignKey(Department, related_name='depertment', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.id}: {self.depertment.name}.  {self.name}"
    

class Routeen(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    pdf_file = models.FileField(upload_to='routeens/')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id}. {self.depertment.name} {self.title}"