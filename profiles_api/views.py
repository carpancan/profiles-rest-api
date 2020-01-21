from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HellowApiView(APIView):
    """APIView example"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uno',
            'Dos',
            'Tres',
            'Cuatro',
        ]

        return Response({
            'message':  'Hellow', 'an_apiview': an_apiview
        }, 200)

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating objects"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
