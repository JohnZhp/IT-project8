
from rest_framework import viewsets, permissions
from .models import AIUserScale
from .serializer import AIUserScaleSerializer

class AIUserScaleViewSet(viewsets.ModelViewSet):
    serializer_class = AIUserScaleSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AIUserScale.objects.filter(username=self.request.user.username)

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["request"] = self.request
        return ctx
