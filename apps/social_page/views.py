from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from DjangoBaseSetup.common_modules.mainService import MainService
from django.contrib import messages

from DjangoBaseSetup.messages.messages import SocialAppMessage
from apps.social_page.form import SocialPageForm, SocialLinkForm
from apps.social_page.models import SocialPage, SocialLink

SOCIAL_PAGE_MODEL_NAME_SINGULAR = 'Social Page'
SOCIAL_PAGE_MODEL_NAME_PLURAL = 'Social Pages'

SOCIAL_LINK_MODEL_NAME_SINGULAR = 'Social Link'
SOCIAL_LINK_MODEL_NAME_PLURAL = 'Social Links'


# Create your views here.
@login_required(login_url='login')
def indexSocialPage(request):
    DB = SocialPage.objects.filter(is_delete=False)

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
        'model_name_singular': SOCIAL_PAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_PAGE_MODEL_NAME_PLURAL
    }
    return render(request, "social-page/index.html", context)


@login_required(login_url='login')
def addSocialPage(request):
    if request.method == "POST":
        form = SocialPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, SocialAppMessage.social_page_has_been_added_successfully.value)
            return redirect('social_page.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = SocialPageForm()
    context = {
        "form": form,
        'model_name_singular': SOCIAL_PAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_PAGE_MODEL_NAME_PLURAL
    }
    return render(request, "social-page/add.html", context)


@login_required(login_url='login')
def updateSocialPage(request, id):
    obj = SocialPage.objects.get(id=id)
    if not obj:
        return redirect('social_page.index')
    if request.method == "POST":
        form = SocialPageForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, SocialAppMessage.social_page_has_been_updated_successfully.value)
            return redirect('social_page.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "name": obj.name,
            "icon": obj.icon
        }
        form = SocialPageForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': SOCIAL_PAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_PAGE_MODEL_NAME_PLURAL
    }
    return render(request, 'social-page/edit.html', context)


@login_required(login_url='login')
def viewSocialPage(request, id):
    obj = SocialPage.objects.get(id=id)
    if not obj:
        return redirect('social_page.index')
    context = {
        "data": obj,
        'model_name_singular': SOCIAL_PAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_PAGE_MODEL_NAME_PLURAL
    }
    return render(request, "social-page/view.html", context)


@login_required(login_url='login')
def statusSocialPage(request, id):
    obj = SocialPage.objects.get(id=id)
    if not obj:
        return redirect('social_page.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, SocialAppMessage.social_page_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, SocialAppMessage.social_page_has_been_activated_successfully.value)
    return redirect('social_page.index')


@login_required(login_url='login')
def deleteSocialPage(request, id):
    obj = SocialPage.objects.get(id=id)
    if not obj:
        return redirect('social_page.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, SocialAppMessage.social_page_has_been_deleted_successfully.value)
    return redirect('social_page.index')


@login_required(login_url='login')
def indexSocialLink(request):
    DB = SocialLink.objects.filter(is_delete=False)

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
        'model_name_singular': SOCIAL_LINK_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_LINK_MODEL_NAME_PLURAL
    }
    return render(request, "social-link/index.html", context)


@login_required(login_url='login')
def addSocialLink(request):
    if request.method == "POST":
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, SocialAppMessage.social_link_has_been_added_successfully.value)
            return redirect('social_link.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = SocialLinkForm()
    context = {
        "form": form,
        'model_name_singular': SOCIAL_PAGE_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_PAGE_MODEL_NAME_PLURAL
    }
    return render(request, "social-link/add.html", context)


@login_required(login_url='login')
def updateSocialLink(request, id):
    obj = SocialLink.objects.get(id=id)
    if not obj:
        return redirect('social_page.index')
    if request.method == "POST":
        form = SocialLinkForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, SocialAppMessage.social_link_has_been_updated_successfully.value)
            return redirect('social_link.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "social_page": obj.social_page,
            "link": obj.link
        }
        form = SocialLinkForm(initial=data)
    context = {
        'form': form,
        'data': obj,
        'model_name_singular': SOCIAL_LINK_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_LINK_MODEL_NAME_PLURAL
    }
    return render(request, 'social-link/edit.html', context)


@login_required(login_url='login')
def viewSocialLink(request, id):
    obj = SocialLink.objects.get(id=id)
    if not obj:
        return redirect('social_link.index')
    context = {
        "data": obj,
        'model_name_singular': SOCIAL_LINK_MODEL_NAME_SINGULAR,
        'model_name_plural': SOCIAL_LINK_MODEL_NAME_PLURAL
    }
    return render(request, "social-link/view.html", context)


@login_required(login_url='login')
def statusSocialLink(request, id):
    obj = SocialLink.objects.get(id=id)
    if not obj:
        return redirect('social_link.index')
    if obj.is_active:
        obj.is_active = False
        obj.save()
        messages.success(request, SocialAppMessage.social_link_has_been_deactivated_successfully.value)
    else:
        obj.is_active = True
        obj.save()
        messages.success(request, SocialAppMessage.social_link_has_been_activated_successfully.value)
    return redirect('social_link.index')


@login_required(login_url='login')
def deleteSocialLink(request, id):
    obj = SocialLink.objects.get(id=id)
    if not obj:
        return redirect('social_link.index')
    obj.is_delete = True
    obj.save()
    messages.success(request, SocialAppMessage.social_link_has_been_deleted_successfully.value)
    return redirect('social_link.index')
