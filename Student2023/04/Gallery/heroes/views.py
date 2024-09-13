from pathlib import Path
from django.views.generic import TemplateView

herolist = [
    {"id" : 0, "Name" : "Richard Nixon", "Strengths" : "Cool new advancements in electronics, swagger", "Weaknesses" : "Canada, The TRUTH", "Image" : "/static/images/1.webp"},
    {"id" : 1, "Name" : "Peter Griffin", "Strengths" : "Middle class income, strong support system", "Weaknesses" : "Alcoholism, His Wife", "Image" : "/static/images/2.png"},
    {"id" : 2, "Name" : "Howard Hughes", "Strengths" : "Absolutely decimating a steak, staying in a movie theatre for 4 months", "Weaknesses" : "OCD, Planes", "Image" : "/static/images/3.jpg"}
]

def photo_list():
    def photo_details(i, f):
        return dict(id=i, file=f)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        
        return herolist[i]

        #return dict(photo=p)
