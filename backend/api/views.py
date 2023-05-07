from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser


class CompareMeshAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        mesh1 = request.FILES.get('mesh1')
        mesh2 = request.FILES.get('mesh2')
        print(mesh1, mesh2)

        return Response({"msg": "hello"})


class PredictFailuresAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # img = request.FILES.get('img')

        # codigo do FERNANDAO

        return Response({"msg": "hello"})
