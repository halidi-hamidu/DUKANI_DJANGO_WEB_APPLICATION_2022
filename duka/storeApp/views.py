from calendar import month
from http.client import HTTPResponse
from imp import reload
from importlib.abc import ResourceLoader
from itertools import count
from multiprocessing import context
import re
from select import select
from time import strftime
from turtle import update
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from . models import *
from .forms import *
from django.contrib import messages
import datetime
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template, render_to_string
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.conf.global_settings import LOGIN_URL
from django.utils import timezone
from io import BytesIO
from msilib.schema import File
from re import template
from unittest import result
from django.template.loader import get_template
# from xhtml2pdf import pisa


# from django.views.generic import View
# from .process import html_to_pdf
def html_to_pdf(template_src, context_dict = {}):
  template = get_template(template_src)
  html = template.render(context_dict)
  result = BytesIO()
  pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
  if not pdf.err:
    return HttpResponse(result.getvalue(), content_type = 'application/pdf')
  return None

def myView(request):

  get_products =  ProductTable.objects.all()
  open('templates/temp.html', "w").write(render_to_string('result.html',{'get_products':get_products} ))

  # converting html inot pdf  File
  pdf = html_to_pdf('temp.html')

  # render the template
  return HttpResponse(pdf, content_type = 'application/pdf')
#  Create your views here.
# storePage
def testPage(request):
  ResourceLoader.create_module()
def loginPage(request):
  if request.method == "POST":
    # login(request, request.user)
    get_username =request.POST.get("username") 
    get_password = request.POST.get('password')
    user = authenticate(username = get_username, password=get_password)
    if user is not None:
      get_user = User.objects.get(id =user.id)
      # print(get_user)
      # get_user_id = get_user.id
      try:
         get_user_authorization = AuthorizeUsers.objects.get(select_user = get_user)
      except:
        messages.info(request, f"{user.username} account not authorized yet!")
        return redirect("storeApp:loginPage")

      if get_user_authorization.view_dashboard:
        login(request, user)
        return redirect ("storeApp:homepage")
      elif get_user_authorization.manage_sales:
        login(request, user)
        return redirect ("storeApp:salesPage")
      else:
        messages.info(request, f"{user.username} account deactivated!")
        return redirect("storeApp:loginPage")


    else:
      messages.info(request, "Incorrect username or password")
      return redirect ("storeApp:loginPage")
  else:
    template_name = 'store/loginPage.html'
    context = {}
    return render(request, template_name, context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_URL)
def logoutPage(request):
  logout(request)
  return redirect("storeApp:loginPage")


