from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Joke, Addition
from .forms import JokesForm, AdditionsForm, RegisterUserForm, LoginUserForm


def index(request):
    jokes = Joke.objects.all()
    return render(request, 'jokes/index.html',{'title':'Главная страничка', 'jokes':jokes})


# class JokesList(ListView):
#     models = Joke

# class JokeList(CreateView):
#     form_class = JokesForm
#     template_name = 'jokes/list_of_jokes.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         success_url = reverse_lazy('jokeslist')
#         return context


def list_of_jokes(request):
    error = ''
    if request.method == 'POST':
        form = JokesForm(request.POST)
        if form.is_valid():
            joke = form.save(commit=False)
            joke.creator = request.user
            joke.save()
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
            add = form.save(commit=False)
            add.joke_id = post
            add.save()
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

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'jokes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'jokes/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')