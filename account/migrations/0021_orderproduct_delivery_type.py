# Generated by Django 4.1.7 on 2023-02-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_orderproduct_issue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='delivery_type',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]