# Generated by Django 5.0.3 on 2024-03-29 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=155, verbose_name='Assunto')),
                ('mensagem', models.TextField(max_length=255, verbose_name='Mensagem')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Contato',
                'db_table': 'contato',
            },
        ),
    ]