@login_required(login_url=LOGIN_URL)
def homepage(request):
  try:
    get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
    x = datetime.datetime.now()
    today_date = datetime.datetime.today().date()
    get_all_today_orders = CustomersOrders.objects.filter(updated_at=today_date )
    print('= homepage=======')
    number_of_order_received_tody=get_all_today_orders.count()
    # today sales start here
    get_all_product_sold_today = productSoldInCash.objects.filter(date_product_sold = today_date)
    # print(get_all_product_sold_today.total_product_cost)
    today_sales_sum = 0
    today_emergence_cost_sum = 0
    # get_emergence_info
    get_emergence_info = EmergenceInformations.objects.filter(spending_date = today_date)
    if get_all_product_sold_today.count():
      number_of_poduct_sold = get_all_product_sold_today.count()
      print(number_of_poduct_sold)
      # print(get_all_product_sold_today.total_product_cost)
      
      
      for product in get_all_product_sold_today:
        print(product.total_product_cost)
        today_sales_sum +=product.total_product_cost
        print(today_sales_sum)
    
    # current_monthly_sales
    curent_month = timezone.now().month
    curent_year = timezone.now().year
    x = datetime.datetime.now()
    current_month = (x.strftime("%B"))
    print(current_month)
    get_all_product_sold_this_month_this_year = productSoldInCash.objects.filter(updated_at__month=curent_month, updated_at__year = curent_year)
    current_month_current_year_sales_sum = 0
    for sales in get_all_product_sold_this_month_this_year:
      current_month_current_year_sales_sum += sales.total_product_cost
    
    # 'January',
    get_all_product_sold_january_this_year = productSoldInCash.objects.filter(updated_at__month=1, updated_at__year = curent_year)
    january_sales_sum = 0
    for sales in get_all_product_sold_january_this_year:
      january_sales_sum += sales.total_product_cost
    # 'February',
    get_all_product_sold_february_this_year = productSoldInCash.objects.filter(updated_at__month=2, updated_at__year = curent_year)
    february_sales_sum = 0
    for sales in get_all_product_sold_february_this_year:
      february_sales_sum += sales.total_product_cost
    # 'March',
    get_all_product_sold_march_this_year = productSoldInCash.objects.filter(updated_at__month=3, updated_at__year = curent_year)
    march_sales_sum = 0
    for sales in get_all_product_sold_march_this_year:
      march_sales_sum += sales.total_product_cost
    # 'April',
    get_all_product_sold_april_this_year = productSoldInCash.objects.filter(updated_at__month=4, updated_at__year = curent_year)
    april_sales_sum = 0
    for sales in get_all_product_sold_april_this_year:
      april_sales_sum += sales.total_product_cost
    # 'May',
    get_all_product_sold_may_this_year = productSoldInCash.objects.filter(updated_at__month=5, updated_at__year = curent_year)
    may_sales_sum = 0
    for sales in get_all_product_sold_may_this_year:
      may_sales_sum += sales.total_product_cost
    # 'June',
    get_all_product_sold_june_this_year = productSoldInCash.objects.filter(updated_at__month=6, updated_at__year = curent_year)
    june_sales_sum = 0
    for sales in get_all_product_sold_june_this_year:
      june_sales_sum += sales.total_product_cost
    # 'July',
    get_all_product_sold_july_this_year = productSoldInCash.objects.filter(updated_at__month=7, updated_at__year = curent_year)
    july_sales_sum = 0
    for sales in get_all_product_sold_july_this_year:
      july_sales_sum += sales.total_product_cost
    # 'August',
    get_all_product_sold_august_this_year = productSoldInCash.objects.filter(updated_at__month=8, updated_at__year = curent_year)
    august_sales_sum = 0
    for sales in get_all_product_sold_august_this_year:
      august_sales_sum += sales.total_product_cost
    # 'September',
    get_all_product_sold_september_this_year = productSoldInCash.objects.filter(updated_at__month=9, updated_at__year = curent_year)
    september_sales_sum = 0
    for sales in get_all_product_sold_september_this_year:
      september_sales_sum += sales.total_product_cost
    # 'October',
    get_all_product_sold_october_this_year = productSoldInCash.objects.filter(updated_at__month=10, updated_at__year = curent_year)
    october_sales_sum = 0
    for sales in get_all_product_sold_october_this_year:
      october_sales_sum += sales.total_product_cost
    # 'November',
    get_all_product_sold_november_this_year = productSoldInCash.objects.filter(updated_at__month=11, updated_at__year = curent_year)
    november_sales_sum = 0
    for sales in get_all_product_sold_november_this_year:
      november_sales_sum += sales.total_product_cost
    # 'December'
    get_all_product_sold_december_this_year = productSoldInCash.objects.filter(updated_at__month=12, updated_at__year = curent_year)
    december_sales_sum = 0
    for sales in get_all_product_sold_december_this_year:
      december_sales_sum += sales.total_product_cost

    # curent_year_sales
    get_all_product_sold_this_year = productSoldInCash.objects.filter(updated_at__year = curent_year)
    current_year_sales_sum = 0
    current_year = (x.strftime("%Y"))

    for sales in get_all_product_sold_this_year:
      current_year_sales_sum += sales.total_product_cost
    
    today_emergence_cost_sum = 0
    # get_emergence_info
    get_emergence_info = EmergenceInformations.objects.filter(spending_date = today_date)
    for emergence in get_emergence_info:
      today_emergence_cost_sum +=emergence.spending_cost

    today = x.strftime("%x")
    all_product = []
    get_all_products = ProductAndSupplierAndReceiverTable.objects.all()
    for products in get_all_products:
      all_product.append(products)
    print("=========", today_date.day)
    x = datetime.datetime.now()
    january = datetime.datetime(int(x.strftime('%Y')), int(1), int(x.strftime('%d')))
    print(january)
    current_month = (x.strftime("%B"))
    print(current_month)
    print(all_product)
    template_name = 'store/homePage.html'
    context = {
      'get_all_user_authorizations':get_all_user_authorizations,
      'today_sales_sum':today_sales_sum,
      'current_month_current_year_sales_sum':current_month_current_year_sales_sum,
      'current_year_sales_sum':current_year_sales_sum,
      'current_month':current_month,
      'current_year':current_year,
      'today':today,
      'today_emergence_cost_sum':today_emergence_cost_sum,
      'get_all_products':get_all_products,
      'all_product':all_product,
      'january_sales_sum':january_sales_sum,
      'february_sales_sum':february_sales_sum,
      'march_sales_sum':march_sales_sum,
      'april_sales_sum': april_sales_sum,
      'may_sales_sum' :may_sales_sum, 
      'june_sales_sum' :june_sales_sum, 
      'july_sales_sum' :july_sales_sum, 
      'august_sales_sum' :august_sales_sum, 
      'september_sales_sum': september_sales_sum, 
      'october_sales_sum': october_sales_sum, 
      'november_sales_sum' :november_sales_sum, 
      'december_sales_sum': december_sales_sum

      }
    return render(request, template_name, context)
  
  except:
    messages.info(request, "user not authorized")
    return redirect ("storeApp:loginPage")
  

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_URL)
def storePage(request):
  # product
  if request.method =="POST" and request.POST.get('product'):
    form = ProductTableForm(request.POST)
    if form.is_valid():
      form.save()
      product_name = request.POST.get('product_name')
      messages.success(request, f"{product_name} added successFull")
      return redirect("storeApp:storePage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:storePage")
  
  # supplier
  elif request.method =="POST" and request.POST.get('supplier'):
    form = ProductAndSupplierTableForm(request.POST)
    if form.is_valid():
      form.save()
      supplier_name = request.POST.get('supplier')
      messages.success(request, f"{supplier_name} added successFull")
      return redirect("storeApp:storePage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:storePage")
  
  # receiver
  elif request.method =="POST" and request.POST.get('receiver'):
    form = ProductAndSupplierAndReceiverTableForm(request.POST)
    print(request.POST.get('product_receiver'))
    if form.is_valid():
      product_instance = form.save(commit = False)
      product_instance.total_product_cost = int(request.POST.get('product_cost')) * int(request.POST.get('product_quantity'))
      product_instance.save()
      product_name = request.POST.get('product_name')
      get_product_name = ProductTable.objects.get(id = product_name)
      messages.success(request, f"{get_product_name} added successFull by {request.user.username}")
      return redirect("storeApp:storePage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:storePage")
  # update_store_product_record
  elif request.method =="POST" and request.POST.get('update_store_product_record'):
    get_store_id = request.POST.get('store_id')
    get_product_name = request.POST.get('product_name')
    get_product_cost = request.POST.get('product_cost')
    get_product_quantity = request.POST.get('product_quantity')
    get_total_product_cost = int(get_product_cost) * int(get_product_quantity)
    get_amount_to_sold = request.POST.get('amount_to_sold')
    get_supplier_full_name = request.POST.get('supplier_full_name')
    get_shop_info = request.POST.get('shop_info')
    get_product_receiver = request.POST.get('product_receiver')
    get_product_in_store_to_update = ProductAndSupplierAndReceiverTable.objects.filter(id = get_store_id).update(
      product_name =get_product_name ,
      product_cost =get_product_cost ,
      product_quantity = get_product_quantity,
      total_product_cost = get_total_product_cost,
      amount_to_sold= get_amount_to_sold, 
      supplier_full_name=get_supplier_full_name , 
      shop_info = get_shop_info,
      product_receiver =get_product_receiver ,
    )
    # get_product_name = ProductTable.objects.get(id = product_name)
    messages.success(request, f"{get_product_name} updated successFull by {request.user.username}")
    return redirect("storeApp:storePage")

  # add_employee
  elif request.method == "POST" and request.POST.get('add_employee'):
    print(request.POST.get('employee_Full_name'))
    form = EmployeeDetailInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      employee_Full_name = request.POST.get('employee_Full_name')
      messages.success(request, f"{employee_Full_name} added successFull by {request.user.username}")
      return redirect("storeApp:storePage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:storePage")
  
  # add_shop
  elif request.method == "POST" and request.POST.get('add_shop'):
    print(request.POST.get('employee_Full_name'))
    form = ShopsTableForm(request.POST)
    if form.is_valid():
      form.save()
      shop_name = request.POST.get('shop_name')
      messages.susccess(request, f"{shop_name} added successFull by {request.user.username}")
      return redirect("storeApp:storePage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:storePage")

  # add_product_Quantity_in_store
  elif request.method == "POST" and request.POST.get("add_product_Quantity_in_store"):
    get_product_name = request.POST.get('product_name')
    get_how_much_each = request.POST.get('how_much_each')
    get_quantity_received = request.POST.get('quantity_received')
    get_price_to_sell_each = request.POST.get('price_to_sell_each')
    try:
      get_product_in_store = ProductAndSupplierAndReceiverTable.objects.get(id = get_product_name)
      old_each_product_cost = get_product_in_store.product_cost
      old_product_quantity_in_sore = get_product_in_store.product_quantity
      old_total_product_cost_used = get_product_in_store.total_product_cost
      old_amount_to_sold = get_product_in_store.amount_to_sold

      new_each_product_cost = get_how_much_each
      new_product_quantity_in_sore = int(old_product_quantity_in_sore) + int(get_quantity_received)
      # total product cost used to add
      new_total_product_cost_used  = int(new_each_product_cost) * int(get_quantity_received)
      new_total_product_cost_to_add = new_total_product_cost_used + old_total_product_cost_used
      new_amount_to_sold = int(get_price_to_sell_each)
      get_product_in_store = ProductAndSupplierAndReceiverTable.objects.filter(id = get_product_name).update(product_cost = new_each_product_cost, product_quantity = new_product_quantity_in_sore, total_product_cost =new_total_product_cost_to_add, amount_to_sold = new_amount_to_sold )
      messages.success(request, f"{get_product_name} new quantity added to the store by {request.user}")
      return redirect("storeApp:storePage")
      
    except:
      messages.info(request, f"{get_product_name} is not available in a store")
      return redirect("storeApp:storePage")

  else:
    try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
    except:
      messages.info(request, f"{request.user} does not have any credential yet!")
      return redirect("storeApp:storePage")
    get_all_users = User.objects.all().order_by('-id')
    get_all_products = ProductTable.objects.all().order_by('-id')
    get_all_suppliers = ProductAndSupplierTable.objects.all().order_by('-updated_at')
    get_all_shops = ShopsTable.objects.all().order_by('-updated_at')
    get_all_products_received = ProductAndSupplierAndReceiverTable.objects.all().order_by('-updated_at')
    get_last_products_number = ProductAndSupplierAndReceiverTable.objects.all().count()
    get_last_products_received = ProductAndSupplierAndReceiverTable.objects.last()
    get_all_employee = EmployeeDetailInformations.objects.all().order_by('-updated_at')
    get_all_product_in_store = ProductAndSupplierAndReceiverTable.objects.all().order_by('updated_at')
    form = EmployeeDetailInformationsForm()
    template_name= "store/storePage.html"
    context = {
      'get_all_employee':get_all_employee,
      'get_last_products_received':get_last_products_received,
      'form':form,
      'get_all_products':get_all_products,
      'get_all_suppliers':get_all_suppliers,
      'get_all_shops':get_all_shops,
      'get_all_products_received':get_all_products_received,
      'get_all_user_authorizations':get_all_user_authorizations,
      'get_all_product_in_store':get_all_product_in_store,
    }
    return render(request, template_name, context)
  

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_URL)
# shopPage
def shopPage(request):

  if request.method == "POST" and request.POST.get('add_shop'):
    print(request.POST.get('employee_Full_name'))
    form = ShopsTableForm(request.POST)
    if form.is_valid():
      form.save()
      shop_name = request.POST.get('shop_name')
      messages.success(request, f"{shop_name} added successFull by {request.user.username}")
      return redirect("storeApp:shopPage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:shopPage")
  elif request.method == "POST" and request.POST.get('update_shop'):
    get_shop_id = request.POST.get('shop_id')
    print("==========++++++++++", get_shop_id)
    # get_shop = get_object_or_404(ShopsTable, id = get_shop_id)
    # get_shop_id = 
    get_shop_name = request.POST.get('shop_name')
    get_shop_street = request.POST.get('shop_street')
    get_shop_district = request.POST.get('shop_district')
    get_shop_region = request.POST.get('shop_region')
    get_shop_supervisor = request.POST.get('shop_supervisor')
    # update_shop_information
    ShopsTable.objects.filter(id = get_shop_id).update(
      shop_name = get_shop_name,
      shop_street = get_shop_street,
      shop_district = get_shop_district,
      shop_region = get_shop_region,
      shop_supervisor = get_shop_supervisor
    )
    messages.success(request, f"{get_shop_name} updated successFull by {request.user.username}")
    return redirect("storeApp:shopPage")
  else:
    try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
    except:
      messages.info(request, f"{request.user} does not have any credential yet!")
      return redirect("storeApp:shopPage")
    
    get_all_employee = EmployeeDetailInformations.objects.all().order_by('-updated_at')
    get_all_shops = ShopsTable.objects.all().order_by('-updated_at')
    get_number_of_shops = ShopsTable.objects.all().count()
    try:
      get_last_opened_shops = ShopsTable.objects.first()
    except Exception as e:
      get_last_opened_shops = 0
      
    template_name = 'store/shopPage.html'
    context = {
      'get_all_employee':get_all_employee,
      'get_all_shops':get_all_shops,
      'get_number_of_shops':get_number_of_shops,
      'get_last_opened_shops':get_last_opened_shops,
      'get_all_user_authorizations':get_all_user_authorizations,
    }
    return render(request, template_name, context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_URL)
