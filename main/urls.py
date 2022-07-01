from django.contrib import admin
from django.urls import path,include

# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Student Quiz API",
        default_version="v1",
        description="Student quiz and answer api",
        terms_of_service="#",
        # Change e-mail on this line!
        contact=openapi.Contact(email="murat201082@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(
        cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('users/', include('users.urls')),
    
    
    # path('nested_admin/', include('nested_admin.urls')),
    
    

    
    
]
