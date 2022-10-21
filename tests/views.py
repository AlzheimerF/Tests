from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import TestSet, Questions_and_answers, QAAU, TestSetAU
from .forms import CreateQA, CreateTestSet
from django.contrib.auth.forms import UserCreationForm

def list_test(request):
    context = {}
    tests = TestSet.objects.all()
    tests_au = TestSetAU.objects.all()
    context['tests'] = tests
    context['tests_au'] = tests_au
    return render(request, 'test_sets/list_test.html', context)

def use_test(request, id):
    context = {}
    points = int()
    unpoints = int()
    correct_answers = []
    wrong_answers = []
    tests = TestSet.objects.get(id=id)
    questions_and_answers = Questions_and_answers.objects.filter(test=id)
    context['tests'] = tests
    context['questions_and_answers'] = questions_and_answers
    if request.method == "POST":
        for question in questions_and_answers:
            if request.POST.get(f'Answer{question.id}') == question.correct_answer:
                points += 1
                correct_answers.append(question.title)
            else:
                unpoints += 1
                wrong_answers.append(question.title)
        proccent = points / len(questions_and_answers) * 100
        context['points'] = points
        context['unpoints'] = unpoints
        context['correct_answers'] = correct_answers
        context['wrong_answers'] = wrong_answers
        context['proccent'] = proccent
    return render(request, 'test_sets/using_test.html', context)

def use_test_au(request, id):
    context = {}
    points = int()
    unpoints = int()
    correct_answers = []
    wrong_answers = []
    tests = TestSetAU.objects.get(id=id)
    questions_and_answers = QAAU.objects.filter(test=id)
    context['tests'] = tests
    context['questions_and_answers'] = questions_and_answers
    if request.method == "POST":
        for question in questions_and_answers:
            if request.POST.get(f'Answer{question.id}') == question.correct_answer:
                points += 1
                correct_answers.append(question.title)
            else:
                unpoints += 1
                wrong_answers.append(question.title)
        proccent = points / len(questions_and_answers) * 100
        context['points'] = points
        context['unpoints'] = unpoints
        context['correct_answers'] = correct_answers
        context['wrong_answers'] = wrong_answers
        context['proccent'] = proccent
    return render(request, 'test_sets/using_test_au.html', context)

def add_test_set(request):
    form = CreateTestSet()
    if request.method == "POST":
        form = CreateTestSet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_')
    else:
        form = CreateTestSet()
    return render(request, 'test_sets/create_test_set.html', context={'form': form})

def add_answer_and_question(request):
    form = CreateQA()
    if request.method == "POST":
        form = CreateQA(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_')
    else:
        form = CreateQA()
    return render(request, 'test_sets/create_answer_and_question.html', context={'form': form})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', context={'form': form})

def list_of_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users/list_of_users.html', context=context)

def list_qa(request):
    context = {}
    qa = Questions_and_answers.objects.all()
    qa_au = QAAU.objects.all()
    context['qa'] = qa
    context['qa_au'] = qa_au
    return render(request, 'test_sets/list_qa.html', context=context)

def delete_test(request, id):
    test = TestSet.objects.get(id=id)
    test.delete()
    return redirect('list_')

def delete_qa(request, id):
    qa = Questions_and_answers.objects.get(id=id)
    qa.delete()
    return redirect('list_qa')
