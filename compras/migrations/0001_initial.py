# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-19 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('contas_a_pagar', '0001_initial'),
        ('empresas', '0001_initial'),
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitante', models.CharField(max_length=20)),
                ('data_compra', models.DateField()),
                ('nota_fiscal', models.CharField(max_length=15)),
                ('valor_total', models.DecimalField(decimal_places=2, default=b'0', max_digits=15)),
                ('status_compra', models.CharField(default=b'NAO LANCADO', max_length=30)),
                ('observacoes', models.TextField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresas')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.Fornecedores')),
                ('pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contas_a_pagar.ContasPagar')),
            ],
            options={
                'ordering': ('-data_compra',),
                'db_table': 'compras',
            },
        ),
        migrations.CreateModel(
            name='EntradaProdutos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=3, max_digits=15)),
                ('preco_compra', models.DecimalField(decimal_places=3, default=b'0', max_digits=15)),
                ('data_entrada', models.DateField()),
                ('data_fabricacao', models.DateField(blank=True, null=True)),
                ('data_validade', models.DateField(blank=True, null=True)),
                ('numero_lote', models.CharField(blank=True, default=b'0', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, default=b'0', max_digits=15)),
                ('balanco', models.CharField(default=b'ABERTO', max_length=20)),
                ('status_entrada', models.CharField(default=b'LANCADO', max_length=15)),
                ('observacoes_entrada', models.TextField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Compras')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresas')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.Produtos')),
            ],
            options={
                'ordering': ('compra',),
                'db_table': 'entrada_produtos',
            },
        ),
    ]
