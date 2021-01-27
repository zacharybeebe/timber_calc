# timberscale
Python module for calculating Timber data from tree species of the west coast


The 'Timber' class within timberscale can be thought of as a single tree,
the required inputs are Species (by Species Code), Diameter at Breast Height (DBH), and
the Total Height of the tree.


The 'Timber' class creates four main dictionaries of tree data, 
although the other methods within Timber can be used as well
for specific needs or testing.



The four methods that return the main dictionaries are...


1.)	tree_single(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)
	
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
	
		This method returns a dictionary with the following keys...
			SPP:      (Species Code, Species Common Name)
                	DBH:      Diameter at Breast Height (inches)
                	M_DIB:    Merchantble Diameter Inside Bark (inches)
                	T_HGT:    Total Height (feet)
                	M_HGT:    Merchantble Height (feet)
                	HDR:      Height to Diameter Ratio
                	BA:       Basal Area (square feet)
                	RD:       Relative Density
                	BF:       Total Board Feet
                	CF:       Total Cubic Feet
                	VBAR:     Volume to Basal Area Ratio (board feet per 1 sqft of basal area)




2.)	tree_acre(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length, Plot_Factor)
		
		This method requires one more parameter than tree_to_dict, which is Plot_Factor
			
			Plot_Factor is the factor of the plot in which the tree was counted, 
			and is used to get the Trees per Acre that the indvidual tree represents.

				For Variable Radius Plots enter the Basal Area Factor (BAF) 
				of the plot.

				For Fixed Radius Plots enter the negative-inverse of the fixed
				radius - for example a 1/30th acre plot would be entered as -30.
		
		This method returns a dictionary with the following keys...
			TPA:      Trees per Acre
                	BA_AC:    Basal Area per acre
                	RD_AC:    Relative Density per acre
                	BF_AC:    Total Board Feet per acre
                	CF_AC:    Total Cubic Feet per acre




3.)	log_single(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)
		
		This method requires the same inputs as tree_single.

		This method returns a dictionary with the following data...
			For each log of the tree (which are the main keys of the dictionary) 
			it returns a dictionary with the following keys...
				S_HGT:    Stem Height of the top of the log (feet)
                		DIB:      Diameter Inside Bark at the top of the log (inches)
                		L_LGT:    Length of log (feet)
                		L_GRD:    (Grade Code, Grade Name) of the log
                		L_BF:     Board Feet of the log
                		L_CF:     Cubic Feet of the log




4.)	log_acre(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length, Plot_Factor)
		
		This method requires the same inputs as tree_acre.

		This method returns a dictionary with the following data...
			For each log of the tree (which are the main keys of the dictionary) 
			it returns a dictionary with the following keys...
				S_HGT:    Stem Height of the top of the log (feet)
                		DIB:      Diameter Inside Bark at the top of the log (inches)
                		L_LGT:    Length of log (feet)
                		L_GRD:    (Grade Code, Grade Name) of the log
                		L_BF_AC:  Board Feet of the log per acre
                		L_CF_AC:  Cubic Feet of the log per acre
				L_CT_AC:  Logs per acre



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

	from timberscale import Timber

	spp = 'DF'		# Douglas Fir
	dbh = 16.6		# inches
	hgt = 95		# feet
	pref_log = 40		# feet
	min_log = 0		# feet
	plot_factor = -20

	tree = Timber(spp, dbh, hgt)

	merch_dib = tree.merch_dib()

	print(tree.tree_single(merch_dib, pref_log, min_log))
	print(tree.tree_acre(merch_dib, pref_log, min_log, plot_factor))
	print(tree.log_single(merch_dib, pref_log, min_log))
	print(tree.log_acre(merch_dib, pref_log, min_log, plot_factor))

		


