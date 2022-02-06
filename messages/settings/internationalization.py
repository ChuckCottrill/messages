# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

from settings import env

# see env for ENV variables:
# LANGUAGE_CODE
# TIME_ZONE
# USE_TZ

LANGUAGE_CODE = env(LANGUAGE_CODE, default="en-us")
TIME_ZONE = env(TIME_ZONE, default="UTC")
USE_TZ = env.bool(USE_TZ, default=True)
USE_I18N = True
USE_L10N = True

