from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import ItemViewSet, UserViewSet,ExampleView

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')), #handled by router
    url(r'^testauth/$', ExampleView.as_view())
]
# urlpatterns = format_suffix_patterns(urlpatterns) # for use format argument # handled by router
