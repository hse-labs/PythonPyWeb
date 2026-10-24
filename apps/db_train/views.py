from django.shortcuts import render
from django.views import View
from django.db.models import Q, Max, Min, Avg, Count
from .models import Author, AuthorProfile, Entry, Tag

class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        max_entries = Author.objects.annotate(count=Count('entries')).aggregate(max_count=Max('count'))
        self.answer2 = Author.objects.annotate(count=Count('entries')).filter(count=max_entries['max_count']).first()

        self.answer3 = Entry.objects.filter(Q(tags__name='Кино') | Q(tags__name='Музыка')).distinct()

        self.answer4 = Author.objects.filter(gender='ж').count()

        total = Author.objects.count()
        agreed = Author.objects.filter(status_rule=True).count()
        self.answer5 = round(agreed / total * 100, 1) if total > 0 else 0

        self.answer6 = Author.objects.filter(authorprofile__stage__gte=1, authorprofile__stage__lte=5)

        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = Author.objects.filter(age=max_age['max_age']).first()

        self.answer8 = Author.objects.filter(phone_number__isnull=False).exclude(phone_number='').count()

        self.answer9 = Author.objects.filter(age__lt=25)

        self.answer10 = Author.objects.annotate(count=Count('entries')).filter(count__gt=0).values('username', 'count')

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}
        return render(request, 'train_db/training_db.html', context=context)
