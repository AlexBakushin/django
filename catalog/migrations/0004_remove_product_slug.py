# Generated by Django 4.2.7 on 2023-12-03 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_slug_alter_product_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
