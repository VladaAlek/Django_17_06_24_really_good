from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('<slug:slug>/edit_review/<int:review_id>/', views.review_edit, name='review_edit'),

    #path('<int:review_id>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment')

    path('delete_review/<int:review_id>', views.review_edit, name="review_delete"),
    #path('<int:review_id>/delete/', views.review_delete, name='review_delete'),
]

#path('<slug:slug>/edit_comment/<int:comment_id>',)