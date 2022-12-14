from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.AccountLogin.as_view()),
    path("accounts/", views.AccountView.as_view()),
    path("accounts/newest/<int:num>/", views.AccountDetailsView.as_view()),
    path("accounts/<pk>/", views.AccountUpdate.as_view()),
    path("accounts/<pk>/management/", views.AccountManagement.as_view()),
]
