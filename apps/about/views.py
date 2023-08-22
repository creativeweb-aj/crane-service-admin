from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from DjangoBaseSetup.common_modules.mainService import MainService
from django.contrib import messages
from DjangoBaseSetup.messages.messages import AboutAppMessage
from apps.about.form import AboutForm, KeyPointForm, OurValueForm, PersonForm, WorkingDayForm
from apps.about.models import About, KeyPoint, OurValue, Person, WorkingDay

ABOUT_MODEL_NAME_SINGULAR = 'About'
ABOUT_MODEL_NAME_PLURAL = 'Abouts'

KEYPOINT_MODEL_NAME_SINGULAR = 'Key Point'
KEYPOINT_MODEL_NAME_PLURAL = 'Key Points'

OUR_VALUE_MODEL_NAME_SINGULAR = 'Our Value'
OUR_VALUE_MODEL_NAME_PLURAL = 'Our Values'

PERSON_MODEL_NAME_SINGULAR = 'Person'
PERSON_MODEL_NAME_PLURAL = 'Persons'

WORKING_DAY_MODEL_NAME_SINGULAR = 'Working Day'
WORKING_DAY_MODEL_NAME_PLURAL = 'Working Days'


# Create your views here.

# About View
@login_required(login_url='login')
def indexAbout(request):
    DB = About.objects.filter(is_delete=False)

    if request.GET.get('title'):
        name = request.GET.get('title').strip()
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
        'model_name_singular': ABOUT_MODEL_NAME_SINGULAR,
        'model_name_plural': ABOUT_MODEL_NAME_PLURAL
    }
    return render(request, "about/index.html", context)


@login_required(login_url='login')
def addAbout(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.about_has_been_added_successfully.value)
            return redirect('about.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = AboutForm()
    context = {
        "form": form,
        'model_name_singular': ABOUT_MODEL_NAME_SINGULAR,
        'model_name_plural': ABOUT_MODEL_NAME_PLURAL
    }
    return render(request, "about/add.html", context)


@login_required(login_url='login')
def updateAbout(request, id):
    obj = About.objects.get(id=id)
    if not obj:
        return redirect('about.index')
    if request.method == "POST":
        form = AboutForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.about_has_been_updated_successfully.value)
            return redirect('about.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "title": obj.title,
            "description": obj.description
        }
        form = AboutForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': ABOUT_MODEL_NAME_SINGULAR,
        'model_name_plural': ABOUT_MODEL_NAME_PLURAL
    }
    return render(request, 'about/edit.html', context)


@login_required(login_url='login')
def viewAbout(request, id):
    obj = About.objects.get(id=id)
    if not obj:
        return redirect('about.index')
    context = {
        "data": obj,
        'model_name_singular': ABOUT_MODEL_NAME_SINGULAR,
        'model_name_plural': ABOUT_MODEL_NAME_PLURAL
    }
    return render(request, "about/view.html", context)


@login_required(login_url='login')
def statusAbout(request, id):
    obj = About.objects.get(id=id)
    if not obj:
        return redirect('about.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, AboutAppMessage.about_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, AboutAppMessage.about_has_been_activated_successfully.value)
    return redirect('about.index')


@login_required(login_url='login')
def deleteAbout(request, id):
    obj = About.objects.get(id=id)
    if not obj:
        return redirect('about.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, AboutAppMessage.about_has_been_deleted_successfully.value)
    return redirect('about.index')


# Key Point View
@login_required(login_url='login')
def indexKeyPoint(request):
    DB = KeyPoint.objects.filter(is_delete=False)

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
        'model_name_singular': KEYPOINT_MODEL_NAME_SINGULAR,
        'model_name_plural': KEYPOINT_MODEL_NAME_PLURAL
    }
    return render(request, "key-point/index.html", context)


@login_required(login_url='login')
def addKeyPoint(request):
    if request.method == "POST":
        form = KeyPointForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.key_point_has_been_added_successfully.value)
            return redirect('keypoint.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = KeyPointForm()
    context = {
        "form": form,
        'model_name_singular': KEYPOINT_MODEL_NAME_SINGULAR,
        'model_name_plural': KEYPOINT_MODEL_NAME_PLURAL
    }
    return render(request, "key-point/add.html", context)


@login_required(login_url='login')
def updateKeyPoint(request, id):
    obj = KeyPoint.objects.get(id=id)
    if not obj:
        return redirect('keypoint.index')
    if request.method == "POST":
        form = KeyPointForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.key_point_has_been_updated_successfully.value)
            return redirect('keypoint.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "name": obj.name,
            "icon": obj.icon
        }
        form = KeyPointForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': KEYPOINT_MODEL_NAME_SINGULAR,
        'model_name_plural': KEYPOINT_MODEL_NAME_PLURAL
    }
    return render(request, 'key-point/edit.html', context)


