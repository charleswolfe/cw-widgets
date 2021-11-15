from .models import Widget
from .serializers import WidgetSerializer
from rest_framework import generics


class WidgetList(generics.ListCreateAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer


class WidgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
