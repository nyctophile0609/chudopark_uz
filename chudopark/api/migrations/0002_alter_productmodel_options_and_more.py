# Generated by Django 5.1.2 on 2024-10-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='productsubsetmodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='productsubsetmodel',
            name='products',
            field=models.ManyToManyField(blank=True, to='api.productmodel'),
        ),
    ]
