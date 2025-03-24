from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class HomeView(generic.View):
 def get(self, request):
        return render(request, 'partC/home.html')
