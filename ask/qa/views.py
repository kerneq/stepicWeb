from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from qa.models import Question


def test(request):
    qs = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def test2(request, id):
    try:
        int(id)
        qs = Question.objects.filter(pk=id)[0]
        answers = qs.answer_set.all()
    except KeyboardInterrupt:
        raise Http404
    return render(request, 'qa/question.html', {
        'qs': qs,
        'answers': answers,
    })


def test3(request):
    qs = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
