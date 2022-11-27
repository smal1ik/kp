from django.urls import path, include
from .views import *
#from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/', include('djoser.urls')),     
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth', include('rest_framework.urls')),   
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('auth/token', obtain_auth_token, name='token'),
    #path('auth/logout', Logout.as_view()),

    # path('test1/', example_view),
    path('test/', TestView.as_view()),
    path('get_roles/', GetRolesView.as_view()),
    path('refresh_users/', RefreshUsersView.as_view()),
    path('update_users/', UpdateUsersView.as_view()),


    path('users/all/', UserListView.as_view()),   
    path('other_workers/all/', OtherWorkerListView.as_view()),

    path('user_settings/all/', UserSettingsListView.as_view()),
    path('user_settings/update/<int:pk>', UserSettingsUpdateView.as_view()),
    path('user_settings/<int:pk>/', UserSettingsRetrieveView.as_view()),
    path('user_settings/new/', UserSettingsCreateView.as_view()),

    path('workers/al<str:pk>', WorkerListView.as_view()),
    # path('workers/update/<int:pk>', WorkerUpdateView.as_view()),
    path('workers/<int:pk>/', WorkerRetrieveView.as_view()),
    # path('workers/new/', WorkerCreateView.as_view()),

    
    path('service/for_me/', AppServiceForUserView.as_view()),
    path('service/all/', AppServiceListView.as_view()), 
    path('service/update/<int:pk>', AppServiceUpdateView.as_view()),
    path('service/<int:pk>/', AppServiceRetrieveView.as_view()),
    path('service/new/', AppServiceCreateView.as_view()),

    path('posts/all/', PostsListView.as_view()),
    path('posts/update/<int:pk>', PostsUpdateView.as_view()),
    path('posts/<int:pk>/', PostsRetrieveView.as_view()),
    path('posts/new/', PostsCreateView.as_view()),
    path('posts/delete/<int:pk>/', PostsDeleteView.as_view()),
]