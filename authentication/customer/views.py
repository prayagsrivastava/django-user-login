from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request, username):
    return render(
        request,
        'customer/homepage.html'
    )