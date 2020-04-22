from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    TexturesAdminViewset,
    ObjectsAdminViewset,
    FileViewset,
)

router = DefaultRouter()

router.register(r"texture", TexturesAdminViewset, "text_view")
router.register(r"object", ObjectsAdminViewset, "object_view")
router.register(r"files", FileViewset)

urlpatterns = [
    path("api/", include(router.urls)),
]
