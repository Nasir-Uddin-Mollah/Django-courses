from django.db import models
from datetime import timedelta
import uuid
# Create your models here.


class mymodel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField(default=timedelta(days=1))
    file_field = models.FileField(default=1)
    float_field = models.FloatField(default=1.1)
    image_field = models.ImageField(default='myimage')
    generic_ip_address_field = models.GenericIPAddressField(default='0.0.0.0', blank=True, null=True)
    integer_field = models.IntegerField(default=0)
    json_field = models.JSONField(default=dict, blank=True, null=True)
    null_boolean_field = models.BooleanField(null=True, blank=True)
    positive_big_integer_field = models.PositiveBigIntegerField(default=1)
    positive_integer_field = models.PositiveIntegerField(default=1)
    positive_small_integer_field = models.PositiveSmallIntegerField(default=1)
    small_integer_field = models.SmallIntegerField(default=0)
    slug_field = models.SlugField(default='', blank=True)
    url_field = models.URLField(default='', blank=True, null=True)
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.char_field