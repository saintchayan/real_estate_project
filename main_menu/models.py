from django.db import models


# Create your models here.
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
    #images = models.ImageField(height_field=500, width_field=700, max_length=10)

    def __str__(self):
        return f"""
        Тип объявления - {self.type}, Город - {self.city}, Район - {self.district}, Адрес - {self.address}, 
        Владелец - {self.owner}, Номер телефона - {self.phone_number}, Цена - {self.price_in_lira},
        Дата создания - {self.created_data}, Описание: {self.description}
        """
