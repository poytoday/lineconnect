from django.urls import path, include
from .views import callback

urlpatterns=[
	path('callback/', callback, name='callback')
]