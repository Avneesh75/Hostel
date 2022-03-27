# Generated by Django 4.0 on 2022-03-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_adminstudent_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Aadhar_no',
        ),
        migrations.AddField(
            model_name='student',
            name='Aadhar_pic',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='student',
            name='Profile_pic',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Course',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=15, null=True),
        ),
    ]
