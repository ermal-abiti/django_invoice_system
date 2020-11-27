from django.shortcuts import render, get_object_or_404
from django import forms
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, Http404
from django.views.generic import (
	View,
	CreateView,
	UpdateView,
	DetailView,
	ListView,
	DeleteView,
	)


def dashboardView(request):
	return render(request, 'invoice_system/dashboard.html')


class FletpercjelljaCV(CreateView):
	model = Fletpercjellja
	template_name = 'invoice_system/fletpercjellja_create.html'
	fields = '__all__'

class FletpercjelljaLV(ListView):
	model = Fletpercjellja
	template_name = 'invoice_system/fletpercjellja_listview.html'
	context_object_name = 'fletpercjelliet'

def fletpercjellja_detail_view(request, f_id):

	fletpercjellja = Fletpercjellja.objects.get(fletpercjellja_id=f_id)
	shitjet = Shitje.objects.filter(fletpercjellja=f_id).order_by('id')

	form = ShitjeForm(f_id=f_id)
	if request.method == "POST":
		form = ShitjeForm(request.POST, f_id=f_id)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(f'/fletpercjellja_detail/{f_id}/')

	search_form = SearchGetFletpercjellja()
	if request.method=="POST":
		search_form = SearchGetFletpercjellja(request.POST)
		if search_form.is_valid():
			search_str = request.POST.get('search')
			if search_str:
				obj = get_object_or_404(Fletpercjellja, fletpercjellja_id=search_str)
				return HttpResponseRedirect(f'/fletpercjellja_detail/{search_str}/')

	next = None
	previous = None
	nextTrigger = False
	fletpercjelljet = Fletpercjellja.objects.all()

	for i in range(len(fletpercjelljet)):
		if fletpercjelljet[i] == fletpercjellja:
			nextTrigger = True
			if i != 0:
				previous = fletpercjelljet[i-1]
			continue
		if nextTrigger:
			next = fletpercjelljet[i]
			nextTrigger = False
			
		
	context = {
		"next": next,
		"previous": previous,
		"fletpercjellja": fletpercjellja,
		"shitjet": shitjet,
		"form": form,
		"search_form": search_form,
	}
	return render(request, 'invoice_system/fletpercjellja_detail.html', context)



class ProductDV(DetailView):
	model = Product
	template_name = 'invoice_system/produkt_detail.html'

	def post(self, request, *args, **kwargs):
		product_id = request.POST.get('product')
		try:
			product = Product.objects.get(product_id=product_id)
		except Product.DoesNotExist:
			product = self.kwargs['pk']
		
		return HttpResponseRedirect(f'/produkt_detail/{product}/')
	
	def get_context_data(self, **kwargs):
		context = super(ProductDV, self).get_context_data(**kwargs)
		context['shitjet'] = Shitje.objects.filter(product=self.kwargs['pk']).order_by('-id')
		context['produktet'] = Product.objects.all()
		return context


class ProductCV(CreateView):
	model = Product
	template_name = 'invoice_system/produkt_create.html'
	fields = '__all__'

class ProductUV(UpdateView):
	model = Product
	template_name = 'invoice_system/produkt_create.html'
	fields = '__all__'

class ProductDelete(DeleteView):
	model = Product
	template_name = 'invoice_system/delete_form.html'
	success_url = '/'

def produkt_listview(request):
	produktet = Product.objects.all()
	if request.method == 'POST':
		product_id = request.POST.get('product')
		return HttpResponseRedirect(f'/produkt_detail/{product_id}/')
	context = {'produktet': produktet}
	return render(request, 'invoice_system/produkt_listview.html', context)


