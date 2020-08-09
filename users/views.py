from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import Profile_F,EProfile_F
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import Profile_F
from django.http import Http404
# Create your views here.

def registrations(request):
    #' register the user '
    if request.method != 'POST':
        form = Profile_F()
        Eform= EProfile_F()
    else:
        form = Profile_F(data=request.POST)
        Eform = EProfile_F(request.POST,request.FILES)

        if form.is_valid() and Eform.is_valid():
             user=form.save()
             profile=Eform.save(commit=False)
             profile.user=user
             profile.save()
             return redirect('intex')
    context = {'form': form,'Eform':Eform}
    return render(request, 'registrations.html', context)
@login_required
def Edit_profile(request,id):

    use = User.objects.get(id=id)
    pro = use.profile
    owner_topic_matcher(use, request.user)
    if request.method != 'POST':
        form = Profile_F(instance=use)
        Pform= EProfile_F(instance=pro)
    else:
        Pform = EProfile_F(request.POST, request.FILES, instance=pro)
        form= Profile_F(request.POST,instance=use)
        if form.is_valid and Pform.is_valid:
            edited_user = form.save()
            Eprofile = Pform.save(commit=False)
            Eprofile.user = edited_user
            Eprofile.save()
            return redirect('profile', id=use.id)

    context = {'form': form, 'use': use,'Pform': Pform}
    return render(request, 'edit_profile.html', context)
def owner_topic_matcher(topic,user):
    if topic != user:
        raise Http404