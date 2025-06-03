from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from core.models import AboutUs, Blog, CompanyStats, ContactUs, ProjectCategory, Projects, Services, TeamMember, Testimonial, WhyChooseUs

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
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project = request.POST.get('project')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Veritabanına kaydet
        ContactUs.objects.create(
            name=name,
            email=email,
            phone=phone,
            project=project,
            subject=subject,
            message=message,
        )
        full_message = f"""
Yeni bir kontakt formu mesajı alındı:

Ad: {name}
E-poçt: {email}
Telefon: {phone}
Layihə: {project}
Mövzu: {subject}

Mesaj:
{message}
        """

        send_mail(
            subject=f"Arccon kontakt formu - {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['info@arccon.az'],
            fail_silently=False,
        )

        messages.success(request, "Mesajınız uğurla göndərildi!")
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

def projects_by_category(request, category_name):
    category = get_object_or_404(ProjectCategory, name=category_name)
    projects = Projects.objects.filter(category=category)
    categories = ProjectCategory.objects.all()
    return render(request, 'project.html', context={
        'projects': projects,
        'categories': categories,
        'active_category': category
    })

def features(request):
    why_choose_us = WhyChooseUs.objects.all()

    return render(request, 'feature.html', context={'why_choose_us': why_choose_us})

def testimonials(request):
    reviews = Testimonial.objects.all()
    return render(request, 'testimonial.html', context={'reviews': reviews})