from django.urls import path
from django.views.generic import TemplateView

from django_paystack import views

app_name = "paystack"

urlpatterns = [
    path("verify/<order_id>/", views.verify_payment, name="verify_payment"),
    path("successful-verification/<order_id>/", views.success_redirect_view, name="successful_verification"),
    path("failed-verification/<order_id>/", views.failure_redirect_view, name="failed_verification"),
    path("success-page/", TemplateView.as_view(template_name="django_paystack/sample.htmx"), name="success_page"),
    path("failure-page/", TemplateView.as_view(template_name="django_paystack/sample.htmx"), name="failure_page"),
    path("example/", TemplateView.as_view(template_name="django_paystack/sample.htmx"), name="home"),

]