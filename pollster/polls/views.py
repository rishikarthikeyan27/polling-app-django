from django.urls import reverse
from multiprocessing import context
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from httplib2 import Http
from .models import Question, Choice

# Get questions and display them.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# Show specific question and choices
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


# Get questions and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    print("CHOICE ---> ", request.POST["choice"])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST["choice"])
        print("SELECTED CHOICE --> ", selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {"question": question, "error_message": "You did not select a choice"},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
