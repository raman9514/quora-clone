from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Q
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


@method_decorator(login_required, name='dispatch')
class AskQuestionView(View):
    def get(self, request):
        form = QuestionForm()
        return render(request, 'discussion/ask_question.html', {'form': form})

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('my-questions')
        return render(request, 'discussion/ask_question.html', {'form': form})


class QuestionListView(View):
    def get(self, request):
        questions = Question.objects.select_related('user').order_by('-created_at')
        return render(request, 'discussion/question_list.html', {'questions': questions})


@method_decorator(login_required, name='dispatch')
class QuestionDetailView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        form = AnswerForm()
        answers = question.answers.select_related('user').prefetch_related('upvote', 'downvote').order_by('-created_at')
        return render(request, 'discussion/question_detail.html', {
            'question': question,
            'form': form,
            'answers': answers,
        })

    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question-detail', pk=pk)
        answers = question.answers.select_related('user').order_by('-created_at')
        return render(request, 'discussion/question_detail.html', {
            'question': question,
            'form': form,
            'answers': answers,
        })


@method_decorator(login_required, name='dispatch')
class MyQuestionsView(View):
    def get(self, request):
        questions = Question.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'discussion/my_questions.html', {'questions': questions})


@method_decorator(login_required, name='dispatch')
class EditQuestionView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk, user=request.user)
        form = QuestionForm(instance=question)
        return render(request, 'discussion/edit_question.html', {'form': form})

    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk, user=request.user)
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('my-questions')
        return render(request, 'discussion/edit_question.html', {'form': form})


@login_required
@require_POST
def vote_answer(request, pk, action):
    answer = get_object_or_404(Answer, pk=pk)
    if action == 'up':
        answer.upvote.add(request.user)
        answer.downvote.remove(request.user)
    elif action == 'down':
        answer.downvote.add(request.user)
        answer.upvote.remove(request.user)
    return render(request, 'discussion/partials/vote_buttons.html', {'answer': answer, 'user': request.user})


def similar_questions(request):
    # here we can use the Elastic Search instead of using icontains
    query = request.GET.get('question', '')
    if not query:
        return HttpResponse("")

    matches = Question.objects.filter(
        Q(question__icontains=query)
    ).order_by('-created_at')[:5]  #suppose its elastic search

    return render(request, 'discussion/partials/similar_questions.html', {'matches': matches})
