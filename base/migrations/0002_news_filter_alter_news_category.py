# Generated by Django 4.2.16 on 2024-11-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='filter',
            field=models.CharField(choices=[('most_viewed', 'Most Viewed'), ('most_read', 'Most Read'), ('most_recent', 'Most Recent')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('featured', 'Featured'), ('popular', 'Popular'), ('latest', 'Latest'), ('technology', 'Technology'), ('sports', 'Sports'), ('nieee', 'Nieee')], max_length=50),
        ),
    ]
