# -*-encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from cadastros.usuarios.models import Usuarios, Permissoes
from cadastros.usuarios.forms import FormPermissoesUsuarios
from django.http import HttpResponse
from django.http import QueryDict
import json
from functions.views import deserialize_form
from functions.views import mensagem_erro_padrao, titulo_mensagem_erro_padrao, mensagem_permissao_negada, titulo_mensagem_permissao_negada


@login_required
def cadastrar_permissao_usuario(request):
    permissao_id = request.POST.get('id')
    usuario = Usuarios.objects.get(usuario=request.user.id)
    retorno = {}
    sucesso = {}
    erro = []
    if permissao_id != '0':
        if not usuario.permissoes.administrador and not usuario.permissoes.administrador_super and not usuario.permissoes.edita_permissoes_usuario:
            sucesso['negado'] = 1
            sucesso['mensagem'] = mensagem_permissao_negada()
            sucesso['titulo'] = titulo_mensagem_permissao_negada()
            retorno = json.dumps(sucesso)
            return HttpResponse(retorno, content_type="application/json")
        else:
            permissao = Permissoes.objects.get(id=int(permissao_id))
    else:
        permissao = None
        if not usuario.permissoes.administrador and not usuario.permissoes.administrador_super and not usuario.permissoes.cadastra_permissoes_usuario:
            sucesso['negado'] = 1
            sucesso['mensagem'] = mensagem_permissao_negada()
            sucesso['titulo'] = titulo_mensagem_permissao_negada()
            retorno = json.dumps(sucesso)
            return HttpResponse(retorno, content_type="application/json")

    if request.method == 'POST':
        form = FormPermissoesUsuarios(deserialize_form(request.POST.get('form')), instance=permissao)

        if form.is_valid():
            registro = form.save(commit=False)

            if not permissao_id != '0':
                registro.empresa = usuario.empresa
                registro.usuario = request.user
                titulo_mensagem = 'SALVANDO REGISTRO...'
                mensagem = 'O registro foi salvo com sucesso !!!'
            else:
                titulo_mensagem = 'ALTERANDO REGISTRO...'
                mensagem = 'O registro foi alterado com sucesso!!!'

            registro.save()

            sucesso['success'] = True
            sucesso['mensagem'] = mensagem
            sucesso['id'] = registro.id
            sucesso['titulo'] = titulo_mensagem
            retorno = json.dumps(sucesso)

        else:
            cont = 0
            for error in form.errors:
                erro += {error}
                cont += 1
            titulo_mensagem = 'ERRO NA VALIDA????O DOS DADOS . . .'
            mensagem = '''O formul??rio apresentou erros no seu preenchimento.
                       Corrija os campos listados em vermelho e tente novamente. . .'''

            retorno = json.dumps({
                'titulo': titulo_mensagem,
                'mensagem': mensagem,
                'erro': erro,
                'cont': cont,
            })
    return HttpResponse(retorno, content_type="application/json")


