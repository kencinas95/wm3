import os
import datetime

ENVIRONMENTS = ['dev', 'test', 'prod']

# App active profile (test, qa, pre-prod, prod)
PROFILE = os.environ.get('PROFILE', 'dev')

# Frontend build version
WEB_VERSION = "0.0.0-SNAPSHOT"

# Backend build version
API_VERSION = "0.0.0-SNAPSHOT"

# Location (country/tz)
LOCATION_INFO = "AR/UTC-3"

# The Cave website information
WEBSITE_INFO = {
    "Name": "cave",
    "Description": "Wishmakers",
    "Web-Version": WEB_VERSION,
    "Api-Version": API_VERSION,
    "Release-Date": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%s"),
    "Location": LOCATION_INFO
}

# Website signature
SIGNATURE = f"{PROFILE}:6024188771625540361998461010582834363623646621381720856213532762"
