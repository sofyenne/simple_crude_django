
from django.urls import path
from .import views


urlpatterns = [

   
    path('register/' , views.upload , name='register'),
    path('index/' , views.index , name='index'),
    path('' , views.Login , name='login'),
    path('delete/<int:id>' , views.delete, name='delete'),
    path('listsup' , views.listsup , name = 'listsup'),
    path('add' , views.addclient , name = 'add'),
    path('client' , views.indexclient , name = 'client'),

    

]