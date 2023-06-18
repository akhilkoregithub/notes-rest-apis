from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    TEXT = "text"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE_TYPE_CHOICES = (
        (TEXT, "Text"),
        (AUDIO, "Audio"),
        (VIDEO, "Video"),
    )
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    note_type = models.CharField(max_length=5, choices=NOTE_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class NoteShare(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='shared_notes')
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_with_users')
    
    def __str__(self):
        return f'{self.note} shared with {self.shared_with.username}'