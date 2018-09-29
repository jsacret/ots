# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Person
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



@login_required
def index(request):
	return render(request, 'addressbook/index.html')

def person_table(request):
	filter = request.GET.get('filter')
	page_count = request.GET.get('pagecount') if request.GET.get('pagecount') else 10
	page = request.GET.get('page') if request.GET.get('page') else 0
	skip = int(page_count) * int(page);
	total_count = Person.objects.all().count()
	if filter is None:
		people = Person.objects.all()[skip:page_count]
	else:
		people = Person.objects.filter(Q(first_name__contains=filter) |
									   Q(last_name__contains=filter) |
									   Q(phone_number__contains=filter) |
									   Q(email_address__contains=filter) |
									   Q(street_address__contains=filter))[skip:page_count]

	return render(request, 'addressbook/persontable.html', {'people': people, 'total_count': total_count})
	
@login_required
def details(request, person_id):
	person = Person.objects.get(pk=person_id)
	return render(request, 'addressbook/details.html', {'person': person})

@login_required
def add_person(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			person = form.save()
			return redirect('details', person_id=person.pk)
	else:
		form = PostForm()
	return render(request, 'addressbook/addperson.html', {'form': form})

@login_required
def update_person(request, person_id):
	if request.method == "POST":
		if form.is_valid():
			person = Person.objects.get(pk=person_id)
			person.first_name = request.GET.get('first_name')
			person.last_name = request.GET.get('last_name')
			person.email_address = request.GET.get('email_address')
			person.street_address = request.GET.get('street_address')
			person.phone_number = request.GET.get('phone_number')
			person.save()
		redirect('index')
	else:
		redirect('index')


@login_required
def delete_person(request, person_id):
	if request.method == "POST":
		Person.objects.filter(id=person_id).delete()
	return redirect('index')

