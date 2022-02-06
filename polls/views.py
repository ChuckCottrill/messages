from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# get_list_or_404
# from django.template import loader


from .models import Question, Choice

HOWMANY=5

def index(request):
    latest_question_list = Question.objects.order_by("-published")[:HOWMANY]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))
    # output = ", ".join([q.question for q in latest_question_list])
    # return HttpResponse(output)


def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You did not select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return HttpResponseRedirect after successful handle POST
        # prevents data from being POSTed twice when user hits back button
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

