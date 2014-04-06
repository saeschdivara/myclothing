from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _

from clothing.models import ClothingTime



def show(request):
    return render(request, 'clothing/layouts/index.html', {

    })


""" AngularJS views """
from djangular.views.crud import NgCRUDView

class ClothingTimeCRUDView(NgCRUDView):
    model = ClothingTime