# suppliersPage
def suppliersPage(request):
  get_supplier_id = request.POST.get('supplier_id')
  get_supplier_full_name = request.POST.get('supplier_full_name')
  get_supplier_phone_number = request.POST.get('supplier_phone_number')
  get_gender = request.POST.get('gender')
  get_product_name = request.POST.get('product_name')
  if request.method == "POST" and request.POST.get('add_supplier'):
    form = ProductAndSupplierTableForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"{get_supplier_full_name} added successful by {request.user.username}")
      return redirect("storeApp:suppliersPage")
    else:
      messages.error(request, f"{get_supplier_full_name} not added yet! Try again latter")
      return redirect("storeApp:suppliersPage")

  elif request.method == "POST" and request.POST.get('update_supplier'):
    try:
      update_suppier_info = ProductAndSupplierTable.objects.filter(id = get_supplier_id).update(
      supplier_full_name =get_supplier_full_name ,
      supplier_phone_number = get_supplier_phone_number,
      gender =get_gender ,
      product_name =get_product_name ,
    
      )
      messages.success(request, f"{get_supplier_full_name} updated successful by {request.user.username}")
      return redirect("storeApp:suppliersPage")
    except:
      messages.success(request, f"{get_supplier_full_name} not updated Yet! Try again")
      return redirect("storeApp:suppliersPage")

  try:
    get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
    return redirect("storeApp:suppliersPage")
  get_all_suppliers = ProductAndSupplierTable.objects.all().order_by('-updated_at')
  get_all_products = ProductTable.objects.all().order_by('updated_at')
  template_name= "store/suppliersPage.html"
  context = {
    "get_all_user_authorizations":get_all_user_authorizations,
    "get_all_suppliers":get_all_suppliers,
    "get_all_products":get_all_products,
  }
  return render(request, template_name, context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_URL)
