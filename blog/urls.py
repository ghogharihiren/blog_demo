from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('blog/',views.blog,name='blog'),
    path('profile/',views.profile,name="profile"),
    path('my-blog/',views.my_blog,name='my-blog'),
    path('update-post/<int:pk>',views.update_post,name='update-post'),
    path('delete-post/<int:pk>',views.delete_poat,name='delete-post'),
    path('forgot-password',views.forgot_password,name='forgot-password')
    
]