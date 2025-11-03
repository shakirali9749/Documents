from django.urls import path

# from eventBookingSystem.urls import urlpatterns

from .views import (
        SignupView,
        SigninView,
        ProfileView

)

urlpatterns = [
        path("signup/", SignupView.as_view(), name="signup"),
        path("login/", SigninView.as_view(),name="login"),
        path("profile/", ProfileView.as_view(), name="profile"),
]