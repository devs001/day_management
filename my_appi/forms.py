from django import forms
from .models import Topic, Entry

class Topicfroms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['txt']
        labels = {'txt': ''}
class new_entry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['txt', 'image']


