from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth import logout

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want
        return render(request, 'register.html', {'form': form})


class LoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    


def logout_view(request):
    logout(request)
    return redirect('home')
