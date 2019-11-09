from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"


class IframeView(TemplateView):
    template_name = "iframe.html"
