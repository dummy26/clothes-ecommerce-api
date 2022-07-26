# Generated by Django 4.0.6 on 2022-07-23 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_alter_cloth_retail_price_alter_cloth_sell_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.cloth')),
            ],
        ),
    ]