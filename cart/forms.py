from django import forms

Product_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
        quantity = forms.TypedChoiceField(choices=Product_QUANTITY_CHOICE,
                                        coerce=int)
        update = forms.BooleanField(required=False, initial=False,
                                    widget=forms.HiddenInput)
