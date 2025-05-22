from django.shortcuts import render
from . import services

# Create your views here.
  
def schedule(request):
    return render(request, 'study_schedule/schedule_form.html')


def schedule_generate_result(request):
    if request.method == 'POST':
        selected_days = request.POST.getlist('days')
        topics_raw = request.POST.get('topics', '')

    schedule = services.schedule_generate(selected_days, topics_raw)
    
    context = {
        'schedule': schedule
    }

    return render(request, 'study_schedule/result.html', context)