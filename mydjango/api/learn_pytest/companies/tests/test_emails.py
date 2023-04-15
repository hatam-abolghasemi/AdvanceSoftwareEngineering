import json
from unittest.mock import patch
from django.core import mail
import pytest


def test_send_email_should_success(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0
    mail.send_mail(
        subject="subject",
        message="message",
        from_email="john1990ford@gmail.com",
        recipient_list=["john1990ford@gmail.com"],
        fail_silently=False,
    )
    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == "subject"


@pytest.mark.xfail
def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch(
        "api.learn_pytest.companies.views.send_mail"
    ) as mocked_send_mail_function:
        response = client.post(path="/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"
        mocked_send_mail_function.assert_called_with(
            subject=None,
            message=None,
            from_email="john1990ford@gmail.com",
            recipient_list=["john1990ford@gmail.com"],
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path="/send-email")
    response_content = json.loads(response.content)
    assert response.status_code == 405
    assert response_content["detail"] == 'Method "GET" not allowed.'
