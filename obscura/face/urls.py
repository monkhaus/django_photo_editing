from django.urls import path

from . import views


app_name = 'face'
urlpatterns = [
    # ex: /polls/
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('<int:post_id>/', views.post_detail, name='detail'),
    path('<int:post_id>/edit/', views.post_update, name='update'),
    path('<int:post_id>/delete/', views.post_delete, name='delete'),
]



