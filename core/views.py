from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Forma yaratildi')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'signup.html', context)
    

def recover(request):
    return render(request, 'recover.html')