@login_required(login_url='login')
def viewKeyPoint(request, id):
    obj = KeyPoint.objects.get(id=id)
    if not obj:
        return redirect('keypoint.index')
    context = {
        "data": obj,
        'model_name_singular': KEYPOINT_MODEL_NAME_SINGULAR,
        'model_name_plural': KEYPOINT_MODEL_NAME_PLURAL
    }
    return render(request, "key-point/view.html", context)


@login_required(login_url='login')
def statusKeyPoint(request, id):
    obj = KeyPoint.objects.get(id=id)
    if not obj:
        return redirect('keypoint.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, AboutAppMessage.key_point_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, AboutAppMessage.key_point_has_been_activated_successfully.value)
    return redirect('keypoint.index')


@login_required(login_url='login')
def deleteKeyPoint(request, id):
    obj = KeyPoint.objects.get(id=id)
    if not obj:
        return redirect('keypoint.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, AboutAppMessage.key_point_has_been_deleted_successfully.value)
    return redirect('keypoint.index')


# Our Value View
@login_required(login_url='login')
def indexOurValue(request):
    DB = OurValue.objects.filter(is_delete=False)

    if request.GET.get('title'):
        name = request.GET.get('title').strip()
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
        'model_name_singular': OUR_VALUE_MODEL_NAME_SINGULAR,
        'model_name_plural': OUR_VALUE_MODEL_NAME_PLURAL
    }
    return render(request, "our-value/index.html", context)


@login_required(login_url='login')
def addOurValue(request):
    if request.method == "POST":
        form = OurValueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.our_value_has_been_added_successfully.value)
            return redirect('our_value.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = OurValueForm()
    context = {
        "form": form,
        'model_name_singular': OUR_VALUE_MODEL_NAME_SINGULAR,
        'model_name_plural': OUR_VALUE_MODEL_NAME_PLURAL
    }
    return render(request, "our-value/add.html", context)


@login_required(login_url='login')
def updateOurValue(request, id):
    obj = OurValue.objects.get(id=id)
    if not obj:
        return redirect('our_value.index')
    if request.method == "POST":
        form = OurValueForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.our_value_has_been_updated_successfully.value)
            return redirect('keypoint.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "title": obj.title,
            "description": obj.description
        }
        form = OurValueForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': OUR_VALUE_MODEL_NAME_SINGULAR,
        'model_name_plural': OUR_VALUE_MODEL_NAME_PLURAL
    }
    return render(request, 'our-value/edit.html', context)


@login_required(login_url='login')
def viewOurValue(request, id):
    obj = OurValue.objects.get(id=id)
    if not obj:
        return redirect('our_value.index')
    context = {
        "data": obj,
        'model_name_singular': OUR_VALUE_MODEL_NAME_SINGULAR,
        'model_name_plural': OUR_VALUE_MODEL_NAME_PLURAL
    }
    return render(request, "our-value/view.html", context)


@login_required(login_url='login')
def statusOurValue(request, id):
    obj = OurValue.objects.get(id=id)
    if not obj:
        return redirect('our_value.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, AboutAppMessage.our_value_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, AboutAppMessage.our_value_has_been_activated_successfully.value)
    return redirect('our_value.index')


@login_required(login_url='login')
def deleteOurValue(request, id):
    obj = OurValue.objects.get(id=id)
    if not obj:
        return redirect('our_value.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, AboutAppMessage.our_value_has_been_deleted_successfully.value)
    return redirect('our_value.index')


# Person View
@login_required(login_url='login')
def indexPerson(request):
    DB = Person.objects.filter(is_delete=False)

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
        'model_name_singular': PERSON_MODEL_NAME_SINGULAR,
        'model_name_plural': PERSON_MODEL_NAME_PLURAL
    }
    return render(request, "person/index.html", context)


@login_required(login_url='login')
def addPerson(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.person_has_been_added_successfully.value)
            return redirect('person.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = PersonForm()
    context = {
        "form": form,
        'model_name_singular': PERSON_MODEL_NAME_SINGULAR,
        'model_name_plural': PERSON_MODEL_NAME_PLURAL
    }
    return render(request, "person/add.html", context)


@login_required(login_url='login')
def updatePerson(request, id):
    obj = Person.objects.get(id=id)
    if not obj:
        return redirect('person.index')
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.person_has_been_updated_successfully.value)
            return redirect('person.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "title": obj.title,
            "designation": obj.designation,
            "image": obj.image
        }
        form = PersonForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': PERSON_MODEL_NAME_SINGULAR,
        'model_name_plural': PERSON_MODEL_NAME_PLURAL
    }
    return render(request, 'person/edit.html', context)