# employeePage
def employeePage(request):
  if request.method == "POST" and request.POST.get('add_employee'):
    print(request.POST.get('employee_Full_name'))
    form = EmployeeDetailInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      employee_Full_name = request.POST.get('employee_Full_name')
      messages.success(request, f"{employee_Full_name} added successFull by {request.user.username}")
      return redirect("storeApp:employeePage")
    else:
      messages.info(request, "please try again.")
      return redirect("storeApp:employeePage")
# update_employee
  elif request.method =="POST" and request.POST.get('update_employee'):
    # ==============update employee infomation============
    get_employeeId =request.POST.get('employeeId')
    print('===========', get_employeeId)
    get_employee_Full_name = request.POST.get('employee_Full_name')
    get_employee_info = get_object_or_404(EmployeeDetailInformations, id = get_employeeId )
    get_employee_gender = request.POST.get('employee_gender')
    get_employee_email_address = request.POST.get('employee_email_address')
    get_employee_start_date = request.POST.get('employee_start_date')
    get_employee_phone_number1 = request.POST.get('employee_phone_number1')
    get_employee_phone_number2 = request.POST.get('employee_phone_number2')
    get_employee_residence_area = request.POST.get('employee_residence_area')
    get_username = request.POST.get('username')
    get_password1 = request.POST.get('password1')
    get_password2 = request.POST.get('password2')
    print(request.POST)
    # get_password2 = request.POST.get('password2')
    csrf_token = request.POST.get('csrfmiddlewaretoken')
    # form = EmployeeDetailInformationsForm(
    #   { 
    #     'csrfmiddlewaretoken':[csrf_token],
    #     'employee_Full_name':[get_employee_Full_name],
    #     'employee_gender' : [get_employee_gender],
    #     'employee_email_address': [get_employee_email_address],
    #     'employee_start_date': [get_employee_start_date],
    #     'employee_phone_number1': [get_employee_phone_number1],
    #     'employee_phone_number2': [get_employee_phone_number2],
    #     'employee_residence_area': [get_employee_residence_area],
    #     'employee_username': [get_username],
    #     'employee_password': [get_password1],
        
    #   }
    #   ,instance=get_employee_info
    #   )
    if get_username:
      if get_password1 == get_password2:
        data_to_save = EmployeeDetailInformations.objects.filter(id = get_employeeId).update(
          employee_Full_name = get_employee_Full_name,
          employee_gender =  get_employee_gender,
          employee_email_address = get_employee_email_address,
          employee_start_date =  get_employee_start_date,
          employee_phone_number1 = get_employee_phone_number1,
          employee_phone_number2 =  get_employee_phone_number2,
          employee_residence_area = get_employee_residence_area,
          employee_username =  get_username,
          employee_password =  get_password1,
        )
        data_to_save = User.objects.filter(username = get_username).update(
          first_name =  get_employee_Full_name,
          username =  get_username,
          password =  get_password1,
          # confirm_password =  get_password2,
        )
        messages.success(request, f"{get_employee_Full_name} updated successFull by {request.user.username}")
        return redirect("storeApp:employeePage")
      else:
        messages.info(request, f"{get_employee_Full_name} Password missmatch")
        return redirect("storeApp:employeePage")
    else:
      data_to_save = EmployeeDetailInformations.objects.filter(id = get_employeeId).update(
          employee_Full_name = get_employee_Full_name,
          employee_gender =  get_employee_gender,
          employee_email_address = get_employee_email_address,
          employee_start_date =  get_employee_start_date,
          employee_phone_number1 = get_employee_phone_number1,
          employee_phone_number2 =  get_employee_phone_number2,
          employee_residence_area = get_employee_residence_area,
          employee_username =  get_username,
          employee_password =  get_password1,
        )
      messages.success(request, f"{get_employee_Full_name} updated successFull by {request.user.username}")
      return redirect("storeApp:employeePage")
    
    
# add_employee_account
  elif request.method == "POST" and request.POST.get('add_employee_account'):
    print(request.POST.get('first_name'))
    form = EmployeeAcountForm(request.POST)
    if form.is_valid():
      get_employee_id = request.POST.get('first_name')
      get_employee_username = request.POST.get('username')
      get_employee_password = request.POST.get('password1')
      get_employee = EmployeeDetailInformations.objects.get(id =get_employee_id )
      get_employee.employee_username = get_employee_username
      get_employee.employee_password = get_employee_password
      get_employee.save()
      print(get_employee.employee_username)
      form.save()
      employee_Full_name = request.POST.get('first_name')
      messages.success(request, f"{get_employee.employee_Full_name} added successFull by {request.user.username}")
      return redirect("storeApp:employeePage")
    else:
      messages.info(request, "Oops! username arleady exit or Password missmatch, please try again.")
      return redirect("storeApp:employeePage")
  else:
    try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
    except:
      messages.info(request, f"{request.user} does not have any credential yet!")
      return redirect("storeApp:employeePage")
    get_all_employee = EmployeeDetailInformations.objects.all()
    get_number__of_all_employee = EmployeeDetailInformations.objects.all().count()
    get_number__of_all_employee_with_no_account = EmployeeDetailInformations.objects.filter(employee_username = None).count()
    get_number__of_all_employee_with_account = get_number__of_all_employee - get_number__of_all_employee_with_no_account
    form = EmployeeAcountForm()
    template_name = 'store/employeePage.html'
    context = {
      'form':form,
      'get_number__of_all_employee':get_number__of_all_employee,
      'get_number__of_all_employee_with_no_account':get_number__of_all_employee_with_no_account,
      'get_number__of_all_employee_with_account':get_number__of_all_employee_with_account,
      'get_all_employee':get_all_employee,
      'get_all_user_authorizations':get_all_user_authorizations,
    }
    return render(request, template_name, context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_URL)
