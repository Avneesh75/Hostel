# Generated by Django 4.0 on 2022-03-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_adminstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Roll',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]