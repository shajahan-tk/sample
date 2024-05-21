from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('why',views.why,name='why'),
    path('trainer',views.trainer,name='trainer'),
    path('login',views.login,name='login'),
    
]
