# myapp/views.py
from django.shortcuts import render

def check_odd_even(request):
    result = None
    if request.method == 'POST':
        number = int(request.POST['number'])
        if number % 2 == 0:
            result = f"{number} is an even number"
        else:
            result = f"{number} is an odd number"
    return render(request, 'index.html', {'result': result})

def name_filter(request):
    names = ['Hello', 'Hai', 'Welcome', 'Django']
    filtered_names = []
    if request.method == 'POST':
        char = request.POST['char']
        filtered_names = [name for name in names if name.startswith(char)]
    return render(request, 'index.html', {'filtered_names': filtered_names})
