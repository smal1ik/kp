from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from .models import *
from .permissions import IsNewsEditor
from .serializers import *
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response


# Create your views here.

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'status': 'request was permitted'
#     }
#     return Response(content)

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({f'key': 'test'})


class GetRolesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        roles = list()
        for g in request.user.groups.all():
            roles.append(g.name)

        return Response({
            'username': request.user.username,
            'roles': roles
        })


class RefreshUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # обновить данные users из workers и anotherworkers

        # сначала сравнить workers и anotherworkers - у кого приоритет?

        # если пользователь отключен в workers, то отключить в users
        # если
        return Response({'key': 'selty'})


class UpdateUsersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # Обновление данных из DV

        # выгрузить данные из DV в БД

        # сравнить список пользователей в Workers и Users

        # обновить данные в Users (с учетом OtherWorkers)
        return Response({'message': 'users updated from Docsvision'})


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsExecutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        return obj.owner == request.user


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkerListView(generics.ListAPIView):
    # queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    # фильтр для поиска в адресной строке
    # http://127.0.0.1:8000/api/workers/all/?gender=Female&inner_phone=5003
    def get_queryset(self):
        queryset = Worker.objects.all()
        params = self.request.query_params
        gender = params.get('gender', None)
        inner_phone = params.get('inner_phone', None)
        if gender:
            queryset = queryset.filter(gender=gender)
        if inner_phone:
            queryset = queryset.filter(inner_phone=inner_phone)
        return queryset


'''
class WorkerListView(APIView):
    def get(self, request):
        queryset = Worker.objects.all()
        serializer_class = WorkerSerializer(queryset, many=True)
        return Response({ 'workers': serializer_class.data })
'''


##############################################################
# WORKERS
# all
class WorkerListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


# one
class WorkerRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


# update
class WorkerUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    # premission_class = [permissions.IsAuthenticatedOrReadOnly,]


# create
class WorkerCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


##############################################################
# OTHER WORKERS
# all
class OtherWorkerListView(generics.ListAPIView):
    queryset = OtherWorker.objects.all()
    serializer_class = OtherWorkerSerializer


# one
class OtherWorkerRetrieveView(generics.RetrieveAPIView):
    queryset = OtherWorker.objects.all()
    serializer_class = OtherWorkerSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


# update
class OtherWorkerUpdateView(generics.UpdateAPIView):
    queryset = OtherWorker.objects.all()
    serializer_class = OtherWorkerSerializer
    # premission_class = [permissions.IsAuthenticatedOrReadOnly,]


# create
class OtherWorkerCreateView(generics.CreateAPIView):
    queryset = OtherWorker.objects.all()
    serializer_class = OtherWorkerSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


##############################################################
# SERVICES
# all
class AppServiceListView(generics.ListAPIView):
    queryset = AppService.objects.all()
    serializer_class = AppServicesSerializer


# one
class AppServiceRetrieveView(generics.RetrieveAPIView):
    queryset = AppService.objects.all()
    serializer_class = AppServicesSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


# update
class AppServiceUpdateView(generics.UpdateAPIView):
    queryset = AppService.objects.all()
    serializer_class = AppServicesSerializer
    # premission_class = [permissions.IsAuthenticatedOrReadOnly,]


# create
class AppServiceCreateView(generics.CreateAPIView):
    queryset = AppService.objects.all()
    serializer_class = AppServicesSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


# list for user
class AppServiceForUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # вернет все сервисы, к которым есть доступ
        services = AppService.objects.all()
        print(services)
        if not request.user.groups.filter(name='service_news').exists():
            services = services.filter(~Q(url='news'))

        serializer = AppServiceSerializer(services, many=True)

        return JsonResponse(serializer.data, safe=False)


##############################################################
# USER SETTINGS
# all
class UserSettingsListView(generics.ListAPIView):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingsSerializer


# one
class UserSettingsRetrieveView(generics.RetrieveAPIView):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingsSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


# update
class UserSettingsUpdateView(generics.UpdateAPIView):
    queryset = UserSetting.objects.all()
    serializer_class = CreateUserSettingsSerializer

    # premission_classes = (IsExecutor,)
    # premission_class = [permissions.IsAuthenticatedOrReadOnly,]
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return UserSetting.objects.filter(user=user)
        return PermissionDenied


# create
class UserSettingsCreateView(generics.CreateAPIView):
    queryset = UserSetting.objects.all()
    serializer_class = CreateUserSettingsSerializer
    # premission_class = permissions.IsAuthenticatedOrReadOnly


##############################################################
# Posts
# all
class PostsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


# one
class PostsRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


# update
class PostsUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsNewsEditor]
    queryset = Post.objects.all()
    serializer_class = CreatePostsSerializer


# create
class PostsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsNewsEditor]
    queryset = Post.objects.all()
    serializer_class = CreatePostsSerializer


class PostsDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsNewsEditor]
    queryset = Post.objects.all()
    serializer_class = CreatePostsSerializer
