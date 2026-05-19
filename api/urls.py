from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, ChangePasswordView, 
    BookListCreateView, BookDetailUpdateDeleteView,
    BookReviewListCreateView, ReviewDetailUpdateDeleteView
)

urlpatterns = [
    # Auth Endpoints
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    # Book Endpoints
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),

    # Review Endpoints
    path('books/<int:book_id>/reviews/', BookReviewListCreateView.as_view(), name='book_reviews'),
    path('reviews/<int:pk>/', ReviewDetailUpdateDeleteView.as_view(), name='review_detail_update_delete'),
]