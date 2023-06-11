from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .forms import CustomUserCreationForm

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")

        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})
