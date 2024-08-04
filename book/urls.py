from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('<int:review_id>/edit/', views.review_detail, name='review_edit'),
    path('delete_review/<int:review_id>', views.review_edit, name="review_delete"),
    #path('<int:review_id>/delete/', views.review_delete, name='review_delete'),
]