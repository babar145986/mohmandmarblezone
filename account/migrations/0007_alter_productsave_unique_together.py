# Generated by Django 4.1.5 on 2023-02-10 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0002_alter_add_color_options_alter_add_country_options_and_more'),
        ('account', '0006_productsave'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productsave',
            unique_together={('name', 'product')},
        ),
    ]