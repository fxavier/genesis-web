from django.urls import path
from core.views import InqueritoListView
from core import views

app_name = 'core'

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('familia-tem-machamba', views.total_familia_tem_machamba,
         name='familia-tem-machamba'),
    # path('inquerito-list', InqueritoListView.as_view(), name='inquerito-list'),
]
