from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

@require_http_methods(['GET','POST'])
def signup(request):
    # 로그인한 사용자가 들어오면 ???
    if request.user.is_authenticated:
        return redirect('boards:index')

    #  METHOD가 GET일 때와 POST일 때 
    # POST : 실제로 회원가입을 진행
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 유저 정보를 저장한 이후에, 회원 가입 즉시 로그인 
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')

    # GET : 회원가입 페이지를 보여줘야함 
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def login(request):
    # 로그인한 사용자가 들어오면 ???
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    if request.method == 'POST':
        # 여기가 달라지네
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유저를 저장할 필요 없이 그냥 로그인 
            auth_login(request, form.get_user())
            return redirect('boards:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html', context)

@require_POST
def logout(request):
    # 로그인된 사용자만 로그아웃 
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('boards:index')