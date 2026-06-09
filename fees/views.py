from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import StudentFee
from .forms import StudentFeeForm


# Home Page


def admin_dashboard(request):

    total_students = StudentFee.objects.count()

    paid_students = StudentFee.objects.filter(
        fee_status='Paid'
    ).count()

    unpaid_students = StudentFee.objects.filter(
        fee_status='Unpaid'
    ).count()

    context = {
        'total_students': total_students,
        'paid_students': paid_students,
        'unpaid_students': unpaid_students,
    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )

def home(request):

    total_students = StudentFee.objects.count()

    paid_students = StudentFee.objects.filter(
        fee_status='Paid'
    ).count()

    unpaid_students = StudentFee.objects.filter(
        fee_status='Unpaid'
    ).count()

    context = {
        'total_students': total_students,
        'paid_students': paid_students,
        'unpaid_students': unpaid_students
    }

    return render(
        request,
        'home.html',
        context
    )


# Add Student Fee Record
def add_fee(request):

    if request.method == "POST":
        form = StudentFeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view_fee')

    else:
        form = StudentFeeForm()

    return render(request, 'add_fee.html', {'form': form})


# View All Records
def view_fee(request):

    records = StudentFee.objects.all()

    return render(
        request,
        'view_fee.html',
        {'records': records}
    )


# Edit Record
def edit_fee(request, id):

    record = get_object_or_404(
        StudentFee,
        id=id
    )

    if request.method == "POST":

        form = StudentFeeForm(
            request.POST,
            instance=record
        )

        if form.is_valid():
            form.save()
            return redirect('view_fee')

    else:
        form = StudentFeeForm(instance=record)

    return render(
        request,
        'edit_fee.html',
        {'form': form}
    )


# Delete Record
def delete_fee(request, id):

    record = get_object_or_404(
        StudentFee,
        id=id
    )

    record.delete()

    return redirect('view_fee')


# Search Student
def search_fee(request):

    query = request.GET.get('q')

    if query:

        results = StudentFee.objects.filter(
            Q(name__icontains=query) |
            Q(roll_no__icontains=query)
        )

    else:
        results = []

    return render(
        request,
        'search.html',
        {'results': results}
    )