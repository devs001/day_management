from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # name is name of page
    path('home', views.home, name='home'),
    path('', views.intex, name='intex'),
    #name="XXX" it important
    path('topics',views.topics,name='topics'),
    path('topic/<int:topic_id>', views.Topic_v, name='topic'),
    path('test/<int:t>', views.test, name='test'),
    path('new_forms',views.new_forms,name='new_forms'),
    path('neo_entry/<int:topic_u>/',views.neo_entry, name='neo_entry'),
    path('edits_entry/<int:entry_id>/', views.edits_entry, name='edits_entry'),
    #path('', include('my_appi.urls', name='my_appi')),
    path('profile/<int:id>/', views.profile, name='profile')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)