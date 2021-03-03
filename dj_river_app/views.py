from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sample(request):
    return HttpResponse(' Django River Example')



# django river
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect

from river.models import State

from dj_river_app.models import Ticket


def approve_ticket(request, ticket_id, next_state_id=None):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    next_state = get_object_or_404(State, pk=next_state_id)

    try:
        ticket.river.status.approve(as_user=request.user, next_state=next_state)
        return redirect(reverse('admin:dj_river_app_ticket_changelist'))
    except Exception as e:
        return HttpResponse(e.message)
