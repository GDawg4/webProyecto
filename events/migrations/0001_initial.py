# Generated by Django 3.0.5 on 2020-04-19 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, null=True)),
                ('notes', models.CharField(max_length=500)),
                ('baby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='babies.Baby')),
            ],
        ),
    ]
