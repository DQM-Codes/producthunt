from django.urls.conf import path, include
from . import views

urlpatterns = [
    path('create/', views.createpage, name='create'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]