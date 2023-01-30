#pylint:disable=E0402
from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail

urlpatterns = [
    path('polls/', polls_list, name="polls_list"),
    path('polls/<int:pk>/', polls_detail, name="polls_detail"),
    path('pollsapi/', PollList.as_view(), name='pollsapi_list'),
    path('pollsapi/<int:pk>/', PollDetail.as_view(), name="pollsapi_detail"),
]
