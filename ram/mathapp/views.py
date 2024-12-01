from django.shortcuts import render

def calculate_power(request):
    print("calculate_power view called")
    context = {
        'power': "0",
        'current': "0",
        'resistance': "0"
    }
    if request.method == 'POST':
        print("POST request received")
        try:
            current = float(request.POST.get('current', 0))
            resistance = float(request.POST.get('resistance', 0))
            context['power'] = round(current**2 * resistance, 2)
            context['current'] = current
            context['resistance'] = resistance
        except ValueError:
            context['power'] = "Invalid input"
    return render(request, 'mathapp/power.html', context)

