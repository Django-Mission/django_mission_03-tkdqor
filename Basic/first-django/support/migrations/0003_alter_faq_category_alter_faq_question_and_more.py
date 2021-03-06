# Generated by Django 4.0.3 on 2022-05-01 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_inquiry_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='category',
            field=models.CharField(choices=[('NORMAL', '일반'), ('ACCOUNT', '계정'), ('ETC', '기타')], default='NORMAL', max_length=10, verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='최종 수정 일시'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='category',
            field=models.CharField(choices=[('ORDER', '주문'), ('PAYMENT', '결제'), ('DELIVERY', '배송'), ('REFUND', '환불'), ('ACCOUNT', '계정'), ('ETC', '기타')], default='ETC', max_length=10, verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성 일시'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='title',
            field=models.CharField(max_length=200, verbose_name='질문 제목'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
    ]
