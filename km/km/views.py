# views.py

from django.shortcuts import render, redirect
from .models import KeyPair, Message
from .forms import KeyPairForm, MessageForm

def keypair_list(request):
    keypairs = KeyPair.objects.all()
    return render(request, 'keypair_list.html', {'keypairs': keypairs})

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def create_keypair(request):
    if request.method == 'POST':
        form = KeyPairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('keypair_list')
    else:
        form = KeyPairForm()
    return render(request, 'create_keypair.html', {'form': form})

def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'create_message.html', {'form': form})
