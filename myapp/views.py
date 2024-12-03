from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from .models import Product

# Create your views here.
def create_product(request):

	if request.method == 'POST':
	
		code_v = request.POST['code']
		#return HttpResponse(code_v)
		name_v = request.POST['name']
		qty_v = int(request.POST['qty'])

		rec = Product(code = code_v, name = name_v, price = 30.50,
		quantity = 20, description = 'bla bla bla',
		is_available = True)
		rec.save()

		records = Product.objects.all()
		context = {'products':records}
		return render(request, 'home.html')

	return render(request, 'create_product.html')

def fetch_all(request):
	records = Product.objects.all()
	context = {'products':records}
	return render(request, 'products.html', context)

def delete(request, pk):
	product_obj = get_object_or_404(Product, id = pk)
	product_obj.delete()
	return redirect('fetch_all')

def edit_product(request, pk):
	product_obj = get_object_or_404(Product, id = pk)

	if request.method == 'POST':
		product_obj.code = request.POST['code']
		product_obj.name = request.POST['name']
		product_obj.price = request.POST['price']
		product_obj.quantity = request.POST['qty']
		product_obj.description = request.POST['description']

		product_obj.save()

		return redirect('fetch_all')
	context = {'product':product_obj}
	return render(request, 'edit_product.html', context)





def greeting(request):
	return HttpResponse('Hello world....!')

def test(request):
	return HttpResponse("Another response")


def home(request):
	return render(request, 'home.html')

def  contact(request):
	return render(request, 'contact.html')

def  photos(request):
	return render(request, 'gallary.html')