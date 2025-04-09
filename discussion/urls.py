from django.urls import path
from .views import *

urlpatterns = [
    path('ask/', AskQuestionView.as_view(), name='ask-question'),
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('answers/<int:pk>/vote/<str:action>/', vote_answer, name='answer-vote'),
    path('questions/similar/', similar_questions, name='similar-questions'),
    path('my-questions/', MyQuestionsView.as_view(), name='my-questions'),
    path('edit-question/<int:pk>/', EditQuestionView.as_view(), name='edit-question'),
]
