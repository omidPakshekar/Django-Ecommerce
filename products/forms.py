from django import forms



class ProductPriceForm(forms.Form):
        price1 = forms.IntegerField(
            widget=forms.NumberInput(
                attrs = {
                    "style" : "width: 95%;"
                }
            ), required=False)

        price2 = forms.IntegerField(
            widget=forms.NumberInput(
                    attrs = {
                        "style" : "width: 95%;"
                    }
                ), required=False)
class ProductCommentForm(forms.Form):
    new_comment_text = forms.CharField(
                widget=forms.Textarea(
                attrs = {
                        "style" : "width: 100%; border: none;"
                                + "background: #E8E8E8; padding: 5px 10px;"
                                + "height: 100px;	border-radius: 5px 5px 0px 0px;"
                                + "border-bottom: 2px solid #016BA8; transition: all 0.5s;"
                                + "margin-top: 15px; margin-bottom: 5px;"
                                + "float:right;",
                                'placeholder': 'User'
                    }
                ),initial=' ', required=True)
