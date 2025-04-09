from django.contrib import admin
from .models import Appointment
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('get_patient', 'get_doctor', 'appointment_type',
                    'appointment_status', 'symptom', 'time', 'cancel')

    def get_patient(self, obj):
        return obj.patient.user.first_name
    get_patient.short_description = 'Patient'

    def get_doctor(self, obj):
        return obj.doctor.user.first_name
    get_doctor.short_description = 'Doctor'

    list_filter = ('doctor', 'appointment_status')
    search_fields = ('patient__user__first_name',
                     'doctor__user__first_name', 'time')
    list_per_page = 10


admin.site.register(Appointment, AppointmentAdmin)
