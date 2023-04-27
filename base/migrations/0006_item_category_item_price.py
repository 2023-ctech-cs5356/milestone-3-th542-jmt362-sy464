# Generated by Django 4.2 on 2023-04-27 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.01, max_digits=15),
            preserve_default=False,
        ),
    ]