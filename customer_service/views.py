from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, CustomerAccount
from .forms import ServiceRequestForm


@login_required
def submit_service_request(request):
    customer_account, created = CustomerAccount.objects.get_or_create(
        user=request.user)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer_account
            service_request.save()
            return redirect('track_service_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_service_request.html', {'form': form})


@login_required
def track_service_requests(request):
    customer_account, created = CustomerAccount.objects.get_or_create(
        user=request.user)
    service_requests = ServiceRequest.objects.filter(customer=customer_account)
    return render(request, 'customer_service/track_service_requests.html', {'service_requests': service_requests})