# salesPage
def salesPage(request):
  # sell_product
  if request.method == "POST" and request.POST.get('sell_product'):

    print(request.POST.get('product_name'))
    get_product_id = request.POST.get('product_name')
    date_product_sold = request.POST.get('date_product_sold')
    number_of_product_nedeed = request.POST.get('number_of_product_nedeed')
    number_of_product_nedeed = int(number_of_product_nedeed)
    get_product = ProductAndSupplierAndReceiverTable.objects.get(id=get_product_id )
    get_product_quantity_in_a_store = int(get_product.product_quantity)
    form = productSoldInCashForm(request.POST)
    if form.is_valid():
      if number_of_product_nedeed > get_product_quantity_in_a_store:
        messages.info(request, f" {get_product} remains only {get_product_quantity_in_a_store} please add more quantity to the store to continue selling this products")
        return redirect("storeApp:salesPage")
      elif number_of_product_nedeed < get_product_quantity_in_a_store:
        get_product_cost_after_sold= int(get_product.amount_to_sold) * number_of_product_nedeed
        instance = form.save(commit= False)
        instance.total_product_cost =get_product_cost_after_sold
        store_remain =int(get_product.product_quantity) - number_of_product_nedeed
        product_cost_remain_in_store = store_remain * int(get_product.product_cost)
        update_product_quantity_in_store = ProductAndSupplierAndReceiverTable.objects.filter(id =get_product_id ).update(
        product_quantity=store_remain,total_product_cost = product_cost_remain_in_store)
        x = datetime.datetime.now()
        print(x.strftime("%d"))
        print(date_product_sold)
        # print(get_product.created_at,"created")
        # get_product.update(product_quantity=store_remain)
        # get_product.save()
        instance.store_remain =store_remain
        get_login_user = request.user.username
        print(get_login_user)
        try:

          filter_login_user = EmployeeDetailInformations.objects.get( employee_username = get_login_user )
          print('-------------', filter_login_user)
          instance.store_remain =store_remain
          instance.supervisor = filter_login_user
        # instance.shop_name = filter_login_user
          instance.save()
          get_product = ProductAndSupplierAndReceiverTable.objects.get(id=get_product_id) 
          messages.success(request, f"{get_product_id} sold by {request.user.username}")
          return redirect("storeApp:salesPage")
        except:
          instance.store_remain =store_remain
          # instance.supervisor = filter_login_user
        # instance.shop_name = filter_login_user
          instance.save()
          get_product = ProductAndSupplierAndReceiverTable.objects.get(id=get_product_id) 
          messages.success(request, f"{get_product_id} sold by {request.user.username}")
          return redirect("storeApp:salesPage")

    else:
      messages.info(request, "Oops! something wrong, please try again.")
      return redirect("storeApp:salesPage")
  elif request.method == "POST" and request.POST.get("update_sells"):
    get_sales_id= request.POST.get('sales_id')
    get_product_id= request.POST.get('product_name')
    get_product = ProductAndSupplierAndReceiverTable.objects.get(id = get_product_id)
    get_number_of_product_nedeed = request.POST.get('number_of_product_nedeed')
    get_number_of_product_nedeed = int(get_number_of_product_nedeed)
    get_supervisor_id = request.POST.get('supervisor')
    get_shop_id = request.POST.get('shop_name')
    get_product = ProductAndSupplierAndReceiverTable.objects.get(id=get_product_id )
    get_supervisor = EmployeeDetailInformations.objects.get(id=get_supervisor_id )
    get_shop = ShopsTable.objects.get(id=get_shop_id )
    get_product_quantity_in_a_store = int(get_product.product_quantity)
    
    if get_number_of_product_nedeed > get_product_quantity_in_a_store:
      messages.info(request, f" {get_product} remains only {get_product_quantity_in_a_store} please add more quantity to the store to continue selling this products")
      return redirect("storeApp:salesPage")
    elif get_number_of_product_nedeed <= get_product_quantity_in_a_store:
      
      update_sales = productSoldInCash.objects.get(id = get_sales_id)
      if (update_sales.product_name.id) != (get_product.id):
        # get_old_record_from_sales_of_this_product ========>productSoldInCashTbale
        update_sales = productSoldInCash.objects.get(id = get_sales_id)
        get_old_product_name = update_sales.product_name
        get_old_number_of_product_nedeed = update_sales.number_of_product_nedeed
        get_old_total_product_cost = update_sales.total_product_cost 
        get_old_supervisor = update_sales.supervisor
        get_old_shop_name = update_sales.shop_name
        get_old_store_remain = update_sales.store_remain
        print(get_old_product_name)
        print(get_old_number_of_product_nedeed)
        print(get_old_total_product_cost)
        print(get_old_supervisor)
        print(get_old_shop_name)
        print(get_old_store_remain)
        # =========get_old_product_in_a_store =========>ProductAndSupplierAndReceiverTable
        

        get_product_cost_after_sold= int(get_product.amount_to_sold) * get_number_of_product_nedeed
        store_remain =int(get_product.product_quantity) - get_number_of_product_nedeed
        product_cost_remain_in_store = store_remain * int(get_product.product_cost)
        print('===========',update_sales.product_name.id)
        print('===========',get_product.id)
        update_product_sold_only = productSoldInCash.objects.filter(id = get_sales_id).update(
        product_name = get_product_id,
        number_of_product_nedeed = get_number_of_product_nedeed,
        total_product_cost = get_product_cost_after_sold,
        store_remain = store_remain
        )
        
        update_product = productSoldInCash.objects.get(id = get_sales_id)
        get_product = ProductAndSupplierAndReceiverTable.objects.filter(id=get_product_id).update(
        product_quantity=store_remain,total_product_cost = product_cost_remain_in_store)
        messages.success(request, f"product sold changed from {update_sales.product_name} to {update_product.product_name}  sucesfull by {request.user.username}")
        return redirect("storeApp:salesPage")
      elif (update_sales.number_of_product_nedeed) != (get_number_of_product_nedeed):
        get_product_cost_after_sold= int(get_product.amount_to_sold) * get_number_of_product_nedeed
        store_remain =int(get_product.product_quantity) - get_number_of_product_nedeed
        product_cost_remain_in_store = store_remain * int(get_product.product_cost)
        update_sales_on_number_of_product_nedeed_only = productSoldInCash.objects.get(id = get_sales_id)
        update_ = productSoldInCash.objects.filter(id = get_sales_id).update(
        number_of_product_nedeed = get_number_of_product_nedeed,
        total_product_cost = get_product_cost_after_sold,
        store_remain = store_remain
        )
        get_product_which_sold = productSoldInCash.objects.get(id = get_sales_id)
        product_id = get_product_which_sold.product_name.id
        update_product_quantity_in_store = ProductAndSupplierAndReceiverTable.objects.filter(id =product_id ).update(
        product_quantity=store_remain,total_product_cost = product_cost_remain_in_store)
        messages.success(request, f"quantity  from {update_sales_on_number_of_product_nedeed_only}  to {get_number_of_product_nedeed}updated sucesfull by {request.user.username}")
        return redirect("storeApp:salesPage")
      elif ( update_sales.supervisor.id )!= (get_supervisor.id):
        update_supervisor_name = productSoldInCash.objects.get(id = get_sales_id)
        update_= productSoldInCash.objects.filter(id = get_sales_id).update(
        supervisor =get_supervisor_id, 
        )
        get_supervisor = EmployeeDetailInformations.objects.get( id = get_supervisor_id)
        messages.success(request, f"supervisor name from {update_supervisor_name.supervisor}  to {get_supervisor.employee_Full_name} updated sucesfull by {request.user.username}")
        return redirect("storeApp:salesPage")
      elif (update_sales.shop_name.id) != (get_shop.id):
        update_supervisor_name = productSoldInCash.objects.get(id = get_sales_id)
        update_= productSoldInCash.objects.filter(id = get_sales_id).update(
        shop_name =get_shop_id, 
        )
        get_shop = ShopsTable.objects.get( id = get_shop_id)
        messages.success(request, f"shop name from {update_supervisor_name.shop_name}  to {get_shop.shop_name} updated sucesfull by {request.user.username}")
        return redirect("storeApp:salesPage")
      else:
        return redirect("storeApp:salesPage")

  # add_emergence
  elif request.method == "POST" and request.POST.get("add_emergence"):
    form = EmergenceInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"emergence information added by {request.user.username}")
      return redirect("storeApp:salesPage")
  
  # add_order
  elif request.method == "POST" and request.POST.get("add_order"):
    form = CustomersOrdersForm(request.POST)
    if form.is_valid():
      instance = form.save(commit = False)
      # get_employee = EmployeeDetailInformations.objects.get(employee_username = request)
      instance.supervisor=request.user
      instance.save()
      customer_order = request.POST.get("customer_order")
      messages.success(request, f"{customer_order} added by {request.user.username}")
      return redirect("storeApp:salesPage")

  else:
    try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
    except:
      messages.info(request, f"{request.user} does not have any credential yet!")
      return redirect("storeApp:employeePage")
    form = productSoldInCashForm()
    get_all_employee = EmployeeDetailInformations.objects.all()
    get_all_products = ProductAndSupplierAndReceiverTable.objects.all().order_by('-id')
    get_all_shops = ShopsTable.objects.all().order_by('-updated_at')
    get_all_product_sold = productSoldInCash.objects.all().order_by('-updated_at')
    get_all_product_in_store = ProductAndSupplierAndReceiverTable.objects.all().order_by('id')
    
    today_date = datetime.datetime.today().date()
    
    
    # today_date = datetime.datetime.now()
    print( "--------------------",today_date)
    
    get_all_today_orders = CustomersOrders.objects.filter(delivery_date_expected=today_date )
    number_of_order_received_tody=get_all_today_orders.count()
    # today sales start here
    get_all_product_sold_today = productSoldInCash.objects.filter(date_product_sold = today_date)
    # print(get_all_product_sold_today.total_product_cost)
    today_sales_sum = 0
    today_emergence_cost_sum = 0
    # get_emergence_info
    get_emergence_info = EmergenceInformations.objects.filter(spending_date = today_date)
    if get_all_product_sold_today.count():
      number_of_poduct_sold = get_all_product_sold_today.count()
      print(number_of_poduct_sold)
      
      
      for product in get_all_product_sold_today:
        today_sales_sum +=product.total_product_cost
      
      
      
      for emergence in get_emergence_info:
        today_emergence_cost_sum +=emergence.spending_cost

    amount_remain_after_deducting_emergence_cost = today_sales_sum - today_emergence_cost_sum
    x = datetime.datetime.now()
    today = x.strftime("%x")
    template_name = 'store/salesPage.html'
    
    context = {
      'form':form,
      'today':today,
      'get_all_products':get_all_products,
      'get_all_shops':get_all_shops,
      'get_all_employee':get_all_employee,
      'get_all_product_sold':get_all_product_sold,
      'get_all_product_in_store':get_all_product_in_store,
      'get_all_product_sold_today':get_all_product_sold_today.first,
      'today_sales_sum':today_sales_sum,
      'get_emergence_info':get_emergence_info,
      'today_emergence_cost_sum':today_emergence_cost_sum,
      'amount_remain_after_deducting_emergence_cost':amount_remain_after_deducting_emergence_cost,
      'number_of_order_received_tody':number_of_order_received_tody,
      'get_all_user_authorizations':get_all_user_authorizations,

    }
    return render (request, template_name, context)


