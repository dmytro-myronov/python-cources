from datetime import datetime

from django.shortcuts import render

# Create your views here.

def chat(request):
    """
    View for the about page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered about template with an updated_at field.
    """
    updated_at_str = '2025-03-12'
    updated_at = datetime.strptime(updated_at_str, '%Y-%m-%d')
    return render(request, 'chat.html', {'updated_at': updated_at})