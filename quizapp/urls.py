from rest_framework import routers
from .views import CategoryViews

router = routers.DefaultRouter()
router.register('categories',CategoryViews)

urlpatterns = [
    
]
urlpatterns += router.urls 