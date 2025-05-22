from django.shortcuts import redirect, render
from django.contrib import messages

from core.models import AboutUs, Blog, CompanyStats, ContactUs, Projects, Services, TeamMember, Testimonial, WhyChooseUs

def index(request):
    about_us = AboutUs.objects.first()
    why_choose_us = WhyChooseUs.objects.all()[:3]
    services = Services.objects.all()
    company_stats = CompanyStats.objects.first()
    projects = Projects.objects.all()
    team_members = TeamMember.objects.all()
    blogs = Blog.objects.all()
    reviews = Testimonial.objects.all()

    context = {
        'about_us': about_us,
        'why_choose_us': why_choose_us,
        'services': services,
        'company_stats': company_stats,
        'projects': projects,
        'team_members': team_members,
        'blogs': blogs,
        'reviews': reviews,
    }
    return render(request, 'index.html', context)

def about(request):
    about_us = AboutUs.objects.first()
    team_members = TeamMember.objects.all()
    context = {
        'about_us': about_us,
        'why_choose_us': WhyChooseUs.objects.all(),
        'company_stats': CompanyStats.objects.first(),
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def services(request):
    services = Services.objects.all()
    company_stats = CompanyStats.objects.first()
    reviews = Testimonial.objects.all()
    context = {
        'services': services,
        'company_stats': company_stats,
        'reviews': reviews,
    }
    return render(request, 'service.html', context)

def contact(request):
    if request.method == 'POST':
        ContactUs.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            project=request.POST.get('project'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        return redirect('contact')
    return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', context={'blogs': blogs})

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', context={'team_members': team_members})

def projects(request):
    projects = Projects.objects.all()

    return render(request, 'project.html', context={'projects': projects})

def features(request):
    why_choose_us = WhyChooseUs.objects.all()

    return render(request, 'feature.html', context={'why_choose_us': why_choose_us})

def testimonials(request):
    reviews = Testimonial.objects.all()
    return render(request, 'testimonial.html', context={'reviews': reviews})