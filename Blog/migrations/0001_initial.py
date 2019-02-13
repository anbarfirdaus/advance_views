# Generated by Django 2.1.5 on 2019-02-12 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.TextField()),
                ('Created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]