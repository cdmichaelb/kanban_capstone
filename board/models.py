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
    
class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date_joined',)
    def __str__(self):
        return self.username

class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
    
class Column(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
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