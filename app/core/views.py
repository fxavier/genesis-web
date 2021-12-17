from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date
from django.db.models import Q, Count
import gspread

from django.views.generic import ListView

from core.models import Inquerito, TipoSementeGerminou, TipoAreaGerminacao, VerificacaoSementes
from core.helpers import Helpers

from core.constants import Constants

service_account = gspread.service_account(filename="credentials.json")


def get_data_from_spreadsheet(worksheet: str, sheet: str):
    sh = service_account.open(worksheet)
    wks = sh.worksheet(sheet)
    return wks.get_all_records()


def refresh_inquerito_data():
    Inquerito.objects.all().delete()
    TipoAreaGerminacao.objects.all().delete()
    TipoSementeGerminou.objects.all().delete()
    questionario = 1
    for data in get_data_from_spreadsheet("Inquerito_resultados", "Folha1"):

        inquerito = Inquerito.objects.create(
            uuid=data.get("KEY"),
            codigo_familia=data.get("data-dados_iniciais-codigo_familia"),
            data_inquerito=data.get("data-dados_iniciais-data_inquerito"),
            nome_inquiridor=data.get("data-dados_iniciais-nome_inquiridor"),
            numero_questionario=questionario,
            local_entrevista=data.get("data-dados_iniciais-local_entrevista"),
            gps_local_lat_long=data.get(
                "data-dados_iniciais-gps_local_entrevista"),
            gps_local_accuracy=data.get(
                "data-dados_iniciais-gps_local_entrevista-accuracy"),
            tipo_beneficiario=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-tipo_beneficiario"))),
            tipo_familia=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-tipo_familia"))),
            nome_agg_familiar=data.get(
                "data-identificacao_receptor-nome_agg_familiar"),
            tipo_documento=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-tipo_doc"))),
            documento=data.get("data-identificacao_receptor-documento"),
            photo_doc_url=data.get("data-identificacao_receptor-photo_doc"),
            data_nascimento=Helpers.formatDate(data.get(
                "data-identificacao_receptor-data_nascimento")),
            genero=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-genero"))),
            outro_genero=data.get("data-identificacao_receptor-outro_genero"),
            contacto=data.get("data-identificacao_receptor-contacto"),
            parte_bd=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-part_bd"))),
            criterios_elegib_agg_familiar=Constants().get_dicionario().get(
                str(data.get("data-identificacao_receptor-criterios_eleg_agg_familiar"))),
            provincia=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-provincia"))),
            distrito=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-distrito"))),
            posto_administrativo=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-posto_administrativo"))),
            localidade=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-localidade"))),
            comunidade=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-comunidade"))),
            ficha=Constants().get_dicionario().get(
                str(data.get("data-localizacao_agregado-ficha"))),
            familia_tem_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-familia_tem_machamba"))),
            machamba_familia=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-machamba_familia"))),
            tipo_posse=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-tipo_posse"))),
            outro_tipo_posse=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outro_tipo_posse"))),
            forma_aquisicao=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-forma_aquisicao_machamba"))),
            outra_forma_aquisicao=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outra_forma"))),
            quando_conseguiu_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-quando_conseguiu_machamba"))),
            outra_data=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outra_data"))),
            tamanho_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-tamanho_machamba"))),
            outro_tamanho=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-outro_tamanho"))),
            local_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-local_machamba"))),
            outro_local_machamba=data.get("data-alocacao_terra-outro_local"),
            caracteristica_solos=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-caracteristica_solo"))),
            outra_caracteristica_solos=data.get(
                "data-alocacao_terra-outra_caracteristica_solo"),
            cor_solo=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-cor_solo"))),
            outra_cor=data.get("data-alocacao_terra-outra_cor"),
            historico_uso_solo=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-historico_uso_terra"))),
            outro_historico_uso_solo=data.get(
                "data-alocacao_terra-outro_historico"),
            tempo_gasto_casa_machamba=Constants().get_dicionario().get(
                str(data.get("data-alocacao_terra-tempo_gasto_casa_machamba"))),
            outro_tempo_gasto=data.get(
                "data-alocacao_terra-outro_tempo_gasto"),
            recebeu_semente=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-recebeu_semente"))),
            quando_recebeu=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-quando_recebeu_semente"))),
            outra_data_recebeu=data.get(
                "data-kits_para_agricultura-outra_data_recebimento"),
            identificacao_lote=data.get(
                "data-kits_para_agricultura-idntificacao_lote"),
            tipo_kit=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-tipo_kit"))),
            composicao_kit_a=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_a"))),
            comentario_kit_a=data.get(
                "data-kits_para_agricultura-comentario_kit_a"),
            composicao_kit_b=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_b"))),
            comentario_kit_b=data.get(
                "data-kits_para_agricultura-comentario_kit_b"),
            composicao_kit_c=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_c"))),
            comentario_kit_c=data.get(
                "data-kits_para_agricultura-comentario_kit_c"),
            composicao_kit_d=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-composicao_kit_d"))),
            comentario_kit_d=data.get(
                "data-kits_para_agricultura-comentario_kit_d"),
            conservacao_semente=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-conservacao_semente"))),
            foto_semente_url=data.get(
                "data-kits_para_agricultura-foto_semente"),
            de_quem_recebeu_semente=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-de_quem_recebeu_semente"))),
            outro_de_quem_recebeu_semente=data.get(
                "data-kits_para_agricultura-outro_de_quem_recebeu"),
            quem_escolheu_kit=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-quem_escolheu_kit"))),
            outro_quem_escolheu_kit=data.get(
                "data-kits_para_agricultura-outro_quem_escolheu_kit"),
            quando_realizou_sementeira=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-quando_realizou_sementeira"))),
            familia_necess_nao_recebeu=Constants().get_dicionario().get(
                str(data.get("data-kits_para_agricultura-fam_necess_nao_recebeu"))),
            nome_familia=data.get(
                "data-kits_para_agricultura-nome_familia_nao_recebeu"),
            sementes_germinou=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-sementes_germinaram"))),
            foto_sementes_germinou_url=Constants().get_dicionario().get(str(
                data.get("data-germinacao_semente_uso_fertilizante-foto_semente_germinaram"))),
            semente_nao_germinou=Constants().get_dicionario().get(str(
                data.get("data-germinacao_semente_uso_fertilizante-sementes_nao_germinaram"))),
            usou_fertilizante=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-usou_fertilizante"))),
            tipo_fertilizante=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-tipo_fertilizante"))),
            outro_tipo_fertilizante=data.get(
                "data-germinacao_semente_uso_fertilizante-outro_tipo_fertilizante"),
            momento_usou_adubo=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-momento_usou_adubo"))),
            outro_momento_usou_adubo=data.get(
                "data-germinacao_semente_uso_fertilizante-outro_momento_usou_adubo"),
            adubo_usado=Constants().get_dicionario().get(
                str(data.get("data-germinacao_semente_uso_fertilizante-adubo_usado"))),
            recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-recebeu_treinamento"))),
            lugar_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-lugar_treinamento"))),
            outro_lugar_treinamento=data.get(
                "data-treinamento-outro_lugar_treinamento"),
            de_quem_recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-de_quem_recebeu_treinamento"))),
            outro_de_quem_recebeu_treinamento=data.get(
                "data-treinamento-outro_de_quem_recebeu_treinamento"),
            quando_recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-quando_recebeu_treinamento"))),
            outro_quando_recebeu_treinamento=data.get(
                "data-treinamento-outro_quando_recebeu_treinamento"),
            tipo_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-recebeu_tipo_treinamento"))),
            recebeu_visita_assistencia=Constants().get_dicionario().get(
                str(data.get("data-treinamento-recebeu_visita_assistencia"))),
            de_quem_recebeu_visita_assistencia=Constants().get_dicionario().get(
                str(data.get("data-treinamento-de_quem_recebeu_visita"))),
            outro_de_quem_recebeu_visita_assistencia=Constants().get_dicionario().get(
                str(data.get("data-treinamento-outro_de_quem_recebeu_visita"))),
            momento_recebeu_visita=Constants().get_dicionario().get(
                str(data.get("data-treinamento-momento_recebeu_visita"))),
            familia_nao_recebeu_treinamento=Constants().get_dicionario().get(
                str(data.get("data-treinamento-familia_nao_recebeu_treinamento"))),
            nome_familia_nao_recebeu=data.get(
                "data-treinamento-nome_familia_nao_recebeu_treinamento"),
            canais_apresentar_reclamacao=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-canais_apresentar_reclamacoes"))),
            apresentou_reclamacao=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-apresentou_reclamacao"))),
            canal_que_usou=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-canal_que_usou"))),
            outro_canal=data.get("data-reclamacoes-outro_canal"),
            tempo_gasto_resolver=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-tempo_gasto_resolver"))),
            ficou_satisfeito=Constants().get_dicionario().get(
                str(data.get("data-reclamacoes-ficou_satisfeito_solucao"))),
            ouviu_falar_vbg=Constants().get_dicionario().get(
                str(data.get("data-vbg-ouviu_falar_vbg"))),
            ja_foi_vitima_vbg=Constants().get_dicionario().get(
                str(data.get("data-vbg-ja_foi_vitima_vbg"))),
            canais_denunciar_vbg=Constants().get_dicionario().get(
                str(data.get("data-vbg-canais_denunciar_vbg"))),
            outro_canal_denuncia=data.get("data-vbg-outro_canal_denuncia"),
            teve_toda_assistencia=Constants().get_dicionario().get(
                str(data.get("data-vbg-teve_toda_assistencia"))),
            e_comum_vbg_comunidade=Constants().get_dicionario().get(
                str(data.get("data-vbg-e_comum_vbg_comunidade"))),
            casos_vbg_ouviu_falar=Constants().get_dicionario().get(
                str(data.get("data-vbg-casos_vbg_ouviu_falar"))),
            outro_caso_vbg_ouviu_falar=data.get(
                "data-vbg-outro_caso_vbg_ouviu_falar"),
            foto_caso_vbg_url=data.get("data-vbg-foto_caso_vbg")

        )
        questionario += 1
        inquerito.save()

    for data in get_data_from_spreadsheet("Inquerito_resultados", "data-germinacao_semente_uso_fertilizante-germinacao_semente_repeat"):
        tipo_semente_germinou = TipoSementeGerminou.objects.create(
            uuid=data.get("KEY"),
            nome_semente=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-germinacao_semente_repeat-tipo_semente_germinou"))),
            tempo_germinacao=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-germinacao_semente_repeat-tempo_germinacao"))),
            parent_key=data.get("PARENT_KEY")
        )

        tipo_semente_germinou.save()

    for data in get_data_from_spreadsheet("Inquerito_resultados", "data-germinacao_semente_uso_fertilizante-tipo_area_de_germinacao"):
        tipo_area_de_germinacao = TipoAreaGerminacao.objects.create(
            uuid=data.get("KEY"),
            nome_semente=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-tipo_area_de_germinacao-tipo_semente_germinou_area"))),
            area=Constants().get_dicionario().get(str(data.get(
                "data-germinacao_semente_uso_fertilizante-tipo_area_de_germinacao-tamanho_area_germinou"))),
            parent_key=data.get("PARENT_KEY")
        )

        tipo_area_de_germinacao.save()


