from django.shortcuts import render
from bat_modules.calorie_calculator_tools.forms import FoodItemsForm
from scripts.calorie_calculator import calculate_nutrition

def calorie_tracker_view(request):
    df = None

    if request.method == 'POST':
        form = FoodItemsForm(request.POST)
        if form.is_valid():
            food_items = form.cleaned_data['food_items']
            df = calculate_nutrition(food_items)
    else:
        form = FoodItemsForm()

    return render(request, 'calorie_calculator_tools/calorie_tracker.html', {'form': form, 'nutrition_data': df})