# authMaster/views.py

# 📁 Import necessary modules
from django.shortcuts import render

# Define the index view function
def index(request):
    # Check if the user is authenticated
    user = request.user if request.user.is_authenticated else None
    # Get the full name of the user if available, otherwise default to None
    full_name = user.get_full_name().title() if user and user.get_full_name() else None
    # If full name is not available, use username; if username is not available, default to "User"
    if not full_name:
        full_name = user.username if user else None
    if not full_name:
        full_name = "User"
    return render(request, 'index.html', {'user': user, 'full_name': full_name})
