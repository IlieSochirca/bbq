# Generated by Django 2.1.7 on 2019-09-04 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Drink Name', max_length=50)),
                ('quantity', models.IntegerField(help_text='Drink Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Event Day')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Event Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Event Final time')),
                ('description', models.TextField(blank=True, help_text='Event details', null=True, verbose_name='Event Description')),
                ('public_invite_url', models.URLField(null=True)),
                ('no_participants', models.IntegerField(help_text='Number of Participants', null=True)),
                ('drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Drink', to='event.Drink')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Food Name', max_length=50)),
                ('quantity', models.IntegerField(help_text='Food Quantity')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Food', to='event.Food'),
        ),
    ]
