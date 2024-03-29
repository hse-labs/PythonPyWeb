import django
import os
import datetime
import pprint
from django.db.models import Count, Max, Min, Sum, F, Value, Subquery, Window
from django.db.models import Avg, Q, StdDev, Variance
from django.db import connection
from django.db.models import Case, When, BooleanField, CharField

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # obj = Entry.objects.filter(author__name__contains='author')
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)

    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))
    # print(Entry.objects.filter(headline__contains='мод'))
    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    # print(Entry.objects.filter(number_of_comments__in='123'))
    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)
    # print(Entry.objects.filter(number_of_comments__gt=10))
    # print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    # print(Entry.objects.filter(headline__lte='Зя'))
    # print(Entry.objects.filter(headline__startswith='Как'))
    # print(Entry.objects.filter(headline__endswith='ния'))
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    # print(Entry.objects.filter(pub_date__range=(start_date, end_date)))
    # print(Entry.objects.filter(pub_date__year=2023))
    # print(Entry.objects.filter(pub_date__year__lt=2022))
    # print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(
    # pub_date__day__lte=15).values_list("author__name").distinct())
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))
    # print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))
    # print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))
    # print(Entry.objects.filter(pub_date__time=datetime.time(12, 00)))
    # print(Entry.objects.filter(pub_date__time__range=(datetime.time(6), datetime.time(17))))
    # print(AuthorProfile.objects.filter(city__isnull=True))
    # print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())
    # all_obj = Blog.objects.all()
    # print("Вывод всех значений в таблице Blog\n", all_obj)
    # all_obj = Blog.objects.all()
    # obj_first = all_obj.first()
    # obj_last = all_obj.last()
    # print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
    #      f"Все значения = {all_obj}")
    # print(f'{obj_last}')
    # all_obj = Blog.objects.all()
    # for idx, value in enumerate(all_obj):
    #        print(f"idx = {idx}, value = {value}")
    #    print(all_obj[0])  # Получение 0-го элемента
    #    print(all_obj[2:4])  # Получение 2 и 3 элемента
    # print(Blog.objects.exclude(id__gte=2))
    # try:
    #   Blog.objects.get(id=2, name="Путешествия по миру")
    # except Blog.DoesNotExist:
    #   print("Не существует")
    # print(Blog.objects.filter(id=1, name="Путешествия по миру").exists())
    # f_data = Blog.objects.filter(id__gte=2)
    # print(f_data.order_by('-name', '-id'))
    # entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
    # print(entry)
    # blogs = Blog.objects.alias(number_of_entries=Count('entries')).filter(number_of_entries__gt=4)
    # print(blogs)
    # blogs = Blog.objects.alias(number_of_entries_new=Count('entries')).filter(number_of_entries__gt=4).values('blog', 'entries_new')
    # average_rating = Entry.objects.aggregate(
    #   average_rating1=Avg('rating', distinct=True))
    # print(average_rating)
    # average_rating_with_default = Entry.objects.aggregate(
    #        average_rating2=Avg('rating', default=5.0))
    #   print(average_rating_with_default)
    # average_rating = Entry.objects.aggregate(
    #   average_rating3=Avg('rating', filter=Q(pub_date__year__gt=2023)))
    # print(average_rating)
    #    count_authors = Entry.objects.aggregate(
    #        count_authors=Count('author', distinct=True))
    # print(count_authors)
    # entries_with_tags_count = Entry.objects.annotate(
    #        tag_count=Count('tags')).values('id', 'tag_count')
    #    print(entries_with_tags_count)
    #    calc_rating = Entry.objects.aggregate(
    #        max_rating=Max('rating'), min_rating=Min('rating'), avg_rating=Avg('rating'))
    # print(calc_rating)
    #    calc_rating = Entry.objects.aggregate(
    #        std_rating=StdDev('rating'), var_rating=Variance('rating'))
    # print(calc_rating)
    #    calc_rating = Entry.objects.aggregate(
    #        sum_comments=Sum('number_of_comments'))
    # print(calc_rating)
    # filtered_data = Blog.objects.filter(id__gte=2)#.order_by("id")
    # print(filtered_data)
    # print(filtered_data.reverse())
    # print(Entry.objects.order_by('author', 'pub_date').distinct('author', 'pub_date'))
    # print(Blog.objects.filter(name__startswith='Фитнес').values())
    # items = Blog.objects.values('id','name')
    # for _ in items:
    #        print(_)
    # print(Blog.objects.values_list('id', 'name'))
    # blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру')
    # blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения')
    # blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни')
    # result_qs = blog_a_entries.union(blog_b_entries, blog_c_entries)
    # qs_1 = Entry.objects.filter(blog__name__in=['Путешествия по миру', 'Кулинарные искушения', 'Фитнес и здоровый образ жизни'])
    # blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру').values('author')
    # blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения').values('author')
    # blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни').values('author')
    # qs_1 = blog_a_entries.intersection(blog_b_entries, blog_c_entries)
    # print(qs_1)
    # blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру').values('author')
    # blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения').values('author')
    # blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни').values('author')
    # result_qs = Entry.objects.values('author').difference(blog_a_entries, blog_b_entries, blog_c_entries)
    # print(result_qs)
    # print(Author.objects.filter(entries__author=None))
    # entry = Entry.objects.select_related('blog').get(id=5)
    # blog = entry.blog
    # print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    # print('Результатзапроса = ', blog)
    # entry = Entry.objects.all()
    # print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    # for row in entry:
    #    tags = [tag.name for tag in row.tags.all()]
    #    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    #    print('Результат запроса = ', tags)
    # entry = Entry.objects.prefetch_related("tags")
    # for row in entry:
    #    tags = [tag.name for tag in row.tags.all()]
    #    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    #    print('Результат запроса = ', tags)
    # print(Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks')).values('id',
    #                                                                                  'number_of_comments',
    #                                                                                  'number_of_pingbacks'))
    # print(Entry.objects.annotate(sum_number=F('number_of_pingbacks') + F('number_of_comments')).values('id',
    #                                                                                                   'number_of_comments',
    #                                                                                                   'number_of_pingbacks',
    # print(Entry.objects.alias(sum_number=F('number_of_pingbacks') + F('number_of_comments')).
    #      annotate(val1=F('sum_number') / F('number_of_comments')).values('id',
    #                                                                      'number_of_comments',
    #                                                                      'number_of_pingbacks',
    #                                                                      'val1'))
    # entries = Entry.objects.filter(
    #    Q(headline__icontains='тайны') | Q(body_text__icontains='город'))
    # print(entries)
    # entries = Entry.objects.filter(
    #    Q(blog__name='Путешествия по миру') & Q(pub_date__date__range=(datetime.date(2022, 5, 1),datetime.date(2023, 5, 1))))
    # pr1int(entries)
    # entries = Entry.objects.filter(Q(rating__gt=4) | Q(number_of_comments__lt=10))
    # print(entries)
    # entries = Entry.objects.annotate(
    #    is_popular=Case(
    #        When(rating__gte=4, then=True),
    #        default=False,
    #        output_field=BooleanField())
    # ).values('id', 'rating', 'is_popular')
    # print(entries)
    #entries = Entry.objects.annotate(
    #    count_tags=Count("tags"),
    #    tag_label=Case(
    #        When(count_tags__gte=3, then=Value('Много')),
    #        When(count_tags=2, then=Value('Средне')),
    #        default=Value('Мало'),
    #        output_field=CharField())
    #).values('id', 'count_tags', 'tag_label')
    #print(entries)
    #subquery = AuthorProfile.objects.filter(bio__isnull=True).values('author_id')

    # Фильтруем записи блога по авторам
    #query = Entry.objects.filter(author__in=Subquery(subquery))
    #print(query)
    #print(Entry.objects.filter(author__authorprofile__bio__isnull=True))
    #)

    # Выводим результаты
    #for result in results:
    #    print(result.id, result.headline)
    queryset = Entry.objects.annotate(
        avg_comments=Window(
            expression=Avg('number_of_comments'),
            partition_by=F('blog'),
        ),
        max_comments=Window(
            expression=Max('number_of_comments'),
            partition_by=F('blog'),
        ),
        min_comments=Window(
            expression=Min('number_of_comments'),
            partition_by=F('blog'),
        ),

    ).values('id', 'headline', 'avg_comments', 'max_comments', 'min_comments')
    for _ in queryset:
        print(_)
