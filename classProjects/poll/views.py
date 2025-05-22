from django.shortcuts import render

# Create your views here.
question = "Qual o melhor esporte?"
alternatives = ["Futebol","Basquete","Vôlei", "Tênis"]
votes = [0, 0, 0, 0]

def poll_select(request):
    context = {'question': question, 
               'alternatives': alternatives,
               }
    return render (request, 'poll/poll.html', context)

def ranking(request):
    if request.method == 'POST':
        option=int(request.POST.get('option'))
        global votes
        votes[option-1] += 1
        result = zip(alternatives,votes)
        context = {
            'result': result,
            'question': question,
        }
    return render(request, 'poll/ranking.html', context)
    