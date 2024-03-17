from django.db import models

class profile_extended(models.Model):
	username = models.CharField(max_length=255, unique=True)
	role = models.CharField(max_length=255)
	department = models.CharField(max_length=255)

class branches(models.Model):
	branch_code = models.IntegerField(max_length=255, unique=True)
	division = models.CharField(max_length=255)
	zone = models.CharField(max_length=255)
	branch_name = models.CharField(max_length=255)

class pos_request(models.Model):
	request_id = models.CharField(max_length=255, unique=True)
	merchant_name = models.CharField(max_length=255)
	status	= models.CharField(max_length=50)
	number_of_pos_requested = models.IntegerField()
	document_name_1 = models.BooleanField(default=False)
	document_name_2 = models.BooleanField(default=False)
	document_name_3	= models.BooleanField(default=False)
	document_name_4 = models.BooleanField(default=False)
	document_name_5 = models.BooleanField(default=False)
	currency = models.CharField(max_length=255)
	ownership_type = models.CharField(max_length=255)
	set_up_fee = models.IntegerField()
	date_requested = models.DateTimeField()
	remarks = models.TextField()

class merchant_information(models.Model):
	business_name = models.CharField(max_length=255)
	merchant_name = models.CharField(max_length=255)
	trade_name = models.CharField(max_length=255)
	rsm = models.CharField(max_length=255)
	office_address = models.CharField(max_length=255)
	postal_address = models.CharField(max_length=255)
	industry = models.CharField(max_length=255)
	nature_of_business = models.CharField(max_length=255)
	contact_person = models.IntegerField(max_length=12)
	settlement_account_number = models.IntegerField(max_length=20)
	scheme_platform = models.CharField(max_length=255)
	commissions = models.IntegerField(max_length=255)
	settlement_period = models.CharField(max_length=255)

class pos_information(models.Model):
	terminal_name = models.CharField(max_length=255)
	pos_id = models.CharField(max_length=255, unique=True)
	pos_brand = models.CharField(max_length=255)
	pos_serial_number = models.CharField(max_length=255, unique=True)
	pos_model = models.CharField(max_length=255)
	pos_collection_account_number = models.CharField(max_length=20)
	sim_network_type = models.CharField(max_length=255)
	sim_serial_number = models.CharField(max_length=255)
	connection_type = models.CharField(max_length=150)
	deployed = models.BooleanField(default=False)

class pos_deployment_report(models.Model):
	request_id = models.CharField(max_length=255)
	pos_id = models.CharField(max_length=255)
	business_name = models.CharField(max_length=255)
	branch_code = models.IntegerField(max_length=255)
	rsm = models.CharField(max_length=255)
	location_deployed_to = models.CharField(max_length=255)
	period_of_inactivity = models.DateTimeField()
	period_of_activity =  models.DateTimeField()
	status = models.CharField(max_length=255)
	date_of_deployment = models.CharField(max_length=255)
	date_of_retrieval = models.CharField(max_length=255)
	last_date_of_transaction = models.DateTimeField()


'''class CustomUserManager(UserManager):
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email Error")

			email = self.normalize_email(email)
			user = self.model(email=email, **extra_fields)
			user.set_password(password)
			user.save(using=self._db)

			return user


	def create_user(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser():
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(blank=True, default='', unique=True)
	name = models.CharField(max_length=255, blank=True, default='')

	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)

	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(blank=True, null=True)

	objects = CustomUserManager()

	USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

'''