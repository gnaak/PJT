# views.py
from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Survey

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mypolls:result')
    else:
        form = SurveyForm()

    return render(request, 'mypolls/survey.html', {'form': form})


def result(request):
    surveys = Survey.objects.all()
    return render(request, 'mypolls/result.html', {'surveys': surveys})
