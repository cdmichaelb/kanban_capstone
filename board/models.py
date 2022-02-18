from django.db import models
from users.models import CustomUser

# Create your models here.
class Kanban(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='kanbans')
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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE, related_name='columns')
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    index = models.IntegerField(default=0) # redundant
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')
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
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name