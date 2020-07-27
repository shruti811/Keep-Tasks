from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('details/<int:id>/',views.details,name='details'),
    path('del/<int:id>/',views.remove,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]