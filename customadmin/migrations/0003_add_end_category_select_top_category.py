# Generated by Django 4.1.5 on 2023-02-11 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0002_alter_add_color_options_alter_add_country_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_end_category',
            name='select_top_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customadmin.add_top_category'),
        ),
    ]
