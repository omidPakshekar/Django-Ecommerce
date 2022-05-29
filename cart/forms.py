from django import forms
from customers.models import Address


Product_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CartAddProductForm, self).__init__(*args, **kwargs)

    quantity = forms.TypedChoiceField(label="تعداد", choices=Product_QUANTITY_CHOICE,
                                    coerce=int)
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)

class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['country']  = forms.CharField(required=False)
        self.fields['firstname'] = forms.CharField(widget=forms.TextInput(attrs={"style" :"text-align:right; ",}))
        self.fields['lastname'] = forms.CharField(widget=forms.TextInput(attrs={"style" :"text-align:right; ",}))
        self.fields['city'] = forms.CharField(widget=forms.TextInput(attrs={"style" :"text-align:right; ",}))
        self.fields['province'] = forms.CharField(widget=forms.TextInput(attrs={"style" :"text-align:right; ",}))
        self.fields['postcode'] = forms.CharField(widget=forms.TextInput(attrs={"style" :"text-align:right; ",}))
        self.fields['address_text'] = forms.CharField(widget=forms.TextInput(attrs={
                     "style" :"text-align:right; width:65%; height:90px;",
                   }))

    class Meta:
        model = Address
        fields = ["firstname", "lastname", "address_text", "phone_number",
                 "phone_number", "postcode", "city", "province", "country"]
