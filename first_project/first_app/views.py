from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, LoginInfo
from first_app import forms
from first_app.forms import NewUserForm
import requests
from first_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
# def index(request):
#     webpage_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records': webpage_list}
#
#     return render(request, 'index.html', context=date_dict)


def myStr(request):
    return HttpResponse("<em>Its ur boi ajay</em>")


def index1(request):
    my_dict = {'add_me': 'Hello this is from views.py'}
    return render(request, 'index1.html', context=my_dict)


def index2(request):
    return render(request, 'index2.html')


def api(request):
    url = "http://calapi.inadiutorium.cz/api/v0/en/calendars/default"
    data = requests.get(url)
    my_dict = {'data1': data.json()}
    return render(request, 'jsondata.html', context=my_dict)


def users(request):
    users_list = LoginInfo.objects.order_by('first_name')
    users_dict = {'users': users_list}

    return render(request, 'users.html', context=users_dict)


def index(request):
    return render(request, 'basicApp/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Textarea: " + form.cleaned_data['text'])
    return render(request, 'basicApp/form_page.html', {'form': form})


def index_users(request):
    return render(request, "login/index.html")


def users_sign_up(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index_users(request)
        else:
            print("ERROR form invalid")
    return render(request, 'login/users.html', {'form': form})


def index_four(request):
    my_context = {'text': "Hello all", 'number': 100}
    return render(request, 'learning_templates/index.html', my_context)


def other_four(request):
    return render(request, 'learning_templates/other.html')


def relative_four(request):
    return render(request, 'learning_templates/relative_url.html')


def index_five(request):
    return render(request, 'register/index.html')


def register_five(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'register/registration.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index_five'))
            else:
                return HttpResponseRedirect("Account Not active")
        else:
            print("Someone tried to login and failed!")
            print("Username:{} and password {}".format(username, password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request, 'register/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_five'))

@login_required
def special(request):
    return HttpResponse("You are logged in Nice!")
