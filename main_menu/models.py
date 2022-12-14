from django.core.validators import MinLengthValidator
from django.db import models


class RentSale(models.Model):
    TYPE_CHOICES = [
        ('R', 'Rent'),
        ('S', 'Sale'),
    ]

    PROVINCE_CHOICES = [
        ('ANTAL', 'Antalya')
    ]

    DISTRICT_CHOICES = [
        ('ASKE', 'Akseki'),
        ('AKSU', 'Aksu'),
        ('ALAN', 'Alanya'),
        ('DEMR', 'Demre'),
        ('DESH', 'Döşemealtı'),
        ('ELMA', 'Elmalı'),
        ('FINI', 'Finike'),
        ('GAZI', 'Gazipaşa'),
        ('GUND', 'Gündoğmuş'),
        ('IBRA', 'İbradı'),
        ('KASH', 'Kaş'),
        ('KEME', 'Kemer'),
        ('KEPE', 'Kepez'),
        ('KORK', 'Korkuteli'),
        ('KONY', 'Konyaaltı'),
        ('KUML', 'Kumluca'),
        ('MANA', 'Manavgat'),
        ('MURA', 'Muratpaşa'),
        ('SERI', 'Serik')
    ]

    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='R')
    city = models.CharField(max_length=5, choices=PROVINCE_CHOICES, default='ANTAL')
    district = models.CharField(max_length=4, choices=DISTRICT_CHOICES, default='KEPE')
    address = models.CharField(max_length=40)
    room = models.IntegerField()
    floor = models.IntegerField()
    square = models.FloatField()
    owner = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    price_in_lira = models.IntegerField()
    created_data = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return (f'Тип объявления: {self.type}, '
                f'Адрес: {self.address}, '
                f'Владелец: {self.owner}, Номер телефона: {self.phone_number}, '
                f'Цена: {self.price_in_lira}, '
                f'Дата создания: {self.created_data}, Дата обновления: {self.updated_time}')


class Picture(models.Model):
    image = models.ImageField(upload_to='images/')
    rentsale = models.ForeignKey(RentSale, on_delete=models.CASCADE, null=True, related_name='pictures')


class ClientRequest(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(4)], help_text='Input your name')
    phone = models.IntegerField(help_text='Phone number')
    email = models.EmailField(max_length=254, blank=True, null=True, help_text='Your email (optional)')
    message = models.TextField(blank=True, null=True, help_text='Your message')

    def __str__(self):
        return (f'Имя: {self.name}; '
                f'Телефон: {self.phone}; '
                f'Сообщение: {self.message}')
