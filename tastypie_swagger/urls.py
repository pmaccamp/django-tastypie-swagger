from .views import SwaggerView, ResourcesView, SchemaView
from tastypie_swagger.views import SwaggerSpecs2View

from django.urls import re_path

urlpatterns = [
    re_path(r'^$', SwaggerView.as_view(), name='index'),
    re_path(r'^resources/$', ResourcesView.as_view(), name='resources'),
    re_path(r'^specs/(swagger.json)?$', SwaggerSpecs2View.as_view(), name='specs'),
    re_path(r'^schema/(?P<resource>\S+)/$', SchemaView.as_view()),
    re_path(r'^schema/$', SchemaView.as_view(), name='schema'),
]
