# Generated by Django 4.0 on 2022-03-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'PENDING')], default=2),
        ),
        migrations.AddField(
            model_name='booking',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(1, 'Room Book'), (2, 'Room Not Available')], default=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
