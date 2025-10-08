from django import forms
from django.forms import widgets
from .models import Transactions


class TransactionForm(forms.ModelForm):
    """
    A form for creating and updating Transaction objects.
    It automatically generates form fields based on the Transaction model.
    """

    class Meta:
        model = Transactions
        # Specifies the fields from model to include in the form
        fields = ["date", "description", "amount", "category"]
        widgets = {
            "date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-input"}
            ),
            "description": forms.TextInput(
                attrs={"placeholder": "e.g., Coffe with friends"}
            ),
            "amount": forms.NumberInput(
                attrs={"step": "0.01", "placeholder": "e.g., 4.50"}
            ),
            "category": forms.TextInput(attrs={"placeholder": "e.g., Food"}),
        }