def buscar_permissoes_usuarios(request):
    usuario = Usuarios.objects.get(usuario=request.user.id)
    tb_permissoes = {}
    mensagem = ''
    permissoes = []
    classe = ''
    titulo = 'BUSCANDO PERMISS??ES DE USU??RIOS...'

    if usuario.permissoes.acessa_permissoes_usuario:
        tb_permissoes = Permissoes.objects.filter(empresa=usuario.empresa,
                                                  administrador=0,
                                                  administrador_super=0)
    if usuario.permissoes.administrador:
        tb_permissoes = Permissoes.objects.filter(empresa=usuario.empresa,
                                                  administrador_super=0)
    if usuario.permissoes.administrador_super:
        tb_permissoes = Permissoes.objects.filter()

    for index in tb_permissoes:
        usuarios = ''
        permissoes_usuarios = ''
        colaboradores = ''
        clientes = ''
        produtos = ''
        fornecedores = ''
        tabela_precos = ''
        vendas = ''
        compras = ''
        contas_pagar = ''
        contas_receber = ''
        saida_produtos = ''
        entrada_produtos = ''
        recebimentos = ''
        pagamentos = ''
        mensagens_site = ''
        conteudo_site = ''
        if index.status == 'ATIVO':
            classe = 'success'
        else:
            classe = 'danger'

        # inicio cadastro de colaboradores
        if index.cadastra_colaborador:
            colaboradores += 'Cadastra(SIM)'
        else:
            colaboradores += 'Cadastra(N??O)'

        if index.edita_colaborador:
            colaboradores += ', Edita(SIM)'
        else:
            colaboradores += ', Edita(N??O)'

        if index.muda_status_colaborador:
            colaboradores += ', Muda st??tus(SIM)'
        else:
            colaboradores += ', Muda st??tus(N??O)'

        if index.acessa_cadastro_colaboradores:
            colaboradores += ', Acessa cadastro(SIM)'
        else:
            colaboradores += ', Acessa cadastro(N??O)'
        # fim cadastro de colaboradores

        # inicio cadastro de usuarios
        if index.cadastra_usuario:
            usuarios += 'Cadastra(SIM)'
        else:
            usuarios += 'Cadastra(N??O)'

        if index.edita_usuario:
            usuarios += ', Edita(SIM)'
        else:
            usuarios += ', Edita(N??O)'

        if index.muda_status_usuario:
            usuarios += ', Muda st??tus(SIM)'
        else:
            usuarios += ', Muda st??tus(N??O)'

        if index.acessa_cadastro_usuarios:
            usuarios += ', Acessa cadastro(SIM)'
        else:
            usuarios += ', Acessa cadastro(N??O)'
        # fim cadastro de usuarios


        # inicio cadastro de clientes
        if index.cadastra_cliente:
            clientes += 'Cadastra(SIM)'
        else:
            clientes += 'Cadastra(N??O)'

        if index.edita_cliente:
            clientes += ', Edita(SIM)'
        else:
            clientes += ', Edita(N??O)'

        if index.muda_status_cliente:
            clientes += ', Muda st??tus(SIM)'
        else:
            clientes += ', Muda st??tus(N??O)'

        if index.acessa_cadastro_cliente:
            clientes += ', Acessa cadastro(SIM)'
        else:
            clientes += ', Acessa cadastro(N??O)'
        # fim cadastro de clientes

        # inicio cadastro de fornecedores
        if index.cadastra_fornecedor:
            fornecedores += 'Cadastra(SIM)'
        else:
            fornecedores += 'Cadastra(N??O)'
        if index.edita_fornecedor:
            fornecedores += ', Edita(SIM)'
        else:
            fornecedores += ', Edita(N??O)'
        if index.muda_status_fornecedor:
            fornecedores += ', Muda st??tus(SIM)'
        else:
            fornecedores += ', Muda st??tus(N??O)'
        if index.acessa_cadastro_fornecedor:
            fornecedores += ', Acessa cadastro(SIM)'
        else:
            fornecedores += ', Acessa cadastro(N??O)'
        # fim cadastro de fornecedores

        # inicio cadastro de produtos
        if index.cadastra_produto:
            produtos += 'Cadastra(SIM)'
        else:
            produtos += 'Cadastra(N??O)'
        if index.edita_produto:
            produtos += ', Edita(SIM)'
        else:
            produtos += ', Edita(N??O)'
        if index.muda_status_produto:
            produtos += ', Muda st??tus(SIM)'
        else:
            produtos += ', Muda st??tus(N??O)'
        if index.acessa_cadastro_produto:
            produtos += ', Acessa cadastro(SIM)'
        else:
            produtos += ', Acessa cadastro(N??O)'
        if index.altera_preco_produto:
            produtos += ', Altera pre??o(SIM)'
        else:
            produtos += ', Altera pre??o(N??O)'
        if index.anuncia_produto:
            produtos += ', Anuncia produto(SIM)'
        else:
            produtos += ', Anuncia produto(N??O)'
        # fim cadastro de produtos

        # inicio tabela de precos
        if index.tabela_preco:
            tabela_precos += 'Tabela pre??o(SIM)'
        else:
            tabela_precos += 'Tabela pre??o(N??O)'
        if index.edita_tabela_de_precos:
            tabela_precos += ', Edita(SIM)'
        else:
            tabela_precos += ', Edita(N??O)'
        if index.exclui_preco_tabelado:
            tabela_precos += ', Exclui(SIM)'
        else:
            tabela_precos += ', Exclui(N??O)'
        if index.acessa_tabela_de_precos:
            tabela_precos += ', Acessa(SIM)'
        else:
            tabela_precos += ', Acessa(N??O)'
        # fim tabela de precos

        # inicio registro de vendas
        if index.registra_venda:
            vendas += 'Registra(SIM)'
        else:
            vendas += 'Registra(N??O)'
        if index.edita_venda:
            vendas += ', Edita(SIM)'
        else:
            vendas += ', Edita(N??O)'
        if index.fecha_venda:
            vendas += ', Fecha(SIM)'
        else:
            vendas += ', Fecha(N??O)'
        if index.acessa_registro_venda:
            vendas += ', Acessa(SIM)'
        else:
            vendas += ', Acessa(N??O)'
        if index.muda_status_venda:
            vendas += ', Muda st??tus(SIM)'
        else:
            vendas += ', Muda st??tus(N??O)'
        if index.cancela_venda:
            vendas += ', Cancela(SIM)'
        else:
            vendas += ', Cancela(N??O)'
        if index.imprime_cupom_venda:
            vendas += ', Imprime cupom(SIM)'
        else:
            vendas += ', imprime cupom(N??O)'
        # fim registro de vendas

        # inicio registro de compras
        if index.registra_compra:
            compras += 'Registra(SIM)'
        else:
            compras += 'Registra(N??O)'
        if index.edita_compra:
            compras += ', Edita(SIM)'
        else:
            compras += ', Edita(N??O)'
        if index.finaliza_compra:
            compras += ', Finaliza(SIM)'
        else:
            compras += ', Finaliza(N??O)'
        if index.acessa_registro_compra:
            compras += ', Acessa(SIM)'
        else:
            compras += ', Acessa(N??O)'
        if index.muda_status_compra:
            compras += ', Muda st??tus(SIM)'
        else:
            compras += ', Muda st??tus(N??O)'
        if index.cancela_compra:
            compras += ', Cancela(SIM)'
        else:
            compras += ', Cancela(N??O)'
        # fim registro de compras

        # inicio contas a pagar
        if index.quita_contas_pagar:
            contas_pagar += 'Quita(SIM)'
        else:
            contas_pagar += 'Quita(N??O)'
        if index.edita_contas_pagar:
            contas_pagar += ', Edita(SIM)'
        else:
            contas_pagar += ', Edita(N??O)'
        if index.exclui_contas_pagar:
            contas_pagar += ', Exclui(SIM)'
        else:
            contas_pagar += ', Exclui(N??O)'
        if index.acessa_contas_pagar:
            contas_pagar += ', Acessa(SIM)'
        else:
            contas_pagar += ', Acessa(N??O)'
        # fim contas a pagar

        # inicio contas a receber
        if index.quita_contas_receber:
            contas_receber += 'Quita(SIM)'
        else:
            contas_receber += 'Quita(N??O)'
        if index.edita_contas_receber:
            contas_receber += ', Edita(SIM)'
        else:
            contas_receber += ', Edita(N??O)'
        if index.exclui_contas_receber:
            contas_receber += ', Exclui(SIM)'
        else:
            contas_receber += ', Exclui(N??O)'
        if index.acessa_contas_receber:
            contas_receber += ', Acessa(SIM)'
        else:
            contas_receber += ', Acessa(N??O)'
        # fim contas a receber

        # inicio saida de produtos
        if index.registra_saida_produto:
            saida_produtos += 'Registra(SIM)'
        else:
            saida_produtos += 'Registra(N??O)'
        if index.edita_saida_produto:
            saida_produtos += ', Edita(SIM)'
        else:
            saida_produtos += ', Edita(N??O)'
        if index.acessa_saida_produto:
            saida_produtos += ', Acessa(SIM)'
        else:
            saida_produtos += ', Acessa(N??O)'
        if index.muda_status_saida_produto:
            saida_produtos += ', Muda st??tus(SIM)'
        else:
            saida_produtos += ', Muda st??tus(N??O)'
        if index.cancela_saida_produto:
            saida_produtos += ', Cancela(SIM)'
        else:
            saida_produtos += ', Cancela(N??O)'
        # fim saida de produtos

        # inicio entrada de produtos
        if index.registra_entrada_produto:
            entrada_produtos += 'Registra(SIM)'
        else:
            entrada_produtos += 'Registra(N??O)'
        if index.edita_entrada_produto:
            entrada_produtos += ', Edita(SIM)'
        else:
            entrada_produtos += ', Edita(N??O)'
        if index.acessa_entrada_produto:
            entrada_produtos += ', Acessa(SIM)'
        else:
            entrada_produtos += ', Acessa(N??O)'
        if index.muda_status_entrada_produto:
            entrada_produtos += ', Muda st??tus(SIM)'
        else:
            entrada_produtos += ', Muda st??tus(N??O)'
        if index.cancela_entrada_produto:
            entrada_produtos += ', Cancela(SIM)'
        else:
            entrada_produtos += ', Cancela(N??O)'
        # fim entrada de produtos

        # inicio registro de pagamentos
        if index.registra_pagamento:
            pagamentos += 'Registra(SIM)'
        else:
            pagamentos += 'Registra(N??O)'
        if index.edita_pagamento:
            pagamentos += ', Edita(SIM)'
        else:
            pagamentos += ', Edita(N??O)'
        if index.acessa_pagamento:
            pagamentos += ', Acessa(SIM)'
        else:
            pagamentos += ', Acessa(N??O)'
        if index.muda_status_pagamento:
            pagamentos += ', Muda st??tus(SIM)'
        else:
            pagamentos += ', Muda st??tus(N??O)'
        if index.exclui_pagamento:
            pagamentos += ', Exclui(SIM)'
        else:
            pagamentos += ', Exclui(N??O)'
        # fim registro de pagamentos

        # inicio registro de recebimentos
        if index.registra_recebimento:
            recebimentos += 'Registra(SIM)'
        else:
            recebimentos += 'Registra(N??O)'
        if index.edita_recebimento:
            recebimentos += ', Edita(SIM)'
        else:
            recebimentos += ', Edita(N??O)'
        if index.acessa_recebimento:
            recebimentos += ', Acessa(SIM)'
        else:
            recebimentos += ', Acessa(N??O)'
        if index.muda_status_recebimento:
            recebimentos += ', Muda st??tus(SIM)'
        else:
            recebimentos += ', Muda st??tus(N??O)'
        if index.exclui_recebimento:
            recebimentos += ', Exclui(SIM)'
        else:
            recebimentos += ', Exclui(N??O)'
        # fim registro de recebimentos

        # inicio publicacao de mensagens do site
        if index.publica_mensagem_site:
            mensagens_site += 'Publica(SIM)'
        else:
            mensagens_site += 'Publica(N??O)'
        if index.edita_mensagem_site:
            mensagens_site += ', Edita(SIM)'
        else:
            mensagens_site += ', Edita(N??O)'
        if index.acessa_mensagem_site:
            mensagens_site += ', Acessa(SIM)'
        else:
            mensagens_site += ', Acessa(N??O)'
        if index.muda_status_mensagem_site:
            mensagens_site += ', Muda st??tus(SIM)'
        else:
            mensagens_site += ', Muda st??tus(N??O)'
        if index.exclui_mensagem_site:
            mensagens_site += ', Exclui(SIM)'
        else:
            mensagens_site += ', Exclui(N??O)'
        # fim publicacao de mensagens do site

        # inicio publicacao de conteudo do site
        if index.publica_conteudo_site:
            conteudo_site += 'Publica(SIM)'
        else:
            conteudo_site += 'Publica(N??O)'
        if index.edita_conteudo_site:
            conteudo_site += ', Edita(SIM)'
        else:
            conteudo_site += ', Edita(N??O)'
        if index.acessa_conteudo_site:
            conteudo_site += ', Acessa(SIM)'
        else:
            conteudo_site += ', Acessa(N??O)'
        if index.muda_status_conteudo_site:
            conteudo_site += ', Muda st??tus(SIM)'
        else:
            conteudo_site += ', Muda st??tus(N??O)'
        if index.exclui_conteudo_site:
            conteudo_site += ', Exclui(SIM)'
        else:
            conteudo_site += ', Exclui(N??O)'
            # fim publicacao de conteudo do site

        if index.administrador:
            administrador = 'SIM'
            administrador_super = 'N??O'
            usuarios = 'Sem restri????es'
            colaboradores = 'Sem restri????es'
            permissoes_Usuarios = 'Sem restri????es'
            clientes = 'Sem restri????es'
            produtos = 'Sem restri????es'
            fornecedores = 'Sem restri????es'
            tabela_precos = 'Sem restri????es'
            vendas = 'Sem restri????es'
            compras = 'Sem restri????es'
            contas_pagar = 'Sem restri????es'
            contas_receber = 'Sem restri????es'
            saida_produtos = 'Sem restri????es'
            entrada_produtos = 'Sem restri????es'
            recebimentos = 'Sem restri????es'
            pagamentos = 'Sem restri????es'
            mensagens_site = 'Sem restri????es'
            conteudo_site = 'Sem restri????es'
        else:
            administrador = 'N??O'

        if index.administrador_super:
            administrador_super = 'SIM'
            administrador = 'SIM'
            usuarios = 'Sem restri????es'
            colaboradores = 'Sem restri????es'
            permissoes_Usuarios = 'Sem restri????es'
            clientes = 'Sem restri????es'
            produtos = 'Sem restri????es'
            fornecedores = 'Sem restri????es'
            tabela_precos = 'Sem restri????es'
            vendas = 'Sem restri????es'
            compras = 'Sem restri????es'
            contas_pagar = 'Sem restri????es'
            contas_receber = 'Sem restri????es'
            saida_produtos = 'Sem restri????es'
            entrada_produtos = 'Sem restri????es'
            recebimentos = 'Sem restri????es'
            pagamentos = 'Sem restri????es'
            mensagens_site = 'Sem restri????es'
            conteudo_site = 'Sem restri????es'
        else:
            administrador_super = 'N??O'

        permissoes += [{
            'descricao': index.descricao,
            'administrador_super': administrador_super,
            'administrador': administrador,
            'usuarios': usuarios,
            'permissoes_usuarios': permissoes_usuarios,
            'clientes': clientes,
            'fornecedores': fornecedores,
            'produtos': produtos,
            'tabela_precos': tabela_precos,
            'vendas': vendas,
            'compras': compras,
            'contas_pagar': contas_pagar,
            'contas_receber': contas_receber,
            'saida_produtos': saida_produtos,
            'entrada_produtos': entrada_produtos,
            'pagamentos': pagamentos,
            'recebimentos': recebimentos,
            'mensagens_site': mensagens_site,
            'conteudo_site': conteudo_site,
            'observacoes': index.observacoes,
            'status': index.status,
            'empresa': str(index.empresa),
            'id': index.id,
            'classe': classe,
            'mensagem': mensagem,
            'titulo': titulo,
        }]
    if permissoes:
        retorno = json.dumps(permissoes)
    else:
        retorno = json.dumps({
            'titulo': titulo,
            'mensagem': '''Nenhum registro de permiss??o de usuarios foi encontrado.
            Talvez, voc?? n??o tenha permiss??o para acessar estes registros...
            ''',
            'info': 1,
        })
    return HttpResponse(retorno, content_type='application/json')


