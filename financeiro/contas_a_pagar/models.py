# -*- encoding: utf-8 -*-
from django.db import models
from cadastros.empresas.models import Empresas
from cadastros.fornecedores.models import Fornecedores


class ContasPagar(models.Model):
    favorecido = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    data_conta = models.DateField(auto_now_add=True)
    valor_conta = models.DecimalField(max_digits=15, decimal_places=2)
    forma_de_pagamento = models.CharField(max_length=8, blank=False, choices=(('A VISTA', 'A VISTA'),
                                                                              ('A PRAZO', 'A PRAZO')
                                                                              ))
    meio_de_pagamento = models.CharField(max_length=15, blank=False,
                                         choices=(('DINHEIRO', 'DINHEIRO'),
                                                  ('CARTAO DEBITO', 'CARTAO DEBITO'),
                                                  ('CARTAO CREDITO', 'CARTAO CREDITO'),
                                                  ('CHEQUE', 'CHEQUE'),
                                                  ('OUTROS', 'OUTROS')
                                                  ))
    quantidade_parcelas = models.IntegerField(blank=False, default='1')
    primeiro_vencimento = models.DateField()
    valor_entrada = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    documento_vinculado = models.IntegerField(blank=True, null=True, default=0, unique=True)
    status_conta = models.CharField(max_length=17, blank=False, default='PENDENTE', choices=(
        ('PENDENTE', 'PENDENTE'),
        ('PARCIALMENTE PAGO', 'PARCIALMENTE PAGO'),
        ('PAGO', 'PAGO'),
        ('CANCELADO', 'CANCELADO')
    ))
    descricao = models.CharField(blank=True, max_length=100)
    empresa = models.ForeignKey(Empresas, blank=True, null=True, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    observacoes_conta = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('-data_conta', 'valor_conta')
        db_table = 'contas_a_pagar'

    def __str__(self):
        data_conta = self.data_conta.strftime('%d/%m/%Y')
        valor_conta = '%0.02f' % self.valor_conta
        return '%s - %s (%s) - Compra:000%s' % (valor_conta, self.favorecido, data_conta, self.documento_vinculado)

