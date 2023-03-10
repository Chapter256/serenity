from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('edit_comment/<comment_id>', views.EditComment, name='edit_comment'),
    path('delete_comment/<comment_id>', views.DeleteComment, name='delete_comment'),
]