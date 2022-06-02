from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ( ListView, DetailView,
                    TemplateView, CreateView)
from .models import CustomUser
from orders.models import Order
from .forms import ChangeProfileImageForm

class ProfileView(TemplateView):
    template_name = 'customers/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_ = CustomUser.objects.get(email=self.request.user)
        slug_ = self.kwargs.get('slug')
        order_ = None
        if slug_ == "order-history":
            order_ = Order.objects.filter(user= user_)
            self.template_name = 'customers/order_history.html'
        form_ = None
        if slug_ == "change-profile-image":
            form_ = ChangeProfileImageForm()
            self.template_name = 'customers/change_profile_image.html'
        context.update({'user': user_, 'order_': order_, 'form_' : form_})
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ChangeProfileImageForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                print('hiii')

        return redirect('customers:profile')
