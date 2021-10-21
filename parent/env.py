import os
import dotenv

# Load .profile env
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv.load_dotenv(os.path.join(basedir, '.profile'))

# App active profile (test, qa, pre-prod, prod)
PROFILE = os.environ['PROFILE']

# Location (country/tz)
LOCATION_INFO = "AR/UTC-3"

# Website signature
SIGNATURE = os.environ['SIGNATURE']

# Website information
WEBSITE_INFO = {
    "Name": "cave",
    "Profile": PROFILE,
    "Description": "Wishmakers",
    "Location": LOCATION_INFO,
    "Signature": SIGNATURE
}
