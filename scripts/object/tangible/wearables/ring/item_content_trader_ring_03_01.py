import sys

def setup(core, object):
	object.setAttachment('objType', 'ring')
	object.setStfFilename('static_item_n')
	object.setStfName('item_content_trader_ring_03_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_content_trader_ring_03_01')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 6)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:general_assembly', 6)
	object.setStringAttribute('class_required', 'Trader')
	object.setAttachment('radial_filename', 'ring/unity')
	return