
from django.contrib import admin
from django.urls import path,include

from apis import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register("admin" , views.BookAdminViewSet , basename="library-admin")
router.register("student" , views.BookStudentViewSet , basename="library-student")
router.register("user" , views.CustomUserViewSet , basename= "library-users")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', views.Custom_auth_token.as_view()),
]
