import sys
from services.equipment import BonusSetTemplate
from java.util import Vector

def addBonusSet(core):
	bonusSet = BonusSetTemplate("set_bonus_medic_dps")
	
	bonusSet.addRequiredItem("item_band_set_medic_dps_01_01")
	bonusSet.addRequiredItem("item_ring_set_medic_dps_01_01")
	bonusSet.addRequiredItem("item_necklace_set_medic_dps_01_01")
	bonusSet.addRequiredItem("item_bracelet_r_set_medic_dps_01_01")
	bonusSet.addRequiredItem("item_bracelet_l_set_medic_dps_01_01")
	
	core.equipmentService.addBonusSetTemplate(bonusSet)
	
def handleChange(core, creature, set):
	wornItems = set.getWornTemplateCount(creature)
	
	if wornItems == 3:
		core.buffService.addBuffToCreature(creature, "set_bonus_medic_dps_1", creature)
		creature.sendSystemMessage('@set_bonus:set_bonus_medic_dps_1_sys', 0)
	elif wornItems == 4:
		core.buffService.addBuffToCreature(creature, "set_bonus_medic_dps_2", creature)
		creature.sendSystemMessage('@set_bonus:set_bonus_medic_dps_2_sys', 0)
	elif wornItems == 5:
		core.buffService.addBuffToCreature(creature, "set_bonus_medic_dps_3", creature)
		creature.sendSystemMessage('@set_bonus:set_bonus_medic_dps_3_sys', 0)
	else:
		core.buffService.removeBuffFromCreatureByName(creature, "set_bonus_medic_dps_1")
		core.buffService.removeBuffFromCreatureByName(creature, "set_bonus_medic_dps_2")
		core.buffService.removeBuffFromCreatureByName(creature, "set_bonus_medic_dps_3")