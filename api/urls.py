from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Configuración del Schema de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Salud en el postparto",
        default_version='v2',
        description="Documentación de Salud en el postparto",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@saludenposparto.org"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... tus otras URLs

# URLs de Swagger
    path('api/v2/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v2/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v2/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)