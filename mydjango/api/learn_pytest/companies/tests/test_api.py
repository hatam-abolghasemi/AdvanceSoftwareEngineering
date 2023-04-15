import json
import pytest
from django.urls import reverse
from api.learn_pytest.companies.models import Company
from api.conftest import netflix

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db

# ==========================TEST GET COMPANIES===========================


def test_zero_companies_should_return_empty_list(client) -> None:
    resource = client.get(companies_url)
    assert resource.status_code == 200
    assert json.loads(resource.content) == []


def test_one_company_exist_should_succeed(client, netflix) -> None:
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == netflix.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


# ==========================TEST POST COMPANIES===========================


def test_create_company_with_out_argument_failed(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="Facebook")
    response = client.post(path=companies_url, data={"name": "Facebook"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_all_fields_should_be_default(client) -> None:
    response = client.post(path=companies_url, data={"name": "test company name"})
    assert response.status_code == 201
    response_content = response.json()
    assert response_content.get("name") == "test company name"
    assert response_content.get("application_link") == ""
    assert response_content.get("status") == "Hiring"
    assert response_content.get("notes") == ""


def test_create_company_with_layoff_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "test company ", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "test company", "status": "mio"}
    )
    assert response.status_code == 400
    res = str(response.content)
    assert "mio" in res
    assert "is not a valid choice" in res


@pytest.mark.parametrize("companies", [["instagram", "spacex", "TEST INC"], ["paypal", "bitmain"]], ids=["american simple companies", "american companies hold crypto currencies"], indirect=True)
def test_multiple_companies_exist_should_success(client, companies) -> None:
    company_names = set(map(lambda x: x.name, companies))
    response_companies = client.get(companies_url).json()
    assert len(company_names) == len(response_companies)
    response_companies_names = set(
        map(lambda company: company.get("name"), response_companies)
    )
    assert company_names == response_companies_names
