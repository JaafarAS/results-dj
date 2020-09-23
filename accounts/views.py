from django.shortcuts import render
from .models import Profile

# Create your views here.


def profile(request):
    file = Profile.objects.get(user =request.user)
  
    return render(request ,'profile/profile.html',{'file': file})

   