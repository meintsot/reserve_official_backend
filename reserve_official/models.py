from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name="name")
    city = models.CharField(max_length=256, null=False, blank=False, verbose_name="city")
    store_type = models.IntegerField(null=False, blank=False, default=1, verbose_name="store_type")
    attachment_id = models.IntegerField(null=False, blank=False, verbose_name="attachment_id")
    stars = models.DecimalField(max_digits=6, decimal_places=5, default=0, null=False, blank=False, verbose_name="stars")
    stars_count = models.IntegerField(default=0, null=False, blank=False, verbose_name="stars_count")

    class Meta:
        db_table = "COMPANY"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    has_parties = models.BooleanField(default=False, null=False, blank=False, verbose_name="has_parties")
    has_deals = models.BooleanField(default=False, null=False, blank=False, verbose_name="has_deals")
    minimum_reservation_price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="minimum_reservation_price")
    minimum_reservation_persons = models.IntegerField(null=False, blank=False, verbose_name="minimum_reservation_persons")
    is_open = models.BooleanField(default=False, null=False, blank=False, verbose_name="is_open")
    date = models.DateField(verbose_name="date", null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="company")

    class Meta:
        db_table = "SCHEDULE"

    def __str__(self):
        return str(self.date) + " - " + self.company.name


class Notification(models.Model):
    img = models.CharField(max_length=512, null=True, blank=True, verbose_name="img")
    title = models.CharField(max_length=256, null=False, blank=False, verbose_name="title")
    content = models.TextField(verbose_name="content", null=False, blank=False)
    type = models.CharField(choices=(('GENERAL', 'GENERAL'), ('STORE', 'STORE')), default='GENERAL', verbose_name='type', max_length=64)
    store_id = models.IntegerField(null=True, blank=True, verbose_name="store_id", default=0)
    time = models.DateTimeField(auto_now_add=True, verbose_name="time")

    class Meta:
        db_table = "NOTIFICATION"

    def __str__(self):
        return self.title


