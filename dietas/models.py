from django.db import models
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from fcred.models import Alimento
from usuarios.models import User
from django.db.models import Sum
from recomendado.models import Recomendado


# http://portal.anvisa.gov.br/documents/33916/394219/RDC_269_2005.pdf/2e95553c-a482-45c3-bdd1-f96162d607b3

class Dieta(models.Model):
    nome = models.CharField(max_length=255)
    alimentos = models.ManyToManyField(Alimento, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observacao = models.TextField(max_length=600, blank=True, null=True)
    recomendacao = models.ForeignKey(Recomendado,on_delete=models.CASCADE,null=True)

    total_alanine_g = models.FloatField(blank=True, null=True)
    total_arginine_g = models.FloatField(blank=True, null=True)
    total_ashes_g = models.FloatField(blank=True, null=True)
    total_aspartic_g = models.FloatField(blank=True, null=True)
    total_calcium_mg = models.FloatField(blank=True, null=True)
    total_carbohydrate_g = models.FloatField(blank=True, null=True)
    total_cholesterol_mg = models.FloatField(blank=True, null=True)
    total_copper_mg = models.FloatField(blank=True, null=True)
    total_cystine_g = models.FloatField(blank=True, null=True)
    total_energy_kcal = models.FloatField(blank=True, null=True)
    total_energy_kj = models.FloatField(blank=True, null=True)
    total_fiber_g = models.FloatField(blank=True, null=True)
    total_glutamic_g = models.FloatField(blank=True, null=True)
    total_glycine_g = models.FloatField(blank=True, null=True)
    total_histidine_g = models.FloatField(blank=True, null=True)
    total_humidity_percents = models.FloatField(blank=True, null=True)
    total_iron_mg = models.FloatField(blank=True, null=True)
    total_isoleucine_g = models.FloatField(blank=True, null=True)
    total_leucine_g = models.FloatField(blank=True, null=True)
    total_lipidius_g = models.FloatField(blank=True, null=True)
    total_lysine_g = models.FloatField(blank=True, null=True)
    total_magnesium_mg = models.FloatField(blank=True, null=True)
    total_manganes_mg = models.FloatField(blank=True, null=True)
    total_methionine_g = models.FloatField(blank=True, null=True)
    total_monounsaturated_g = models.FloatField(blank=True, null=True)
    total_niacin_mg = models.FloatField(blank=True, null=True)
    total_phenylalanine_g = models.FloatField(blank=True, null=True)
    total_phosphorus_mg = models.FloatField(blank=True, null=True)
    total_polyunsaturated_g = models.FloatField(blank=True, null=True)
    total_potassium_mg = models.FloatField(blank=True, null=True)
    total_proline_g = models.FloatField(blank=True, null=True)
    total_protein_g = models.FloatField(blank=True, null=True)
    total_pyridoxine_mg = models.FloatField(blank=True, null=True)
    total_rae_mcg = models.FloatField(blank=True, null=True)
    total_re_mcg = models.FloatField(blank=True, null=True)
    total_retinol_mcg = models.FloatField(blank=True, null=True)
    total_riboflavin_mg = models.FloatField(blank=True, null=True)
    total_saturated_g = models.FloatField(blank=True, null=True)
    total_serine_g = models.FloatField(blank=True, null=True)
    total_sodium_mg = models.FloatField(blank=True, null=True)
    total_threonine_g = models.FloatField(blank=True, null=True)
    total_tiamina_mg = models.FloatField(blank=True, null=True)
    total_tryptophan_g = models.FloatField(blank=True, null=True)
    total_tyrosine_g = models.FloatField(blank=True, null=True)
    total_valine_g = models.FloatField(blank=True, null=True)
    total_vitaminc_mg = models.FloatField(blank=True, null=True)
    total_zinc_mg = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'dieta'


@receiver(m2m_changed, sender=Dieta.alimentos.through)
def alimento_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    pk_set = kwargs.pop('pk_set', None)
    action = kwargs.pop('action', None)
    # if action == "post_add":
    alimentos = instance.alimentos.all()
    print(alimentos)

    instance.total_alanines_g = 0
    instance.total_arginine_g = 0
    instance.total_ashes_g = 0
    instance.total_aspartic_g = 0
    instance.total_calcium_mg = 0
    instance.total_carbohydrate_g = 0
    instance.total_cholesterol_mg = 0
    instance.total_copper_mg = 0
    instance.total_cystine_g = 0
    instance.total_energy_kcal = 0
    instance.total_energy_kj = 0
    instance.total_fiber_g = 0
    instance.total_glutamic_g = 0
    instance.total_glycine_g = 0
    instance.total_histidine_g = 0
    instance.total_humidity_percents = 0
    instance.total_iron_mg = 0
    instance.total_isoleucine_g = 0
    instance.total_leucine_g = 0
    instance.total_lipidius_g = 0
    instance.total_lysine_g = 0
    instance.total_magnesium_mg = 0
    instance.total_manganes_mg = 0
    instance.total_methionine_g = 0
    instance.total_monounsaturated_g = 0
    instance.total_niacin_mg = 0
    instance.total_phenylalanine_g = 0
    instance.total_phosphorus_mg = 0
    instance.total_polyunsaturated_g = 0
    instance.total_potassium_mg = 0
    instance.total_proline_g = 0
    instance.total_protein_g = 0
    instance.total_pyridoxine_mg = 0
    instance.total_rae_mcg = 0
    instance.total_re_mcg = 0
    instance.total_retinol_mcg = 0
    instance.total_riboflavin_mg = 0
    instance.total_saturated_g = 0
    instance.total_serine_g = 0
    instance.total_sodium_mg = 0
    instance.total_threonine_g = 0
    instance.total_tiamina_mg = 0
    instance.total_tryptophan_g = 0
    instance.total_tyrosine_g = 0
    instance.total_valine_g = 0
    instance.total_vitaminc_mg = 0
    instance.total_zinc_mg = 0

    for alimento in alimentos:
        instance.total_alanines_g = instance.total_alanines_g + alimento.alanines_g
        instance.total_arginine_g = instance.total_arginine_g + alimento.arginine_g
        instance.total_ashes_g = instance.total_ashes_g + alimento.ashes_g

        instance.total_aspartic_g = instance.total_aspartic_g + alimento.aspartic_g
        instance.total_calcium_mg = instance.total_calcium_mg + alimento.calcium_mg
        instance.total_carbohydrate_g = instance.total_carbohydrate_g + alimento.carbohydrate_g
        instance.total_cholesterol_mg = instance.total_cholesterol_mg + alimento.cholesterol_mg
        instance.total_copper_mg = instance.total_copper_mg + alimento.copper_mg
        instance.total_cystine_g = instance.total_cystine_g + alimento.cystine_g
        instance.total_energy_kcal = instance.total_energy_kcal + alimento.energy_kcal
        instance.total_energy_kj = instance.total_energy_kj + alimento.energy_kj
        instance.total_fiber_g = instance.total_fiber_g + alimento.fiber_g
        instance.total_glutamic_g = instance.total_glutamic_g + alimento.glutamic_g
        instance.total_glycine_g = instance.total_glycine_g + alimento.glycine_g
        instance.total_histidine_g = instance.total_histidine_g + alimento.histidine_g
        instance.total_humidity_percents = instance.total_humidity_percents + alimento.humidity_percents
        instance.total_iron_mg = instance.total_iron_mg + alimento.iron_mg
        instance.total_isoleucine_g = instance.total_isoleucine_g + alimento.isoleucine_g
        instance.total_leucine_g = instance.total_leucine_g + alimento.leucine_g
        instance.total_lipidius_g = instance.total_lipidius_g + alimento.lipidius_g
        instance.total_lysine_g = instance.total_lysine_g + alimento.lysine_g
        instance.total_magnesium_mg = instance.total_magnesium_mg + alimento.magnesium_mg
        instance.total_manganes_mg = instance.total_manganes_mg + alimento.manganes_mg
        instance.total_methionine_g = instance.total_methionine_g + alimento.methionine_g
        instance.total_monounsaturated_g = instance.total_monounsaturated_g + alimento.monounsaturated_g
        instance.total_niacin_mg = instance.total_niacin_mg + alimento.niacin_mg
        instance.total_phenylalanine_g = instance.total_phenylalanine_g + alimento.phenylalanine_g
        instance.total_phosphorus_mg = instance.total_phosphorus_mg + alimento.phosphorus_mg
        instance.total_polyunsaturated_g = instance.total_polyunsaturated_g + alimento.polyunsaturated_g
        instance.total_potassium_mg = instance.total_potassium_mg + alimento.potassium_mg
        instance.total_proline_g = instance.total_proline_g + alimento.proline_g
        instance.total_protein_g = instance.total_protein_g + alimento.protein_g
        instance.total_pyridoxine_mg = instance.total_pyridoxine_mg + alimento.pyridoxine_mg
        instance.total_rae_mcg = instance.total_rae_mcg + alimento.rae_mcg
        instance.total_re_mcg = instance.total_re_mcg + alimento.re_mcg
        instance.total_retinol_mcg = instance.total_retinol_mcg + alimento.retinol_mcg
        instance.total_riboflavin_mg = instance.total_riboflavin_mg + alimento.riboflavin_mg
        instance.total_saturated_g = instance.total_saturated_g + alimento.saturated_g
        instance.total_serine_g = instance.total_serine_g + alimento.serine_g
        instance.total_sodium_mg = instance.total_sodium_mg + alimento.sodium_mg
        instance.total_threonine_g = instance.total_threonine_g + alimento.threonine_g
        instance.total_tiamina_mg = instance.total_tiamina_mg + alimento.tiamina_mg
        instance.total_tryptophan_g = instance.total_tryptophan_g + alimento.tryptophan_g
        instance.total_tyrosine_g = instance.total_tyrosine_g + alimento.tyrosine_g
        instance.total_valine_g = instance.total_valine_g + alimento.valine_g
        instance.total_vitaminc_mg = instance.total_vitaminc_mg + alimento.vitaminc_mg
        instance.total_zinc_mg = instance.total_zinc_mg + alimento.zinc_mg

    instance.save()
