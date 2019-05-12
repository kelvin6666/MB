from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, User, UserUpdateForm, ProfileUpdateForm
from QnA.models import comment,question
from django.views.generic import ListView
from .models import Reward

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #adds user to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account: {username}. Please login and add a Profile Picture!')
            return redirect("profile_update")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class ProfileListView(ListView):
    model = question
    template_name : 'users/profile.html'
    context_object_name = 'question'
    ordering = ['-date_published']
    paginate_by = 5


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update.html', context)



    








