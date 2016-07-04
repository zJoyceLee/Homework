from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Form, Field
from django.views import generic

from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

import sqlite3

def save2db(ss):
    try:
        db = sqlite3.connect("./db.sqlite3")
        cursor = db.cursor()
        cursor.execute(ss)
        results = cursor.fetchall()
        for row in results:
            print(row)
        db.commit()
    except:
        db.rollback()
        print("database: something error.")
    finally:
        db.close()

class IndexView(generic.ListView):
    template_name = 'forms/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Form.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Form
    template_name = 'forms/detail.html'
    def get_queryset(self):
        return Form.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Form
    template_name = 'forms/results.html'

@csrf_exempt
def fill(request, question_id):
    form = get_object_or_404(Form, pk=question_id) # value: Test
    try:
        fields = form.field_set.all()
        print(fields)
        for i, field in enumerate(fields) :
            if i < 4:
                key = '{}'.format(field)
                value = request.POST.get(key)
                if value == '':
                    return render(request, 'forms/detail.html', {
                        'form': form,
                        'error_message': "Didn't fill in."
                    })
                else:
                    print(key, ':', value)
                    ss = """
                    INSERT INTO forms_field(field_text, answer, form_id) VALUES
                    ('{0}', '{1}', {2});
                    """.format(key, value, question_id)
                    save2db(ss)
    except (KeyError, Field.DoesNotExist):
        print('Some Error')
        return render(request, 'forms/detail.html', {
            'form': form,
            'error_message': "Didn't fill in."
        })
    else:
        print('hi, this is else.')
        return HttpResponseRedirect(reverse('forms:results', args=(form.id,)))
