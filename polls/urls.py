from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import (
    PollList, PollDetail,
    ChoiceList, CreateVote,
    UserCreate, LoginView)
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet
router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path('polls/', polls_list, name="polls_list"),
    # path('polls/<int:pk>/', polls_detail, name="polls_detail"),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('polls/', PollList.as_view(), name='pollsapi_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name="pollsapi_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(), name="create_vote"),

    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('vote/', CreateVote.as_view(), name="create_vote"),
    path('login/', LoginView.as_view(), name='login'),
    # path('login/', views.obtain_auth_token, name='login'),

]
urlpatterns += router.urls
