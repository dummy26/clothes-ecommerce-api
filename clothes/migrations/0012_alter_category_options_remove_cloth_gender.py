# Generated by Django 4.0.6 on 2022-07-31 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0011_category_alter_cloth_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='gender',
        ),
    ]