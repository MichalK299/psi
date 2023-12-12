# Generated by Django 4.2.8 on 2023-12-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=255)),
                ('opis', models.TextField()),
                ('rok_produkcji', models.IntegerField()),
                ('rezyser', models.CharField(max_length=255)),
                ('data_dodania', models.DateField(auto_now_add=True)),
            ],
        ),
    ]