from django.utils import timezone
from django.db import models

class CompanyInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return "Company Info"

    class Meta:
        verbose_name = "Company Info"
        verbose_name_plural = "Company Info"

class SocialMedia(models.Model):
    facebook = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.facebook or self.twitter or self.instagram or self.linkedin

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Why Choose Us"
        verbose_name_plural = "Why Choose Us"
    
class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class CompanyStats(models.Model):
    completed_projects = models.PositiveIntegerField()
    happy_clients = models.PositiveIntegerField()
    qualified_team = models.PositiveIntegerField()
    years_experience = models.PositiveIntegerField()


    def __str__(self):
        return "Company Stats"

    class Meta:
        verbose_name = "Company Stat"
        verbose_name_plural = "Company Stats"

class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

class Projects(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

class Testimonial(models.Model):
    rate = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    project = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"