# Generated by Django 4.2.3 on 2023-07-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(default='email_address', max_length=300),
        ),
    ]
