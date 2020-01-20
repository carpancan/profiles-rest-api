from rest_framework.views import APIView
from rest_framework.response import Response


class HellowApiView(APIView):
    """APIView example"""

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
