"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import rest_framework

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('products.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    ]
#     path(r'^test_auth/$', TestAuthView.as_view(), name='test_auth', ),
#     path(r'^rest-auth/logout/$', LogoutViewEx.as_view(), name='rest_logout', ),
#     path(r'^rest-auth/login/$', LoginView.as_view(), name='rest_login', ),
#     path(r'^', HomeTemplateView.as_view(), name='home', ),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
