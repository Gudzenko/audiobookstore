import logging
from django.http import HttpResponse


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Main.view')


def index(request):
    return HttpResponse("Hello world!")