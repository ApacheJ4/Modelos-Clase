from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import render
from django.utils.timezone import localtime


# Create your views here.

def Portada(request):
    if request.user.is_authenticated:
        # Convertimos la hora actual y el último inicio de sesión a la hora local
        last_login = localtime(request.user.last_login) if request.user.last_login else None
        current_time = localtime(timezone.now())
    else:
        last_login = None
        current_time = None

    return render(request, 'registration/portada.html', {
        'last_login': last_login,
        'current_time': current_time,
    })

class SignupView(CreateView):
    form_class=UserCreationForm
    success_url= reverse_lazy("login")
    template_name= "registration/signup.html"
