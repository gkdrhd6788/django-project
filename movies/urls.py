from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('<int:movie_pk>/',views.detail,name='detail'),
    path('<int:movie_pk>/update/',views.update,name='update'),
    path('<int:movie_pk>/delete/',views.delete,name='delete'),
]