def productPage(request):
  if request.method == "POST" and request.POST.get('add_product'):
    form = ProductTableForm(request.POST)
    if form.is_valid():
      form.save()
      product_name = request.POST.get('product_name')
      messages.success(request, f"{product_name} added successfull by {request.user.username} ")
      return redirect("storeApp:productPage")
    else:
      messages.info(request, f"{product_name}  not added yet try again later")
      return redirect("storeApp:productPage")
  elif request.method == "POST" and request.POST.get('update_product'):
    try:
      get_product_id = request.POST.get('product_id')
      get_product_name= request.POST.get('product_name')
      update_product_info = ProductTable.objects.filter(id = get_product_id).update(
        product_name = get_product_name
      )
      messages.success(request, f"{get_product_name} updated successfull by {request.user.username} ")
      return redirect("storeApp:productPage")
    except:
      messages.info(request, f"{product_name}  not added yet try again later")
      return redirect("storeApp:productPage")
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
    return redirect("storeApp:productPage")

  get_products = ProductTable.objects.all().order_by('updated_at')
  template_name = 'store/productPage.html'
  context = {
    'get_all_user_authorizations':get_all_user_authorizations,
    'get_products':get_products,
  }
  return render(request, template_name, context)


def ordersPage(request):
  if request.method == "POST" and request.POST.get("add_order"):
    form = CustomersOrdersForm(request.POST)
    if form.is_valid():
      print('==========')
      instance = form.save(commit = False)
      # get_employee = EmployeeDetailInformations.objects.get(employee_username = request)
      instance.supervisor=request.user
      instance.save()
      customer_order = request.POST.get("customer_order")
      messages.success(request, f"{customer_order} added by {request.user.username}")
      return redirect("storeApp:ordersPage")
  form = CustomersOrdersForm()
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
    return redirect("storeApp:shopPage")
  get_all_customers_orders = CustomersOrders.objects.all().order_by('-updated_at')
  get_all_customers_orders_registered_by_me = CustomersOrders.objects.filter(supervisor = request.user).order_by('-updated_at')
  update = False
  template_name = 'store/ordersPage.html'
  context  = {
     'get_all_user_authorizations':get_all_user_authorizations,
     'form':form,
     'update':update,
     'get_all_customers_orders':get_all_customers_orders,
     'get_all_customers_orders_registered_by_me':get_all_customers_orders_registered_by_me
  }
  return render(request, template_name, context)

