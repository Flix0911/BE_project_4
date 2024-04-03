from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
# prebuilt views that allow obtaining access and refresh tokens
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# configure urls to link them up

urlpatterns = [
    path('admin/', admin.site.urls),
    # register a new user
    path('api/user/register/', CreateUserView.as_view(), name="register"),
    # get a token
    path('api/token/', TokenObtainPairView.as_view(), name="get_token"),
    # refresh the token
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh"),
    # API auth view ~ built into the rest framework
    path('api-auth', include("rest_framework.urls")),
    # Link so urls re forward to api.urls.py
    path("api/", include("api.urls")),
]
