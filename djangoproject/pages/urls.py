# from django.urls import path
# from .import views
# from .views import HomePageView
# app_name = "pages"   


# pages/urls.py
from django.urls import path
from .views import HomePageView,ThankyouPage
# from .views import home_view 
urlpatterns = [
    path("", ThankyouPage.as_view(), name="index"),
    path("home/", HomePageView.as_view(), name="home"),
   
    
]