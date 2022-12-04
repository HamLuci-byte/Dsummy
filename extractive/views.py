from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Form, Formm, URLForm, DataForm, ContactForm

from gensim.summarization import summarize
from .tfidf_summarization import tfidf_sum
from .nltk_summarization import nltk_summarizer
from .text_rank import TextRankSummarizer


#from .scraping import get_text



from bs4 import BeautifulSoup
from urllib.request import urlopen

from rake_nltk import Rake

from.models import Blog, Contact



#def get_text(raw_text):
#   page = urlopen(raw_text)
#	soup = BeautifulSoup(page)
#	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
#   return fetched_text

# Create your views here.

def index(request):
    text = 'No search query'
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            pc = form.cleaned_data.get('info')


            result = tfidf_sum(text, pc)
            return render(request, 'SimpleSummary.html', {'result':result, 'percent':pc})

    my_form = ContactForm()
    if request.method == "POST":
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            Contact.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
        my_form = ContactForm()
        blogs = Blog.objects.all()
        context = {
            "form":my_form,
            "blogs":blogs
        }
        return render(request,"index.html",context)


    blogs = Blog.objects.all()
    return render(request,"index.html",{'blogs':blogs})
    


def compare(request):
    text = 'No search query'
    percent = 40
    if request.method == 'POST':
        form = Formm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            genresult = summarize(text)
            tfresult = tfidf_sum(text, percent)
            nltkresult = nltk_summarizer(text)
            
            tr = TextRankSummarizer(6)
            trresult = tr(text)
            
            return render(request, 'compare.html', {'tfresult':tfresult, 'genresult':genresult, 'nltkresult':nltkresult, 'trresult':trresult})
    return render(request, "compare.html")

    
def scrap(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            page = urlopen(url)
            soup = BeautifulSoup(page)
            fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            return render(request, 'scrap.html', {'data':fetched_text})
    percent = 40
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('data')
            urlresult = tfidf_sum(data, percent)
            #genresult = summarize(data)
            return render(request, 'SimpleSummary.html', {'urlresult':urlresult})
    return render(request, "scrap.html")


#def blog(request):
   #return render(request, "single.html")
   
# Dynamic URL routing
def bloglookup(request, my_id):
    obj = Blog.objects.get(id = my_id)
    context = {
        "object":obj
    }
    return render(request, "single.html", context)


    
    


    
    
    
        
        
            
            
	        
	        
            
    
    





  



