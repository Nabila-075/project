from django import forms
from .models import UserAccount

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name",max_length=100)
    mobile = forms.IntegerField(label="Mobile Number")
    email = forms.EmailField(label="Email ID",max_length=254)
    address = forms.CharField(label="Address",max_length=100)
    city = forms.CharField(label="City",max_length=25)
    postal = forms.CharField(label="Enter Postal Code",max_length=20)
 
class MyForm(forms.ModelForm):
  class Meta:
    model = UserAccount
    fields = ["first_name", "last_name", "email",]
    labels = {'first_name': "First Name", 'last_name': "Last Name",
              'email': "Email",}


class Subscribe(forms.Form):
    Message = forms.CharField()
    def __str__(self):
        return self.Message




