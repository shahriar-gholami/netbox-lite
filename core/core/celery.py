from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیمات دایجنگو برای celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# پیکربندی با تنظیمات دایجنگو
app.config_from_object('django.conf:settings', namespace='CELERY')

# خودکار taskها را از اپ‌ها لود می‌کند
app.autodiscover_tasks()
