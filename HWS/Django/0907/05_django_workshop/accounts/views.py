from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    User = get_user_model()
    members = User.objects.all()

    context = {
        'members': members,
    }
    return render(request, 'accounts/index.html', context)