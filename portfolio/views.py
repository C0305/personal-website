from django.shortcuts import render, redirect
from .models import PortfolioSettings, Project
from crm.forms import LeadForm
from django.core.mail import EmailMessage
from threading import Thread



# Create your views here.
def home(request):
    portfolio_settings = PortfolioSettings.objects.get(is_default=True)
    featured_projects = Project.objects.filter(featured=True)
    tech_stack = []
    for value in portfolio_settings.technologiesstack_set.all():
        if len(tech_stack) != 0 and len(tech_stack[-1]) < 5:
            tech_stack[-1].append(value)
        else:
            tech_stack.append([value])

    form = LeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        subject = f"Get In Touch - {request.POST.get('subject')}"
        message = f"""
            Name: {request.POST.get('name')}.
            E-Mal: {request.POST.get('email')}
            Message: {request.POST.get('message')}.
        """
        msg = EmailMessage(
            subject,
            message,
            "no-reply@cobos.io",
            ["ernesto@cobos.io"],
            reply_to=[request.POST.get('email')],
        )
        thread = Thread(target=msg.send)
        thread.start()
        return redirect(to='/send_email/')

    return render(request, 'home.html', {
        'portfolio': portfolio_settings,
        'tech_stack': tech_stack,
        'featured_projects' : featured_projects,
        'form': form
    })
def send_email(request):
    return render(request, 'send_email.html',)