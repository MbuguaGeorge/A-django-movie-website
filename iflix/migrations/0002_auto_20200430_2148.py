# Generated by Django 3.0.5 on 2020-04-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]