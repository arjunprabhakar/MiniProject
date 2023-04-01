# Generated by Django 3.2.18 on 2023-03-31 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0010_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_review',
            name='negative_score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='tbl_review',
            name='neutral_score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='tbl_review',
            name='positive_score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
