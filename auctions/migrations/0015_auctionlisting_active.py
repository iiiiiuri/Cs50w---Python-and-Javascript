# Generated by Django 4.2.7 on 2023-12-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auctionlisting_last_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
