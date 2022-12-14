from django.urls import path
from .views import DogInfo, KeyInfo, IncrementKeys

urlpatterns = [
    path('doginfo/', DogInfo.as_view()),
    path('keyinfo/', KeyInfo.as_view()),
    path('incrementkey/<int:value>/', IncrementKeys.as_view()),
]
