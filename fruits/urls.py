from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>',views.get_fruit,name="get_fruit"),
]