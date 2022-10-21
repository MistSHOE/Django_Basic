from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    # функции в views, Если используем класс вместо функции добавляй .as_view() к url патерну
    path('contacts/', views.ContactsView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    path('doc/', views.DocView.as_view()),
    path('', views.IndexView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('news/', views.NewsView.as_view()),


]