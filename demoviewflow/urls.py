from django.urls import include, path
from django.views import generic
from material.frontend import urls as frontend_urls

urlpatterns = [
    path(r'', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    path(r'', include(frontend_urls)),
]