from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

# function based view
def register(request):
    # if it is a post request, we validate the form data
    if request.method == 'POST':
        # intsantiate the form with the Post data
        form = UserRegistrationForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            form.save()
            # the validated form data is in the form.cleaned_data dictionary
            username = form.cleaned_data.get('username')
            # flash message send sone time alert to the template
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    # else, we will simply display a blank form
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# we restrict the profile page to logged in users only
@login_required
def profile(request):
    if request.method == 'POST':

        # we populate the forms with the information of the current logged in user
        # These are model forms expecting to be working on a speciifc model object
        # we can populate the field of the form by passing an instance of the object that it expects

        # An instance of a user
        u_form = UserUpdateForm(data=request.POST, instance=request.user)
        # An instance of a profile
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        
        messages.success(request, "Your profile has been updated!")
        # we redirect here (post get redirect pattern)
        return redirect('profile')

    else:
        # An instance of a user
        u_form = UserUpdateForm(instance=request.user)
        # An instance of a profile
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)