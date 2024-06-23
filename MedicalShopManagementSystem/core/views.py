from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
from .models import * 
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    if request.method == "POST":
        data = request.POST
        dealer_name = data.get("dealer_name")
        dealer_address = data.get("dealer_address")
        dealer_email = data.get("dealer_email")
        dealer_number = data.get("dealer_number")


        medicine_code = data.get("medicine_code")
        medicine_name = data.get("medicine_name")
        medicine_dealer_name_id=data.get("medicine_dealer_name")    
        medicine_price = data.get("medicine_price")
        medicine_stock = data.get("medicine_stock")
        medicine_desc = data.get("medicine_desc")


        employee_id = data.get("employee_id")
        employee_first_name = data.get("employee_first_name")
        employee_last_name = data.get("employee_last_name")
        employee_address = data.get("employee_address")
        employee_salary = data.get("employee_salary")
        employee_contact = data.get("employee_contact")
        employee_email = data.get("employee_email")


        customer_first_name = data.get("customer_first_name")
        customer_last_name = data.get("customer_last_name")
        customer_address = data.get("customer_address")
        customer_contact = data.get("customer_contact")
        customer_email = data.get("customer_email")


        product_name = data.get("product_name") 
        purchase_customer_id = data.get("purchase_customer_name")
        purchase_contact = data.get("purchase_contact")
        purchase_price = data.get("purchase_price")
        purchase_quantity = data.get("purchase_quantity")

        # Fetch the Customer instance
        try:
            purchase_customer_name = Customer.objects.get(id=purchase_customer_id)
        except Customer.DoesNotExist:
            purchase_customer_name = None


        # if dealer_name and dealer_address and dealer_email and dealer_number:
        if 'dealer_name' in data:
            Dealer.objects.create(
                dealer_name=dealer_name,
                dealer_address=dealer_address,
                dealer_email=dealer_email,
                dealer_number=dealer_number,
            )

        # elif medicine_code and medicine_name and medicine_dealer_name_id and medicine_price and medicine_stock and medicine_desc:
        elif 'medicine_name' in data:
            Medicine.objects.create(
                medicine_code=medicine_code,
                medicine_name=medicine_name,
                medicine_dealer_name_id=medicine_dealer_name_id,
                medicine_price=medicine_price,
                medicine_stock=medicine_stock,
                medicine_desc=medicine_desc,
            )
            
        # elif employee_id and employee_first_name and employee_last_name and employee_address and employee_salary and employee_contact and employee_email:
        elif 'employee_first_name' in data:
            Employee.objects.create(
                employee_id = employee_id,
                employee_first_name = employee_first_name,
                employee_last_name = employee_last_name,
                employee_address = employee_address,
                employee_salary = employee_salary,
                employee_contact = employee_contact,
                employee_email = employee_email,
            )
        
        # elif employee_id and employee_first_name and employee_last_name and employee_address and employee_salary and employee_contact and employee_email:
        elif 'customer_first_name' in data:
            Customer.objects.create(
                customer_first_name = customer_first_name,
                customer_last_name = customer_last_name,
                customer_address = customer_address,
                customer_contact = customer_contact,
                customer_email = customer_email,
            )

        elif 'product_name' in data:
            Purchase.objects.create(
                product_name = product_name,
                purchase_customer_name = purchase_customer_name,
                purchase_contact = purchase_contact,
                purchase_price = purchase_price,
                purchase_quantity = purchase_quantity,
            )
        # messages.success(request, "Your data is submitted...")
        # return redirect('home')

    dealers = Dealer.objects.all()
    default_dealer = Dealer.objects.first()
    medicine = Medicine.objects.all()
    employee = Employee.objects.all()
    customers = Customer.objects.all()
    customers_first = Customer.objects.first()
    purchases = Purchase.objects.all()
    return render(request, 'core/home.html',{
        'dealers': dealers,
        'default_dealer': default_dealer,
        'medicine':medicine,
        'employee':employee,
        'customer':customers,
        'customers_first':customers_first,
        'purchase':purchases,
    })

def dealer_delete(request, id):
    if request.method == "POST":
        pi = Dealer.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')

