# Generated by Django 2.2 on 2019-06-04 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradores', '0002_auto_20190426_1228'),
        ('empresas', '0002_auto_20190426_1228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=40)),
                ('administrador', models.IntegerField(default=0)),
                ('administrador_super', models.IntegerField(blank=True, default=0, null=True)),
                ('cadastra_colaborador', models.IntegerField(default=0)),
                ('edita_colaborador', models.IntegerField(default=0)),
                ('acessa_cadastro_colaboradores', models.IntegerField(default=0)),
                ('muda_status_colaborador', models.IntegerField(default=0)),
                ('cadastra_usuario', models.IntegerField(default=0)),
                ('edita_usuario', models.IntegerField(default=0)),
                ('acessa_cadastro_usuarios', models.IntegerField(default=0)),
                ('muda_status_usuario', models.IntegerField(default=0)),
                ('cadastra_permissoes_usuario', models.IntegerField(default=0)),
                ('edita_permissoes_usuario', models.IntegerField(default=0)),
                ('acessa_permissoes_usuario', models.IntegerField(default=0)),
                ('muda_status_permissoes_usuario', models.IntegerField(default=0)),
                ('exclui_permissoes_usuario', models.IntegerField(default=0)),
                ('cadastra_cliente', models.IntegerField(default=0)),
                ('edita_cliente', models.IntegerField(default=0)),
                ('acessa_cadastro_cliente', models.IntegerField(default=0)),
                ('muda_status_cliente', models.IntegerField(default=0)),
                ('cadastra_fornecedor', models.IntegerField(default=0)),
                ('edita_fornecedor', models.IntegerField(default=0)),
                ('acessa_cadastro_fornecedor', models.IntegerField(default=0)),
                ('muda_status_fornecedor', models.IntegerField(default=0)),
                ('cadastra_produto', models.IntegerField(default=0)),
                ('edita_produto', models.IntegerField(default=0)),
                ('acessa_cadastro_produto', models.IntegerField(default=0)),
                ('muda_status_produto', models.IntegerField(default=0)),
                ('altera_preco_produto', models.IntegerField(default=0)),
                ('anuncia_produto', models.IntegerField(default=0)),
                ('tabela_preco', models.IntegerField(default=0)),
                ('edita_tabela_de_precos', models.IntegerField(default=0)),
                ('acessa_tabela_de_precos', models.IntegerField(default=0)),
                ('exclui_preco_tabelado', models.IntegerField(default=0)),
                ('muda_status_preco_tabelado', models.IntegerField(default=0)),
                ('registra_venda', models.IntegerField(default=0)),
                ('edita_venda', models.IntegerField(default=0)),
                ('fecha_venda', models.IntegerField(default=0)),
                ('acessa_registro_venda', models.IntegerField(default=0)),
                ('muda_status_venda', models.IntegerField(default=0)),
                ('cancela_venda', models.IntegerField(default=0)),
                ('imprime_cupom_venda', models.IntegerField(default=0)),
                ('registra_compra', models.IntegerField(default=0)),
                ('edita_compra', models.IntegerField(default=0)),
                ('acessa_registro_compra', models.IntegerField(default=0)),
                ('muda_status_compra', models.IntegerField(default=0)),
                ('cancela_compra', models.IntegerField(default=0)),
                ('finaliza_compra', models.IntegerField(default=0)),
                ('edita_contas_pagar', models.IntegerField(default=0)),
                ('acessa_contas_pagar', models.IntegerField(default=0)),
                ('exclui_contas_pagar', models.IntegerField(default=0)),
                ('quita_contas_pagar', models.IntegerField(default=0)),
                ('edita_contas_receber', models.IntegerField(default=0)),
                ('acessa_contas_receber', models.IntegerField(default=0)),
                ('exclui_contas_receber', models.IntegerField(default=0)),
                ('quita_contas_receber', models.IntegerField(default=0)),
                ('registra_pagamento', models.IntegerField(default=0)),
                ('edita_pagamento', models.IntegerField(default=0)),
                ('acessa_pagamento', models.IntegerField(default=0)),
                ('muda_status_pagamento', models.IntegerField(default=0)),
                ('exclui_pagamento', models.IntegerField(default=0)),
                ('registra_recebimento', models.IntegerField(default=0)),
                ('edita_recebimento', models.IntegerField(default=0)),
                ('acessa_recebimento', models.IntegerField(default=0)),
                ('muda_status_recebimento', models.IntegerField(default=0)),
                ('exclui_recebimento', models.IntegerField(default=0)),
                ('registra_entrada_produto', models.IntegerField(default=0)),
                ('edita_entrada_produto', models.IntegerField(default=0)),
                ('acessa_entrada_produto', models.IntegerField(default=0)),
                ('muda_status_entrada_produto', models.IntegerField(default=0)),
                ('cancela_entrada_produto', models.IntegerField(default=0)),
                ('registra_saida_produto', models.IntegerField(default=0)),
                ('edita_saida_produto', models.IntegerField(default=0)),
                ('acessa_saida_produto', models.IntegerField(default=0)),
                ('muda_status_saida_produto', models.IntegerField(default=0)),
                ('cancela_saida_produto', models.IntegerField(default=0)),
                ('publica_conteudo_site', models.IntegerField(default=0)),
                ('edita_conteudo_site', models.IntegerField(default=0)),
                ('exclui_conteudo_site', models.IntegerField(default=0)),
                ('acessa_conteudo_site', models.IntegerField(default=0)),
                ('muda_status_conteudo_site', models.IntegerField(default=0)),
                ('publica_mensagem_site', models.IntegerField(default=0)),
                ('edita_mensagem_site', models.IntegerField(default=0)),
                ('exclui_mensagem_site', models.IntegerField(default=0)),
                ('acessa_mensagem_site', models.IntegerField(default=0)),
                ('muda_status_mensagem_site', models.IntegerField(default=0)),
                ('observacoes', models.TextField(blank=True, max_length=200)),
                ('status', models.CharField(default='ATIVO', max_length=10, verbose_name='Státus')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresas.Empresas')),
            ],
            options={
                'db_table': 'permissoes',
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=15, verbose_name='Cpf')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='E-mail')),
                ('status', models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO'), ('BLOQUEADO', 'BLOQUEADO'), ('EXCLUIDO', 'EXCLUIDO')], default='ATIVO', max_length=10, verbose_name='Státus')),
                ('suporte_tecnico', models.IntegerField(choices=[(0, 'NAO'), (1, 'SIM')], default=0)),
                ('observacoes', models.TextField(blank=True, max_length=200, verbose_name='Observações')),
                ('model_template', models.CharField(blank=True, max_length=100, null=True)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('colaborador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='colaboradores.Colaboradores')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresas.Empresas')),
                ('permissoes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.Permissoes')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ('nome',),
            },
        ),
    ]
