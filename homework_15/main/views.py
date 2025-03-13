from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    """
    View for the homepage.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered homepage template.
    """
    return render(request, 'main/home.html')


def about(request):
    """
    View for the about page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered about template with an updated_at field.
    """
    updated_at_str = '2025-03-12'
    updated_at = datetime.strptime(updated_at_str, '%Y-%m-%d')
    return render(request, 'main/about.html', {'updated_at': updated_at})


class ContactView(TemplateView):
    """
    View for the contact page.
    Inherits from TemplateView and renders the contact template.
    """
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):

        context = {
            'has_support': True,
            'free_consultation': False
        }
        return context


class ServiceView(TemplateView):
    """
    View for the services page, listing different services and providing filter options.

    Inherits from TemplateView and renders the services template.
    """
    template_name = 'main/services.html'
    FILTER_TYPES = ['IT', 'MARKETING', 'SEO']

    def parse_filter(self, context):
        """
        Filters the services based on the 'filter' query parameter in the request.

        Args:
            context: The context data passed to the template.

        Returns:
            A filtered list of services if the filter exists and matches one of ['IT', 'MARKETING', 'SEO'],
            or the full list of services if no valid filter is provided.
        """
        try:
            filter_type = self.request.GET['filter']
            if filter_type in self.FILTER_TYPES:
                # Filter services by the selected filter type
                return list(filter(lambda el: el['type'] == filter_type, context['services']))
        except KeyError:
            pass  # If no filter is provided, return all services.
        return context['services']

    def get_context_data(self, **kwargs: object) -> dict:
        """
        Provides the context data for the services template, including a list of services
        and applying any requested filter.

        Args:
            kwargs: Additional arguments for the context.

        Returns:
            A dictionary containing the filtered or unfiltered list of services.
        """
        context = super().get_context_data(**kwargs)
        context['services'] = [
            {'name': 'Web Development', 'description': 'Creating professional websites.', 'type': "IT"},
            {'name': 'SEO Optimization', 'description': 'Improving visibility in search engines.', 'type': "SEO"},
            {'name': 'Marketing', 'description': 'Advertising campaigns and brand promotion.', 'type': "MARKETING"},
            {'name': "Context advertisement", 'description': "Advertising campaigns in Google AdWords.", 'type': "SEO"},
            {'name': "SMM", 'description': "Advertising on social media.", 'type': "MARKETING"},
            {'name': "Site Supporting", 'description': "Support for your site by our developers.", 'type': "IT"},
            {'name': "Site Migration", 'description': "Migrating your site to another server.", 'type': "IT"},
        ]
        # Apply any requested filter to the services
        f_context = {'services': self.parse_filter(context)}
        return f_context
