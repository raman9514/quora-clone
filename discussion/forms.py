from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Question
from .models import Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your question here...',
                'rows': 4
            }),
        }



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        widgets = {
            'answer':CKEditor5Widget(attrs={'class': 'django_ckeditor_5', 'placeholder': 'Write your answer...'}),
        }
        
