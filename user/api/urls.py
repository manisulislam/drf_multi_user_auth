from django.urls import path
from .views import FreelancerSignUpView,ClientSignUpView

urlpatterns=[
    path('signup/freelancer/',FreelancerSignUpView.as_view(),name='signup_freelancer'),
    path('signup/client/',ClientSignUpView.as_view(),name='signup_client')
    
]