from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages
from DjangoBaseSetup.common_modules.mainService import MainService
from apps.work_management.form import StaffForm, CustomerForm
from apps.work_management.models import Staff, Customer

STAFF_MODEL_NAME_SINGULAR = 'Staff'
STAFF_MODEL_NAME_PLURAL = 'Staffs'


# Create your views here.
@login_required(login_url='login')
def indexStaff(request):
    DB = Staff.objects.filter(is_delete=False)

    orderBy = request.GET.get('order_by', "created_at")
    direction = request.GET.get('direction', "DESC")
    if direction == "DESC":
        DB = DB.order_by("-" + orderBy).all()
    else:
        DB = DB.order_by(orderBy).all()

    # Create main service instance with request
    service = MainService(request)
    totalRecord = DB.count()
    # get page record data from service
    # Get page size value
    recordPerPage = service.getPageRecordSize()

    page = request.GET.get('page', 1)
    paginator = Paginator(DB, recordPerPage)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    pageStart = results.start_index()
    pageEnd = results.end_index()

    # Get page range
    pageRange = service.getPageRange(results, paginator)

    searchingVariables = request.GET
    queryString = searchingVariables.copy()
    if 'page' in queryString:
        queryString.pop("page")
    if 'direction' in queryString:
        queryString.pop("direction")
    if 'order_by' in queryString:
        queryString.pop("order_by")
    queryString = urlencode(queryString)

    context = {
        'results': results,
        'page_start': pageStart,
        'page_end': pageEnd,
        'total_record': totalRecord,
        'page_size': recordPerPage,
        'page': page,
        'page_range': pageRange,
        'order_by': orderBy,
        'direction': direction,
        'searching_variables': searchingVariables,
        'query_string': queryString,
        'model_name_singular': STAFF_MODEL_NAME_SINGULAR,
        'model_name_plural': STAFF_MODEL_NAME_PLURAL
    }
    return render(request, "staff/index.html", context)


@login_required(login_url='login')
def addStaff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff added successfully")
            return redirect('staff.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = StaffForm()
    context = {
        "form": form,
        'model_name_singular': STAFF_MODEL_NAME_SINGULAR,
        'model_name_plural': STAFF_MODEL_NAME_PLURAL
    }
    return render(request, "staff/add.html", context)


@login_required(login_url='login')
def updateStaff(request, id):
    obj = Staff.objects.get(id=id)
    if not obj:
        return redirect('staff.index')
    if request.method == "POST":
        form = StaffForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff updated successfully")
            return redirect('staff.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "user": obj.user,
            "staff_type": obj.staff_type,
            "salary": obj.salary
        }
        form = StaffForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': STAFF_MODEL_NAME_SINGULAR,
        'model_name_plural': STAFF_MODEL_NAME_PLURAL
    }
    return render(request, 'staff/edit.html', context)


@login_required(login_url='login')
def statusStaff(request, id):
    obj = Staff.objects.get(id=id)
    if not obj:
        return redirect('staff.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, "Staff deactivated successfully")
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, "Staff activated successfully")
    return redirect('staff.index')


@login_required(login_url='login')
def deleteStaff(request, id):
    obj = Staff.objects.get(id=id)
    if not obj:
        return redirect('staff.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, "Staff deleted successfully")
    return redirect('staff.index')


CUSTOMER_MODEL_NAME_SINGULAR = 'Customer'
CUSTOMER_MODEL_NAME_PLURAL = 'Customer'


@login_required(login_url='login')
def indexCustomer(request):
    DB = Customer.objects.filter(is_delete=False)

    orderBy = request.GET.get('order_by', "created_at")
    direction = request.GET.get('direction', "DESC")
    if direction == "DESC":
        DB = DB.order_by("-" + orderBy).all()
    else:
        DB = DB.order_by(orderBy).all()

    # Create main service instance with request
    service = MainService(request)
    totalRecord = DB.count()
    # get page record data from service
    # Get page size value
    recordPerPage = service.getPageRecordSize()

    page = request.GET.get('page', 1)
    paginator = Paginator(DB, recordPerPage)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    pageStart = results.start_index()
    pageEnd = results.end_index()

    # Get page range
    pageRange = service.getPageRange(results, paginator)

    searchingVariables = request.GET
    queryString = searchingVariables.copy()
    if 'page' in queryString:
        queryString.pop("page")
    if 'direction' in queryString:
        queryString.pop("direction")
    if 'order_by' in queryString:
        queryString.pop("order_by")
    queryString = urlencode(queryString)

    context = {
        'results': results,
        'page_start': pageStart,
        'page_end': pageEnd,
        'total_record': totalRecord,
        'page_size': recordPerPage,
        'page': page,
        'page_range': pageRange,
        'order_by': orderBy,
        'direction': direction,
        'searching_variables': searchingVariables,
        'query_string': queryString,
        'model_name_singular': CUSTOMER_MODEL_NAME_SINGULAR,
        'model_name_plural': CUSTOMER_MODEL_NAME_PLURAL
    }
    return render(request, "customer/index.html", context)


@login_required(login_url='login')
def addCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully")
            return redirect('customer.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = CustomerForm()
    context = {
        "form": form,
        'model_name_singular': CUSTOMER_MODEL_NAME_SINGULAR,
        'model_name_plural': CUSTOMER_MODEL_NAME_PLURAL
    }
    return render(request, "customer/add.html", context)


@login_required(login_url='login')
def updateCustomer(request, id):
    obj = Customer.objects.get(id=id)
    if not obj:
        return redirect('customer.index')
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully")
            return redirect('customer.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "customer_name": obj.customer_name,
            "customer_email": obj.customer_email,
            "customer_mobile": obj.customer_mobile,
            "customer_address": obj.customer_address
        }
        form = CustomerForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': STAFF_MODEL_NAME_SINGULAR,
        'model_name_plural': STAFF_MODEL_NAME_PLURAL
    }
    return render(request, 'customer/edit.html', context)


@login_required(login_url='login')
def statusCustomer(request, id):
    obj = Customer.objects.get(id=id)
    if not obj:
        return redirect('customer.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, "Customer deactivated successfully")
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, "Customer activated successfully")
    return redirect('customer.index')


@login_required(login_url='login')
def deleteCustomer(request, id):
    obj = Customer.objects.get(id=id)
    if not obj:
        return redirect('customer.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, "Customer deleted successfully")
    return redirect('customer.index')
