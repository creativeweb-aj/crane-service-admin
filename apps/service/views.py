from urllib.parse import urlencode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from DjangoBaseSetup.common_modules.mainService import MainService
from django.contrib import messages
from DjangoBaseSetup.messages.messages import ServiceAppMessage
from apps.service.form import ServiceForm
from apps.service.models import Service

SERVICE_MODEL_NAME_SINGULAR = 'Service'
SERVICE_MODEL_NAME_PLURAL = 'Services'


# Create your views here.

@login_required(login_url='login')
def index(request):
    DB = Service.objects.filter(is_delete=False)

    if request.GET.get('name'):
        name = request.GET.get('name').strip()
        DB = DB.filter(name__icontains=name)

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
        'model_name_singular': SERVICE_MODEL_NAME_SINGULAR,
        'model_name_plural': SERVICE_MODEL_NAME_PLURAL
    }
    return render(request, "service/index.html", context)


@login_required(login_url='login')
def add(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ServiceAppMessage.service_has_been_added_successfully.value)
            return redirect('service.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ServiceForm()
    context = {
        "form": form,
        'model_name_singular': SERVICE_MODEL_NAME_SINGULAR,
        'model_name_plural': SERVICE_MODEL_NAME_PLURAL
    }
    return render(request, "service/add.html", context)


@login_required(login_url='login')
def update(request, id):
    obj = Service.objects.get(id=id)
    if not obj:
        return redirect('service.index')
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ServiceAppMessage.service_has_been_updated_successfully.value)
            return redirect('service.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "name": obj.name,
            "description": obj.description,
            "image": obj.image,
            "icon": obj.icon
        }
        form = ServiceForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': SERVICE_MODEL_NAME_SINGULAR,
        'model_name_plural': SERVICE_MODEL_NAME_PLURAL
    }
    return render(request, 'service/edit.html', context)


@login_required(login_url='login')
def view(request, id):
    obj = Service.objects.get(id=id)
    if not obj:
        return redirect('service.index')
    context = {
        "data": obj,
        'model_name_singular': SERVICE_MODEL_NAME_SINGULAR,
        'model_name_plural': SERVICE_MODEL_NAME_PLURAL
    }
    return render(request, "service/view.html", context)


@login_required(login_url='login')
def status(request, id):
    obj = Service.objects.get(id=id)
    if not obj:
        return redirect('service.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, ServiceAppMessage.service_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, ServiceAppMessage.service_has_been_activated_successfully.value)
    return redirect('service.index')


@login_required(login_url='login')
def delete(request, id):
    obj = Service.objects.get(id=id)
    if not obj:
        return redirect('service.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, ServiceAppMessage.service_has_been_deleted_successfully.value)
    return redirect('service.index')
