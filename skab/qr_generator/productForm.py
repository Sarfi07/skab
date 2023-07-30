from django import forms

class Product_form(forms.Form):
    
    product_name = forms.CharField(label="Product Name", max_length=48, widget=forms.TextInput(attrs={'class':'form-control'}))

    description = forms.CharField(label="Description", max_length=128, widget=forms.TextInput(attrs={'class':'form-control'}))

    sku = forms.CharField(label="SKU", max_length=16, widget=forms.TextInput(attrs={'class':'form-control'}))

    price = forms.IntegerField(label="Price", widget=forms.TextInput(attrs={'class':'form-control'}))

    size = forms.CharField(max_length=8, label="Size", widget=forms.TextInput(attrs={'class':'form-control'}))

    color = forms.CharField(max_length=16, label="Color", widget=forms.TextInput(attrs={'class':'form-control'}))

    shade = forms.CharField(max_length=48, label="Shade", widget=forms.TextInput(attrs={'class':'form-control'}))

    material = forms.CharField(max_length=32, label="Material", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    imageURL = forms.URLField(label="Image URL", widget=forms.TextInput(attrs={'class':'form-control'}))


