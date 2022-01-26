from django.db import models

# Create your models here.
class Kanban(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=255)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Columns(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Notes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name