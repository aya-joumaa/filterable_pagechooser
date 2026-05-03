from .base import *
from .base import env

SECRET_KEY = env.str('DJANGO_SECRET_KEY', default="django-insecure-)rz$+ud$oi1$&w(@$^dtr_@_p5*fk_n)h!_ih6)37j$h=ng4hb")

# ---------------------------------------------------------------------------------------------------------------------
# DataBase Configurations
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# DataBase Configurations
# ---------------------------------------------------------------------------------------------------------------------
DATABASES = {
    'default': env.db(),
}

# ---------------------------------------------------------------------------------------------------------------------
# This Section Is Used If we need to set-up our project with django-storages and Amazon S3
# Helper Article to get more information about django-storages and Amazon S3:
#   https://wearecodevision.com/blog/configuring-django-storages-aws-s3
#   https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
#   https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html
#
# Needed Packages:
#   1- boto3: https://pypi.org/project/boto3/
#   2- django-storages: https://pypi.org/project/django-storages/
# ---------------------------------------------------------------------------------------------------------------------
USE_S3 = env.bool("USE_S3", default=False)
if USE_S3:
    AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_S3_BUCKET")
    AWS_S3_REGION_NAME = env.str("AWS_S3_REGION")
    AWS_IS_GZIPPED = True
    AWS_S3_ENDPOINT_URL = env.str(
        "AWS_S3_ENDPOINT_URL", f"https://s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    )

    # CloudFront domain
    AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", default=None)

    # Configure storage backends (Django 4.2+)
    STORAGES = {
        "default": {
            "BACKEND": "config.storages.MediaRootS3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "config.storages.StaticRootS3Boto3Storage",
        },
    }

    # Static on S3/CloudFront
    STATICFILES_LOCATION = "static"
    if AWS_S3_CUSTOM_DOMAIN:
        STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    else:
        STATIC_URL = "{}/{}/{}/".format(AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME, STATICFILES_LOCATION)

    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_STORAGE = "config.storages.StaticRootS3Boto3Storage"
    COMPRESS_URL = STATIC_URL

    # Media on S3/CloudFront
    MEDIAFILES_LOCATION = "media"
    if AWS_S3_CUSTOM_DOMAIN:
        MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
    else:
        MEDIA_URL = "{}/{}/{}/".format(AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION)
# ---------------------------------------------------------------------------------------------------------------------
# Reference To Redis With Django: https://pypi.org/project/django-redis/
# ---------------------------------------------------------------------------------------------------------------------
REDIS_URL = env.str("REDIS_URL", default="")
if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        },

        "redis": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL,
            "TIMEOUT": 6000,
            "OPTIONS": {
                "MAX_ENTRIES": 1000
            }
        },

        "renditions": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL,
            "TIMEOUT": 600,
            "OPTIONS": {
                "MAX_ENTRIES": 1000
            }
        }
    }

DEBUG = STAGING = env.bool("DJANGO_DEBUG", False)
if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)
