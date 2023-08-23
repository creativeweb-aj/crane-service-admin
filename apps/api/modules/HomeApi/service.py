from apps.customers.models import Message
from apps.settings.models import Setting


class HomeService:
    def __init__(self):
        pass

    @staticmethod
    def siteSettingDetail():
        siteSettings = Setting.objects.filter(key__icontains='Site', editable=True)
        data = {}
        for siteSetting in siteSettings:
            if siteSetting.key == "Site.logo":
                data['logo'] = siteSetting.value
            elif siteSetting.key == "Site.name":
                data['site_name'] = siteSetting.value
            elif siteSetting.key == "Site.tagline":
                data['tagline'] = siteSetting.value
            elif siteSetting.key == "Site.site-email":
                data['email'] = siteSetting.value
            elif siteSetting.key == "Site.mobile1":
                data['mobile'] = siteSetting.value
            elif siteSetting.key == "Site.address":
                data['address'] = siteSetting.value
            else:
                pass
        return data

    @staticmethod
    def saveMessage(data):
        message = Message()
        message.name = data.get('name', None)
        message.email = data.get('email', None)
        message.subject = data.get('subject', None)
        message.message = data.get('message', None)
        message.save()
        return True
