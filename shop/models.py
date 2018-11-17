import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='', blank=True)
    price = models.FloatField()
    currency = models.CharField(max_length=3, default='RUB')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return "%s (%s)" % (self.name, self.price)


class Rest(models.Model):
    class Meta:
        unique_together = (('store', 'item'),)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return "%s - %s (%s)" % (self.item.name, self.store.name, self.count)


class Client(models.Model):
    tg_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return "Client: %s" % self.tg_id


class Request(models.Model):
    def generate_code(self):
        today = datetime.date.today()
        day = today.strftime('%d')
        month = today.strftime('%m')
        year = today.strftime('%Y')[-1]
        return "%s%s%s%s" % (day, month, self.pk, year)

    code = models.CharField(max_length=10, default=generate_code)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    purchase_time = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%s)[%s]" % (self.item.name, self.count, self.store.name)
