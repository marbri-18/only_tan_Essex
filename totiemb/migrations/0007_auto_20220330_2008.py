# Generated by Django 3.2 on 2022-03-30 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('totiemb', '0006_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['lname']},
        ),
        migrations.AddField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='email', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='lname',
            field=models.CharField(default='lname', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='password', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='telephone',
            field=models.CharField(default='telephone', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default='username', max_length=50),
            preserve_default=False,
        ),
    ]