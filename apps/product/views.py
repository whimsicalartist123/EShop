from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductCreateUpdateForm

from apps.core.decorators import user_is_seller
from apps.cart.forms import CartAddProductForm


# Product READ
def product_list(request):
    """
        Return list of products, optionally based on category
    """

    category_slug = str(request.GET.get('category'))
    category = None
    products = Product.objects.filter(active=True)
    if request.user.is_authenticated and not request.user.is_customer:
        products = products.filter(seller=request.user)
    if category_slug != 'None':
        products = products.filter(category__slug=category_slug)
    return render(
        request,
        'product/list.html',
        {
            'category': category,
            'products': products
        }
    )

def product_detail(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
    except Product.DoesNotExist:
        raise ValueError("No such Product")
    form = CartAddProductForm()
    return render(
        request,
        "product/details.html",
        {
            "product": product,
            "cart_add_form": form
        }
    )

class ProductDetailView(DetailView):
    model = Product
    template_name = "product/details.html"
    queryset = Product.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cart_add_form"] = CartAddProductForm()
        return ctx


# Product CREATE
@login_required
@user_is_seller
def product_create(request):
    form = ProductCreateUpdateForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.seller = request.user
        product.save()
    return render(
        request,
        "create.html",
        {
            "form": form
        }
    )


# Product UPDATE
@login_required
@user_is_seller
def product_update(request, product_id):
    pass


# Product DELETE
@login_required
@user_is_seller
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.delete()
    return HttpResponse({"message": "Product has been deleted"})




class ProductCreateUpdateDeleteView( CreateView, UpdateView, DeleteView): 
    pass