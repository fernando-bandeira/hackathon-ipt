from django.urls import path
from .views import CompareMeshAPIView, PredictFailuresAPIView

urlpatterns = [
    # path('compare/', CompareMeshAPIView.as_view()),
    path('compare/', CompareMeshAPIView.as_view()),
    path('predict/', PredictFailuresAPIView.as_view()),
]
