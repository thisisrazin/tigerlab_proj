from django.urls import path
from .views import UploadView, AddMatch, EditView, EditMatch, DeleteMatch, downloadCSV


urlpatterns=[
    path('upload/', UploadView.as_view()),
    path('upload/<str:resultID>', UploadView.as_view(), name='uploaded'),
    path('match/edit/<str:resultID>/<str:matchPK>', EditView.as_view(), name='editing'),
    path('match/edit/save/<str:resultID>/<str:matchPK>', EditMatch.as_view()),
    path('match/add/<str:resultID>/', AddMatch.as_view()),
    path('match/delete/<str:resultID>/<str:matchPK>', DeleteMatch.as_view()),
    path('documentCSV/<str:filename>/', downloadCSV)
]