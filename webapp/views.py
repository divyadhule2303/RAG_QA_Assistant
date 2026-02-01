import os
from django.shortcuts import render
from django.conf import settings
from rag.pipeline import RAGPipeline

rag = RAGPipeline()

def home(request):

    answer = None
    sources = []

    if request.method == "POST":

        if request.FILES.getlist("files"):
            files = request.FILES.getlist("files")

            for file in files:
                path = os.path.join(settings.MEDIA_ROOT, file.name)
                with open(path, "wb+") as dest:
                    for chunk in file.chunks():
                        dest.write(chunk)

            rag.build_index()

        elif request.POST.get("question"):
            question = request.POST.get("question")
            answer, sources = rag.query(question)

    return render(request, "index.html", {
        "answer": answer,
        "sources": sources
    })
