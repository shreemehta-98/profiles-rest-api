from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list APIView Features"""
        an_aipview=[
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Dango View',
            'Gives you tjr most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview': an_aipview})
