from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    price = models.PositiveIntegerField(verbose_name = 'Цена')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self) -> str:
        return self.title
    
class Meta:
    verbose_name = "Товар"
    verbose_name_plural = "Товары"
