from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from .serializers import NoteSerializer


class NoteAPIList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return (
            Note.objects.filter(user=self.request.user)
        )


class NoteAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class NoteAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwnerOrAdmin, )
