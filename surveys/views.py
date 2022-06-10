from enum import unique

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
# Create your views here.
from django.views.generic import FormView
from surveys.forms import SurveyForm
from collections import Counter
from scipy.io import wavfile
from surveys.models import Survey
import numpy as np
from scipy.fft import fft, ifft, fftfreq
import csv
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
    })
def authors(request):
    return render(request, 'authors.html', {
    })
class SurveyFillView(TemplateView, FormView):
    success_url = reverse_lazy('filled_success')
    template_name = "survey_form.html"

    def get_form_class(self):
        return SurveyForm

    def form_valid(self, form):
        form.instance.save()
        return super(SurveyFillView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(SurveyFillView, self).get_context_data(**kwargs)
        return context


class SurveyFilledView(TemplateView):
    template_name = "survey_filled.html"

    def get_context_data(self, **kwargs):
        context = super(SurveyFilledView, self).get_context_data(**kwargs)
        return context


def unique_counter(queryset,field_name):
    return Counter([getattr(i, field_name) for i in queryset])

class SurveyStatsView(TemplateView):
    template_name = "survey_stats.html"

    def get_context_data(self, **kwargs):
        context = super(SurveyStatsView, self).get_context_data(**kwargs)

        survey_answers = Survey.objects.all()
        context['unique_sample_string'] = unique_counter(survey_answers, 'sample_text')
        context['bool_distribution'] = unique_counter(survey_answers, 'sample_bool')
        context['total_count'] = survey_answers.count()
        return context


class WavFileDetailsView(TemplateView):
    template_name = "wav_details.html"

    def get_context_data(self, **kwargs):
        context = super(WavFileDetailsView, self).get_context_data(**kwargs)

        survey_answers = Survey.objects.get(pk = self.kwargs['wav_pk'])
        context['total_count'] = survey_answers

        samplerate, data = wavfile.read(survey_answers.wav_file.path)
        print(f'{samplerate:/^20}')
        flatten_data = [item for sublist in data for item in sublist if item % 10 == 0][0:1000]
        context['data'] = flatten_data
        context['data_labels'] = [round(i,2) for i in range(len(flatten_data))]
        context['mean'] = np.mean(flatten_data)
        context['std'] = np.std(flatten_data)

        # print("pgasgasg",samplerate)
        
        nparrrayyy = np.array(flatten_data)
        ## Perform FFT with SciPy
        signalFFT = fft(nparrrayyy)
        ## Get power spectral density
        signalPSD = np.abs(signalFFT) ** 2
        ## Get frequencies corresponding to signal PSD
        fftFreq = fftfreq(len(signalPSD), 1)
        ## Get positive half of frequencies
        i = fftFreq>0

        x=fftFreq[i].tolist()
        y = (10*np.log10(signalPSD[i])).tolist()

        N = nparrrayyy.shape[0]
        yf = fft(nparrrayyy)
        xf = fftfreq(N, 1/samplerate)[:N//2]

        context['data_labels_fft'] = np.around(xf, decimals=2).tolist()
        context['data_fft'] = (2.0/N * np.abs(yf[0:N//2])).tolist()

        print(context['data'][0:20])
        print(context['data_labels'][0:20])
        print("Shape0: ", nparrrayyy.shape)
        print()
        return context

class WavlistView(ListView):
    template_name = "wav_list.html"
    paginate_by = 2
    model = Survey
    
    def get_context_data(self, **kwargs):
        context = super(WavlistView, self).get_context_data(**kwargs)
        context['wavs'] = Survey.objects.all()

        return context

def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'wav_list.html', {'page_obj': page_obj})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['name'])

    for wave in iter(Survey.objects.all()):
        # print(wave)
        writer.writerow([wave.sample_text])

    response['Content-Disposition'] = 'attachment; filename="waves.csv"'
    return response