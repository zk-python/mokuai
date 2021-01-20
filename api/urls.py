from django.urls import path
from rest_framework_jwt import views as view

urlpatterns=[
    # 通过jwt完成登录并签发token  依赖于django默认的auth_user
    path("login/", view.ObtainJSONWebToken.as_view()),
    # path("login/", view.obtain_jwt_token),
    path("users/", view.UserDetailAPIVIew.as_view()),
    path("user/", view.LoginAPIView.as_view()),


]