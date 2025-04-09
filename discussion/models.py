from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(null=True,blank=True)
    #category = models.CharField(null=True,blank=True) # can be used later

    def __str__(self):
        return self.question

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = CKEditor5Field('answer', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvote = models.ManyToManyField(User, related_name='upvote', blank=True)
    downvote = models.ManyToManyField(User, related_name='downvote', blank=True)
    # redundent but helps in optimization
    upvote_count = 0
    downvote_count = 0

    def update_upvote_count(self):
        self.upvote_count = self.upvote.count()
        self.save()
    
    def update_downvote_count(self):
        self.downvote_count = self.downvote.count()
        