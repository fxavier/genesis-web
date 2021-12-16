from django.urls import path
from core.views import IndexView, InqueritoListView
from core import views

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home', views.home, name='home'),
    path('inquerito-list', InqueritoListView.as_view(), name='inquerito-list'),
]
