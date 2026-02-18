from django.db import models

class Price(models.Model):
    """Модель для хранения цен на позиции меню"""
    item_name = models.CharField('Название позиции', max_length=200, unique=True)
    price = models.IntegerField('Цена')
    
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ['item_name']
    
    def __str__(self):
        return f"{self.item_name} - {self.price}₽"