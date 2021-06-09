from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.conf import re_path
from .models import User
from .models import Sign
import hashlib
from django.shortcuts import redirect
from django.http import HttpResponse
import sys


def get_name(request, *args, **kwargs):
    # print(args)
    print(request.method)
    # print(form.cleaned_data['your_name'])
    # if this is a POST request we need to process the form data
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        # check whether it's valid:

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        context = {}
        a = request.POST['your_name']
        print(a)
        b = hashlib.md5(str(a).encode()).hexdigest()
        try:
            if (User.objects.get(pk=b[:5])):
                if (str(User.objects.get(pk=b[:5]).login) == request.session['username']):
                    context['post'] = b[:5]
                    return render(request, 'name.html', context)
                else:
                    print("dfdsfsdzdcnsdcnsknkx v,mdx v, ckzc z,mdc sdc skc sm")
                    context['post'] = 'Wrong User'
                    return render(request, 'name.html', context)

            print(a, b)
        except:
            try:
                if request.session['username']:
                    c = request.session['username']

                    c = (Sign.objects.get(pk=c))

                    reg = User(name=a, id=b[:5], login=c)
                    print(request)

                    reg.save()
                    l = User.objects.filter(s_name=b).first()
                    # a = (User.objects.get(pk=b[:3]))
                    # b = a.name
                    context['post'] = 'http://127.0.0.1:8000/'+b[:5]

                    return render(request, 'name.html', context)
            except:
                return redirect("/login")

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'name.html')


def get_url(request, *args, **kwargs):
    print(request.method, args, kwargs)
    # redirect(User.get(pk=request.path[1:]))

    try:
        a = (User.objects.get(pk=request.path[1:]))
        return redirect(a.name)
    except:
        print(request.path[1:])
        return render(request, 'name.html', {})
    # create a form instance and populate it with data from the request:
    # if request.method == 'POST':
    #     form = urlForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():

    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         a = form.cleaned_data['your_url']
    #         print(a)
    #         l = User.objects.get(pk=a)
    #         print(l.name)
    #         return redirect(l.name)
    #         # print(l)
    # else:
    #     form = urlForm()

    # return render(request, 'list.html')


def get_list(request):
    context = {'li': [],
               'df': []}
    try:
        for i in User.objects.all():
            print(i.login)
            print(1, request.session['username'])
            if str(i.login) == request.session['username']:
                print(2, i.login)
                context['li'].append([i.name, i.id])
    except:
        return redirect('/login')

    return render(request, 'list.html', context)


def get_del(request, **kwargs):
    # print("dhsjfhdsjsdfsdgfdgdskndsjfdskjfhksjzdcbm,zscbmzxcbmzbcmzscbkzjscbjzskcbzsjhcjzscbjzshxjzscjdzshckjzsbcfjzsgfjzsbfvjsdzbfjxzdhvjxdbf")
    print(kwargs['id'])
    id = kwargs['id']
    User.objects.filter(id=kwargs['id']).delete()
    return redirect("/list")


def get_sign(request):
    if request.method == 'POST':

        a = request.POST.get('User_name')

        b = request.POST.get('Password')
        if len(b) == 0:
            context = {
                'a': 'password should not be empty'}
            return render(request, 'signup.html', context)

        reg = Sign(username=a, password=b)
        reg.save()
        return redirect('/login')
    return render(request, 'signup.html')


def get_login(request):
    try:
        if (request.session['username']) != None:
            print(request.session['username'])
            context1 = {'a': "Already logged in"}
        return render(request, 'name.html', context1)

    except:
        if request.method == 'POST':
            a = request.POST.get('User_name')
            b = request.POST.get('Password')
            try:
                c = (Sign.objects.get(pk=a))
                if b == c.password and b != None:

                    request.session['username'] = a
                    return redirect('/')
            except:
                context = {
                    'a': 'password or username not match or please enter correct password'}
                return render(request, 'login.html', context)
        # print(request.session['username'])
    return render(request, 'login.html', {})


def logout(request):
    try:
        del request.session['username']
        return redirect("/")
    except:
        context = {'a': 'Please login to logout'}
        return render(request, 'login.html', context)
