from django.urls import path
from . import views

app_name = "polls"
# This is a way for us to link our polls urls in particular to our polls views.
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]  # for /polls
