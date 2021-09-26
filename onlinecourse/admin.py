from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 1

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inline = [ChoiceInLine]
    list_display = ['course', 'content', 'grade']
    list_filter = ['course']
    search_fields = ['content']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'content', 'is_correct']
    list_filter = ['question']
    search_fields = ['content']

# <HINT> Register Question and Choice models here
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
