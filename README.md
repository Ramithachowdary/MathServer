# Ex.05 Design a Website for Server Side Processing
## Date:01.12.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
power.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lamp Filament Power Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f9;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .calculator {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background: white;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        }
        label {
            font-weight: bold;
        }
        input {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #007BFF;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        .error {
            color: red;
            text-align: center;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>Lamp Filament Power Calculator</h1>
    <div class="calculator">
        <!-- Form for user input -->
        <form method="post">
            {% csrf_token %}
            <label for="current">Current (I) in Amps:</label>
            <input type="number" step="any" id="current" name="current" value="{{ current }}" required placeholder="Enter current in amps">  
            <label for="resistance">Resistance (R) in Ohms:</label>
            <input type="number" step="any" id="resistance" name="resistance" value="{{ resistance }}" required placeholder="Enter resistance in ohms">

            <button type="submit">Calculate Power</button>
        </form>
        <!-- Display the calculated power or error message -->
        <div class="result">
            <h2>Calculated Power: {{ power }} Watts</h2>
        </div>
        {% if power == "Invalid input" %}
            <p class="error">Please provide valid numeric values for both current and resistance.</p>
        {% endif %}
    </div>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('powercalc/', views.calculate_power, name="powercalc"),
    path('', views.calculate_power, name="powercalcroot"),  # This will map the root URL to the same view
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-12-01 135953.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-12-01 140402.png>)

## RESULT:
The program for performing server side processing is completed successfully.
