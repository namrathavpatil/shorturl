from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .forms import NameForm, urlForm
import hashlib
from django.shortcuts import redirect
from django.http import HttpResponse


def get_name(request, *args, **kwargs):
    # print(args)
    print(request.method)
    # print(form.cleaned_data['your_name'])
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            context = {}
            a = form.cleaned_data['your_name']
            print(a)
            b = hashlib.md5(str(a).encode()).hexdigest()
            print(a, b)
            reg = User(name=a, id=b[:3])

            reg.save()
            l = User.objects.filter(s_name=b).first()
            context['e'] = b[:3]
        return render(request, 'name.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def get_url(request, *args, **kwargs):
    # print(request.method)
    # redirect(User.get(pk=request.path[1:]))
    try:
        a = (User.objects.get(pk=request.path[1:]))
        return redirect(a.name)
    except:
        print(request.path[1:])
        return render(request, 'list.html', {})
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
