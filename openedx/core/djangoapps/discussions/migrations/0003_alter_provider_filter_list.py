# Generated by Django 2.2.19 on 2021-03-23 14:46

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_add_provider_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerfilter',
            name='allow',
            field=django_mysql.models.ListCharField(models.CharField(choices=[('legacy', 'legacy'), ('piazza', 'piazza')], max_length=20), blank=True, help_text='Comma-separated list of providers to allow, eg: legacy,piazza', max_length=63, size=3, verbose_name='Allow List'),
        ),
        migrations.AlterField(
            model_name='providerfilter',
            name='deny',
            field=django_mysql.models.ListCharField(models.CharField(choices=[('legacy', 'legacy'), ('piazza', 'piazza')], max_length=20), blank=True, help_text='Comma-separated list of providers to deny, eg: legacy,piazza', max_length=63, size=3, verbose_name='Deny List'),
        ),
    ]
