from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AddAddressMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request, *args, **kwargs):
        if request.user.is_authenticated and request.path != "/order/address/":
            user_orders = request.user.order_set.all()

            if user_orders:
                if not hasattr(request.user, "useraddress"):
                    return redirect("create-address-to-order", **kwargs)