def buscar_permissao_usuario(request):
    usuario = Usuarios.objects.get(usuario=request.user)
    permissao = {}
    retorno = {}
    titulo = 'BUSCANADO PERMIS??ES DE Usuarios...'
    id = request.GET.get('id')
    try:
        if usuario.permissoes.edita_permissoes_usuario and not usuario.permissoes.administrador and not usuario.permissoes.administrador_super:
            permissao = Permissoes.objects.get(id=int(id),
                                               administrador_super=0,
                                               administrador=0,
                                               empresa=usuario.empresa.id)
        if usuario.permissoes.administrador and usuario.permissoes.administrador and not usuario.permissoes.administrador_super:
            permissao = Permissoes.objects.get(id=int(id),
                                               empresa=usuario.empresa.id,
                                               administrador_super=0)
        if usuario.permissoes.administrador_super:
            permissao = Permissoes.objects.get(id=int(id))
    except:
        pass

    if permissao:
        form = FormPermissoesUsuarios(instance=permissao)
        mensagem = 'Busca efetuada com sucesso !!!'
        campos = {}
        for campo in form.fields:
            if campo in form.initial:
                campos[form.auto_id % campo] = unicode(form.initial[campo])

        retorno = json.dumps({
            'id': id,
            'titulo': titulo,
            'mensagem': mensagem,
            'campos': campos,
        })
    else:
        retorno = json.dumps({
            'titulo': titulo,
            'mensagem': 'Nenhum registro de permiss??o de colaborador corresponde ao ID informado.'
                        'Ou talvez, voc?? n??o tenha permiss??o para acessar estes dados...',
            'info': 1,
        })

    return HttpResponse(retorno, content_type='application/json')


