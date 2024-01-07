from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.

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
            return redirect('blog-home')
    # else, we will simply display a blank form
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})