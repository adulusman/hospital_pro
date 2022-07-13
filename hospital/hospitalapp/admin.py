from django.contrib import admin


from .models import *

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(District)
admin.site.register(SubBranches)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'phn', 'booking_date','doctor', 'booked_on')


admin.site.register(Booking,BookingAdmin)

