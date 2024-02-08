from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.CustomerViewSet) 
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]






# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from . import views

# # Create a router and register our ViewSets with it.
# router = DefaultRouter()
# router.register('category', views.CustomerViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', views.UserRegistrationApiView.as_view(), name='register')
# ]