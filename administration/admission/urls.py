from django import urls
from django.urls import  include , path
from rest_framework import routers
from admission import views
from rest_framework.urlpatterns import format_suffix_patterns
from admission.views import *
from admission.views import MyTokenObtainPairView, ApplicationListView, ApplicationDetailView
router =routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('students/', views.students_list),
    # path('students/<int:pk>/', views.students_detail),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', registerUser, name='register'),
    path('profile/', getUserProfile, name="users-profile"),
    path('profile/update/', updateUserProfile, name="user-profile-update"),
    path('', getUsers, name="users"),
    # path('<str:pk>/', getUserById, name='user'), 
    path('update/<str:pk>/', updateUser, name='user-update'),
    path('delete/<str:pk>/', deleteUser, name='user-delete'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
    path('applications/<str:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('userprofile/', registerUser, name='profile'),

]


urlpatterns = format_suffix_patterns(urlpatterns)