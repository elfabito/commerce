# Generated by Django 4.2.4 on 2023-09-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlistings_category_watchlist_comments_bids_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='current_bid',
            field=models.IntegerField(default=0),
        ),
    ]