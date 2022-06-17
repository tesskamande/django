# Generated by Django 4.0.5 on 2022-06-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(verbose_name='')),
                ('created_date', models.DateTimeField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
