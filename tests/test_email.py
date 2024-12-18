import pytest
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

    
@pytest.mark.asyncio
async def test_send_markdown_email(email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }
    await email_service.send_user_email(user_data, 'email_verification')
    # Manual verification in Mailtrap

@pytest.mark.asyncio
async def test_send_professional_status_update_markdown_to_email(email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
    }
    await email_service.send_user_email(user_data, 'professional_status_is_now_upgraded')
    # Manual verification in Mailtrap
