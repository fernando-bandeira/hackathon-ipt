from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .services import diff_meshes
from django.http import HttpResponse

class CompareMeshAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        mesh1 = request.FILES.get('mesh1')
        mesh2 = request.FILES.get('mesh2')

        result = diff_meshes(mesh1, mesh2)

        response = HttpResponse(result, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="result.bin"'

        return response


class PredictFailuresAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # img = request.FILES.get('img')

        # codigo do FERNANDAO

        return Response({"msg": "hello"})
