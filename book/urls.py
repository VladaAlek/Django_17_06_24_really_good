from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('<int:bibliography_id>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/review_edit/<int:review_id>/', views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
]

