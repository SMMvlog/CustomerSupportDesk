from django.contrib import admin
from django.urls import path
from csa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='home'),
    path('query/', views.Query,name='query'),
    path('<int:id>/', views.Resp,name='resp'),
    path('review/', views.Review,name='review'),
]
