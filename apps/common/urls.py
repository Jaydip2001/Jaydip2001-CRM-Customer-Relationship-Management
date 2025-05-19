from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    client_list, client_create, client_edit, client_delete,
    lead_list, lead_create, lead_edit, lead_delete,
    invoice_list, invoice_create, invoice_edit, invoice_delete,
    task_create, task_list, task_edit, task_delete,
    product_create, product_list, product_edit, product_delete,
)

urlpatterns = [
    # Client URLs
    path("clients/", client_list, name="client_list"),
    path("clients/add/", client_create, name="client_create"),
    path("clients/edit/<int:pk>/", client_edit, name="client_edit"),
    path("clients/delete/<int:pk>/", client_delete, name="client_delete"),

    # Lead URLs
    path("leads/", lead_list, name="lead_list"),
    path("leads/add/", lead_create, name="lead_create"),
    path("leads/edit/<int:pk>/", lead_edit, name="lead_edit"),
    path("leads/delete/<int:pk>/", lead_delete, name="lead_delete"),

    # Invoice URLs
    path("invoices/", invoice_list, name="invoice_list"),
    path("invoices/add/", invoice_create, name="invoice_create"),
    path("invoices/edit/<int:pk>/", invoice_edit, name="invoice_edit"),
    path("invoices/delete/<int:pk>/", invoice_delete, name="invoice_delete"),

        # Task URLs
    path("tasks/", task_list, name="task_list"),
    path("tasks/add/", task_create, name="task_create"),
    path("tasks/edit/<int:pk>/", task_edit, name="task_edit"),
    path("tasks/delete/<int:pk>/", task_delete, name="task_delete"),

    # Product URLs
    path('products/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/edit/<int:pk>/', product_edit, name='product_edit'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Download buttons

from django.urls import path
from .views import (
    export_clients_excel, export_leads_excel, export_invoices_pdf
)

urlpatterns += [
    path("clients/download/", export_clients_excel, name="export_clients"),
    path("leads/download/", export_leads_excel, name="export_leads"),
    path("invoices/download/", export_invoices_pdf, name="export_invoices"),
]
