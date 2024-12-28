# account/views.py

# 📦 Import necessary modules, classes and functions
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Define the login view function
def login_view(request):
    if request.user.is_authenticated:
        # If user is already authenticated, redirect to the next URL or home page
        next_url = request.GET.get('next', 'index')
        return redirect(next_url)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ✅ If user is authenticated, log them in and redirect to the next URL
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            # ❌ Error message for invalid login attempt
            error_message = 'Invalid username or password'
    else:
        error_message = None
    # 🎨 Render login page with error message (if any)
    return render(request, 'login.html', {'error_message': error_message})

 # 🔑 Only authenticated users can access this view
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
