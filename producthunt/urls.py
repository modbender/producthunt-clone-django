from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import products.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', products.views.home, name='home'),

    path('acc/',include('accounts.urls')),
    path('product/',include('products.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
