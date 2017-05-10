from django.shortcuts import  redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import ChangeUser
from django.contrib.auth.models import User

def login(request): #вход в систему/авторизация
    args={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден" #если введён незарегестрированый юзер
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request): #функция выйти из системы
    auth.logout(request)
    return redirect('/')




def register(request ): #функция регистрации нового пользователя
    args = {}
    args.update(csrf(request))
    args['form']= UserCreationForm()
 
    if request.POST:
        newuser_form = UserCreationForm (request.POST)
        if newuser_form.is_valid():
            username = newuser_form.cleaned_data['username']
            password1 = newuser_form.cleaned_data['password1']
            password2 = newuser_form.cleaned_data['password2']
           
            newuser_form.save()
            new_user = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, new_user)  # сразу авторизуем если всё валидно/без ошибок
            return redirect('/')
        else:
            args['form'] = newuser_form  # если есть ошибки, снова на странтцу регистрации
    return render_to_response('register.html' , args)


def changeuser(request ): #функция редактирования пользователя
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form']= ChangeUser()
    if request.POST:
        changeuser_form = ChangeUser(request.POST, request.FILES)
    
        print(changeuser_form)
        if changeuser_form.is_valid():
        
           changeuser_form.save()
           return redirect('/')
        else:
            args['form'] = changeuser_form  # если есть ошибки, снова на странтцу регистрации
    return render_to_response('usersettings.html' , args)




def acc(request): 
    args = {}
    args['username'] = auth.get_user(request).username
    args['user'] = request.user
    print(args)
    return render_to_response('akk.html', args)