# Generated by Django 4.0.3 on 2022-04-30 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_alter_inquiry_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='state',
            field=models.CharField(choices=[('REGISTER', '문의 등록'), ('RECEIPT', '접수 완료'), ('ANSWER', '답변 완료')], default='REGISTER', max_length=10, verbose_name='상태'),
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
