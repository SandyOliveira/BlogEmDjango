# Generated by Django 2.2.7 on 2020-06-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.SlugField(max_length=100, unique=True, verbose_name='Identificação Rede Social')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('url', models.URLField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('alterado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['chave'],
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]
