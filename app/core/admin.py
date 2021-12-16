from django.contrib import admin


from core.models import Inquerito, TipoSementeGerminou, TipoAreaGerminacao, VerificacaoSementes


class InqueritoAdmin(admin.ModelAdmin):
    ordering = ["nome_agg_familiar", ]
    list_display = ["numero_questionario", "codigo_familia", "nome_agg_familiar",
                    "local_entrevista", "nome_inquiridor", "tipo_documento"]


class VerificacaoSementesAdmin(admin.ModelAdmin):
    ordering = ["responsavel_local", ]
    list_display = ["responsavel_local", "data", "horas", "provincia", "embalagens_tem_info",
                    "sementes_tratadas_produto_quimico", "etiquetas_classificadas"]


admin.site.register(Inquerito, InqueritoAdmin)
admin.site.register(TipoAreaGerminacao)
admin.site.register(TipoSementeGerminou)
admin.site.register(VerificacaoSementes, VerificacaoSementesAdmin)
