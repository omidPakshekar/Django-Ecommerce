from django import forms



class ProductPriceForm(forms.Form):
        price1 = forms.IntegerField(widget=forms.NumberInput(
                attrs = {
                    "style" : "width: 95%;"
                }
            ), required=False)

        price2 = forms.IntegerField(widget=forms.NumberInput(
                    attrs = {
                        "style" : "width: 95%;"
                    }
                ), required=False)
