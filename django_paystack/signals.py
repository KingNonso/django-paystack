from django.dispatch import Signal

payment_verified = Signal()

event_signal = Signal()

successful_payment_signal = Signal()

successful_transfer_signal = Signal()

failed_transfer_signal = Signal()
