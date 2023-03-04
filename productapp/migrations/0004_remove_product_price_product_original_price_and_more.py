# Generated by Django 4.1.2 on 2023-03-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_alter_tbl_review_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='percentage',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
