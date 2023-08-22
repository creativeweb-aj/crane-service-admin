from rest_framework import serializers

from apps.about.models import WorkingDay
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
