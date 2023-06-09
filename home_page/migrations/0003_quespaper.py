# Generated by Django 3.2.3 on 2021-05-31 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_delete_quespaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('sub_name', models.CharField(max_length=20)),
                ('notes_id', models.CharField(max_length=200)),
                ('fl_id', models.CharField(max_length=100)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.course')),
            ],
        ),
    ]
