from django.urls import path
from django.contrib import admin
from accounts import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
]
