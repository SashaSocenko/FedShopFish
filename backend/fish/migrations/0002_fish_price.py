# Generated by Django 3.0.7 on 2020-06-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='price',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
