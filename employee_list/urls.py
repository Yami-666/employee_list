from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),  
    path('', RedirectView.as_view(url='/employee/list', permanent=True)),  
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
