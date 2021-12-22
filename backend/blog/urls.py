from django.urls import path
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import edit_post, eliminar_post, detalle_post

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name ="register"),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('post',views.post, name="post"),
    path('edit/<content>/', edit_post, name ='edit'),
    path('eliminar/<content>', eliminar_post, name='eliminar'),
    path('<slug:slug>/',detalle_post, name='detalle_post'),
    path('comentario/<slug>',views.comentario, name="comentario"),
    
    ]