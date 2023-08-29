from urllib.parse import urlencode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from DjangoBaseSetup.common_modules.mainService import MainService
from DjangoBaseSetup.messages.messages import ProjectAppMessages
from .models import Crane, Project
from django.contrib import messages
from .form import CraneForm, ProjectForm

CRANE_MODEL_NAME_SINGULAR = 'Crane'
CRANE_MODEL_NAME_PLURAL = 'Cranes'

PROJECT_MODEL_NAME_SINGULAR = 'Project'
PROJECT_MODEL_NAME_PLURAL = 'Projects'


@login_required(login_url='login')
def craneIndex(request):
    DB = Crane.objects.filter(is_delete=False)

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
        'model_name_singular': CRANE_MODEL_NAME_SINGULAR,
        'model_name_plural': CRANE_MODEL_NAME_PLURAL
    }
    return render(request, "crane/index.html", context)


@login_required(login_url='login')
def addCrane(request):
    if request.method == "POST":
        form = CraneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ProjectAppMessages.crane_has_been_updated_successfully.value)
            return redirect('crane.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = CraneForm()
    context = {
        "form": form,
        'model_name_singular': CRANE_MODEL_NAME_SINGULAR,
        'model_name_plural': CRANE_MODEL_NAME_PLURAL
    }
    return render(request, "crane/add.html", context)


@login_required(login_url='login')
def updateCrane(request, id):
    crane = Crane.objects.get(id=id)
    if not crane:
        return redirect('crane.index')
    if request.method == "POST":
        form = CraneForm(request.POST, request.FILES, instance=crane)
        if form.is_valid():
            form.save()
            messages.success(request, ProjectAppMessages.crane_has_been_updated_successfully.value)
            return redirect('crane.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "name": crane.name,
            "description": crane.description,
        }
        form = CraneForm(initial=data)
    context = {
        'form': form,
        'crane': crane,
        'model_name_singular': CRANE_MODEL_NAME_SINGULAR,
        'model_name_plural': CRANE_MODEL_NAME_PLURAL
    }
    return render(request, 'crane/edit.html', context)


@login_required(login_url='login')
def craneView(request, id):
    crane = Crane.objects.get(id=id)
    if not crane:
        return redirect('crane.index')
    context = {
        "crane": crane,
        'model_name_singular': CRANE_MODEL_NAME_SINGULAR,
        'model_name_plural': CRANE_MODEL_NAME_PLURAL
    }
    return render(request, "crane/view.html", context)


@login_required(login_url='login')
def craneStatus(request, id):
    crane = Crane.objects.get(id=id)
    if not crane:
        return redirect('crane.index')
    if crane.is_active:
        crane.is_active = False
        crane.save()
        messages.success(request, ProjectAppMessages.crane_has_been_deactivated_successfully.value)
    else:
        crane.is_active = True
        crane.save()
        messages.success(request, ProjectAppMessages.crane_has_been_activated_successfully.value)
    return redirect('crane.index')


@login_required(login_url='login')
def craneDelete(request, id):
    crane = Crane.objects.get(id=id)
    if not crane:
        return redirect('crane.index')
    crane.is_delete = True
    crane.save()
    messages.success(request, ProjectAppMessages.crane_has_been_deleted_successfully.value)
    return redirect('crane.index')


@login_required(login_url='login')
def projectIndex(request):
    DB = Project.objects.filter(is_delete=False)

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
        'model_name_singular': PROJECT_MODEL_NAME_SINGULAR,
        'model_name_plural': PROJECT_MODEL_NAME_PLURAL
    }
    return render(request, "project/index.html", context)


@login_required(login_url='login')
def addProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ProjectAppMessages.project_has_been_added_successfully.value)
            return redirect('project.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ProjectForm()
    context = {
        "form": form,
        'model_name_singular': PROJECT_MODEL_NAME_SINGULAR,
        'model_name_plural': PROJECT_MODEL_NAME_PLURAL
    }
    return render(request, "project/add.html", context)


@login_required(login_url='login')
def updateProject(request, id):
    project = Project.objects.get(id=id)
    if not project:
        return redirect('project.index')
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, ProjectAppMessages.project_has_been_updated_successfully.value)
            return redirect('project.index')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        data = {
            "crane": project.crane,
            "image": project.image,
            "title": project.title,
            "description": project.description,
            "address": project.address
        }
        form = ProjectForm(initial=data)
    context = {
        'form': form,
        'project': project,
        'model_name_singular': PROJECT_MODEL_NAME_SINGULAR,
        'model_name_plural': PROJECT_MODEL_NAME_PLURAL
    }
    return render(request, 'project/edit.html', context)


@login_required(login_url='login')
def projectView(request, id):
    project = Project.objects.get(id=id)
    if not project:
        return redirect('project.index')
    context = {
        "project": project,
        'model_name_singular': PROJECT_MODEL_NAME_SINGULAR,
        'model_name_plural': PROJECT_MODEL_NAME_PLURAL
    }
    return render(request, "project/view.html", context)


@login_required(login_url='login')
def projectStatus(request, id):
    project = Project.objects.get(id=id)
    if not project:
        return redirect('project.index')
    if project.is_active:
        project.is_active = False
        project.save()
        messages.success(request, ProjectAppMessages.project_has_been_deactivated_successfully.value)
    else:
        project.is_active = True
        project.save()
        messages.success(request, ProjectAppMessages.project_has_been_activated_successfully.value)
    return redirect('project.index')


@login_required(login_url='login')
def projectDelete(request, id):
    project = Crane.objects.get(id=id)
    if not project:
        return redirect('project.index')
    project.is_delete = True
    project.save()
    messages.success(request, ProjectAppMessages.project_has_been_deleted_successfully.value)
    return redirect('project.index')
