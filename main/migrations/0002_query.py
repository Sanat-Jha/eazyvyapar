# Generated by Django 3.1.2 on 2020-12-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=3000)),
                ('second_name', models.CharField(max_length=3000)),
                ('email', models.CharField(max_length=3000)),
                ('phone', models.CharField(max_length=3000)),
                ('query', models.TextField()),
            ],
        ),
    ]
