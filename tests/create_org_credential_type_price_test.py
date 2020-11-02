from tests.login_admin_test import test_login_admin as LoginStep
from pages.Organization import OrganizationCredentialTypePriceMenu

def test_create_org_credential_type_price(driver):
    LoginStep(driver)
    createRecord = OrganizationCredentialTypePriceMenu(driver)
    createRecord.load()
    createRecord.click_btn_create_new()
    createRecord.choose_organization('101 Supplier')
    createRecord.choose_type('Licence')
    createRecord.enter_price(5)
    createRecord.click_btn_submit()