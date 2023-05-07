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

        with open('mesh1.stl', 'wb+') as destination:
            for chunk in mesh1.chunks():
                destination.write(chunk)

        with open('mesh2.stl', 'wb+') as destination:
            for chunk in mesh2.chunks():
                destination.write(chunk)

        result = diff_meshes('mesh1.stl', 'mesh2.stl')
        result.save('diff_mesh.stl')
        with open('diff_mesh.stl', 'rb') as stl_file:
            response = HttpResponse(stl_file.read(), content_type='application/vnd.ms-pki.stl')
            response['Content-Disposition'] = 'attachment; filename="diff_mesh.stl"'
            return response


class PredictFailuresAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # img = request.FILES.get('img')

        # codigo do FERNANDAO

        return Response({"msg": "hello"})
