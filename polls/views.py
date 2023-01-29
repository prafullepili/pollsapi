from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    # data = {'results': list(polls.values(
    # "question", "created_by__username", "pub_date", "created_by__first_name"))}

    data = {"results": []}
    for poll in polls:
        data["results"].append({
            "question": poll.question,
            "username": poll.created_by.username,
            "first Name": poll.created_by.first_name,
            "last Name": poll.created_by.last_name,
            "pub_date": poll.pub_date,
        })
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date,
        "first_name": poll.created_by.first_name,
        "last_name": poll.created_by.last_name,
    }}
