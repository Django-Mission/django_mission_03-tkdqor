from django.shortcuts import render
from .models import Faq

# Create your views here.

def faq(request):
    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'support/faq.html', context)
