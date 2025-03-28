from django.utils.html import format_html
from django.db import models

import uuid
import jdatetime
import pytz


def to_shamsi(datetime):
    tehran_tz = pytz.timezone('Asia/Tehran')
    datetime_utc = datetime.replace(tzinfo=pytz.utc)
    datetime_tehran = datetime_utc.astimezone(tehran_tz)
    return jdatetime.datetime.fromgregorian(date=datetime_tehran).strftime('%Y/%m/%d %H:%M:%S')


class Poem(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(unique=True)
    poem = models.TextField()
    interpretation = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'poems'

    def __str__(self): return str(self.number)

    def created_at_shamsi(self): return to_shamsi(self.created_at)
    created_at_shamsi.short_description = "created at"

    def updated_at_shamsi(self): return to_shamsi(self.updated_at)
    updated_at_shamsi.short_description = "updated at"

    def poem_detail(self):
        detail_icon = '<span class="material-symbols-outlined text-sm">Edit_square</span>'
        return format_html(f"<a href='/admin/poem/poem/{self.uuid}/change/' target='_self'>{detail_icon}</a>")
    poem_detail.short_description = "Edit"
