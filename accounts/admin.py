from django.contrib import admin
from accounts.models import User1


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('birth_date', 'start_weight', 'goal_weight', 'height')

    def user_info(self, obj):
        return obj.description

    user_info.short_description = 'Info'

admin.site.register(User1, UserProfileAdmin)

