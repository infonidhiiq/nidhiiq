import os

class Settings:
    PROJECT_NAME: str = "NidhiIQ — PolicyBazaar Financial Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./nidhiiq.db"
    CONTACT_PHONE: str = "+91 63618 39979"
    CONTACT_EMAIL: str = "suman@nidhiiq.com"
    WHATSAPP_NUMBER: str = "916361839979"
    OFFICE_ADDRESS: str = "Ground Floor, Behive, HSR Silkboard, Bengaluru-560068, Karnataka, INDIA"

settings = Settings()
