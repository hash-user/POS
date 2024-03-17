from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import profile_extended, branches, pos_request, merchant_information, pos_information, pos_deployment_report
#from .verifyClass import DetailsVerification

# Create your views here.
def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		
		user = auth.authenticate(email=email, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/dashboard')
		else:
			messages.info(request, 'Invalid Login Credentials')
			return redirect('/login')
	return render(request, 'login.html')


def dashboard(request):
	return render(request, 'dashboard.html')


def registration(request):
	return render(request, 'registration.html')


def searchinfo(request):
	return render(request, 'search-info.html')

def newpos(request):
	if request.method == 'POST':
		terminal_id = request.POST['terminal_id']
		terminal_name = request.POST['terminal_name']
		terminal_brand = request.POST['terminal_brand']
		terminal_serial_number = request.POST['terminal_serial_number']
		terminal_model = request.POST['terminal_model']
		network_type = request.POST['network_type']
		connection_type = request.POST['connect_type']
		#sim_number = request.POST['sim_number']
		sim_serial_number = request.POST['sim_serial_number']
		pos_collection_account_number = request.POST['account_number']

		if pos_information.objects.filter((pos_id==terminal_id) | (pos_serial_number==terminal_serial_number) ).exists():
			messages.info(request, 'ID Exists')
			return redirect('/add-new-pos')
		else:
			new_pos = pos_information(terminal_name=terminal_name, pos_id=terminal_id, pos_brand=terminal_brand, pos_serial_number=terminal_serial_number, pos_model=terminal_model, pos_collection_account_number=pos_collection_account_number, sim_network_type=network_type, sim_serial_number=sim_serial_number)
			new_pos.save()

	return render(request, 'add-new-pos.html')

def newuser(request):
	if request.method == 'POST':
		username = request.POST['username']
		last_name = request.POST['last_name']
		first_name = request.POST['first_name']
		department = request.POST['department']
		role = request.POST['role']
		status = request.POST['status']
		user_type = request.POST['user_type']
		email = request.POST['email']
		password = request.POST['password']

		user_length = len(str(username))
		domain_check = email.split("@")

		def domain_name_check(self, domain_name):
			if "." in self.domain_name:
				check = True
			else:
				check = False
			return check

		if user_length == 10:
			name_spell = list(last_name, first_name)
			name = name_spell.capitalize()

			if domain_check[1] == "omnibsic.com.gh":

				check_domain_name = domain_name_check(domain_check[0])

				if check_domain_name == True:

					if User.objects.filter(username=username, email=email).exists():
						messages.info(request, 'username already exists')
						redirect('/add-new-user')
					elif profile_extended.objects.filter(username=username).exists():
						messages.info(request, 'username already exists')
						redirect('/add-new-user')
					else:
						is_super_user = True 
						if user_type == "1":
							is_super_user = True
						elif user_type == "0":
							is_super_user = False

						active_user = True
						if status == "1":
							active_user = True
						elif status == "0":
							active_user = False

						user = User.objects.create_user(password=password, is_superuser=is_super_user, username=username, first_name=first_name, last_name=last_name, email=email, is_active=active_user)
						x = profile_extended(username=username, role=role, department=department)
						user.save()
						x.save()

						redirect('/dashboard')

				elif check_domain_name == False:
					messages.info(request, 'Invalid Email Name')
					return redirect('/add-new-user')
			else:
				messages.info(request, 'Invalid Domain name. Domain name should be omnibsic.com.gh')
				return redirect('/add-new-user')
		else:
			messages.info(request, 'Username length is not up to 10 ')
			redirect('/add-new-user')

	return render(request, 'add-new-user.html')