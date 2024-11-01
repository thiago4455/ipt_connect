from django.utils import translation

url_locale = (('/', 'pt-br'),)


class URLLocaleMiddleware:
    def process_request(self, request):
        for (url, loc) in url_locale:
            if request.path.startswith(url):
                request.LANG = loc
                print request.LANG
                translation.activate(request.LANG)
                request.LANGUAGE_CODE = request.LANG

    def process_response(self, request, response):
        translation.deactivate()
        return response
