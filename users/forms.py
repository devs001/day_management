from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm,forms
from django import forms
#from .models import Profile
"""class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    class Meta:
        model= User
        fields = ('username','first_name', 'last_name',
                  'password1', 'password2', 'email')
        #fields = ('bio','profile_pic','twitter_link',
                  #'insta_link','facebook_link','website_link')

    def __init__(self,*args,**kwargs):
            super(SignUpForm,self).__init__()
            #self.fields=[]"""
class Profile_F(UserCreationForm):


   """ email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)"""
   class Meta:
        model = User
        fields = ('username','first_name', 'last_name',
                      'password1', 'password2','email')

   """ def __init__(self, *args, **kwargs):
        super(Profile_F, self).__init__()
        # self.fields=[] """

class EProfile_F(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','twitter_link','facebook_link')



