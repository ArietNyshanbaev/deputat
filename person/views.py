from django.shortcuts import render, get_object_or_404
from .models import Party, Person
from promis.models import  Promis

def zhogorku_kenesh(request, party_id=-1):
	args = {}
	if party_id < 1:
		active_party = Party.objects.all()[0]
	else :
		active_party =  get_object_or_404(Party, pk=party_id)
	args['persons'] = Person.objects.filter(party=active_party,category__title='ЖК')
	args['active_party'] = active_party
	args['parties'] = Party.objects.all()
	template = 'person/zhogorku_kenesh.html'
	return render(request, template, args)

def mestnyi_kenesh(request, party_id=-1):
	args = {}
	if party_id < 1:
		active_party = Party.objects.all()[0]
	else :
		active_party =  get_object_or_404(Party, pk=party_id)
	args['persons'] = Person.objects.filter(party=active_party,category__title='МК')
	args['active_party'] = active_party
	args['parties'] = Party.objects.all()
	template = 'person/mestnyi_kenesh.html'
	return render(request, template, args)

def detailed_person(request, person_id):
	args = {}
	person = get_object_or_404(Person, pk=person_id)
	args['promises'] = Promis.objects.filter(person=person)
	args['person'] = person
	args['done_promises'] = Promis.objects.filter(person=person, status='Выполнено').count()
	args['not_done_promises'] = Promis.objects.filter(person=person, status='Не выполнено').count()
	template = 'person/detailed_person.html'
	return render(request, template, args)