# Generated by Django 4.2 on 2023-04-27 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('appliances', 'Appliances'), ('clothes', 'Clothes'), ('education', 'Education'), ('electronics', 'Electronics'), ('free', 'Free'), ('homeandgarden', 'Home & Garden'), ('miscellaneous', 'Miscellaneous'), ('music', 'Music'), ('sports', 'Sports'), ('vehicles', 'Vehicles')], default='miscellaneous', max_length=20),
        ),
    ]
