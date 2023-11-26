from django.shortcuts import render, redirect
from . forms import CreateContactForm
from django.core.mail import send_mail
from django.conf import settings
from threading import Thread


def front(request):
    # all_products = Product.objects.all()
    # context = {'my_products':all_products}
    return render(request, 'front/front.html')


def contact_us(request):

    form = CreateContactForm()

    if request.method == 'POST':

        form = CreateContactForm(request.POST)

        if form.is_valid():

            contact = form.save()
            contact.save()

            # Email message confirmation

            email1 = [
                'MottaDev, Contact form:automated response',
                'Hi!' + '\n\n' + 'We appreciate you getting in touch with Us.' + '\n' +
                'We will answer your message as soon as possible,' +
                '\n' + 'have a wonderful day,' + '\n\n' +
                'Jaime Motta' + '\n' + 'jmottadev@gmail.com' +
                '\n' + 'Sapporo, Japan',
                [contact.email]
            ]
            t1 = Thread(target=loc_send_email, args=email1)
            t1.start()

            # contact information
            email2 = ['MottaDev, New Contact from ' + contact.email,
                'You have a new message! ' + '\n\n' +
                'Name: ' + contact.name + '\n' +
                'email: ' + contact.email + '\n' +
                'Message: ' + contact.textMessage + '\n\n' +
                'Phone Number:  ' + contact.phone + '\n' +
                'Location: ' + contact.location + '\n\n' +

                'have a wonderful day,' + '\n\n' +
                'MottaDev Front' + '\n' +
                'mottadev.pythonanywhere.com',
                ['jmottadev@gmail.com']
            ]
            t2 = Thread(target=loc_send_email, args=email2)
            t2.start()



            return redirect('front')

    context = {'form': form}

    return render(request, 'front/contact-us-form.html', context=context)


def loc_send_email(subject, content, target):
    send_mail(
        subject,
        content,
        settings.EMAIL_HOST_USER,
        target,
        fail_silently=False, )