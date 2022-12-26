from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, View
from .models import Joke, Addition, Profile, User
from .forms import JokesForm, AdditionsForm, RegisterUserForm, LoginUserForm, RatingForm, UserEditForm, ProfileEditForm


def index(request):
    profile1 = Profile.objects.order_by('-rating')[0]
    profile2 = Profile.objects.order_by('-rating')[1]
    profile3 = Profile.objects.order_by('-rating')[2]

    """Объединяет заданный шаблон с заданным контекстным словарем и возвращает 
    объект HttpResponse с результирующим текстом. (содержит метаданные о запросе)"""
    return render(request, 'jokes/index.html', {'title':'Главная страничка','profiles1':profile1, 'profiles2': profile2, 'profiles3':profile3 })


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
    # то, к чему можно обращаться в html:
    context = {
        'title': 'Главная страничка',
        'jokes': jokes,
        'form':form,
        'error': error
        }
    return render(request, 'jokes/list_of_jokes.html', context)


def show_post(request, post_id):
    post = get_object_or_404(Joke, pk=post_id)
    print(post.time_created)
    addition = post.addition_set.all()
    error = ''
    if request.method == 'POST' and 'add_addition' in request.POST:
        """если нажата кнопка добавления добивки"""
        print("REQUEST.POST")
        print(request.POST)
        form = AdditionsForm(request.POST)
        if form.is_valid():
            """если введенная добивочная форма валидна"""
            add = form.save(commit=False)
            add.joke_id = post
            add.creator = request.user
            add.rating = 0
            add.save()
            return redirect('post',post_id)
        else:
            error = 'Форма была неверной'
    elif request.method == 'POST' and 'sort' in request.POST:
        form = AdditionsForm
        addition = addition.order_by('-time_created')
        context = {
            'post': post,
            'title': post.title,
            'addition': addition,
            'form': form,
            'error': error,
        }
        return render(request, 'jokes/post.html', context)
    elif request.method == 'POST' and 'sort1' in request.POST:
        form = AdditionsForm
        addition = addition.order_by('-rating')
        context = {
            'post': post,
            'title': post.title,
            'addition': addition,
            'form': form,
            'error': error,
        }
        return render(request, 'jokes/post.html', context)
    elif request.method == 'POST' and 'add_addition' not in request.POST and 'sort' not in request.POST:
        """если нажата кнопка лайка"""
        get_id = request.POST['name']
        instance = get_object_or_404(Addition, id=get_id)
        form = AdditionsForm(instance=instance)
        add = form.save(commit=False)
        if request.user not in add.marked_by_users.filter():
            """если пользователь еще не отмечал данную добивку"""
            add.rating += 1
            add.marked_by_users.add(request.user)
            add.save()
            """добавляем рейтинг автору добивки"""
            add.creator.profile.rating += 1
            add.creator.profile.save()
        else:
            add.rating -= 1
            add.marked_by_users.remove(request.user)
            add.save()
            """добавляем рейтинг автору добивки"""
            add.creator.profile.rating -= 1
            add.creator.profile.save()
    form = AdditionsForm
    context = {
        'post': post,
        'title': post.title,
        'addition': addition,
        'form': form,
        'error': error,
    }
    return render(request, 'jokes/post.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'jokes/register.html'
    # instance
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        login(self.request, user)
        # http
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'jokes/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        # string
        return reverse('home')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile_page(request):
    return render(request, 'jokes/user_profile.html')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'jokes/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def profile_info(request, user_id):
    prof = get_object_or_404(User, pk=user_id)
    print(prof)
    context = {
        'user_other': prof
    }
    return render(request, 'jokes/profile_info.html', context)


