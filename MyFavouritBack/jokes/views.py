from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Joke, Addition
from .forms import JokesForm, AdditionsForm


def index(request):
    jokes = Joke.objects.all()
    return render(request, 'jokes/index.html',{'title':'Главная страничка', 'jokes':jokes})


def list_of_jokes(request):
    error = ''
    if request.method == 'POST':
        form = JokesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    jokes = Joke.objects.all()
    form = JokesForm()
    context = {
        'title': 'Главная страничка',
        'jokes': jokes,
        'form':form,
        'error': error
        }
    return render(request, 'jokes/list_of_jokes.html', context)


def show_post(request, post_id):
    post = get_object_or_404(Joke, pk=post_id)
    addition = post.addition_set.all()
    error = ''
    if request.method == 'POST':
        # form = AdditionsForm(data = request.POST, joke_id=post_id)
        form = AdditionsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    form = AdditionsForm
    context = {
        'post': post,
        'title': post.title,
        'addition': addition,
        'form': form,
        'error': error
    }
    return render(request, 'jokes/post.html',context)

