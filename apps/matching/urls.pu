from django.urls import path
from .views import RecommendView, SimilarityView


urlpatterns = [
path('recommend/', RecommendView.as_view(), name='recommend'),
path('similarity/<int:other_id>/', SimilarityView.as_view(), name='similarity'),
]