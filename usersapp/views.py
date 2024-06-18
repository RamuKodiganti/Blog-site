from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'usersapp/register.html', {'form':form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')