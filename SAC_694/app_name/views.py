from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Encrypt the password using a strong encryption algorithm
        encrypted_password = make_password(password)
        # Create a new user with the encrypted password
        user = User.objects.create_user(username, password=encrypted_password)
        user.save()

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Encrypt the entered password
        encrypted_password = make_password(password)
        # Check if the entered password matches the stored encrypted password
        user = authenticate(username=username, password=encrypted_password)
        if user is not None:
            # Grant access if passwords match
            login(request, user)
        else:
            # Display an error message if passwords do not match
            print('Incorrect username or password. Please try again.')