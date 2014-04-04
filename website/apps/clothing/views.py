from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _


def show(request):
    return render(request, 'clothing/layouts/index.html', {

    })