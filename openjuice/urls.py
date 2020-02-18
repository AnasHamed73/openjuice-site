from django.urls import path

from . import views

app_name = "openjuice"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('domains', views.domains, name='domains'),
    path('d/<str:code>', views.domain, name='domain'),
    path('topics', views.topics, name='topics'),
    path('t/<str:code>', views.topic, name='topic'),
    path('search_topics', views.search_topics, name='search_topics'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
