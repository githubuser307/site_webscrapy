from django.shortcuts import render, get_object_or_404

from .models import *



class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        return render( request, self.template, context={self.model.__name__.lower(): obj})