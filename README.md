# django_paystack

[![PyPI version](https://badge.fury.io/py/django_paystack.svg)](https://badge.fury.io/py/django_paystack)
[![Build Status](https://travis-ci.org/kingnonso/django_paystack.svg?branch=master)](https://travis-ci.org/kingnonso/django_paystack)
[![codecov](https://codecov.io/gh/kingnonso/django_paystack/branch/master/graph/badge.svg)](https://codecov.io/gh/kingnonso/django_paystack)

Django Paystack Payments package

## Documentation

The full documentation is at [https://django_paystack.readthedocs.io](https://django_paystack.readthedocs.io).

## Quickstart

Install django_paystack:

```bash
pip install django_paystack
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'django_paystack',
    ...
)
```

Then in your settings.py file, create the following settings:
```python

PAYSTACK_SETTINGS = {
    "PUBLIC_KEY": "pk_test_xxx",
    "SECRET_KEY": "sk_test_xxx",
    "CURRENCY": "NGN",
    "BUTTON_CLASS": "",
    "BUTTON_ID": "django-paystack-button",
    "SUCCESS_URL": "paystack:success_page",
    "FAILURE_URL": "paystack:failure_page",
}

```

Add django_paystack's URL patterns:

```python

urlpatterns = [
    ...
    path("paystack/", include(('django_paystack.urls','paystack'),namespace='paystack')),
    ...
]
```

## Features

- TODO

## Running Tests

Does the code actually work?

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```

## Development commands

```bash
pip install -r requirements_dev.txt
invoke -l
```

## Credits

Tools used in rendering this package:

- Based on the work of [pypaystack2](https://gray-adeyi.github.io/pypaystack2/)
- Inspiration from [gbozee/pypaystack](https://github.com/gbozee/pypaystack)
