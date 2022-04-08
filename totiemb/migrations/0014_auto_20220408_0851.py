# Generated by Django 3.2 on 2022-04-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totiemb', '0013_session_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Full_description',
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]