from fishkas.models import Wish
from django.contrib.messages import get_messages
from fishkas.models import Notifier
from main.models import Instance, Instance_buy
from django.core.mail import send_mail
from django.contrib.auth.models import User

def need_for_every(args, request):
	""" This function does everything usual that is needed for evert def """

	test = request.session.get('test_popup', 'no')
	if test == 'no':
		request.session.__setitem__('test_popup', 'yes')
		args['test_popup'] = 1;

	if request.user.is_authenticated():
		user_wish = Wish.objects.filter(user=request.user)
		temp = []
		for wish in user_wish:
			if wish.for_buy:
				temp.append(wish.instance_buy)
			else:
				temp.append(wish.instance)
		args['user_wish'] = temp
	# dealing with messages
	args['messages'] = list(get_messages(request))
	return args

def create_username(username):
	while True:
		counter = 0
		if not User.objects.filter(username=username).exists():
			return username
		if counter != 0:
			username = username[:-len(str(counter))] + str(counter+1)
		else:
			username = username + '1'
		counter += 1

def notify_sell(instance):
	# part of notify for selling ads
	counter = [];
	notifiers = Instance_buy.objects.all().filter(max_price__gte=instance.price).filter(min_price__lte=instance.price)
	for notifier in notifiers:
		if instance.model.title == notifier.model.title:
			counter.append(notifier.user.email)
	counter = list(set(counter))
	for count in counter:
		send_mail('iBox напоминалка.' ,'Привет '+ get_object_or_404(User,
		email=count).first_name +', на iBox.kg поступило объявление '+ instance.model.title +' за '+ str(instance.price) + 
		' сом, которое заинтересует вас. Проверь http://ibox.kg/instance/'+ str(instance.id) ,
		settings.EMAIL_HOST_USER, [count], fail_silently=True)

def notify_buy(instance_buy):
	# part of notify for buying ads
	counter = [];
	min_price = instance_buy.min_price - instance_buy.min_price * 10 / 100
	max_price = instance_buy.max_price + instance_buy.max_price * 10 / 100
	notifiers = Instance.objects.all().filter(price__gte=max_price).filter(price__lte=min_price)
	for notifier in notifiers:
		counter.append(notifier.user.email)
	counter = list(set(counter))

	for count in counter:
		send_mail('iBox напоминалка.' ,'Привет '+ get_object_or_404(User,
		email=count).first_name +', на iBox.kg поступило объявление o купке за примерную цену вашего объявления которое заинтересует вас.'
		+ str(instance.price) + ' Проверь http://ibox.kg/instance/'+ str(instance_buy.id) + '?operation=buy' ,
		settings.EMAIL_HOST_USER, [count], fail_silently=True)



