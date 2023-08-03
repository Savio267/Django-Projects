"""
URL configuration for Project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    # path('admin/', admin.site.urls),
      path('',views.home,name='home'),
      path('addbook',views.addbook,name='addbook'),
      path('addbook1', views.addbook1, name='addbook1'),
      path('view/<int:p>/', views.view_book, name='view'),
      path('edit/<int:p>/',views.edit_book,name='edit'),
      path('delete/<int:p>/', views.delete_book, name='delete'),
      path('viewbook',views.viewbook,name='viewbook'),
      path('viewpersons',views.viewpersons,name='viewpersons'),
      path('addpersons',views.addpersons,name='addpersons'),
      path('addpersons1',views.addpersons1,name='addpersons1'),
      path('fact',views.fact,name='fact'),
      path('register',views.register,name='register'),
      path('user_login',views.user_login,name='user_login'),
      path('user_logout',views.user_logout,name='user_logout'),
      path('adminsignup', views.admin_signup, name='adminsignup'),
      path('teachersignup', views.teacher_signup, name='teachersignup'),
      path('personsignup', views.person_signup, name='personsignup'),
]
