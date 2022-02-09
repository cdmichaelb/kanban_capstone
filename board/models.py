from django.db import models
from users.models import CustomUser

# Create your models here.
class Kanban(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name

# TODO: Add Priority Model - Name - fk

class Column(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #priority = models.ForeignKey(PriorityModel) #, on_delete=models.CASCADE)
    kanban = models.ForeignKey(Column, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
# TODO: Possibly create new apps for notes and tags

class Note(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name