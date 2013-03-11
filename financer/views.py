from django.template.response import TemplateResponse
from django.views.generic import View


class HomePageView(View):
    """Displays the details of a BlogPost"""

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "home.html"

    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            "title": "homepage",
        }
