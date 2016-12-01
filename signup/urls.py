from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_all/', views.get_all_users, name='index'),
    url(r'^register/',views.register,name='register')
]