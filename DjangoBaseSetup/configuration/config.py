import os
from datetime import timedelta


SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'import.path.to.urls.api_info',
    'USE_SESSION_AUTH': False,
    'exclude_namespaces': ['UserApi.api.login'],
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=600),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.environ.get("SECRET_KEY", ""),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=7),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=90),
}

PWA_APP_NAME = 'ADOT Admin'
PWA_APP_DESCRIPTION = "TURNING IDEAS INTO INNOVATIVE SOFTWARE SOLUTIONS."
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        # 'src': 'https://mahalaxmi-crane-service.s3.amazonaws.com/static/img/icon-160x160.png',
        'src': '/static/img/icon-160x160.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        # 'src': 'https://mahalaxmi-crane-service.s3.amazonaws.com/static/img/icon-160x160.png',
        'src': '/static/img/icon-160x160.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        # 'src': 'https://mahalaxmi-crane-service.s3.amazonaws.com/static/img/ADOT.svg',
        'src': '/static/img/ADOT.svg',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

# AWS S3 Bucket Configurations
# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", '')
# AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", '')
# AWS_STORAGE_BUCKET_NAME = 'mahalaxmi-crane-service'
# AWS_S3_REGION_NAME = 'eu-north-1'
# AWS_S3_ADDRESSING_STYLE = "virtual"
# AWS_LOCATION = 'media'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# AWS_S3_VERITY = True
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }