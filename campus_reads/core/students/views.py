from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('library:home_page')  # Adjust this to your login URL
    else:
        form = UserRegistrationForm()
    return render(request, 'students/register.html', {'form': form})
