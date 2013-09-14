import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'officer_1a':
		return

	actor.addSkill('expertise_of_group_buff_duration_1')

	actor.addSkillMod('expertise_buff_duration_line_of_group_buff', 15)
	actor.addSkillMod('expertise_aura_maintain', 1)
	actor.addSkillMod('expertise_action_line_of_group_buff', 5)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'officer_1a':
		return

	actor.removeSkill('expertise_of_group_buff_duration_1')

	actor.removeSkillMod('expertise_buff_duration_line_of_group_buff', 15)
	actor.removeSkillMod('expertise_aura_maintain', 1)
	actor.removeSkillMod('expertise_action_line_of_group_buff', 5)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return