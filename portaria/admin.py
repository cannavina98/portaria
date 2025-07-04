from django.contrib import admin
from .models import Cadastro, PaletControl, Motorista, Veiculos, ChecklistFrota, NfServicoPj, FuncPj


# Register your models here.

class CadastroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('placa', {'fields': ['placa']}),
        ('placa2', {'fields': ['placa2']}),
        ('motorista', {'fields': ['motorista']}),
        ('empresa',{'fields':['empresa']}),
        ('origem', {'fields':['origem']}),
        ('destino', {'fields': ['destino']}),
        ('tipo_mot', {'fields': ['tipo_mot']}),
        ('tipo_viagem', {'fields': ['tipo_viagem']}),
        ('hr_chegada', {'fields':['hr_chegada']}),
        ('hr_saida',{'fields':['hr_saida']}),
        ('autor', {'fields': ['autor']}),
    ]
    list_display = ('id','placa', 'placa2', 'motorista', 'empresa','origem','destino','tipo_viagem','tipo_mot','hr_chegada','hr_saida', 'autor')
admin.site.register(Cadastro, CadastroAdmin)

class PaletControlAdmin(admin.ModelAdmin):
    fieldsets = (
        ('loc_atual',{'fields':['loc_atual']}) ,
        ('ultima_viagem',{'fields':['ultima_viagem']}),
        ('origem',{'fields':['origem']}),
        ('destino',{'fields':['destino']}),
        ('placa_veic',{'fields':['placa_veic']})
    )
    list_display = ('id','loc_atual','ultima_viagem','origem','destino','placa_veic')
admin.site.register(PaletControl, PaletControlAdmin)

class MotoristaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Motorista, MotoristaAdmin)

class VeiculosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Veiculos, VeiculosAdmin)

class ChecklistFrotaAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChecklistFrota, ChecklistFrotaAdmin)

class NfServicoPjAdmin(admin.ModelAdmin):
    fieldsets = (
        ('funcionario',{'fields':['funcionario']}),
        ('premios_faculdade', {'fields':['premios_faculdade']}),
        ('ajuda_custo', {'fields':['ajuda_custo']}),
        ('adiantamento', {'fields':['adiantamento']}),
        ('convenio', {'fields':['convenio']}),
        ('data_emissao', {'fields':['data_emissao']}),
    )
    list_display = ('funcionario', 'premios_faculdade', 'ajuda_custo', 'adiantamento', 'convenio', 'data_emissao')

admin.site.register(NfServicoPj, NfServicoPjAdmin)

class FuncPjAdmin(admin.ModelAdmin):
    pass
admin.site.register(FuncPj, FuncPjAdmin)