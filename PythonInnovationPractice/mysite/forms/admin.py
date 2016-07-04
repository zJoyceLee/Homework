from django.contrib import admin

# Register your models here.
from .models import Form, Field

import xlwt
import sqlite3

def export2excel(modeladmin, request, queryset):
    form = queryset.all()[0]
    print(type(form), form)
    fields = form.field_set.all()
    try:
        db = sqlite3.connect("./db.sqlite3")
        cursor = db.cursor()

        ss = """
        SELECT DISTINCT(field_text)
        FROM forms_field
        WHERE
            form_id = (SELECT id FROM forms_form WHERE form_text = '{}');
        """.format(str(form))
        cursor.execute(ss)
        results = cursor.fetchall()
        fields = [tmp[0] for tmp in results]
        counter = len(fields)

        ss = """
        SELECT id, answer
        FROM forms_field
        WHERE
            form_id = (SELECT id FROM forms_form WHERE form_text = '{}')
        ORDER BY 1;""".format(str(form))
        cursor.execute(ss)
        results = cursor.fetchall()
        print(results)
        wb = xlwt.Workbook()
        ws = wb.add_sheet('{} Sheet'.format(str(form)))
        for i in range(counter):
            ws.write(0, i % counter, '{}'.format(fields[i]))
            print(0, i % counter, '{}'.format(fields[i]))
        for i, result in enumerate(results):
            print(int(i / counter) + 1, i % counter, '{}'.format(result[1]))
            ws.write(int(i / counter) + 1, i % counter, '{}'.format(result[1]))

        wb.save('{}.xls'.format(str(form)))

    except:
        print('Database: Error.')
    finally:
        db.close()

export2excel.short_description = "Export form to Excel"

# class FieldInline(admin.TabularInline):
class FieldInline(admin.TabularInline):
    model = Field
    extra = 3

class FormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['form_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})
    ]
    inlines = [FieldInline]
    list_display = ('form_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['form_text']
    actions = [export2excel]


admin.site.register(Form, FormAdmin)
