from django.shortcuts import render
from .models import Inquiry, Answer

# Create your views here.

def inquiry(request):
    inquiries = Inquiry.objects.all()

    context = {
        'inquiries': inquiries,
    }

    return render(request, 'support/inquiry.html', context)