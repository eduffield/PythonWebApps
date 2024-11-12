from django.core.management.base import BaseCommand
from requests import get

class Command(BaseCommand):

    def handle(self, *args, **options):

        pages = {
            "https://jellyfish-app-m5nzs.ondigitalocean.app/",
            "https://jellyfish-app-m5nzs.ondigitalocean.app/hero/",
            "https://jellyfish-app-m5nzs.ondigitalocean.app/hero/add",
            "https://jellyfish-app-m5nzs.ondigitalocean.app/reporter/",
            "https://jellyfish-app-m5nzs.ondigitalocean.app/reporter/add",
            "https://jellyfish-app-m5nzs.ondigitalocean.app/article/",
            "https://jellyfish-app-m5nzs.ondigitalocean.app/article/add"
                }
        
        for page in pages:
            response = get(page)
            print(response.url + "   Expected Response: 200   Actual Response: " + str(response.status_code))