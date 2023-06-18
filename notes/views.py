from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Note, NoteShare
from .serializers import NoteSerializer, NoteShareSerializer

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['POST'])
    def share_with_user(self, request, pk=None):
        note = self.get_object()
        shared_with_user_id = request.data.get('user_id')
        shared_with_user = get_object_or_404(User, id=shared_with_user_id)
        NoteShare.objects.create(note=note, shared_with=shared_with_user)
        return Response({'message': 'Note shared successfully'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Note deleted successfully'})


class NoteShareViewSet(viewsets.ModelViewSet):
    queryset = NoteShare.objects.all()
    serializer_class = NoteShareSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Note share deleted successfully'})
