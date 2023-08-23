from rest_framework import serializers, exceptions
from DjangoBaseSetup.common_modules.mainService import MainService
from DjangoBaseSetup.messages.messages import ValidationMessages
from apps.about.models import WorkingDay, About, Person, KeyPoint, OurValue
from apps.api.modules.HomeApi.service import HomeService
from apps.customers.models import Message, Testimonial
from apps.project.models import Project
from apps.service.models import Service
from apps.social_page.models import SocialLink


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = ['id', 'day', 'start_time', 'end_time']


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'social_page', 'link']
        depth = 1


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'description']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'image']


class KeyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPoint
        fields = ['id', 'icon', 'name']


class OurValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurValue
        fields = ['id', 'title', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'image', 'icon']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'crane', 'image', 'title', 'description', 'address']
        depth = 1


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'client_name', 'client_image', 'comment']


class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)

    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(MessageSerializer, self).__init__(*args, **kwargs)
        # Override field required and blank message
        MainService.fieldRequiredMessage(self.fields)

    # Validate data
    def validate(self, data):
        errors = []
        name = data.get('name', None)
        email = data.get('email', None)
        subject = data.get('subject', None)
        message = data.get('message', None)

        if name == "" or name is None:
            error = {
                "field": "name",
                "message": ValidationMessages.name_field_is_required.value
            }
            errors.append(error)

        if email == "" or email is None:
            error = {
                "field": "email",
                "message": ValidationMessages.email_field_is_required.value
            }
            errors.append(error)

        if subject == "" or subject is None:
            error = {
                "field": "subject",
                "message": ValidationMessages.subject_field_is_required.value
            }
            errors.append(error)

        if message == "" or message is None:
            error = {
                "field": "message",
                "message": ValidationMessages.message_field_is_required.value
            }
            errors.append(error)

        if len(errors) > 0:
            raise exceptions.ValidationError(errors)
        return data

    def create(self, validated_data):
        HomeService.saveMessage(validated_data)
        return validated_data
