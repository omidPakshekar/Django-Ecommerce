from django import forms

Product_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CartAddProductForm, self).__init__(*args, **kwargs)

    quantity = forms.TypedChoiceField(label="تعداد", choices=Product_QUANTITY_CHOICE,
                                    coerce=int)
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)
