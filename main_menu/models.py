from django.contrib.auth.models import User
from django.db import models


class RentSale(models.Model):
    TYPE_CHOICES = [
        ('R', 'Rent'),
        ('S', 'Sale'),
    ]

    PROVINCE_CHOICES = [
        ('ANTAL', 'Antalya')
    ]

    DISCTRICT_CHOICES = [
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
    district = models.CharField(max_length=4, choices=DISCTRICT_CHOICES, default='KEPE')
    address = models.CharField(max_length=40)
    owner = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    price_in_lira = models.IntegerField()
    created_data = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"""
        Тип объявления - {self.type}, Город - {self.city}, Район - {self.district}, Адрес - {self.address}, 
        Владелец - {self.owner}, Номер телефона - {self.phone_number}, Цена - {self.price_in_lira},
        Дата создания - {self.created_data}, Описание: {self.description}
        """


class Picture(models.Model):
    image = models.ImageField(upload_to='images/')
    rentsale = models.ForeignKey(RentSale, on_delete=models.CASCADE, null=True, related_name='pictures')
#

# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     rentsale = models.ForeignKey(RentSale, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return f"{self.image}"
