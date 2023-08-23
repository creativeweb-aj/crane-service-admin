from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.about.models import WorkingDay, About, KeyPoint, Person, OurValue
from apps.api.modules import responseData, setException
from DjangoBaseSetup.common_modules.mainService import Status
from apps.api.ApiMessages import CommonApiMessages
from apps.api.modules.HomeApi.serializer import WorkingDaySerializer, SocialLinkSerializer, AboutSerializer, \
    PersonSerializer, KeyPointSerializer, OurValueSerializer, ServiceSerializer, ProjectSerializer, \
    TestimonialSerializer, MessageSerializer
from apps.api.modules.HomeApi.service import HomeService
from apps.customers.models import Message, Testimonial
from apps.project.models import Project
from apps.service.models import Service
from apps.settings.models import Setting
from apps.social_page.models import SocialLink


@swagger_auto_schema(
    method='get',
    responses=responseData
)
@api_view(['GET'])
def siteDetails(request):
    siteData = HomeService.siteSettingDetail()
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


@swagger_auto_schema(
    method='get',
    responses=responseData
)
@api_view(['GET'])
def about(request):
    aboutObj = About.objects.filter(is_active=True, is_delete=False).first()
    aboutSerializer = AboutSerializer(aboutObj)
    personsObj = Person.objects.filter(is_active=True, is_delete=False).order_by('id')
    personSerializer = PersonSerializer(personsObj, many=True)
    keyPointsObj = KeyPoint.objects.filter(is_active=True, is_delete=False).order_by('id')
    keyPointSerializer = KeyPointSerializer(keyPointsObj, many=True)
    ourValuesObj = OurValue.objects.filter(is_active=True, is_delete=False).order_by('id')
    ourValueSerializer = OurValueSerializer(ourValuesObj, many=True)
    resData = dict()
    # Make response data success case
    resData['status'] = Status.success.value
    resData['data'] = {
        "about": aboutSerializer.data,
        "persons": personSerializer.data,
        "key_point": keyPointSerializer.data,
        "our_values": ourValueSerializer.data
    }
    resData['message'] = CommonApiMessages.data_sent_successfully.value
    resData['errors'] = []
    status_code = 200
    return Response(resData, status=status_code)


@swagger_auto_schema(
    method='get',
    responses=responseData
)
@api_view(['GET'])
def services(request):
    servicesObj = Service.objects.filter(is_active=True, is_delete=False).order_by('id')
    serviceSerializer = ServiceSerializer(servicesObj, many=True)
    resData = dict()
    # Make response data success case
    resData['status'] = Status.success.value
    resData['data'] = {
        "services": serviceSerializer.data
    }
    resData['message'] = CommonApiMessages.data_sent_successfully.value
    resData['errors'] = []
    status_code = 200
    return Response(resData, status=status_code)


@swagger_auto_schema(
    method='get',
    responses=responseData
)
@api_view(['GET'])
def projects(request):
    projectsObj = Project.objects.filter(is_active=True, is_delete=False).order_by('id')
    projectSerializer = ProjectSerializer(projectsObj, many=True)
    resData = dict()
    # Make response data success case
    resData['status'] = Status.success.value
    resData['data'] = {
        "projects": projectSerializer.data
    }
    resData['message'] = CommonApiMessages.data_sent_successfully.value
    resData['errors'] = []
    status_code = 200
    return Response(resData, status=status_code)


@swagger_auto_schema(
    method='get',
    responses=responseData
)
@api_view(['GET'])
def testimonials(request):
    testimonialsObj = Testimonial.objects.filter(is_active=True, is_delete=False).order_by('id')
    testimonialSerializer = TestimonialSerializer(testimonialsObj, many=True)
    resData = dict()
    # Make response data success case
    resData['status'] = Status.success.value
    resData['data'] = {
        "testimonials": testimonialSerializer.data
    }
    resData['message'] = CommonApiMessages.data_sent_successfully.value
    resData['errors'] = []
    status_code = 200
    return Response(resData, status=status_code)


@swagger_auto_schema(
    method='post',
    request_body=MessageSerializer,
    responses=responseData
)
@api_view(['POST'])
def addMessage(request):
    resData = dict()
    messageSerializer = MessageSerializer(data=request.data, context={'request': request})
    if messageSerializer.is_valid():
        messageSerializer.save()
        resData['status'] = Status.success.value
        resData['data'] = None
        resData['message'] = CommonApiMessages.email_sent_successfully.value
        resData['errors'] = []
        status_code = 200
    else:
        # Make response data fail case
        res = setException(messageSerializer)
        resData['status'] = Status.error.value
        resData['data'] = {}
        resData['message'] = res.get('message')
        resData['errors'] = res.get('errors')
        status_code = 200
    return Response(resData, status=status_code)