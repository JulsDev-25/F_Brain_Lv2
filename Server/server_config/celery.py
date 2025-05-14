from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_config.settings')

app = Celery('server_config')

# Configuration de Celery avec RabbitMQ comme broker
app.config_from_object('django.conf:settings', namespace='CELERY')

# Chargement automatique des tâches
app.autodiscover_tasks()
