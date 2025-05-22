from django.contrib import admin
from .models import AboutUs, Blog, CompanyInfo, CompanyStats, ContactUs, ProjectCategory, Projects, Services, SocialMedia, TeamMember, Testimonial, WhyChooseUs

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if CompanyInfo.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SocialMedia.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if WhyChooseUs.objects.count() >= 3:
            return False
        return super().has_add_permission(request)
    

@admin.register(CompanyStats)
class CompanyStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if CompanyStats.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutUs.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(TeamMember)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(ContactUs)
admin.site.register(ProjectCategory)
