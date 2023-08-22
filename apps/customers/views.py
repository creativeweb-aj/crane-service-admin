from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from DjangoBaseSetup.common_modules.mainService import MainService
from django.contrib import messages
from DjangoBaseSetup.messages.messages import CustomerAppMessage
from apps.customers.form import TestimonialForm
from apps.customers.models import Message, Testimonial

MESSAGE_MODEL_NAME_SINGULAR = 'Message'
MESSAGE_MODEL_NAME_PLURAL = 'Messages'

TESTIMONIAL_MODEL_NAME_SINGULAR = 'Testimonial'
TESTIMONIAL_MODEL_NAME_PLURAL = 'Testimonials'


# Create your views here.
@login_required(login_url='login')
def indexMessage(request):
    DB = Message.objects.filter(is_delete=False)

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
        'model_name_singular': MESSAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': MESSAGE_MODEL_NAME_PLURAL
    }
    return render(request, "message/index.html", context)


@login_required(login_url='login')
def viewMessage(request, id):
    obj = Message.objects.get(id=id)
    if not obj:
        return redirect('message.index')
    context = {
        "data": obj,
        'model_name_singular': MESSAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': MESSAGE_MODEL_NAME_PLURAL
    }
    return render(request, "message/view.html", context)


@login_required(login_url='login')
def deleteMessage(request, id):
    obj = Message.objects.get(id=id)
    if not obj:
        return redirect('message.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, CustomerAppMessage.message_has_been_deleted_successfully.value)
    return redirect('message.index')


@login_required(login_url='login')
def indexTestimonial(request):
    DB = Testimonial.objects.filter(is_delete=False)

    if request.GET.get('name'):
        name = request.GET.get('name').strip()
        DB = DB.filter(client_name__icontains=name)

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
        'model_name_singular': TESTIMONIAL_MODEL_NAME_SINGULAR,
        'model_name_plural': TESTIMONIAL_MODEL_NAME_PLURAL
    }
    return render(request, "testimonial/index.html", context)


@login_required(login_url='login')
def addTestimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, CustomerAppMessage.testimonial_has_been_added_successfully.value)
            return redirect('testimonial.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = TestimonialForm()
    context = {
        "form": form,
        'model_name_singular': TESTIMONIAL_MODEL_NAME_SINGULAR,
        'model_name_plural': TESTIMONIAL_MODEL_NAME_PLURAL
    }
    return render(request, "testimonial/add.html", context)


@login_required(login_url='login')
def updateTestimonial(request, id):
    obj = Testimonial.objects.get(id=id)
    if not obj:
        return redirect('testimonial.index')
    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, CustomerAppMessage.testimonial_has_been_updated_successfully.value)
            return redirect('testimonial.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "client_name": obj.client_name,
            "client_image": obj.client_image,
            "comment": obj.comment
        }
        form = TestimonialForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': TESTIMONIAL_MODEL_NAME_SINGULAR,
        'model_name_plural': TESTIMONIAL_MODEL_NAME_PLURAL
    }
    return render(request, 'testimonial/edit.html', context)


@login_required(login_url='login')
def viewTestimonial(request, id):
    obj = Testimonial.objects.get(id=id)
    if not obj:
        return redirect('testimonial.index')
    context = {
        "data": obj,
        'model_name_singular': TESTIMONIAL_MODEL_NAME_SINGULAR,
        'model_name_plural': TESTIMONIAL_MODEL_NAME_PLURAL
    }
    return render(request, "testimonial/view.html", context)


@login_required(login_url='login')
def statusTestimonial(request, id):
    obj = Testimonial.objects.get(id=id)
    if not obj:
        return redirect('testimonial.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, CustomerAppMessage.testimonial_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, CustomerAppMessage.testimonial_has_been_activated_successfully.value)
    return redirect('testimonial.index')


@login_required(login_url='login')
def deleteTestimonial(request, id):
    obj = Testimonial.objects.get(id=id)
    if not obj:
        return redirect('testimonial.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, CustomerAppMessage.testimonial_has_been_deleted_successfully.value)
    return redirect('testimonial.index')
