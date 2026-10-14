from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .forms import ContactForm
from .models import Product


class HomeView(TemplateView):
    """Home page: carousel of featured products + latest arrivals."""

    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_products"] = Product.objects.filter(is_featured=True)[:5]
        context["latest_products"] = Product.objects.all()[:4]
        return context


class ProductListView(ListView):
    """Product list page: cards, search and pagination, all read from the DB."""

    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        return context


class AboutView(TemplateView):
    template_name = "store/about.html"


class ContactView(FormView):
    template_name = "store/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks for writing to us. We will reply soon.")
        return super().form_valid(form)