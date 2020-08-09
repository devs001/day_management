from django.urls import include,path
from . import views
app_name = 'users'

urlpatterns = [
    #include will get to given addres urls will decate this
    path('', include('django.contrib.auth.urls')),
    path('registrations',views.registrations,name='registrations'),
    path('edit_profile/<int:id>', views.Edit_profile, name='edit_profile')
]