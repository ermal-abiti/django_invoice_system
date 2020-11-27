from django.db import models
from django.urls import reverse
import datetime


class Product(models.Model):
	UNIT_CHOICES = (
		('Cope', 'Cope'),
		('kg', 'kg'),
		('m', 'm'),
		('m^2', 'm^2'),
	)
	product_id = models.CharField(max_length=50, primary_key=True)
	product_name = models.CharField(max_length=50)
	product_desc = models.CharField(max_length=100, null=True, blank=True)
	product_price = models.DecimalField(max_digits=10, decimal_places=2)
	product_unit = models.CharField(max_length=5, choices=UNIT_CHOICES, default='Cope')
	
	class Meta:
		ordering = ['product_id']


	@property
	def quantity(self):
		quantity = 0

		for i in Shitje.objects.filter(product=self.product_id):
			quantity -= i.shitje_quantity

		for i in Hyrje.objects.filter(product=self.product_id):
			quantity += i.hyrje_quantity

		return quantity

	@property
	def hyrje(self):
		hyrje = 0

		for i in Hyrje.objects.filter(product=self.product_id):
			hyrje += i.hyrje_quantity

		return hyrje

	@property
	def dalje(self):
		dalje = 0

		for i in Shitje.objects.filter(product=self.product_id):
			dalje += i.shitje_quantity

		return dalje

	def __str__(self):
		return f'{self.product_id}'

	def get_absolute_url(self):
		return reverse('produkt_detail_url', kwargs={'pk': self.pk})






class Fletpercjellja(models.Model):
	fletpercjellja_id = models.CharField(max_length=4, primary_key=True)
	fletpercjellja_data = models.DateTimeField(default=datetime.datetime.now)
	fletpercjellja_verejtje = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['-fletpercjellja_data']

	@property
	def get_total(self):
		sum = 0.0
		for i in Shitje.objects.filter(fletpercjellja=self.fletpercjellja_id):
			sum += float(i.get_shitje_total)
		return f'{sum:.2f} €'

	def __str__(self):
		return f'{self.fletpercjellja_id}'

	def get_absolute_url(self):
		return reverse('fletpercjellja_detail_url', kwargs={'f_id': self.fletpercjellja_id})


class Shitje(models.Model):
	fletpercjellja = models.ForeignKey(Fletpercjellja, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	shitje_quantity = models.DecimalField(max_digits=10, decimal_places=2)
	shitje_price = models.DecimalField(max_digits=10, decimal_places=2)

	@property
	def get_shitje_total(self):
		return self.shitje_quantity * self.shitje_price

	@property
	def totali(self):
		if self.shitje_quantity != None and self.shitje_price != None:
			total = self.shitje_quantity * self.shitje_price
		else:
			total = 0
			
		return f'{total:.2f}'

	def __str__(self):
		return f'{self.product} - {self.shitje_quantity}'







class FaturaHyrese(models.Model):
	fathyrese_id = models.CharField(max_length=50, primary_key=True)
	fathyrese_data = models.DateTimeField()
	fathyrese_verejtje = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['fathyrese_id']

	@property
	def get_total(self):
		sum = 0.0
		for i in Hyrje.objects.filter(fathyrese=self.fathyrese_id):
			sum += float(i.get_hyrje_total)
		return f'{sum:.2f} €'

	def __str__(self):
		return f'{self.fathyrese_id}'

class Hyrje(models.Model):
	fathyrese = models.ForeignKey(FaturaHyrese, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	hyrje_quantity = models.DecimalField(max_digits=10, decimal_places=2)
	hyrje_price = models.DecimalField(max_digits=10, decimal_places=2)

	@property
	def get_hyrje_total(self):
		return self.hyrje_quantity * self.hyrje_price

	@property
	def totali(self):
		if self.hyrje_quantity != None and self.hyrje_price != None:
			total = self.hyrje_quantity * self.hyrje_price
		else:
			total = 0
			
		return f'{total:.2f}'

	def __str__(self):
		return f'{self.product} - {self.hyrje_quantity}'