def refresh_verificacao_semente_data():
    VerificacaoSementes.objects.all().delete()
    for data in get_data_from_spreadsheet("Ficha_verificacao_sementes", "Sheet1"):
        verificacao_semente = VerificacaoSementes.objects.create(
            data=data.get("data-apresentacao-data"),
            horas=data.get("data-apresentacao-horas"),
            provincia=data.get("data-apresentacao-provincia"),
            distrito=data.get("data-apresentacao-distrito"),
            posto_administrativo=data.get("data-apresentacao-posto_admin"),
            localidade=data.get("data-apresentacao-localidade"),
            comunidade=data.get("data-apresentacao-comunidade"),
            aldeia=data.get("data-apresentacao-aldeia"),
            local_especifico=data.get("data-apresentacao-local_especifico"),
            responsavel_local=data.get("data-apresentacao-responsavel_local"),
            contacto=data.get("data-apresentacao-contacto"),
            sementes_certificadas=Constants().get_numeros().get(
                str(data.get("data-sementes-sementes_certificadas"))),
            observacao1=data.get("data-sementes-observacao1"),
            foto1_url=data.get("data-sementes-foto1"),
            certificados_dentro_prazo=Constants().get_numeros().get(
                str(data.get("data-sementes-certificados_dentro_prazo"))),
            observacao2=data.get("data-sementes-observacao2"),
            foto2_url=data.get("data-sementes-foto2"),
            sementes_etiquetas=Constants().get_numeros().get(
                str(data.get("data-sementes-ementes_etiquetas"))),
            observacao3=data.get("data-sementes-observacao3"),
            foto3_url=data.get("data-sementes-foto3"),
            etiquetas_resistentes=Constants().get_numeros().get(
                str(data.get("data-sementes-etiquetas_resistente"))),
            observacao4=data.get("data-sementes-observacao4"),
            foto4_url=data.get("data-sementes-foto4"),
            etiquetas_duplicadas=Constants().get_numeros().get(
                str(data.get("data-sementes-etiquetas_duplicadas"))),
            observacao5=data.get("data-sementes-observacao5"),
            foto5_url=data.get("data-sementes-foto5"),
            pureza_dentro_padroes=Constants().get_numeros().get(
                str(data.get("data-sementes-pureza_dentro_padroes"))),
            observacao6=data.get("data-sementes-observacao6"),
            foto6_url=data.get("data-sementes-foto6"),
            semente_transportada_condicoes=Constants().get_numeros().get(
                str(data.get("data-sementes-semente_transportada_condicoes"))),
            observacao7=data.get("data-sementes-observacao6"),
            foto7_url=data.get("data-sementes-foto6"),
            sementes_armazenadas_condicoes=Constants().get_numeros().get(
                str(data.get("data-sementes-sementes_armazenadas_condicoes"))),
            observacao8=data.get("data-sementes-observacao8"),
            foto8_url=data.get("data-sementes-foto8"),
            embalagens_tem_info=data.get("data-sementes-embalagens_tem_info"),
            observacao9=data.get("data-sementes-observacao9"),
            foto9_url=data.get("data-sementes-foto9"),
            sementes_tratadas_produto_quimico=data.get(
                "data-sementes-sementes_tratadas_produto_quimico"),
            observacao10=data.get("data-sementes-observacao10"),
            foto10_url=data.get("data-sementes-foto10"),
            embalagem_selada=Constants().get_numeros().get(
                str(data.get("data-sementes-embalagem_selada"))),
            observacao11=data.get("data-sementes-observacao11"),
            foto11_url=data.get("data-sementes-foto11"),
            etiquetas_classificadas=data.get(
                "data-sementes-etiquetas_classificadas"),
            observacao12=data.get("data-sementes-observacao12"),
            foto12_url=data.get("data-sementes-foto12")

        )

        verificacao_semente.save()
        if len(str(verificacao_semente.embalagens_tem_info)) == 37:
            verificacao_semente.embalagens_tem_info = "Embalagem com toda informacao"
            verificacao_semente.save()
        if len(str(verificacao_semente.sementes_tratadas_produto_quimico)) == 10:
            verificacao_semente.sementes_tratadas_produto_quimico = "As sementes foram tratadas com algum produto químico e a embalagem apresenta todas informações"
            verificacao_semente.save()

        if len(str(verificacao_semente.etiquetas_classificadas)) == 14:
            verificacao_semente.etiquetas_classificadas = "As etiquetas estão classificadas de todas as 4 formas"
            verificacao_semente.save()


