from django.urls import path

from crudapp.views import  TestAPI,UpdateApi

urlpatterns = [
    path('employee/',TestAPI.as_view()),
    path('employee/<int:id>',UpdateApi.as_view())

]
