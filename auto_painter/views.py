import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import AutoPainter


def auto_painter(request):
    """Enter auto painter page."""
    return render(request, 'auto_painter/autopainter.html')


def list_view(request):
    """List view function."""
    latest_auto_painter_list = AutoPainter.objects.all()
    context = {
        'latest_auto_painter_list': latest_auto_painter_list
    }
    return render(request, template_name='auto_painter/autopainter_list.html',
                  context=context)


class ListView(generic.ListView):
    """List view class."""
    template_name = 'auto_painter/autopainter_list.html'
    context_object_name = 'latest_auto_painter_list'

    def get_queryset(self):
        return AutoPainter.objects.all()


def detail_view(request, auto_painter_id):
    """Detail view function."""
    # try:
    #     response = AutoPainter.objects.get(id=auto_painter_id)
    # except AutoPainter.DoesNotExist:
    #     raise Http404
    response = get_object_or_404(AutoPainter, pk=auto_painter_id)
    return HttpResponse(str(response))


class DetailView(generic.DetailView):
    """Detail view class."""
    model = AutoPainter
    # Default context object name is the model name. Default template view
    # name is the model_name_detail.html
    # context_object_name = 'autopainter'
    # template_name = 'auto_painter/autopainter_detail.html'


def insert(request):
    print(request.COOKIES)
    stroke = json.loads(request.body)
    auto_painter = AutoPainter()
    auto_painter.class_name = "flower"
    auto_painter.begin_stroke = stroke['begin_stroke']
    auto_painter.follow_stroke = stroke['follow_stroke']
    auto_painter.pub_date = timezone.now()
    auto_painter.save()
    return HttpResponse("insert success.")
