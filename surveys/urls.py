from django.urls import path, include

from surveys.views import *
from . import views
from .views import export_csv


urlpatterns = [
    path('', views.home),
    path(r'survey_fill/', SurveyFillView.as_view(), name='survey_fill'),
    path(r'filled_success/', SurveyFilledView.as_view(), name='filled_success'),
    path(r'survey_stats/', SurveyStatsView.as_view(), name='survey_stats'),
    path(r'wav_details/<int:wav_pk>', WavFileDetailsView.as_view(), name='wav_details'),
    path(r'wav_list', WavlistView.as_view(), name='wav_list'),
    path('export', export_csv, name='export_waves').
]



