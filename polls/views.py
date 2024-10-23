from django.shortcuts import HttpResponse

# Question “index” page – displays the latest few questions.
# Question “detail” page – displays a question text, with no results but with a form to vote.
# Question “results” page – displays results for a particular question.


def index(request):
    return HttpResponse("Hello World. You're at the polls index")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the resuls for question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting for question %s" % question_id)
