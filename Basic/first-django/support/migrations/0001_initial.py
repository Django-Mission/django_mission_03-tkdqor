# Generated by Django 4.0.3 on 2022-04-15 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('NORMAL', '일반'), ('ACCOUNT', '계정'), ('ETC', '기타')], default='NORMAL', max_length=10)),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor_faq', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer_faq', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
