from .models import CompanyInfo, SocialMedia

def company_info(request):
    company = CompanyInfo.objects.first()
    return {'company_info': company}

def social_media(request):
    social_media = SocialMedia.objects.first()
    return {'social_media': social_media}