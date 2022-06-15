from django.views.generic import View
from django.shortcuts import render
class BaseView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, 'index.html', context)
