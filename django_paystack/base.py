from pprint import pprint
from django.http import HttpResponse
from pypaystack2 import Paystack
from django.conf import settings


class DjangoPaystack(Paystack):
    """A subclass of Paystack with additional functionality."""

    def __init__(self, auth_key: str = None):
        # Set the PAYSTACK_AUTHORIZATION_KEY
        auth_key = settings.PAYSTACK_SETTINGS['SECRET_KEY']

        # Call the superclass's __init__ method
        super().__init__(auth_key=auth_key)

    def verify_transaction(self, txref, amount_paid):
        """Verifies a transaction using the Paystack API.

            Args:
                txref (str): The transaction reference ID.
                amount_paid (float): The amount that was paid.

            Returns:
                bool: Whether the transaction was verified or not.

            Raises:
                ValueError: Does not raise a ValueError if the transaction was not verified
                Simply returns false

            """
        verification = self.transactions.verify(txref)
        if verification.status_code == 200:
            amount = verification.data['amount']
            currency = verification.data['currency']
            status = verification.data['status']
            if status == 'success' and int(amount) == int(amount_paid):
                return True
        return False



def get_js_script():
    return "https://js.paystack.co/v2/inline.js"


PAYSTACK_SETTINGS = {
    "PUBLIC_KEY": "pk_test_adc1cf08c1801cbc5bdf8467085dcff49197d410",
    "SECRET_KEY": "sk_test_ba0ac6933be178ee51888e79714c9a8cef4517de",
    "CURRENCY": "NGN",
    "BUTTON_CLASS": "",
    "BUTTON_ID": "django-paystack-button",
    "SUCCESS_URL": "paystack:success_page",
    "FAILURE_URL": "paystack:failure_page",
}