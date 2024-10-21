from django.shortcuts import render,redirect

from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate

from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required

from .models import record

# Create your views here.
def home(request):
    title = 'Index'
    return render(request, 'index.html', {'title': title})

#- register
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form,
               'title': 'Register'}

    return render(request, 'register.html', context= context)

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request,username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home')

    context= {'form': form,
                'title': 'Login'}

    return render(request, 'login.html',context)
@login_required(login_url='login')
def dashboard(request):

    record_ = record.objects.all()

    context = {'records': record_,
                'title': 'Dashboard'}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def create_record(request):
    record_ = record.objects.all()

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        province = request.POST['province']
        country = request.POST['country']
        sex = request.POST['gender']

        record_ = record(first_name=first_name,
        last_name=last_name,
        email=email, phone=phone,
        address=address, city=city,
        province=province, country=country,
        sex=sex)

        if record_:
            record_.save()
            return redirect('dashboard')


    return render(request, 'create-record.html')

@login_required(login_url='login')
def update_record(request, pk):
    pass

@login_required(login_url='login')
def delete_record(request, pk):
    pass

def user_logout(request):
    auth.logout(request)

    redirect('home')
    title = 'Logout'
    return render(request, 'index.html', {'title': title})
