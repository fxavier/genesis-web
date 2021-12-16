from django.db import models
from django.urls import reverse


class Inquerito(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    codigo_familia = models.CharField(max_length=100)
    data_inquerito = models.DateField()
    nome_inquiridor = models.CharField(max_length=255)
    numero_questionario = models.IntegerField(default=0)
    local_entrevista = models.CharField(max_length=100)
    gps_local_lat_long = models.CharField(max_length=255)
    gps_local_accuracy = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_beneficiario = models.CharField(max_length=100)
    tipo_familia = models.CharField(max_length=100)
    nome_agg_familiar = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    photo_doc_url = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=100)
    outro_genero = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    parte_bd = models.CharField(max_length=20)
    criterios_elegib_agg_familiar = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    posto_administrativo = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    comunidade = models.CharField(max_length=100)
    ficha = models.CharField(max_length=100)
    familia_tem_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    machamba_familia = models.CharField(max_length=100, null=True, blank=True)
    tipo_posse = models.CharField(max_length=100, null=True, blank=True)
    outro_tipo_posse = models.CharField(max_length=100, null=True, blank=True)
    forma_aquisicao = models.CharField(max_length=100, null=True, blank=True)
    outra_forma_aquisicao = models.CharField(
        max_length=100, null=True, blank=True)
    quando_conseguiu_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    outra_data = models.CharField(max_length=100, null=True, blank=True)
    tamanho_machamba = models.CharField(max_length=100, null=True, blank=True)
    outro_tamanho = models.CharField(max_length=100, null=True, blank=True)
    local_machamba = models.CharField(max_length=100, null=True, blank=True)
    outro_local_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    caracteristica_solos = models.CharField(
        max_length=100, null=True, blank=True)
    outra_caracteristica_solos = models.CharField(
        max_length=100, null=True, blank=True)
    cor_solo = models.CharField(max_length=100, null=True, blank=True)
    outra_cor = models.CharField(max_length=100, null=True, blank=True)
    historico_uso_solo = models.CharField(
        max_length=100, null=True, blank=True)
    outro_historico_uso_solo = models.CharField(
        max_length=100, null=True, blank=True)
    tempo_gasto_casa_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    outro_tempo_gasto = models.CharField(max_length=100, null=True, blank=True)
    recebeu_semente = models.CharField(max_length=100, null=True, blank=True)
    quando_recebeu = models.CharField(max_length=100, null=True, blank=True)
    outra_data_recebeu = models.CharField(
        max_length=100, null=True, blank=True)
    identificacao_lote = models.CharField(
        max_length=100, null=True, blank=True)
    tipo_kit = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_a = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_a = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_b = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_b = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_c = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_c = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_d = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_d = models.CharField(max_length=100, null=True, blank=True)
    conservacao_semente = models.CharField(
        max_length=100, null=True, blank=True)
    foto_semente_url = models.CharField(max_length=255, null=True, blank=True)
    de_quem_recebeu_semente = models.CharField(
        max_length=100, null=True, blank=True)
    outro_de_quem_recebeu_semente = models.CharField(
        max_length=100, null=True, blank=True)
    quem_escolheu_kit = models.CharField(max_length=100, null=True, blank=True)
    outro_quem_escolheu_kit = models.CharField(
        max_length=100, null=True, blank=True)
    quando_realizou_sementeira = models.CharField(
        max_length=100, null=True, blank=True)
    familia_necess_nao_recebeu = models.CharField(
        max_length=100, null=True, blank=True)
    nome_familia = models.CharField(max_length=100, null=True, blank=True)
    sementes_germinou = models.CharField(max_length=100, null=True, blank=True)
    foto_sementes_germinou_url = models.CharField(
        max_length=255, null=True, blank=True)
    semente_nao_germinou = models.CharField(
        max_length=100, null=True, blank=True)
    usou_fertilizante = models.CharField(max_length=100, null=True, blank=True)
    tipo_fertilizante = models.CharField(max_length=100, null=True, blank=True)
    outro_tipo_fertilizante = models.CharField(
        max_length=100, null=True, blank=True)
    momento_usou_adubo = models.CharField(
        max_length=100, null=True, blank=True)
    outro_momento_usou_adubo = models.CharField(
        max_length=100, null=True, blank=True)
    adubo_usado = models.CharField(max_length=100, null=True, blank=True)
    recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    lugar_treinamento = models.CharField(max_length=100, null=True, blank=True)
    outro_lugar_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    de_quem_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    outro_de_quem_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    quando_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    outro_quando_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    tipo_treinamento = models.CharField(max_length=100, null=True, blank=True)
    recebeu_visita_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    de_quem_recebeu_visita_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    outro_de_quem_recebeu_visita_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    momento_recebeu_visita = models.CharField(
        max_length=100, null=True, blank=True)
    familia_nao_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    nome_familia_nao_recebeu = models.CharField(
        max_length=100, null=True, blank=True)
    canais_apresentar_reclamacao = models.CharField(
        max_length=100, null=True, blank=True)
    apresentou_reclamacao = models.CharField(
        max_length=100, null=True, blank=True)
    canal_que_usou = models.CharField(max_length=100, null=True, blank=True)
    outro_canal = models.CharField(max_length=100, null=True, blank=True)
    tempo_gasto_resolver = models.CharField(
        max_length=100, null=True, blank=True)
    ficou_satisfeito = models.CharField(max_length=100, null=True, blank=True)
    ouviu_falar_vbg = models.CharField(max_length=100, null=True, blank=True)
    ja_foi_vitima_vbg = models.CharField(max_length=100, null=True, blank=True)
    canais_denunciar_vbg = models.CharField(
        max_length=100, null=True, blank=True)
    outro_canal_denuncia = models.CharField(
        max_length=100, null=True, blank=True)
    teve_toda_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    e_comum_vbg_comunidade = models.CharField(
        max_length=100, null=True, blank=True)
    casos_vbg_ouviu_falar = models.CharField(
        max_length=100, null=True, blank=True)
    outro_caso_vbg_ouviu_falar = models.CharField(
        max_length=100, null=True, blank=True)
    foto_caso_vbg_url = models.CharField(max_length=255, null=True, blank=True)
    comentario_geral = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome_agg_familiar

    def get_absolute_url(self):
        return reverse('core:inquerito')


