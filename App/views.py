from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from App.models import BusCoordinates


# Create your views here.
def index(request , *args , **kwargs) :
    return render(request, "index.html" , {})

def usersView(request , *args , **kwargs) :
    return HttpResponse("<h1>Users View</h1>")

@csrf_exempt  # Disable CSRF for simplicity (use cautiously)
def save_location(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            lat = data.get('latitude')
            long = data.get('longitude')
            accuracy = data.get('accuracy')

            # Save data to the database
            location = BusCoordinates(latitude=lat, longitude=long, accuracy=accuracy)
            location.save()

            return JsonResponse({'status': 'success', 'message': 'Location saved successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})