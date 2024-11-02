from django.utils import translation
from django.utils.deprecation import MiddlewareMixin

url_locale = (('/FPT2017', 'fr'),)


class URLLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        for (url, loc) in url_locale:
            if request.path.startswith(url):
                request.LANG = loc
                translation.activate(request.LANG)
                request.LANGUAGE_CODE = request.LANG

    def process_response(self, request, response):
        translation.deactivate()
        return response
