from django.views.generic import TemplateView
from . import models
import json
from django.shortcuts import HttpResponse


class Alarm(TemplateView):
    template_name = "alarms/alarm.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        context['username'] = self.request.user.username

        return context


class ShareMe(TemplateView):
    template_name = "alarms/ShareMe.html"

    def get_context_data(self, **kwargs):
        context=super(TemplateView, self).get_context_data()
        context['username']=self.request.user.username

        return context

    def post(self, request, **kwargs):
        ins=models.Alarm()
        data_unicode=request.body.decode('utf-8')
        data=json.loads(data_unicode)
        ins.message=data['message']
        print(ins.message)
        ins.save()

        return HttpResponse('')