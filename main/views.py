from django.shortcuts import render, redirect
from .forms import NewAdminForm, ContactForm, ContactSupportForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm, ContactSupportForm
from django.core.mail import send_mail, BadHeaderError
from .models import ContactSupport
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .models import ContactSubmission

def index(request):
    """ View function for home page of site. """
    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'pages/index.html')

def about(request):
    """ View function for displaying about page of site. """
    context = {}
    return render(request, 'pages/about.html')

def turbine_data_page(request):
    """ View function for displaying data page of site. """
    context = {}
    return render(request, 'pages/turbine-data/data.html')

def turbine1(request):
	""" View function for displaying data page of site. """
	if request.user.is_authenticated:
		return render(request, 'pages/turbine-data/turbine1.html')
	else:
		raise PermissionDenied()

def turbine2(request):
	""" View function for displaying data page of site. """
	if request.user.is_authenticated:
		return render(request, 'pages/turbine-data/turbine2.html')
	else:
		raise PermissionDenied()

def turbine3(request):
	""" View function for displaying data page of site. """
	if request.user.is_authenticated:
		return render(request, 'pages/turbine-data/turbine3.html')
	else:
		raise PermissionDenied()

def turbine4(request):
	""" View function for displaying data page of site. """
	if request.user.is_authenticated:
		return render(request, 'pages/turbine-data/turbine4.html')
	else:
		raise PermissionDenied()
	
def submissions_list(request):
    submissions = ContactSubmission.objects.all().order_by('-submitted_at')
    return render(request, "pages/submissions_list.html", {'submissions': submissions})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			ContactSubmission.objects.create(
				full_name=form.cleaned_data.get('full_name'),
				email=form.cleaned_data.get('email'),
				phone_number=form.cleaned_data.get('phone_number'),
				subject=form.cleaned_data.get('subject'),
				message=form.cleaned_data.get('message')
			)
			
			subject = f"Inquiry: {form.cleaned_data.get('subject')}"
			body = {
				'full_name': form.cleaned_data.get('full_name'), 
				'email': form.cleaned_data.get('email'), 
				'phone_number': str(form.cleaned_data.get('phone_number')), 
				'message': form.cleaned_data.get('message')
			}
			message = "\n".join(body.values())
			try:
				messages.success(request, "Email successfully sent!")
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
				
			except BadHeaderError:
				messages.error(request, "Unable to send email. Please try again later.")
			return redirect("main:index")
		messages.info(request, f"Could not send email: {form.errors.as_text().split('*')[2]}")
	form = ContactForm()
	return render(request, "pages/contact.html", {'contact_form': form})

def contact_support(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = ContactSupportForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()

				subject = f"Support: {form.cleaned_data.get('subject')}"
				body = {
					'username': form.cleaned_data.get('username'), 
					'email': form.cleaned_data.get('email'),
					'message': form.cleaned_data.get('message'),
					'file': str(form.cleaned_data.get('file_upload'))
				}
				message = "\n".join(body.values())
				try:
					messages.success(request, "Email successfully sent!")
					send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
				except BadHeaderError:
					messages.error(request, "Unable to send email. Please try again later.")
				return redirect("main:contact_submissions")
			else:
				messages.error(request, "Form is invalid, please check the fields.")

		form = ContactSupportForm()
		return render(request, "admin-portal-pages/support.html", {'contact_support_form': form})
	else:
		raise PermissionDenied()

def admin_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Welcome, {username}!")
				if user.is_staff:
					return redirect("main:admin_panel")
				else:
					return redirect("main:index")
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request=request, template_name="pages/login.html", context={"login_form":form})

def admin_logout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:index")

def admin_register(request):
	if request.method == "POST":
		form = NewAdminForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewAdminForm()
	return render (request=request, template_name="pages/register.html", context={"register_form":form})

def admin_panel(request):
	""" View function for displaying admin portal page of site. """
	if request.user.is_authenticated and request.user.is_staff:
		return render(request, 'admin-portal-pages/admin_panel.html')
	else:
		raise PermissionDenied()

def dashboard(request):
	""" View function for displaying dashboard page of site. """
	if request.user.is_authenticated and request.user.is_staff:
		submissions = ContactSubmission.objects.all()
		users = User.objects.all().values()
		return render(request, 'admin-portal-pages/dashboard.html', {"submissions": submissions, "users": users})
	else:
		raise PermissionDenied()

def contact_submissions(request):
	if request.user.is_authenticated and request.user.is_staff:
		submissions = ContactSubmission.objects.all()
		return render(request, 'admin-portal-pages/contact_submissions.html', {'submissions': submissions})
	else:
		raise PermissionDenied()

def registered_users(request):
	""" View function for displaying contact support page of site. """
	if request.user.is_authenticated and request.user.is_staff:
		users = User.objects.all().values()
		return render(request, 'admin-portal-pages/registered_users.html', {'users': users})
	else:
		raise PermissionDenied()

def error_400(request,  exception):
	return render(request,'errors/400.html', status=400, data={})

def error_404(request, exception):
	return render(request,'errors/404.html', status=404)

def error_403(request, exception):
	return render(request,'errors/403.html', status=403)

def error_500(request,  *args, **argv):
	return render(request, 'errors/500.html', status=500, data={})
