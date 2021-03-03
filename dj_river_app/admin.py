from django.contrib import admin
import river_admin


# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

from dj_river_app.models import Ticket

# here shows the river action functionality ie, what will happen after click on each button in the given actions
def create_river_button(obj, transition_approval):
    approve_ticket_url = reverse('approve_ticket', kwargs={'ticket_id': obj.pk, 'next_state_id': transition_approval.transition.destination_state.pk})
    return f"""
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.transition.source_state}  >>  {transition_approval.transition.destination_state}"
            onclick="location.href=\'{approve_ticket_url}\'"
        />
    """
class TicketAdmin(admin.ModelAdmin):
    list_display = ('no', 'subject', 'description', 'status', 'river_actions')

    def get_list_display(self, request):
        self.user = request.user
        return super(TicketAdmin, self).get_list_display(request)

    def river_actions(self, obj):
        content = ""
        for transition_approval in obj.river.status.get_available_approvals(as_user=self.user):# get_available_approvals :to fetch all available approvals waitiong for a specific user according to given source and destination states.
            content += create_river_button(obj, transition_approval)

        return mark_safe(content) #marksafe: mark a string as safe for output purpose.


admin.site.register(Ticket, TicketAdmin)

class TicketRiverAdmin(river_admin.RiverAdmin):
    name = "Django River Fakejira"
    # icon = "mdi-ticket-account"
    list_displays = ['pk', 'no', 'subject', 'description', 'status']
    

river_admin.site.register(Ticket, "status", TicketRiverAdmin)