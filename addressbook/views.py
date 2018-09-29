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
	filter = request.GET.get('filter')
	if filter is None:
		people = Person.objects.all()
	else:
		people = Person.objects.filter(Q(first_name__contains=filter) |
									   Q(last_name__contains=filter) |
									   Q(phone_number__contains=filter) |
									   Q(email_address__contains=filter) |
									   Q(street_address__contains=filter))
	return render(request, 'addressbook/index.html', {'people': people})
	
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
def delete_person(request, person_id):
	if request.method == "POST":
		Person.objects.filter(id=person_id).delete()
	return redirect('index')