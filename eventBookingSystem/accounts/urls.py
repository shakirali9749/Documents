from django.urls import path

# from eventBookingSystem.urls import urlpatterns

from .views import (
        SignupView
)

urlpatterns = [

        path("signup/", SignupView.as_view(), name="signup"),

]