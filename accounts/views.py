from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile(request):
    file = Profile.objects.get(user =request.user)
  
    return render(request ,'profile/profile.html',{'file': file})

   