def dealer_update(request , id):
    queryset = Dealer.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        dealer_name = data.get('dealer_name')
        dealer_email = data.get('dealer_email')
        dealer_number = data.get('dealer_number')
        dealer_address = data.get('dealer_address')

        queryset.dealer_name  = dealer_name 
        queryset.dealer_email  = dealer_email 
        queryset.dealer_number  = dealer_number 
        queryset.dealer_address  = dealer_address 

        queryset.save()
        return redirect('home')
    else:
        context = {'queryset':queryset}
        return render(request,'core/updatedealer.html',context)



def medicine_delete(request, id):
    if request.method == "POST":
        pi = Medicine.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')


def medicine_update(request , id):
    queryset = Medicine.objects.get(id=id)
    dealers = Dealer.objects.all()
    default_dealer = Dealer.objects.first()
    print(queryset)

    if request.method == "POST":
        data = request.POST
        medicine_code = data.get("medicine_code")
        medicine_name = data.get("medicine_name")
        medicine_dealer_name_id = data.get("medicine_dealer_name")
        medicine_price = data.get("medicine_price")
        medicine_stock = data.get("medicine_stock")
        medicine_desc = data.get("medicine_desc")
 
        
        queryset.medicine_code=medicine_code
        queryset.medicine_name=medicine_name
        queryset.medicine_dealer_name_id=medicine_dealer_name_id
        queryset.medicine_price=medicine_price
        queryset.medicine_stock=medicine_stock
        queryset.medicine_desc=medicine_desc

        queryset.save()
        return redirect('home')
    else:
        context = {'queryset':queryset,'dealers':dealers,'default_dealer': default_dealer,}
        return render(request,'core/updatemedicine.html',context)


def employee_delete(request, id):
    if request.method == "POST":
        pi = Employee.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')


def employee_update(request,id):
    queryset = Employee.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        employee_id = data.get('employee_id')
        employee_first_name = data.get('employee_first_name')
        employee_last_name = data.get('employee_last_name')
        employee_address = data.get('employee_address')
        employee_salary = data.get('employee_salary')
        employee_contact = data.get('employee_contact')
        employee_email = data.get('employee_email')

        queryset.employee_id = employee_id
        queryset.employee_first_name = employee_first_name
        queryset.employee_last_name = employee_last_name 
        queryset.employee_address  = employee_address 
        queryset.employee_salary  = employee_salary 
        queryset.employee_contact  = employee_contact 
        queryset.employee_email  = employee_email 

        queryset.save()
        return redirect('home')
    else:
        context = {'queryset':queryset}
        return render(request,'core/updateemployee.html',context)

def customer_delete(request,id):
    if request.method == "POST":
        pi = Customer.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')
    

def customer_update(request,id):
    queryset = Customer.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        customer_first_name = data.get('customer_first_name')
        customer_last_name = data.get('customer_last_name')
        customer_address = data.get('customer_address')
        customer_contact = data.get('customer_contact')
        customer_email = data.get('customer_email')

        queryset.customer_first_name = customer_first_name
        queryset.customer_last_name = customer_last_name 
        queryset.customer_address  = customer_address 
        queryset.customer_contact  = customer_contact 
        queryset.customer_email  = customer_email  

        queryset.save()
        return redirect('home')
    else:
        context = {'queryset':queryset}
        return render(request,'core/updatecustomer.html',context)


def purchase_delete(request,id):
    if request.method == "POST":
        pi = Purchase.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def purchase_update(request, id):
    customers = Customer.objects.all()
    customers_first = Customer.objects.first()
    queryset = Purchase.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        product_name = data.get('product_name')
        purchase_customer_id = data.get('purchase_customer_name')
        purchase_contact = data.get('purchase_contact')
        purchase_price = data.get('purchase_price')
        purchase_quantity = data.get('purchase_quantity')

        # Fetch the Customer instance using the ID
        purchase_customer = get_object_or_404(Customer, id=purchase_customer_id)

        queryset.product_name = product_name
        queryset.purchase_customer_name = purchase_customer
        queryset.purchase_contact = purchase_contact
        queryset.purchase_price = purchase_price
        queryset.purchase_quantity = purchase_quantity

        queryset.save()
        return redirect('home')
    else:
        context = {'queryset': queryset, 'customer': customers, 'customers_first': customers_first}
        return render(request, 'core/updatepurchase.html', context)