# changeOrderStatus
def changeOrderStatus(request, id):
  get_order_to_change = CustomersOrders.objects.filter(id = id).update(order_status = "Completed")
  get_order = CustomersOrders.objects.get(id = id)
  messages.success(request, f"order {get_order.customer_order }  from {get_order.customer_Full_name} completed succesfull ")
  return redirect("storeApp:ordersPage")

# updateOrder
def updateOrder(request, id):
  get_order = get_object_or_404(CustomersOrders, id=id)
  if request.method == "POST" and request.POST.get("update_order"):
    form = CustomersOrdersForm(request.POST, instance=get_order)
    if form.is_valid():
      print('==========')
      instance = form.save(commit = False)
      # get_employee = EmployeeDetailInformations.objects.get(employee_username = request)
      instance.supervisor=request.user
      instance.save()
      customer_order = request.POST.get("customer_order")
      messages.success(request, f"order {get_order.customer_order }  from {get_order.customer_Full_name} Updated succesfull ")
      return redirect("storeApp:ordersPage")
  form = CustomersOrdersForm()
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
    return redirect("storeApp:shopPage")
  get_all_customers_orders = CustomersOrders.objects.all().order_by('-updated_at')
  get_all_customers_orders_registered_by_me = CustomersOrders.objects.filter(supervisor = request.user).order_by('-updated_at')
  template_name = 'store/ordersPage.html'
  update = True
  form = CustomersOrdersForm(instance = get_order)
  context  = {
    'get_all_user_authorizations':get_all_user_authorizations,
    'form':form,
    'update':update,
    'get_order':get_order,
    'get_all_customers_orders':get_all_customers_orders,
    'get_all_customers_orders_registered_by_me':get_all_customers_orders_registered_by_me
  }
  return render (request, template_name, context)


# deleteOrder
def deleteOrder(request, id):
  get_order = get_object_or_404(CustomersOrders, id =id)
  get_order.delete()
  messages.info(request, "Order deleted successfull")
  return redirect ("storeApp:ordersPage")

# emergencePage
def emergencePage(request):
  if request.method == "POST" and request.POST.get("add_emergence"):
    form = EmergenceInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"emergence information added by {request.user.username}")
      return redirect("storeApp:emergencePage")
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
    return redirect("storeApp:shopPage")
  get_all_emergence = EmergenceInformations.objects.all().order_by('-updated_at')
  template_name = 'store/emergencePage.html'
  update = False
  context  = {
   'get_all_user_authorizations':get_all_user_authorizations,
   'get_all_emergence':get_all_emergence,
   'update':update,
  }
  return render (request, template_name, context)

# updateEmergence
def updateEmergence(request, id):
  get_emeregnce = get_object_or_404(EmergenceInformations, id = id)
  if request.method == "POST" and request.POST.get("update_emergence"):
    form = EmergenceInformationsForm(request.POST, instance= get_emeregnce)
    if form.is_valid():
      form.save()
      messages.success(request, f"emergence information added by {request.user.username}")
      return redirect("storeApp:emergencePage")
  form  = EmergenceInformationsForm(instance= get_emeregnce )
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
  get_all_emergence = EmergenceInformations.objects.all().order_by('-updated_at')
  template_name = 'store/emergencePage.html'
  update = True
  context  = {
   'get_all_user_authorizations':get_all_user_authorizations,
   'get_all_emergence':get_all_emergence,
   'update':update,
   'form':form
  }
  return render (request, template_name, context)

# deleteEmergence
def deleteEmergence(request, id):
  get_order = get_object_or_404(EmergenceInformations, id =id)
  get_order.delete()
  messages.info(request, "Emergence deleted successfull")
  return redirect ("storeApp:emergencePage")

# authorizationPage
def authorizationPage(request):
  if request.method == "POST" and request.POST.get('add_user_auth'):
    form = AuthorizeUsersForm (request.POST )
    if form.is_valid():
      form.save()
      messages.success(request, f"user authoriation for {request.POST.get('select_user')} added succesffuly by {request.user.username}")
      return redirect("storeApp:authorizationPage")
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
  form = AuthorizeUsersForm()
  get_all_user_authorizations_who_can = AuthorizeUsers.objects.all().order_by('-updated_at')
  template_name = 'store/authorizationPage.html'
  update = False
  context = {
    'get_all_user_authorizations':get_all_user_authorizations,
    'form':form,
    'update':update,
    'get_all_user_authorizations_who_can':get_all_user_authorizations_who_can,
  }
  return render (request, template_name, context) 

