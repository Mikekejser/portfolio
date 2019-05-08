from django.shortcuts import render, get_object_or_404
from .models import Site
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def main(request):
	sites = Site.objects.all()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			navn = form.cleaned_data['navn']
			email = form.cleaned_data['email']
			besked = form.cleaned_data['besked']

			text = f'{navn}\n{email}\n{besked}'
			send_mail(
				'Email sendt via portfolio',
				text,
				settings.EMAIL_HOST_USER,
				[settings.MESSAGE_RECEIVER],
				fail_silently=False
			)

	else:
		form = ContactForm()
	return render(request, 'core/main.html', {'form': form, 'sites': sites})



def site(request, sitename):
	site = Site.objects.get(sitename=sitename)
	return render(request, 'core/site.html', {'site': site})
