from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("add/", views.add_expense, name="add_expense"),
    path("delete/<int:pk>/", views.delete_expense, name="delete_expense"),
    path("export/csv/", views.export_to_csv, name="export_csv"),
    path("export/xlsx/", views.export_to_xlsx, name="export_xlsx"),
]
