# Generated by Django 4.2.1 on 2023-05-25 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ('name',), 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
    ]
