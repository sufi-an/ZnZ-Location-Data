from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from django.http import HttpResponse
from django.views.generic import View

# from core.utils import render_to_pdf #created in step 4


class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        template_name = "index.html"
        return template_name
