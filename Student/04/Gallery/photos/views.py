from pathlib import Path
from django.views.generic import TemplateView

heroes = {
    # Name, Strengths, Weaknesses
    1 : ["Richard Nixon", "Cool new advancements in electronics, swagger", "Canada, The TRUTH"],
    2 : ["Peter Griffin", "Middle class income, strong support system", "Alcoholism, His Wife"],
    3 : ["Howard Hughes", "Absolutely decimating a steak, staying in a movie theatre for 4 months", "OCD, Planes"]
}

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
        return dict(photo=p)