def status_permissoes_usuario(request):
    retorno = {}
    titulo = ''
    mensagem = ''
    try:
        usuario = Usuarios.objects.get(usuario=request.user)
        if not usuario.permissoes.muda_status_permissoes_usuario and not usuario.permissoes.administrador \
                and not usuario.permissoes.administrador_super:
            retorno['titulo'] = titulo_mensagem_permissao_negada()
            retorno['erro'] = 1
            retorno['mensagem'] = mensagem_permissao_negada()
            return HttpResponse(json.dumps(retorno), content_type="application/json")

        elif request.method == 'POST':
            permissao = Permissoes.objects.get(id=int(QueryDict(request.body).get('permissao_id')))
            status = QueryDict(request.body).get('status')

            permissao.status = status
            permissao.save()

            if status == 'ATIVO':
                mensagem = 'Permiss??es ativadas com sucesso !!!'
                titulo = 'ATIVAR PERMISS??ES DE COLABORADOR...'

            elif status == 'INATIVO':
                mensagem = 'Permiss??es desativadas com sucesso !!!'
                titulo = 'DESATIVAR PERMISS??ES DE COLABORADOR...'

            elif status == 'EXCLUIDO':
                mensagem = 'Permiss??es excluidas com sucesso !!!'
                titulo = 'EXCLUIR PERMISS??ES DE COLABORADOR ...'

            retorno['mensagem'] = mensagem
            retorno['titulo'] = titulo
            retorno['sucesso'] = 1
            retorno['status'] = status
    except:
        retorno['titulo'] = titulo_mensagem_erro_padrao()
        retorno['mensagem'] = mensagem_erro_padrao()
        retorno['erro'] = 1

    return HttpResponse(
            json.dumps(retorno), content_type="application/json")
