from django.shortcuts import render, redirect
from .models import Sport

# Create your views here.

def poll_select(request):
     return render (request, 'poll/poll.html')
 
def vote_result(request):
    if request.method == 'POST':
        choice = request.POST.get('sport')
        sport = Sport.objects.get(name=choice)
        sport.votes += 1
        sport.save()
        return redirect('ranking')

def ranking(request):
    sports = Sport.objects.all().order_by('-votes')
    return render(request, 'poll/ranking.html', {'sports': sports})
    