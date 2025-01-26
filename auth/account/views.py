# account/views.py

# 📦 Import necessary modules, classes and functions
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from oidc_provider.models import Token
from django.views.decorators.csrf import csrf_exempt

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
    next_url = request.GET.get('next', 'index')  # Default to `index` if not provided

    try:
        # Retrieve and delete all tokens associated with the user to invalidate them
        tokens = Token.objects.filter(user=request.user)
        if tokens.exists():
            tokens.delete()
            print(f"Deleted tokens for user: {request.user}")
        else:
            print("No tokens found for user.")
    except Exception as e:
        print(f"Error deleting tokens: {e}")

    # Log out the user locally (clear session)
    logout(request)

    return redirect(next_url)

@csrf_exempt
def auth_logout_view(request):
    next_url = request.GET.get('next', 'index')  # Default to `index` if not provided
    user_id = request.POST.get('user_id')  # Get the `user_id` (user ID) from the POST data
    print('request', request)
    print('user____id', user_id)

    try:
        # Retrieve and delete all tokens associated with the user to invalidate them
        tokens = Token.objects.filter(user=user_id)
        if tokens.exists():
            tokens.delete()
            print(f"Deleted tokens for user: {request.user}")
        else:
            print("No tokens found for user.")
    except Exception as e:
        print(f"Error deleting tokens: {e}")

    # Log out the user locally (clear session)
    logout(request)
    print(f"User logged out: {request.user}")

    # Delete the current session
    session_id = request.session.session_key
    print(session_id)

    request.session.flush()  # Clears the session data
    return redirect(next_url)
