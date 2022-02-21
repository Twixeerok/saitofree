from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.activation.views import RegistrationView
from django_registration.forms import RegistrationFormUniqueEmail

urlpatterns = [	
	path('admin/', admin.site.urls),
	path('lol/', include('riddles.urls')),
    path('', include('main.urls')),
    path('accounts/register/', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='django_registration_register_uniq_email'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)