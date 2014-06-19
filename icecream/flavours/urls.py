from django.conf.urls import patterns, url

from .views import FlavourCreateView, FlavourUpdateView, FlavourDetailView

urlpatterns = patterns('',
    
    # ex: /guides/make-a-seashell-candle
    url(r'^create/$', FlavourCreateView.as_view(template_name="create.html"), name="create"),
    url(r'^update/(?P<slug>[-\w]+)$', FlavourUpdateView.as_view(template_name="update.html"), name="update"),
    url(r'^(?P<slug>[-\w]+)/$', FlavourDetailView.as_view(template_name="detail.html"), name="detail"),
    #url(r'^(?P<slug>[-\w]+)/$', FlavourDetailView.as_view(template_name='detail.html', name='detail'),
    #url(r'^create/$', 'guides.views.create', name='create'),
    #url(r'^create/(?P<guide_id>\d+)/material/$', 'guides.views.create_material', name='create_material'),
    #url(r'^create_steps/(?P<guide_id>\d+)/$', 'guides.views.create_steps', name='create_steps'),    
)