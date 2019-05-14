from django.contrib.auth.forms import UserCreationForm
#use reverse_lazy to redirect the user to the login page upon successful registration
from django.urls import reverse_lazy
from django.views import generic

#class SignUp(generic.CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'signup.html'

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import SignUpForm, EditProfileForm

# New user sign u
# p request
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, User)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# for displaying user profile information
def profile(request):
    args = {'user': request.user}

    return render(request, 'profile.html', args)


# enables user to edit his profile information
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

