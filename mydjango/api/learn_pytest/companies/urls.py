from rest_framework import routers

from api.learn_pytest.companies.views import CompanyViewSet

companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")
