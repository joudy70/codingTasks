
from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('new/', views.note_create, name='note_create'),
    path('<int:pk>/edit/', views.note_update, name='note_update'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('bulletin/', views.bulletin_board_post_list, name='bulletin_board_post_list'),
    path('bulletin/<int:pk>/', views.bulletin_board_post_detail, name='bulletin_board_post_detail'),
    path('bulletin/new/', views.bulletin_board_post_create, name='bulletin_board_post_create'),
    path('bulletin/<int:pk>/edit/', views.bulletin_board_post_update, name='bulletin_board_post_update'),
    path('bulletin/<int:pk>/delete/', views.bulletin_board_post_delete, name='bulletin_board_post_delete'),
]
