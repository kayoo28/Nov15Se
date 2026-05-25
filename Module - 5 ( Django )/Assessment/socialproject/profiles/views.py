from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserProfileForm

import csv

# Create Profile
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'profiles/create.html', {
        'form': form
    })

# List Profiles
def profile_list(request):

    profiles = UserProfile.objects.all()

    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })

# Export CSV
def export_profiles(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = (
        'attachment; filename="profiles.csv"'
    )
    writer = csv.writer(response)
    writer.writerow(['Username', 'Age', 'Public'])
    profiles = UserProfile.objects.all()

    for profile in profiles:

        writer.writerow([
            profile.username,
            profile.age,
            profile.is_public
        ])
    return response