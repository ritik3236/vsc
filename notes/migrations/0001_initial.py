# Generated by Django 3.2.3 on 2021-05-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotesMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('file_date', models.DateField()),
                ('file', models.FileField(upload_to='q_paper')),
                ('notes_id', models.CharField(max_length=50)),
            ],
        ),
    ]