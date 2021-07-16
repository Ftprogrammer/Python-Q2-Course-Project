import json

from django.contrib.auth.models import User
from django.shortcuts import render
from appi.models import UserInfo,Product,AddToCart,Order
from django.views import generic
from datetime import date


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView



@login_required
def index(request):
    return render(request, 'index.html',{})


class ProductList(LoginRequiredMixin,generic.ListView):
    model = Product
    template_name = 'appi/product_list.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin,generic.DetailView):
    model = Product
    template_name = 'appi/product_detail.html'




class MypasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('registration/password_reset_done.html')



class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'



class UserOrderView(generic.DetailView):
   template_name='appi/order_detail.html'
   model=Order
   context_object_name=order

   def dispatch(self,request,*args,**kwargs):
      if request.user.is_authenticated and UserInfo.objects.filter((user=request.user).exists())
           order_id=self.kwargs['pk']
           order=Order.objects.get[id=order_id]
           if request.user != order.id_user:
               return redirect('/index/')
         else:
              return redirect('/index/')
        return redirect('/login/')
      return super().dispatch(request,*args,**kwargs)



## admin pages




class AdminDailyOrderstList(LoginRequiredMixin,generic.ListView):
    model = Order
    template_name = 'appi/order_list.html'
    context_object_name = 'orders'
    queryset=Order.objects,filter(created_time=date.today())



import datetime
class AdminWeekOrdersListView(generic.ListView):
    template_name = 'appi/weekorders_html'
    date=datetime.date.today()
    start_week=date-datetime.timedelta(date.weekday())
    end_week=start_week+datetime.timedelta(7)
    queryset = Order.objects.filter(created_time__range=[start_week,end_week])




class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class=ProductModelForm
    success_url = reverse_lazy('product')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ProductCreate, self).form_valid(form)


class ProductUpdate(LoginRequiredMixin, UpdateView):
    queryset=Product.objects.all()
    model = Product
    fields = ['product_price']
    template_name='appi/product_form.html'

    def put(self,*args,**kwargs):
        json_body=json.loads(self.request.body)
        if Product.objects.filter(id=kwargs.get('pk'))
           active_product=Product.objects.get(id=kwargs.get('pk'))
            for field,value in json_body.items():
                setattr(active_product,field,value)
            active_product.save()
            message="Product price updated "
         else:
           message="This product does not exist"
        return HttpResponse(message)


class ProductDelete(generic.DeleteView):
  template_name="product_delete.html"
  queryset=Product.objects.all()
  model=Product
  succes_url=reverse_lazy('products')

  def delete(self,request,*args,**kwargs)
      print(args,kwargs)
      message="deleted successfully"
      return HttpResponse(message)