class TipoSementeGerminou(models.Model):
    uuid = models.CharField(max_length=255, null=True, blank=True)
    nome_semente = models.CharField(max_length=100, null=True, blank=True)
    tempo_germinacao = models.CharField(max_length=100, null=True, blank=True)
    parent_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.uuid


class TipoAreaGerminacao(models.Model):
    uuid = models.CharField(max_length=255, null=True, blank=True)
    nome_semente = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    parent_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.uuid


class VerificacaoSementes(models.Model):
    data = models.DateField()
    horas = models.TimeField()
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    posto_administrativo = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    comunidade = models.CharField(max_length=100)
    aldeia = models.CharField(max_length=100)
    local_especifico = models.CharField(max_length=100)
    responsavel_local = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    sementes_certificadas = models.CharField(
        max_length=10, null=True, blank=True)
    observacao1 = models.CharField(max_length=255, null=True, blank=True)
    foto1_url = models.CharField(max_length=255, null=True, blank=True)
    certificados_dentro_prazo = models.CharField(
        max_length=10, null=True, blank=True)
    observacao2 = models.CharField(max_length=255, null=True, blank=True)
    foto2_url = models.CharField(max_length=255, null=True, blank=True)
    sementes_etiquetas = models.CharField(max_length=10, null=True, blank=True)
    observacao3 = models.CharField(max_length=255, null=True, blank=True)
    foto3_url = models.CharField(max_length=255, null=True, blank=True)
    etiquetas_resistentes = models.CharField(
        max_length=10, null=True, blank=True)
    observacao4 = models.CharField(max_length=255, null=True, blank=True)
    foto4_url = models.CharField(max_length=255, null=True, blank=True)
    etiquetas_duplicadas = models.CharField(
        max_length=10, null=True, blank=True)
    observacao5 = models.CharField(max_length=255, null=True, blank=True)
    foto5_url = models.CharField(max_length=255, null=True, blank=True)
    pureza_dentro_padroes = models.CharField(
        max_length=10, null=True, blank=True)
    observacao6 = models.CharField(max_length=255, null=True, blank=True)
    foto6_url = models.CharField(max_length=255, null=True, blank=True)
    semente_transportada_condicoes = models.CharField(
        max_length=10, null=True, blank=True)
    observacao7 = models.CharField(max_length=255, null=True, blank=True)
    foto7_url = models.CharField(max_length=255, null=True, blank=True)
    sementes_armazenadas_condicoes = models.CharField(
        max_length=10, null=True, blank=True)
    observacao8 = models.CharField(max_length=255, null=True, blank=True)
    foto8_url = models.CharField(max_length=255, null=True, blank=True)
    embalagens_tem_info = models.CharField(
        max_length=255, null=True, blank=True)
    observacao9 = models.CharField(max_length=255, null=True, blank=True)
    foto9_url = models.CharField(max_length=255, null=True, blank=True)
    sementes_tratadas_produto_quimico = models.CharField(
        max_length=255, null=True, blank=True)
    observacao10 = models.CharField(max_length=255, null=True, blank=True)
    foto10_url = models.CharField(max_length=255, null=True, blank=True)
    embalagem_selada = models.CharField(max_length=10, null=True, blank=True)
    observacao11 = models.CharField(max_length=255, null=True, blank=True)
    foto11_url = models.CharField(max_length=255, null=True, blank=True)
    etiquetas_classificadas = models.CharField(
        max_length=255, null=True, blank=True)
    observacao12 = models.CharField(max_length=255, null=True, blank=True)
    foto12_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.responsavel_local} - {self.data} - {self.horas}'
