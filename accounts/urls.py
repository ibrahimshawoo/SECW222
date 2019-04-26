from django.urls import path
from accounts import views


#urlpatterns = [
#    path('signup/', views.signup.as_view(), name='signup'),
#]

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]