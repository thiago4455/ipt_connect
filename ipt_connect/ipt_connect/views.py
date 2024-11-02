from django.http import HttpResponse


def home(request):
    text = """<h1>IPT Connect</h1>

              <a href="/">Results of BPT dev</a>"""
    return HttpResponse(text)
