from django.shortcuts import render,redirect
from django.shortcuts import render
from .models import Topic,Entry
from .forms import Topicfroms,new_entry
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request, 'login.html')

def intex(request):
    return render(request, 'login.html')

@login_required
def topics(request):
    entry_num=[]
    """show  topics that object's owns_it attribute machts with  request.user"""
    topic = Topic.objects.filter(owns_it=request.user).order_by('date_added')
    for topi in topic:
        top = topi.entry_set.count()
        entry_num.append(top)
    print(entry_num)
    context = {'topic': topic,'entry_num':entry_num}
    return render(request,'topics.html', context)
@login_required
def Topic_v( request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    ent = topic.entry_set.order_by('entry_date')
    # if qwerner of the topic isnt  request's users or owerner that not then
    if topic.owns_it != request.user:
        raise Http404
    context = {'topic': topic, 'ent': ent}
    return render(request,'topici.html',context)

def test(request, t):
    lis = [t, t+23]
    context = {'data': lis}
@login_required
def new_forms(request):
    if request.method != 'POST':
        form = Topicfroms()
        # indicates no old data requeste so create a new new_forms
    else:
        form = Topicfroms(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            #foregin_key attribute must be included in model from outside
            new_topic.owns_it = request.user
            new_topic.save()
            return redirect('topics')
        #display black or invalid
    context={'form': form}
    return render(request, 'new_form.html', context)
@login_required
def neo_entry(request, topic_u):
    topic = Topic.objects.get(id=topic_u)
    if request.method != 'POST':
        #nw data form
        form = new_entry()
    else:
        form = new_entry(request.POST, request.FILES)
        if form.is_valid():
            new_ent = form.save(commit=False)
            #bcos it has no topic connected to it it needs it
            new_ent.topic = topic
            new_ent.save()
            return redirect('topic',topic_id=topic_u)
    # to stop using driect url to get to someone's new_entry
    owner_topic_matcher(topic,request.user)
    context ={'topic': topic, 'form':form}
    return render(request, 'new_entry.html', context)
@login_required
def edits_entry(request, entry_id):
    entry_o = Entry.objects.get(id=entry_id)
    # get its topic Too
    topic_o = entry_o.topic

    if request.method !='POST':
        form = new_entry(instance=entry_o)
    else:
        form = new_entry(request.POST, request.FILES, instance=entry_o)
        if form.is_valid:
            edited_entry = form.save(commit=False)
            edited_entry.topic = topic_o
            edited_entry.save()
            return redirect('topic',topic_id=topic_o.id)

    owner_topic_matcher(topic_o,request.user)
    context = {'form': form, 'topic': topic_o,'entry':entry_o}
    return render(request,'edit_entry.html',context)

def owner_topic_matcher(topic,user):
    if topic.owns_it != user:
        raise Http404
def user_matcher(topic,user):
    if topic != user:
        raise Http404
@login_required
def profile(request,id):

    user = User.objects.get(id=id)
    topic_list = Topic.objects.filter(owns_it=user)
    entry_lis=[]
    user_matcher(user, request.user)
    for topic_t in topic_list:
        entry_liss = Entry.objects.filter(topic=topic_t)
        entry_lis.extend(entry_liss)
        entry_liss=[]
    len_t = len(topic_list)
    len_e=len(entry_lis)
    context= {'user':user,'len_t':len_t,'len_e':len_e}
    return render(request,'profile.html',context)
