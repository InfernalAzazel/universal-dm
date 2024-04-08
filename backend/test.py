import os

from mongoengine import connect

from admin.models import Interface

APP_NAME = os.environ.get("APP_NAME", "universal")
MONGODB_HOST = os.getenv('MONGODB_HOST', '127.0.0.1')
MONGODB_PORT = os.getenv('MONGODB_PORT', "27017")
MONGODB_DATABASE_NAME = os.getenv('MONGODB_DATABASE_NAME', APP_NAME)
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME', 'spb0122003')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'dcaGRzkJpuKsHgMs8hoS')
connect(
    db=APP_NAME,
    host=f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}"
)

for interface in Interface.objects:
    print(interface.title)