def home(request):
    refresh_inquerito_data()
    refresh_verificacao_semente_data()
    return HttpResponse(get_data_from_spreadsheet("Inquerito_resultados", "Folha1"))


# class IndexView(ListView):
#     template_name = "core/index.html"
#     context_object_name = "Inquerito_list"
#     model = Inquerito

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['inquerito'] = Inquerito.objects.all().count()
#         context['inquerito_nampula'] = Inquerito.objects.filter(
#             provincia="Nampula").count()
#         context['inquerito_cabo_delgado'] = Inquerito.objects.filter(
#             provincia="Cabo Delgado").count()

#         return context

#     def get_queryset(self):
#         return Inquerito.objects.all()


def index(request):
    inqueritos = Inquerito.objects.all().count()
    inquerito_nampula = Inquerito.objects.filter(provincia="Nampula").count()
    inquerito_cabo_delgado = Inquerito.objects.filter(
        provincia="Cabo Delgado").count()
    ficha_verificacao = VerificacaoSementes.objects.all().count()
    tem_machamba = Inquerito.objects.filter(familia_tem_machamba='Sim').count()
    nao_tem_machamba = Inquerito.objects.filter(
        familia_tem_machamba='Nao').count()
    machamba_familia_sim = Inquerito.objects.filter(
        machamba_familia="Sim").count()
    machamba_familia_nao = Inquerito.objects.filter(
        machamba_familia="Nao").count()
    emprestada = Inquerito.objects.filter(tipo_posse='Emprestada').count()
    alugada = Inquerito.objects.filter(tipo_posse='Alugada').count()
    outro = Inquerito.objects.filter(tipo_posse='Outro').count()
    comprou = Inquerito.objects.filter(forma_aquisicao='Comprou').count()
    alugada_f = Inquerito.objects.filter(forma_aquisicao='Alugada').count()
    cedido_lider = Inquerito.objects.filter(
        forma_aquisicao='Cedido Pelo Lider').count()
    cedido_governo = Inquerito.objects.filter(
        forma_aquisicao='Cedido Pelo Governo').count()
    outra_forma = Inquerito.objects.filter(forma_aquisicao='Outro').count()
    tamanho_machamba_05 = Inquerito.objects.filter(
        tamanho_machamba='0,5 ha').count()
    tamanho_machamba_15 = Inquerito.objects.filter(
        tamanho_machamba='1,5 ha').count()
    outro_tamanho = Inquerito.objects.filter(tamanho_machamba='Outro').count()
    zona_alta = Inquerito.objects.filter(local_machamba='Zona alta').count()
    zona_baixa = Inquerito.objects.filter(local_machamba='Zona baixa').count()
    pantano = Inquerito.objects.filter(local_machamba='Pantano').count()
    outra_zona = Inquerito.objects.filter(local_machamba='Outro').count()
    arenoso = Inquerito.objects.filter(caracteristica_solos='Arenoso').count()
    argiloso = Inquerito.objects.filter(
        caracteristica_solos='Argiloso').count()
    areno_argiloso = Inquerito.objects.filter(
        caracteristica_solos='Areno Argiloso').count()
    outra_caracteristica = Inquerito.objects.filter(
        caracteristica_solos='Outro').count()
    preto = Inquerito.objects.filter(cor_solo='Preto').count()
    castanho = Inquerito.objects.filter(cor_solo='Castanho').count()
    outra_cor = Inquerito.objects.filter(cor_solo='Outra').count()
    uso = Inquerito.objects.filter(historico_uso_solo='Em Uso').count()
    pousio = Inquerito.objects.filter(historico_uso_solo='Em Pousio').count()
    virgem = Inquerito.objects.filter(historico_uso_solo='Virgem').count()
    outro_historico = Inquerito.objects.filter(
        historico_uso_solo='Outro').count()
    menor_15 = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='Menor ou igual a 15 Minutos').count()
    tempo_15_45 = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='15 a 45 Minutos').count()
    tempo_45_1 = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='45 Minutos a 1 hora"').count()
    mais_1_hora = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='Mais que 1 hora').count()
    outro_tempo = Inquerito.objects.filter(
        tempo_gasto_casa_machamba='Outro').count()

    context = {'inqueritos': inqueritos, 'inquerito_nampula': inquerito_nampula,
               'inquerito_cabo_delgado': inquerito_cabo_delgado,
               'ficha_verificacao': ficha_verificacao, 'tem_machamba': tem_machamba,
               'nao_tem_machamba': nao_tem_machamba, 'machamba_familia_sim': machamba_familia_sim,
               'machamba_familia_nao': machamba_familia_nao, 'emprestada': emprestada,
               'alugada': alugada, 'outro': outro, 'alugada_f': alugada_f, 'cedido_lider': cedido_lider,
               'cedido_governo': cedido_governo, 'outra_forma': outra_forma, 'comprou': comprou,
               'tamanho_machamba_05': tamanho_machamba_05, 'tamanho_machamba_15': tamanho_machamba_15,
               'outro_tamanho': outro_tamanho, 'zona_baixa': zona_baixa, 'zona_alta': zona_alta,
               'pantano': pantano, 'outra_zona': outra_zona, 'arenoso': arenoso, 'argiloso': argiloso,
               'areno_argiloso': areno_argiloso, 'outra_caracteristica': outra_caracteristica,
               'preto': preto, 'castanho': castanho, 'outra_cor': outra_cor, 'uso': uso, 'pousio': pousio,
               'virgem': virgem, 'outro_historico': outro_historico, 'menor_15': menor_15, 'tempo_15_45': tempo_15_45,
               'tempo_45_1': tempo_45_1, 'mais_1_hora': mais_1_hora, 'outro_tempo': outro_tempo
               }

    return render(request, 'core/index.html', context)


class InqueritoListView(ListView):
    template_name = "core/inqueritos_list.html"
    queryset = Inquerito.objects.all()
    paginate_by = 10


def total_familia_tem_machamba(request):
    inqueritos = Inquerito.objects.filter(familia_tem_machamba='Sim').count()

    #     if inquerito.familia_tem_machamba == "Sim":
    #         count_sim += 1
    #     else:
    #         count_nao += 1
    # data.append(count_sim)
    # data.append(count_nao)
    # if count_sim:
    #     labels.append('Familia com Machamba')
    # elif count_nao:
    #     labels.append('Familia sem Machamba')
    print(inqueritos)
    return JsonResponse({'data': 'Teste'})
