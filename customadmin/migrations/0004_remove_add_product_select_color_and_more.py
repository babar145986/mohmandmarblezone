# Generated by Django 4.1.5 on 2023-02-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0003_add_end_category_select_top_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_product',
            name='select_color',
        ),
        migrations.RemoveField(
            model_name='add_product',
            name='select_size',
        ),
        migrations.AddField(
            model_name='add_product',
            name='select_color',
            field=models.ManyToManyField(blank=True, null=True, to='customadmin.add_color'),
        ),
        migrations.AddField(
            model_name='add_product',
            name='select_size',
            field=models.ManyToManyField(blank=True, null=True, to='customadmin.add_size'),
        ),
    ]