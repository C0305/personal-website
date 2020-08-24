from django.shortcuts import render
from .models import PortfolioSettings, Project
from crm.forms import LeadForm

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

    return render(request, 'home.html', {
        'portfolio': portfolio_settings,
        'tech_stack': tech_stack,
        'featured_projects' : featured_projects,
        'form': form
    })
