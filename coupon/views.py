from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models.coupon import Coupon
from .models.category import Category
from .models.student import Student
from .models.PaidCoupon import PaidCoupon
from django.views import View


# Create your views here.
def home(request):
    return render(request,'coupon/basehome.html')
def loginhome(request):
    return render(request,'coupon/home.html')
def pay(request):
    return render(request,'coupon/payment.html')
def download(request):
    return render(request, 'coupon/download.html')
def purchase(request):
    return render(request, 'coupon/index.html')


class Index(View):
    def get(self,request):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        print(request.GET)
        if categoryID:
            products = Coupon.get_all_coupons_by_categoryid(categoryID)
        else:
            products = Coupon.get_all_coupons()

        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'coupon/index.html', data)

    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('couponcart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
        else:
            cart = {}
            cart[product] = 1


        request.session['couponcart'] = cart
        print('cart', request.session['couponcart'])
        return redirect('buy')

def validateStudent(student):
    error_message = None
    if (not student.first_name):
        error_message = "First Name Required !!"
    elif len(student.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not student.last_name:
        error_message = 'Last Name Required'
    elif len(student.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not student.phone:
        error_message = 'Phone Number required'
    elif len(student.phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(student.password) < 6:
        error_message = 'Password must be 6 char long'
    elif len(student.email) < 5:
        error_message = 'Email must be 5 char long'
    elif student.isExists():
        error_message = 'Email Address Already Registered..'
    return error_message


def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        student = Student(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password)
        error_message = validateStudent(student)


        
        if not error_message:
            student.password = make_password(student.password)
            student.register()
            return redirect('login-home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'auth/signup.html', data)


class Login(View):
    def get(self,request):
        return render(request, 'auth/login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = Student.get_student_by_email(email)
        error_message = None
        if student:
            flag = check_password(password, student.password)
            if flag:
                request.session['student_id'] = student.id
                request.session['student_email'] = student.email
                return redirect('login-home')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        return render(request, 'login-home', {'error': error_message})

def logout(request):
    auth_logout(request)
    return redirect('home-page')