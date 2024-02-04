from django.shortcuts import render
from datetime import datetime

def show_time(request):
    current_time = datetime.now().strftime('%H:%M:%S')
    return render(request, 'clockapp\clock.html', {'current_time': current_time})
