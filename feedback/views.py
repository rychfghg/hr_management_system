from django.shortcuts import render, redirect
from .models import Feedback

def feedback_view(request):
    error_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        suggestion = request.POST.get('suggestion')

    
        if not name or not email or not suggestion:
            error_message = 'All fields are required!'
        else:
            Feedback.objects.create(name=name, email=email, suggestion=suggestion)
            return redirect('feedback_list') 

    return render(request, 'feedback/feedback_form.html', {'error_message': error_message})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})