# updateUserAuthorizaitions
def updateUserAuthorizations(request, id):
  get_user_auth = get_object_or_404(AuthorizeUsers , id = id )
  if request.method == "POST"  and request.POST.get('update_user_auth'):
    form = AuthorizeUsersForm (request.POST, instance= get_user_auth)
    if form.is_valid():
      form.save()
      messages.success(request, f"user authoriation Updated succesffuly by {request.user.username}")
      return redirect("storeApp:authorizationPage")
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
  get_all_user_authorizations_who_can = AuthorizeUsers.objects.all().order_by('-updated_at')
  form = AuthorizeUsersForm(instance= get_user_auth)
  template_name = 'store/authorizationPage.html'
  update = True
  context = {
    'get_all_user_authorizations':get_all_user_authorizations,
    'form':form,
    'update':update,
    'get_all_user_authorizations_who_can':get_all_user_authorizations_who_can,
  }
  return render (request, template_name, context) 

# updateUserAuthorizaitions
def deleteUserAuthorizations(request, id):
  get_user_auth = get_object_or_404(AuthorizeUsers, id =id)
  get_user_auth.delete()
  messages.info(request, "Authorization credential for user {get_user_auth.select_user} removed successfull")
  return redirect ("storeApp:authorizationPage")

# updateEmployee
def updateEmployeePage(request, id):
  get_employee_info_from_database = get_object_or_404(EmployeeDetailInformations, id= id)
  print(get_employee_info_from_database)
  form1 = EmployeeDetailInformationsForm(instance= get_employee_info_from_database)
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
      messages.info(request, f"{request.user} does not have any credential yet!")
      return redirect("storeApp:employeePage")
  get_all_employee = EmployeeDetailInformations.objects.all()
  get_number__of_all_employee = EmployeeDetailInformations.objects.all().count()
  get_number__of_all_employee_with_no_account = EmployeeDetailInformations.objects.filter(employee_username = None).count()
  get_number__of_all_employee_with_account = get_number__of_all_employee - get_number__of_all_employee_with_no_account
  form2 = EmployeeAcountForm()
  return redirect('storeApp:employeePage')
 
# deleteUser

def deleteUser(request, id):
  get_user = get_object_or_404(EmployeeDetailInformations, id = id)
  get_user.delete()
  messages.success(request, "employee deleted")
  return redirect('storeApp:employeePage')

  # deleteShop
def deleteShop(request, id):
  try:
    get_shop = get_object_or_404(ShopsTable, id = id)
    get_shop.delete()
    messages.success(request, "shop informations deleted")
    return redirect('storeApp:shopPage')
  except:
    messages.error(request, "shop info not deleted yet try again letter")
    return redirect('storeApp:shopPage')

def deleteProduct(request, id):
  try:
    get_product_id =  get_object_or_404(ProductTable, id = id)
    get_product_id.delete()
    messages.success(request, "product deleted")
    return redirect('storeApp:productPage')
  except:
    messages.success(request, "product not deleted")
    return redirect('storeApp:productPage')
  
def deleteSupplier(request, id):
  try:
    get_supplier_id =  get_object_or_404(ProductAndSupplierTable, id = id)
    get_supplier_id.delete()
    messages.success(request, "supplier deleted")
    return redirect('storeApp:suppliersPage')
  except:
    messages.success(request, "supplier not deleted")
    return redirect('storeApp:suppliersPage')

def deleteProductSold(request, id):
  try:
    get_product_id =  get_object_or_404(productSoldInCash, id = id)
    get_product_id.delete()
    messages.success(request, "product sold  deleted")
    return redirect('storeApp:salesPage')
  except:
    messages.success(request, "product sold not deleted")
    return redirect('storeApp:salesPage')

def deleteProductInStore(request, id):
  try:
    get_product_id =  get_object_or_404(ProductAndSupplierAndReceiverTable, id = id)
    get_product_id.delete()
    messages.success(request, "product   deleted")
    return redirect('storeApp:salesPage')
  except:
    messages.success(request, "product not  deleted")
    return redirect('storeApp:salesPage')

# companyStockPage
def companyStockPage(request):
  if request.method == "POST" and request.POST.get("add_stock_info"):
    form = CompanyStockOrAssetsForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, f"stock information added by {request.user.username}")
      return redirect("storeApp:companyStockPage")
  try:
      get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
  except:
    messages.info(request, f"{request.user} does not have any credential yet!")
    return redirect("storeApp:companyStockPage")
  get_all_company_stock = CompanyStockOrAssets.objects.all().order_by('-updated_at')
  template_name = 'store/companyStockPage.html'
  update = False
  context  = {
   'get_all_user_authorizations':get_all_user_authorizations,
   'get_all_company_stock':get_all_company_stock,
   'update':update,
  }
  return render (request, template_name, context)

def activateUserAuthorizations(request, id):
  get_user_auth = get_object_or_404(AuthorizeUsers, id =id)
  deactivate_user_account = AuthorizeUsers.objects.filter(id = get_user_auth.id).update(
  view_dashboard =False,
  manage_employees  =False,
  manage_shop =False,
  manage_product =False,
  manage_supplier =False,
  manage_store =False,
  manage_sales = True,
  manage_orders = True,
  manage_emergence = True,
  help_center = True,
  manage_authorizations = False
  )
  messages.success(request, f"{get_user_auth.select_user} account Activated")
  return redirect('storeApp:authorizationPage')

def deactivateUserAuthorizations(request, id):
  get_user_auth = get_object_or_404(AuthorizeUsers, id =id)
  deactivate_user_account = AuthorizeUsers.objects.filter(id = get_user_auth.id).update(
  view_dashboard =False,
  manage_employees  =False,
  manage_shop =False,
  manage_product =False,
  manage_supplier =False,
  manage_store =False,
  manage_sales =False,
  manage_orders =False,
  manage_emergence =False,
  help_center =False,
  manage_authorizations =False
  )
  messages.success(request, f"{get_user_auth.select_user} account deactivated")
  return redirect('storeApp:authorizationPage')