"""
URL configuration for oyo_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('home.urls')), # Include URLs from the home app
    path('accounts/', include('accounts.urls')), # Include URLs from the accounts app
    path('admin/', admin.site.urls),
    # path('__debug__/', include('debug_toolbar.urls')),  # Debug toolbar URLs  # add it in if settings.debug is True in code below beacuse it is for development purposes the user can see the debug toolbar in the browser abd the user should not see it in production
]

if settings.DEBUG:
        urlpatterns += [
            path('__debug__/', include('debug_toolbar.urls')),  # Debug toolbar URLs # like this and remove the above code in production
        ]
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()