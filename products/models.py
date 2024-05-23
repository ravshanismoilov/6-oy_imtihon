from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser


class CategoryBooks(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'categorybooks'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(to=CategoryBooks, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    page = models.IntegerField()
    price = models.IntegerField()
    book_lang = models.ForeignKey(to=Language, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='books/', default='default_user/default-book.jpg')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BookAuthor(models.Model):
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f'{self.book.title} {self.author.first_name} {self.author.last_name}'


class Review(models.Model):
    comment = models.CharField(max_length=200)
    star_given = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given} - {self.book.title} - {self.user.username}'

