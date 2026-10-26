import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    print("1. Поиск по полю: author__name__contains")
    obj = Entry.objects.filter(author__name__contains='author')
    print(obj)

    print("\n2. Косвенная связь: автор без города")
    obj = Entry.objects.filter(author__authorprofile__city=None)
    print(obj)

    print("\n3. exact, iexact")
    print(Entry.objects.get(id__exact=4))
    print(Blog.objects.get(name__iexact="Путешествия по миру"))

    print("\n4. contains")
    print(Entry.objects.filter(headline__contains='мод'))

    print("\n5. in")
    print(Entry.objects.filter(id__in=[1, 3, 4]))

    print("\n6. gt, lt")
    print(Entry.objects.filter(number_of_comments__gt=10))

    print("\n7. startswith, endswith")
    print(Entry.objects.filter(headline__startswith='Как'))
    print(Entry.objects.filter(headline__endswith='ния'))













