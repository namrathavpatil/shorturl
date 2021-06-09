from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User

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
        print(a, b)
        reg = User(name=a, id=b[:5])
        print(request)

        reg.save()
        l = User.objects.filter(s_name=b).first()
        # a = (User.objects.get(pk=b[:3]))
        # b = a.name
        context['post'] = b[:5]

        return render(request, 'name.html', context)

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'name.html', context)


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
    for i in User.objects.all():
        context['li'].append([i.name, i.id])

    return render(request, 'list.html', context)


def get_del(request, id):
    # print("dhsjfhdsjsdfsdgfdgdskndsjfdskjfhksjzdcbm,zscbmzxcbmzbcmzscbkzjscbjzskcbzsjhcjzscbjzshxjzscjdzshckjzsbcfjzsgfjzsbfvjsdzbfjxzdhvjxdbf")
    print(id)
    User.objects.filter(id=id).delete()
    return redirect("/list")
