from django.shortcuts import render
from users.models import CustomUser

# Create your views here.
def home_view(request):
    context = {}

    users = CustomUser.objects.all()
    context['users'] = users

    return render(request, 'home.html', context)