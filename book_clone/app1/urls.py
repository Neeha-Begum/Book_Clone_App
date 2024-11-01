from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('login',views.loginview,name="loginpage"),
    path('book',views.bookview,name="bookpage"),
    path('author',views.authorview,name="authorpage"),
    path('delete/<int:rid>',views.deleteview,name="deletepage"),
    path('update/<int:rid>',views.updateview,name="updatepage"),
    path('logout',views.logoutview,name="logoutpage"),
    path('single/<int:rid>',views.dedicatedview,name="dedicatedpage"),
    path('register',views.registerview,name="registerpage")
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)