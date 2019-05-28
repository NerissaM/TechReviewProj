from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'ClubApp/index.html')

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'ClubApp/resources.html', {'resource_list' : resource_list})
    
def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'ClubApp/meeting.html', {'meeting_list' : meeting_list})

def meetingdetail (request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render(request, 'ClubApp/meetingdetail.html', context=context)

def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()

    else: 
            form=ResourceForm()
    return render(request, 'ClubApp/newresource.html', {'form' : form})

def loginmessage(request):
    return render(request, 'ClubApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'ClubApp/logoutmessage.html')

@login_required
def newResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'ClubApp/newresource.html', {'form': form})