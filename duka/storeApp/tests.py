from django.test import TestCase

# # Create your tests here.


#  if request.method == "POST" and request.POST.get('sell_product'):
#     print(request.POST.get('product_name'))
#     form = productSoldInCashForm(request.POST)
#     if form.is_valid():
#       get_product_id = request.POST.get('product_name')
#       date_product_sold = request.POST.get('date_product_sold')
#       number_of_product_nedeed = request.POST.get('number_of_product_nedeed')
#       get_product = ProductAndSupplierAndReceiverTable.objects.get(product_name=get_product_id )
#       get_product_cost_after_sold= int(get_product.amount_to_sold) * int(number_of_product_nedeed)
#       instance = form.save(commit= False)
#       instance.total_product_cost =get_product_cost_after_sold
#       store_remain =int(get_product.product_quantity) - int(number_of_product_nedeed)
#       update_product_quantity_in_store = ProductAndSupplierAndReceiverTable.objects.update(product_quantity=store_remain )
#       x = datetime.datetime.now()
#       print(x.strftime("%d"))
#       print(date_product_sold)
#       # print(get_product.created_at,"created")
#       # get_product.update(product_quantity=store_remain)
#       # get_product.save()
#       instance.store_remain =store_remain
#       instance.save()
#       get_product = ProductTable.objects.get(id=get_product_id)
      
#       messages.success(request, f"{get_product_id} sold by {request.user.username}")
#       return redirect("storeApp:salesPage")
#     else:
#       messages.info(request, "Oops! something wrong, please try again.")
#       return redirect("storeApp:salesPage")
  
#   # add_emergence
#   elif request.method == "POST" and request.POST.get("add_emergence"):
#     form = EmergenceInformationsForm(request.POST)
#     if form.is_valid():
#       form.save()
#       messages.success(request, f"emergence information added by {request.user.username}")
#       return redirect("storeApp:salesPage")
  
#   # add_order
#   elif request.method == "POST" and request.POST.get("add_order"):
#     form = CustomersOrdersForm(request.POST)
#     if form.is_valid():
#       form.save()
#       customer_order = request.POST.get("customer_order")
#       messages.success(request, f"{customer_order} added by {request.user.username}")
#       return redirect("storeApp:salesPage")

#   else:
#     form = productSoldInCashForm()
#     get_all_employee = EmployeeDetailInformations.objects.all()
#     get_all_products = ProductTable.objects.all().order_by('-id')
#     get_all_shops = ShopsTable.objects.all().order_by('-id')
#     get_all_product_sold = productSoldInCash.objects.all().order_by('id')
#     get_all_product_in_store = ProductAndSupplierAndReceiverTable.objects.all().order_by('id')
#     x = datetime.datetime.now()
#     today_date = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))
#     get_all_today_orders = CustomersOrders.objects.filter(order_date=today_date )
#     number_of_order_received_tody=get_all_today_orders.count()
#     # today sales start here
#     get_all_product_sold_today = productSoldInCash.objects.filter(date_product_sold = today_date)
#     # print(get_all_product_sold_today.total_product_cost)
#     today_sales_sum = 0
#     today_emergence_cost_sum = 0
#     # get_emergence_info
#     get_emergence_info = EmergenceInformations.objects.filter(spending_date = today_date)
#     if get_all_product_sold_today.count():
#       number_of_poduct_sold = get_all_product_sold_today.count()
#       print(number_of_poduct_sold)
      
      
#       for product in get_all_product_sold_today:
#         today_sales_sum +=product.total_product_cost
      
      
      
#       for emergence in get_emergence_info:
#         today_emergence_cost_sum +=emergence.spending_cost

#     amount_remain_after_deducting_emergence_cost = today_sales_sum - today_emergence_cost_sum
#   # today_date
#   x = datetime.datetime.now()
#   today_date = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))
#   get_all_today_orders = CustomersOrders.objects.filter(order_date=today_date )
#   number_of_order_received_tody=get_all_today_orders.count()
#   # today sales start here
#   get_all_product_sold_today = productSoldInCash.objects.filter(date_product_sold = today_date)
#   # print(get_all_product_sold_today.total_product_cost)
#   today_sales_sum = 0
#   today_emergence_cost_sum = 0
#   # get_emergence_info
#   get_emergence_info = EmergenceInformations.objects.filter(spending_date = today_date)
#   if get_all_product_sold_today.count():
#     number_of_poduct_sold = get_all_product_sold_today.count()
#     print(number_of_poduct_sold)
    
    
#     for product in get_all_product_sold_today:
#       today_sales_sum +=product.total_product_cost
    
    
    
#     for emergence in get_emergence_info:
#       today_emergence_cost_sum +=emergence.spending_cost
#   # weeekly sales
#   date = datetime.datetime.now()
#   # this_month= datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%b")),int(x.strftime("%m")) )
#   # print(this_month)
#   try:
#     get_all_user_authorizations = AuthorizeUsers.objects.get(select_user = request.user)
#   except:
#     messages.info(request, f"{request.user} does not have any credential yet!")
#     return redirect('storeApp:loginPage')