@login_required(login_url='login')
def viewPerson(request, id):
    obj = Person.objects.get(id=id)
    if not obj:
        return redirect('person.index')
    context = {
        "data": obj,
        'model_name_singular': PERSON_MODEL_NAME_SINGULAR,
        'model_name_plural': PERSON_MODEL_NAME_PLURAL
    }
    return render(request, "person/view.html", context)


@login_required(login_url='login')
def statusPerson(request, id):
    obj = Person.objects.get(id=id)
    if not obj:
        return redirect('person.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, AboutAppMessage.person_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, AboutAppMessage.person_has_been_activated_successfully.value)
    return redirect('person.index')


@login_required(login_url='login')
def deletePerson(request, id):
    obj = Person.objects.get(id=id)
    if not obj:
        return redirect('person.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, AboutAppMessage.person_has_been_deleted_successfully.value)
    return redirect('person.index')


# Working day
@login_required(login_url='login')
def indexWorkingDay(request):
    DB = WorkingDay.objects.filter(is_delete=False)

    if request.GET.get('day'):
        name = request.GET.get('day').strip()
        DB = DB.filter(day__icontains=name)

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
        'model_name_singular': WORKING_DAY_MODEL_NAME_SINGULAR,
        'model_name_plural': WORKING_DAY_MODEL_NAME_PLURAL
    }
    return render(request, "working-day/index.html", context)


@login_required(login_url='login')
def addWorkingDay(request):
    if request.method == "POST":
        form = WorkingDayForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.working_day_has_been_added_successfully.value)
            return redirect('working_day.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = WorkingDayForm()
    context = {
        "form": form,
        'model_name_singular': WORKING_DAY_MODEL_NAME_SINGULAR,
        'model_name_plural': WORKING_DAY_MODEL_NAME_PLURAL
    }
    return render(request, "working-day/add.html", context)


@login_required(login_url='login')
def updateWorkingDay(request, id):
    obj = WorkingDay.objects.get(id=id)
    if not obj:
        return redirect('working_day.index')
    if request.method == "POST":
        form = WorkingDayForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, AboutAppMessage.working_day_has_been_updated_successfully.value)
            return redirect('working_day.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "day": obj.day,
            "start_time": obj.start_time,
            "end_time": obj.end_time
        }
        form = WorkingDayForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': WORKING_DAY_MODEL_NAME_SINGULAR,
        'model_name_plural': WORKING_DAY_MODEL_NAME_PLURAL
    }
    return render(request, 'working-day/edit.html', context)


@login_required(login_url='login')
def viewWorkingDay(request, id):
    obj = WorkingDay.objects.get(id=id)
    if not obj:
        return redirect('working_day.index')
    context = {
        "data": obj,
        'model_name_singular': WORKING_DAY_MODEL_NAME_SINGULAR,
        'model_name_plural': WORKING_DAY_MODEL_NAME_PLURAL
    }
    return render(request, "working-day/view.html", context)


@login_required(login_url='login')
def statusWorkingDay(request, id):
    obj = WorkingDay.objects.get(id=id)
    if not obj:
        return redirect('working_day.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, AboutAppMessage.working_day_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, AboutAppMessage.working_day_has_been_activated_successfully.value)
    return redirect('working_day.index')


@login_required(login_url='login')
def deleteWorkingDay(request, id):
    obj = WorkingDay.objects.get(id=id)
    if not obj:
        return redirect('working_day.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, AboutAppMessage.working_day_has_been_deleted_successfully.value)
    return redirect('working_day.index')
