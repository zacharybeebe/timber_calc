# timber_calc
Python module for calculating Timber data from tree species of the west coast


The 'Timber' class within timber_calc can be thought of as a single tree,
the required inputs are Species (by Species Code), Diameter at Breast Height (DBH), and
the Total Height of the tree.


The 'Timber' class creates three main dictionaries of tree data, 
although the other methods within Tymber can be used as well
for specific needs or testing.


The three methods that return the main dictionaries are...


1.)	tree_to_dict(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)
	
		As you can see this method requires three more parameters
		in addition to the intial Species Code, DBH and Height.

			Merch_DIB (Merchantable Diameter inside Bark) is the point along the
			stem that is considered merchantble, the diamter is in inches, 
			typically this value is 40% of the diameter of the stem at 17 feet, 
			also said as 40% of form. The method get_merch_dib_from_form(Form_Percent, Form_Height)
			can be used to get this dib - the defaults for Form_Percent and Form_Height are 40 and 17.
			Or you can simply put in a integer greater than zero as the parameters.

			Preferred_Log_Length is the log length in feet that is preferred; in forestry typcially
			this value is 40 feet or 32 feet.

			Minimum_Log_Length is the log length in feet that is minimum necessary for a merchantble log;
			in forestry this value is typically 16 feet or 8 feet, but this can be set to zero to obtain
			the full scale of the tree up to the merchantble height.
	
		This returns a dictionary of data for the tree, inlcuding...
			Species
			DBH
			Merch DIB
			Total Height
			Merch Height
			HDR (Height to Diameter Ratio)
			BA (Basal Area)
			RD (Relative Density)
			Board Feet (Volume of the tree)
			Cubic Feet (Volume of the tree)
			VBAR (Volume to Basal Area Ratio - in Board Feet per Basal Area)




2.)	tree_per_acre_to_dict(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length, Plot_Factor)
		
		This method requires one more parameter than tree_to_dict, which is Plot_Factor
			
			Plot_Factor is the factor of the plot in which the tree was counted, 
			and is used to get the Trees per Acre that the indvidual tree represents.

				For Variable Radius Plots enter the Basal Area Factor (BAF) 
				of the plot.

				For Fixed Radius Plots enter the negative-inverse of the fixed
				radius - for example a 1/30th acre plot would be entered as -30.
		
		This method returns a dictionary with the following data...
			TPA (Trees per Acre)
			BA per Acre (Basal Area per Acre)
			RD per Acre (Relative Density per Acre)
			Board Feet per Acre
			Cubic Feet per Acre



3.)	log_data_to_dict(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)
		
		This method requires the same inputs as tree_to_dict.

		This method returns a dictionary with the following data...
			For each log of the tree (which is the key of the dictionary) it calculates
				Stem Height (of the top of the log)
				DIB (of the top of the log)
				Log Length
				Log Grade
				Log Board Feet
				Log Cubic Feet




The species available for calculation are below and must have the correct species code...

	'DF': 'DOUGLAS-FIR'
	'WH': 'WESTERN HEMLOCK'
	'RC': 'WESTERN REDCEDAR'
	'SS': 'SITKA SPRUCE'
	'ES': 'ENGLEMANN SPRUCE'
	'SF': 'SILVER FIR'
	'GF': 'GRAND FIR'
	'NF': 'NOBLE FIR'
	'WL': 'WESTERN LARCH'
	'WP': 'WHITE PINE'
	'PP': 'PONDEROSA PINE'
	'LP': 'LODGEPOLE PINE'
	'JP': 'JEFFERY PINE'
	'SP': 'SUGAR PINE'
	'WF': 'WHITE FIR'
	'RF': 'RED FIR'
	'RW': 'COASTAL REDWOOD'
	'IC': 'INSENCE CEDAR'
	'RA': 'RED ALDER'
	'BM': 'BIGLEAF MAPLE'
	'CW': 'BLACK COTTONWOOD'
	'AS': 'QUAKING ASPEN'


An example of how to get started is....

	from timber_calc import Timber

	spp = 'DF'		# Douglas Fir
	dbh = 16.6		# inches
	hgt = 95		# feet
	pref_log = 40		# feet
	min_log = 0		# feet
	plot_factor = -20

	tree = Timber(spp, dbh, hgt)

	merch_dib = tree.get_merch_dib_from_form()

	print(tree.tree_to_dict(merch_dib, pref_log, min_log))
	print(tree.tree_per_acre_to_dict(merch_dib, pref_log, min_log, plot_factor))
	print(tree.log_data_to_dict(merch_dib, pref_log, min_log))
