# Generated by Django 4.1.5 on 2023-02-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0004_remove_add_product_select_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='select_color',
            field=models.ManyToManyField(blank=True, to='customadmin.add_color'),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='select_size',
            field=models.ManyToManyField(blank=True, to='customadmin.add_size'),
        ),
    ]
