from django import forms

class FoodItemsForm(forms.Form):
    food_items = forms.CharField(
        label='Food Items',
        widget=forms.Textarea(attrs={
            'placeholder': 'e.g., 1 apple, 2 bananas',
            'style': 'width: 100%; height: 100px; padding: 10px; border: 1px solid #ccc; border-radius: 4px; resize: vertical;'
        }),
        help_text='Enter food items separated by commas.'
    )