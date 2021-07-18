from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}Account Has been created.You are able to login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
