from django.contrib import admin

from courses.models import (Courses, LearnRecored)


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'image','description',
        'created_time', 'views', 'likes', 'owner',
        'is_active',
    )

admin.site.register(Courses, CoursesAdmin)
admin.site.register(LearnRecored)

