from django.urls import path
from . import views

app_name = 'web_pages'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("psychotherapy/", views.psychotherapy, name="psychotherapy"),
    path("adhd-support/", views.adhd, name="adhd"),
    path("what-to-expect/", views.what_to_expect, name="what-to-expect"),
    path("resources/", views.resources, name="resources"),
    path("contact-psp/", views.contact_form, name="contact"),
]
