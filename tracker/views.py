from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from .models import Transactions
from .forms import TransactionForm
import csv
import openpyxl


# Create your views here.
def expense_list(request):
    """
    This view handles displaying the list of transaction and filtering them.
    """
    transactions = Transactions.objects.all()

    # Filter the expenses if the parameter exists in the GET request
    # Filter by category
    category = request.GET.get("category")
    if category:
        transactions = transactions.filter(category__icontains=category)

    # Filter by description
    description = request.GET.get("description")
    if description:
        transactions = transactions.filter(description__icontains=description)

    # Filter by date range
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    if start_date and end_date:
        transactions = transactions.filter(date__range=[start_date, end_date])

    # Calculate the balance of the transactions
    # If there are no transactions, the balance is 0.
    balance = transactions.aggregate(Sum("amount"))["amount__sum"] or 0.00

    # Get a unique list of all categories for the filter dropdown
    categories = Transactions.objects.values_list("category", flat=True).distinct()

    context = {
        "transactions": transactions.order_by("-date"),  # Show newest first
        "balance": balance,
        "categories": categories,
    }
    return render(request, "tracker/expenses.html", context)


def add_expense(request):
    """
    Handles the form for adding a new transaction.
    """
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker:expense_list")
    else:
        form = TransactionForm()
    return render(request, "tracker/add_expense.html", {"form": form})


def delete_expense(request, pk):
    """
    Deletes a specific transaction identified by it's primary key (pk).
    """
    transaction = get_object_or_404(Transactions, pk=pk)
    if request.method == "Post":
        transaction.delete()
    return redirect("tracker:expense_list")


def export_to_csv(request):
    """
    Exports the current view of transactions to a CSV file.
    """
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="expenses.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(["Date", "Description", "Amount", "Category"])

    # Write data rows
    for transaction in Transactions.objects.all().values_list(
        "date", "description", "amount", "category"
    ):
        writer.writerow(transaction)

    return response


def export_to_xlsx(request):
    """
    Exports all transactions to an XLSX file.
    """
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="expenses.xlsx"'

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Expenses"

    # Write header row
    sheet.append(["Date", "Description", "Amount", "Category"])

    # Write data rows
    for transaction in Transactions.objects.all():
        # Format date to be timezone-unaware for Excel
        formatted_date = transaction.date.replace(tzinfo=None)
        sheet.append(
            [
                formatted_date,
                transaction.description,
                transaction.amount,
                transaction.category,
            ]
        )

    workbook.save(response)
    return response
