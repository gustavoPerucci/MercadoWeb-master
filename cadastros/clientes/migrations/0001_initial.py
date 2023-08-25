# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-19 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('cpf_cnpj', models.CharField(max_length=20, verbose_name=b'Cpf')),
                ('rg_inscricao_estadual', models.CharField(blank=True, max_length=15, verbose_name=b'Rg ou insci\xc3\xa7\xc3\xa3o estadual')),
                ('telefone', models.CharField(blank=True, max_length=30, verbose_name=b'Telefone')),
                ('celular', models.CharField(blank=True, max_length=30, verbose_name=b'Celular')),
                ('contato', models.CharField(blank=True, max_length=30, verbose_name=b'Contato')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name=b'E-mail')),
                ('status', models.CharField(default=b'ATIVO', max_length=20, verbose_name=b'St\xc3\xa1tus')),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name=b'Endere\xc3\xa7o')),
                ('bairro', models.CharField(blank=True, max_length=50, verbose_name=b'Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name=b'Cidade')),
                ('cep', models.CharField(blank=True, max_length=10, verbose_name=b'CEP')),
                ('estado', models.CharField(max_length=2, verbose_name=b'Estado')),
                ('observacoes', models.TextField(blank=True, max_length=200, verbose_name=b'Observa\xc3\xa7\xc3\xb5es')),
                ('sexo', models.CharField(blank=True, max_length=10, verbose_name=b'Sexo')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('pessoa', models.CharField(max_length=10, verbose_name=b'Pessoa')),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=30)),
                ('data_nascimento_fundacao', models.DateField(blank=True, null=True, verbose_name=b'Data nascimento')),
                ('estado_civil', models.CharField(blank=True, max_length=15, verbose_name=b'Estado civil')),
                ('model_template', models.CharField(blank=True, max_length=20)),
                ('sobre_nome', models.CharField(blank=True, max_length=50, verbose_name=b'Sobre nome')),
                ('nome_fantasia', models.CharField(blank=True, max_length=24, verbose_name=b'Nome fantasia')),
                ('inscricao_municipal', models.CharField(blank=True, max_length=15, verbose_name=b'Rg ou insci\xc3\xa7\xc3\xa3o estadual')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresas.Empresas')),
            ],
            options={
                'ordering': ('nome_razao_social',),
                'db_table': 'clientes',
            },
        ),
    ]