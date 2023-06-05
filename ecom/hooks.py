from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt
from ecom.models import Order, OrderItem

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != 'bizdevesh@gmail.com':
            # Not a valid payment
            print("Not Valid Payment")
            return
        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.
        try:
            my_pk = ipn_obj.invoice
            print(ipn_obj)
            mytransaction = Order.objects.get(pk=my_pk)
            assert ipn_obj.mc_gross == mytransaction.total_amount 
        except Exception:
            mytransaction.invalid = True
            mytransaction.save()
            print('Paypal ipn_obj data not valid!')
        else:
            mytransaction.paid = True
            mytransaction.save()
    else:
        print('Paypal payment status not completed: %s' % ipn_obj.payment_status)