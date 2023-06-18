from django.urls import path, include
from rest_framework import routers
from .views import NoteViewSet, NoteShareViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'note-shares', NoteShareViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
