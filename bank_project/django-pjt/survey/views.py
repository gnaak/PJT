# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SurveyForm

@csrf_exempt
def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if not form.is_valid():
            print(form.errors)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Survey data saved successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data', 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
