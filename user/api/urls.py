from django.urls import path
from .views import FreelancerSignUpView,ClientSignUpView,CustomObtainToken,ClientOnlyView,FreelanceOnlyView

urlpatterns=[
    path('signup/freelancer/',FreelancerSignUpView.as_view(),name='signup_freelancer'),
    path('signup/client/',ClientSignUpView.as_view(),name='signup_client'),
    path('login/', CustomObtainToken.as_view(), name='login'),
    path('client/dashboard/',ClientOnlyView.as_view(),name='client_dashboard'),
    path('freelancer/dashboard/', FreelanceOnlyView.as_view(), name='freelancer_dashboard'),
    
    
]