from django.shortcuts import render

# Create your views here.

def poll_select(request):
     return render (request, 'poll/poll.html')