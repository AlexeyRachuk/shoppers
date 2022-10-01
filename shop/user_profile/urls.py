from django.urls import path

from .views import RegisterUser, register_success, LoginUser, UserCabinet, logout_user, UserCabinetEditing

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('register_success/', register_success, name='register_success'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('cabinet/<int:pk>/', UserCabinet.as_view(), name="cabinet"),
    path('cabinet_editing/<int:pk>/', UserCabinetEditing.as_view(), name="cabinet_update")

]
