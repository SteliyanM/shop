from django.shortcuts import redirect


class AdminRequired:
    def dispatch(self, request, *args, **kwargs):
        if not (self.request.user.is_staff or self.request.user.is_superuser):
            return redirect("index")

        return super().dispatch(request, *args, **kwargs)

