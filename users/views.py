from django.shortcuts import render, redirect

from .forms import AccountCreationForm


def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountCreationForm()
    return render(request, 'signup.html', {'form': form})
