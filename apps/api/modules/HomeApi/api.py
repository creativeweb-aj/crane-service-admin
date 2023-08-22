from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.about.models import WorkingDay
from apps.api.modules import responseData
from DjangoBaseSetup.common_modules.mainService import Status
from apps.api.ApiMessages import CommonApiMessages
from apps.api.modules.HomeApi.serializer import WorkingDaySerializer, SocialLinkSerializer
from apps.api.modules.HomeApi.service import HomeService
from apps.settings.models import Setting
from apps.social_page.models import SocialLink


@swagger_auto_schema(
    method='get',
    responses=responseData
)
@api_view(['GET'])
def siteDetails(request):
    homeService = HomeService()
    siteData = homeService.siteSettingDetail()
    workingDays = WorkingDay.objects.filter(is_active=True, is_delete=False).order_by('id')
    workingDaySerializer = WorkingDaySerializer(workingDays, many=True)
    socialLinks = SocialLink.objects.filter(is_active=True, is_delete=False).order_by('id')
    socialLinkSerializer = SocialLinkSerializer(socialLinks, many=True)
    resData = dict()
    # Make response data success case
    resData['status'] = Status.success.value
    resData['data'] = {
        "site_info": siteData,
        "working_days": workingDaySerializer.data,
        "social_links": socialLinkSerializer.data
    }
    resData['message'] = CommonApiMessages.data_sent_successfully.value
    resData['errors'] = []
    status_code = 200
    return Response(resData, status=status_code)

