from django.contrib import admin
from django.urls import path, include
# from .router import router

from crudapp.views import  TestAPI,UpdateApi

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include(router.urls)),
    path('api/v1/',include("crudapp.urls"))

]
