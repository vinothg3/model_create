# Generated by Django 4.1.7 on 2023-04-11 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic_name',
            fields=[
                ('Topics', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Age', models.IntegerField(max_length=4)),
                ('Topics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic_name')),
            ],
        ),
        migrations.CreateModel(
            name='List_student',
            fields=[
                ('Roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Titls', models.CharField(max_length=200)),
                ('Date', models.DateField()),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]