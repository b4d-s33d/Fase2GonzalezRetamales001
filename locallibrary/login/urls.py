from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ranking', views.ranking, name='ranking'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]