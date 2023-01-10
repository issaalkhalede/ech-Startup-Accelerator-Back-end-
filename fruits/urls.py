from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>',views.get_fruit,name="get_fruit"),
    path('/',views.add_fruit,name="add_fruit")
]