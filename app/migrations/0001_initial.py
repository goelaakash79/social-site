# Generated by Django 2.0.7 on 2018-09-03 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('comment', models.TextField(db_column='comment', max_length='500')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('url', models.URLField(db_column='url')),
                ('image', models.TextField(db_column='image')),
                ('desc', models.TextField(db_column='description', max_length=1000)),
                ('likes', models.IntegerField(db_column='likes')),
                ('dislikes', models.IntegerField(db_column='dislikes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('user', models.TextField(db_column='user_id', max_length=40)),
                ('hash', models.TextField(db_column='hash', max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
