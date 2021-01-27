import math


##### TIMBER CLASS
class Timber(object):
    ## TAPER EQUATION FUNCTIONS
    def czaplewski(DBH, Total_Height, Stem_Height, **kwargs):
        Z = Stem_Height / Total_Height
        Z2 = (Stem_Height ** 2) / (Total_Height ** 2)
        
        if Z >= kwargs['a']:
            I1 = 0
        else: 
            I1 = 1
        if Z >= kwargs['b']:
            I2 = 0
        else: 
            I2 = 1
            
        return DBH * math.sqrt((kwargs['c'] * (Z - 1)) + (kwargs['d'] * (Z2 - 1)) +
                               (kwargs['e'] * ((kwargs['a'] - Z) ** 2) * I1) + (kwargs['f'] * ((kwargs['b'] - Z) ** 2) * I2))



    def kozak1969(DBH, Total_Height, Stem_Height, **kwargs):        
        Z = Stem_Height / Total_Height
        Z2 = (Stem_Height ** 2) / (Total_Height ** 2)
        
        return DBH * math.sqrt(kwargs['a'] + (kwargs['b'] * Z) + (kwargs['c'] * Z2))


    def kozak1988(DBH, Total_Height, Stem_Height, **kwargs):
        Z = Stem_Height / Total_Height

        return (kwargs['a'] * (DBH ** kwargs['b']) * (kwargs['c'] ** DBH)) * ((1 - (Z ** 0.5)) / (1 - (kwargs['d'] ** 0.5))) ** ((kwargs['e'] * (Z ** 2)) +
                                                                                                                                 (kwargs['f'] * math.log(Z + 0.001)) +
                                                                                                                                 (kwargs['g'] * (Z ** 0.5)) +
                                                                                                                                 (kwargs['h'] * math.exp(Z)) +
                                                                                                                                 (kwargs['i'] * (DBH / Total_Height)))


    def wensel(DBH, Total_Height, Stem_Height, **kwargs):
        Z = Stem_Height / Total_Height
        X = (kwargs['c'] + (kwargs['d'] * DBH) + (kwargs['e'] * Total_Height))
        
        return DBH * (kwargs['a'] - (X * (math.log(1 - (((Stem_Height - 1)/(Total_Height - 1)) ** kwargs['b']) * (1 - math.exp(kwargs['a'] / X))))))
    


    EQUATION_DICT = {'CZA': czaplewski,
                     'KOZ69': kozak1969,
                     'KOZ88': kozak1988,
                     'WEN': wensel}

    
    ALL_SPECIES_NAMES = {'DF': 'DOUGLAS-FIR',
                         'WH': 'WESTERN HEMLOCK',
                         'RC': 'WESTERN REDCEDAR',
                         'SS': 'SITKA SPRUCE',
                         'ES': 'ENGLEMANN SPRUCE',
                         'SF': 'SILVER FIR',
                         'GF': 'GRAND FIR',
                         'NF': 'NOBLE FIR',
                         'WL': 'WESTERN LARCH',
                         'WP': 'WHITE PINE',
                         'PP': 'PONDEROSA PINE',
                         'LP': 'LODGEPOLE PINE',
                         'JP': 'JEFFERY PINE',
                         'SP': 'SUGAR PINE',
                         'WF': 'WHITE FIR',
                         'RF': 'RED FIR',
                         'RW': 'COASTAL REDWOOD',
                         'IC': 'INSENCE CEDAR',
                         'RA': 'RED ALDER',
                         'BM': 'BIGLEAF MAPLE',
                         'CW': 'BLACK COTTONWOOD',
                         'AS': 'QUAKING ASPEN'}


    ## LOG GRADE LIST FORMAT: [(Minimum DIB, Minimum Log Length, Grade)]
    OFFICIAL_GRADES = {'DF': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'WH': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'RC': [(28, 16, "S1"), (20, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'SS': [(24, 12, "S1"), (20, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'ES': [(24, 17, "P3"), (20, 16, "S1"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'SF': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'GF': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'NF': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'WL': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'WP': [(24, 17, "P3"), (20, 16, "S1"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],                  
                       'PP': [(24, 12, "S2"), (20, 16, "S3"), (12, 12, "S4"), (6, 1, "S5"), (5, 1, "S6"), (1, 1, 'UT')],                 
                       'LP': [(24, 17, "P3"), (20, 16, "S1"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'JP': [(24, 12, "S2"), (20, 16, "S3"), (12, 12, "S4"), (6, 1, "S5"), (5, 1, "S6"), (1, 1, 'UT')],
                       'SP': [(24, 12, "S2"), (20, 16, "S3"), (12, 12, "S4"), (6, 1, "S5"), (5, 1, "S6"), (1, 1, 'UT')],
                       'WF': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'RF': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'RW': [(24, 17, "P3"), (16, 17, "SM"), (12, 12, "S2"), (6, 1, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'IC': [(24, 12, "S2"), (20, 16, "S3"), (12, 12, "S4"), (6, 1, "S5"), (5, 1, "S6"), (1, 1, 'UT')],
                       'RA': [(16, 8, "S1"), (12, 8, "S2"), (10, 8, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'BM': [(16, 8, "S1"), (12, 8, "S2"), (10, 8, "S3"), (5, 1, "S4"), (1, 1, 'UT')],
                       'CW': [(24, 8, "P3"), (10, 8, "S1"), (6, 8, "S2"), (5, 1, "S4"), (1, 1, 'UT')],
                       'AS': [(16, 8, "S1"), (12, 8, "S2"), (10, 8, "S3"), (5, 1, "S4"), (1, 1, 'UT')]}

    GRADE_NAMES = {'P3': 'PEELER 3',
                   'SM': 'SPECIAL MILL',
                   'S1': 'SAW 1',
                   'S2': 'SAW 2',
                   'S3': 'SAW 3',
                   'S4': 'SAW 4',
                   'S5': 'SAW 5',
                   'S6': 'SAW 6',
                   'UT': 'UTILITY / PULP',
                   'CR': 'CAMP RUN',}


    ##### STEM TAPER EQUATION COEFFICIENTS ACCORDING TO SPECIES

    ## CZAPLEWSKI ('CZA') --- KOZAK 1969 ('KOZ69') --- KOZAK 1988 ('KOZ88') --- WENSEL ('WEN')
    ALL_TAPERS_DICT =  {'SF' : ['CZA', {'a': 0.5, 'b': 0.06, 'c': -1.742, 'd': 0.6184, 'e': -0.8838, 'f': 94.3683, 'g': None, 'h': None, 'i': None}],
                        'GF' : ['CZA', {'a': 0.59, 'b': 0.06, 'c': -1.5332, 'd': 0.56, 'e': -0.4781, 'f': 129.9282, 'g': None, 'h': None, 'i': None}],
                        'NF' : ['CZA', {'a': 0.59, 'b': 0.06, 'c': -1.5332, 'd': 0.56, 'e': -0.4781, 'f': 129.9282, 'g': None, 'h': None, 'i': None}],
                        'WL' : ['CZA', {'a': 0.59, 'b': 0.06, 'c': -1.3228, 'd': 0.3905, 'e': -0.5355, 'f': 115.6905, 'g': None, 'h': None, 'i': None}],
                        'LP' : ['CZA', {'a': 0.41, 'b': 0.06, 'c': -1.2989, 'd': 0.3693, 'e': 0.2408, 'f': 89.1781, 'g': None, 'h': None, 'i': None}],
                        'PP' : ['CZA', {'a': 0.72, 'b': 0.06, 'c': -2.3261, 'd': 0.9514, 'e': -1.0757, 'f': 94.6991, 'g': None, 'h': None, 'i': None}],
                        'DF' : ['CZA', {'a': 0.72, 'b': 0.12, 'c': -2.8758, 'd': 1.3458, 'e': -1.6264, 'f': 20.1315, 'g': None, 'h': None, 'i': None}],
                        'WH' : ['CZA', {'a': 0.59, 'b': 0.06, 'c': -2.0993, 'd': 0.8635, 'e': -1.026, 'f': 91.5562, 'g': None, 'h': None, 'i': None}],
                        'RA' : ['KOZ69', {'a': 0.97576, 'b': -1.22922, 'c': 0.25347, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'BM' : ['KOZ69', {'a': 0.95997, 'b': -1.46336, 'c': 0.50339, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'SS' : ['KOZ69', {'a': 0.99496, 'b': -1.98993, 'c': 0.99496, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'ES' : ['KOZ69', {'a': 0.97449, 'b': -1.42305, 'c': 0.44856, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'AS' : ['KOZ69', {'a': 0.95806, 'b': -1.33682, 'c': 0.37877, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'WP' : ['KOZ69', {'a': 0.96272, 'b': -1.37551, 'c': 0.41279, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'RC' : ['KOZ88', {'a': 1.21697, 'b': 0.84256, 'c': 1.00001, 'd': 0.3, 'e': 1.55322, 'f': -0.39719, 'g': 2.11018, 'h': -1.11416, 'i': 0.0942}],
                        'CW' : ['KOZ88', {'a': 0.85258, 'b': 0.95297, 'c': 1.00048, 'd': 0.25, 'e': 0.73191, 'f': -0.08419, 'g': 0.19634, 'h': -0.06985, 'i': 0.14828}],
                        'JP' : ['WEN', {'a': 0.82932, 'b': 1.50831, 'c': -4.08016, 'd': 0.047053, 'e': 0.0, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'SP' : ['WEN', {'a': 0.90051, 'b': 0.91588, 'c': -0.92964, 'd': 0.0077119, 'e': -0.0011019, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'WF' : ['WEN', {'a': 0.86039, 'b': 1.45196, 'c': -2.42273, 'd': -0.15848, 'e': 0.036947, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'RF' : ['WEN', {'a': 0.87927, 'b': 0.9135, 'c': -0.56617, 'd': -0.01448, 'e': 0.0037262, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'RW' : ['WEN', {'a': 0.955, 'b': 0.387, 'c': -0.362, 'd': -0.00581, 'e': 0.00122, 'f': None, 'g': None, 'h': None, 'i': None}],
                        'IC' : ['WEN', {'a': 1.0, 'b': 0.3155, 'c': -0.34316, 'd': 0.0, 'e': -0.00039283, 'f': None, 'g': None, 'h': None, 'i': None}]}



    #### SCRIBNER LOG LENGTH COEEFICIENTS AND FUNCTION
    # KEY: VALUE -> {DIB: SCRIB COEFFICIENT}
    SCRIBNER_DICT = {0: 0.0, 1: 0.0, 2: 0.143, 3: 0.39, 4: 0.676, 5: 1.07, 6: [1.16, 1.249, 1.57], 7: [1.4, 1.608, 1.8],
                     8: [1.501, 1.854, 2.2], 9: [2.084, 2.41, 2.9], 10: [3.126, 3.542, 3.815], 11: [3.749, 4.167, 4.499],
                     12: 4.9, 13: 6.043, 14: 7.14, 15: 8.88, 16: 10.0, 17: 11.528, 18: 13.29, 19: 14.99, 20: 17.499,
                     21: 18.99, 22: 20.88, 23: 23.51, 24: 25.218, 25: 28.677, 26: 31.249, 27: 34.22, 28: 36.376, 29: 38.04,
                     30: 41.06, 31: 44.376, 32: 45.975, 33: 48.99, 34: 50.0, 35: 54.688, 36: 57.66, 37: 64.319, 38: 66.731,
                     39: 70.0, 40: 75.24, 41: 79.48, 42: 83.91, 43: 87.19, 44: 92.501, 45: 94.99, 46: 99.075, 47: 103.501,
                     48: 107.97, 49: 112.292, 50: 116.99, 51: 121.65, 52: 126.525, 53: 131.51, 54: 136.51, 55: 141.61,
                     56: 146.912, 57: 152.21, 58: 157.71, 59: 163.288, 60: 168.99, 61: 174.85, 62: 180.749, 63: 186.623,
                     64: 193.17, 65: 199.12, 66: 205.685, 67: 211.81, 68: 218.501, 69: 225.685, 70: 232.499, 71: 239.317,
                     72: 246.615, 73: 254.04, 74: 261.525, 75: 269.04, 76: 276.63, 77: 284.26, 78: 292.5, 79: 300.655,
                     80: 308.97, 81: 317.36, 82: 325.79, 83: 334.217, 84: 343.29, 85: 350.785, 86: 359.12, 87: 368.38,
                     88: 376.61, 89: 385.135, 90: 393.98, 91: 402.499, 92: 410.834, 93: 419.166, 94: 428.38, 95: 437.499,
                     96: 446.565, 97: 455.01, 98: 464.15, 99: 473.43, 100: 482.49, 101: 491.7, 102: 501.7, 103: 511.7,
                     104: 521.7, 105: 531.7, 106: 541.7, 107: 552.499, 108: 562.501, 109: 573.35, 110: 583.35, 111: 594.15,
                     112: 604.17, 113: 615.01, 114: 625.89, 115: 636.66, 116: 648.38, 117: 660.0, 118: 671.7, 119: 683.33,
                     120: 695.011}



    def __init__(self, Species, DBH, Total_Height):
        self.SPP = str(Species).upper()
        self.DBH = float(DBH)
        self.HGT = int(Total_Height)
        self.HDR = self.HGT / (self.DBH/12)
        self.BA = self.DBH ** 2 * 0.005454
        self.RD = self.BA / math.sqrt(self.DBH)
        self.coef = self.ALL_TAPERS_DICT[self.SPP]
        self.equation = self.EQUATION_DICT[self.coef[0]]
        


    ## MAIN DICTIONARIES OF TREE DATA
    def tree_single(self, Merch_DIB, Preferred_Log_Length, Minimum_Log_Length):
        mh, bf, cf = self.compile_tree_dict_data(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)

        master = {}
        
        master['SPP'] = (self.SPP, self.ALL_SPECIES_NAMES[self.SPP])
        master['DBH'] = self.DBH
        master['M_DIB'] = int(Merch_DIB)
        master['T_HGT'] = self.HGT
        master['M_HGT'] = mh       
        master['HDR'] = self.HDR
        master['BA'] = self.BA
        master['RD'] = self.RD
        master['BF'] = bf
        master['CF'] = cf
        master['VBAR'] = bf / self.BA

        return master


    def tree_acre(self, Merch_DIB, Preferred_Log_Length, Minimum_Log_Length, Plot_Factor):
        _, bf, cf = self.compile_tree_dict_data(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)

        master = {}

        tpa = self.get_TPA(Plot_Factor)

        master['TPA'] = tpa
        master['BA_AC'] = self.get_BA_acre(Plot_Factor)
        master['RD_AC'] = self.get_RD_acre(Plot_Factor)
        master['BF_AC'] = bf * tpa
        master['CF_AC'] = cf * tpa
        

        return master

    
    def log_single(self, Merch_DIB, Preferred_Log_Length, Minimum_Log_Length):
        s, d, l, g, b, c = self.compile_log_lists(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)

        master = {}

        for (count, (stem_height, dib, length, grade, board_feet, cubic_feet)) in enumerate(zip(s, d, l, g, b, c)):
            temp_dict = {}
            temp_dict['S_HGT'] = stem_height
            temp_dict['DIB'] = dib
            temp_dict['L_LGT'] = length
            temp_dict['L_GRD'] = (grade, self.GRADE_NAMES[grade])
            temp_dict['L_BF'] = board_feet
            temp_dict['L_CF'] = cubic_feet

            key = 'LOG' + str(count + 1)
            master[key] = temp_dict

        return master


    def log_acre(self, Merch_DIB, Preferred_Log_Length, Minimum_Log_Length, Plot_Factor):
        s, d, l, g, b, c = self.compile_log_lists(Merch_DIB, Preferred_Log_Length, Minimum_Log_Length)

        tpa = self.get_TPA(Plot_Factor)

        master = {}

        for (count, (stem_height, dib, length, grade, board_feet, cubic_feet)) in enumerate(zip(s, d, l, g, b, c)):
            temp_dict = {}
            temp_dict['S_HGT'] = stem_height
            temp_dict['DIB'] = dib
            temp_dict['L_LGT'] = length
            temp_dict['L_GRD'] = (grade, self.GRADE_NAMES[grade])
            temp_dict['L_BF_AC'] = board_feet * tpa
            temp_dict['L_CF_AC'] = cubic_feet * tpa
            temp_dict['L_CT_AC'] = tpa

            key = 'LOG' + str(count + 1)
            master[key] = temp_dict

        return master






    

    ## FUNCTIONS FOR GATHERING TREE METRICS
    def merch_dib(self, Form_Percent = 40, Form_Height = 17):
        # Form Percent is the percent of DIB at the Form Height feet above ground,
        # this percent will be rounded down for the merch DIB in inches
        # Defaults are 40% and 17 feet
        
        form_pct = Form_Percent / 100
        
        return int(math.floor(form_pct * self.equation(self.DBH, self.HGT, Form_Height, a = self.coef[1]['a'], b = self.coef[1]['b'], c = self.coef[1]['c'],
                                                       d = self.coef[1]['d'], e = self.coef[1]['e'], f = self.coef[1]['f'], g = self.coef[1]['g'],
                                                       h = self.coef[1]['h'], i = self.coef[1]['i'])))
        

    def get_TPA(self, Plot_Factor):
        if float(Plot_Factor) == 0:
            return 0
        elif float(Plot_Factor) > 0:
            return float(Plot_Factor) / self.BA
        else:
            return abs(float(Plot_Factor))


    def get_BA_acre(self, Plot_Factor):
        if float(Plot_Factor) == 0:
            return 0
        elif float(Plot_Factor) > 0:
            return float(Plot_Factor)
        else:
            
            return abs(float(Plot_Factor)) * self.BA

    def get_RD_acre(self, Plot_Factor):
        return self.get_TPA(Plot_Factor) * self.RD        


    def get_any_dib(self, Stem_Height):
            return int(math.floor(self.equation(self.DBH, self.HGT, Stem_Height, a = self.coef[1]['a'], b = self.coef[1]['b'], c = self.coef[1]['c'],
                                                d = self.coef[1]['d'], e = self.coef[1]['e'], f = self.coef[1]['f'], g = self.coef[1]['g'],
                                                h = self.coef[1]['h'], i = self.coef[1]['i'])))
        


        
        


    ## TREE DATA CALCULATION FUNCTIONS
    def calc_merch_height(self, Merch_DIB):
        #Divide and Conquer Algo from ground level to Total Height
        notcheck = True
        
        floor = 0
        ceiling = self.HGT
        chkhgt = (ceiling - floor) // 2

        while notcheck:
            chkdib = int(math.floor(self.equation(self.DBH, self.HGT, chkhgt, a = self.coef[1]['a'], b = self.coef[1]['b'], c = self.coef[1]['c'],
                                                  d = self.coef[1]['d'], e = self.coef[1]['e'], f = self.coef[1]['f'], g = self.coef[1]['g'],
                                                  h = self.coef[1]['h'], i = self.coef[1]['i'])))
                
            if chkdib == int(Merch_DIB):
                #Since DIBs are rounded down there is a range of stem heights that have the same integer DIB,
                #this looks for the top most height of that range
                for i in range(1, 21):
                    chkhgt += 1
                    
                    chkdib_after = int(math.floor(self.equation(self.DBH, self.HGT, chkhgt, a = self.coef[1]['a'], b = self.coef[1]['b'], c = self.coef[1]['c'],
                                                                d = self.coef[1]['d'], e = self.coef[1]['e'], f = self.coef[1]['f'], g = self.coef[1]['g'],
                                                                h = self.coef[1]['h'], i = self.coef[1]['i'])))

                    if chkdib_after != chkdib:
                        notcheck = False
                        break
                    
            elif chkdib > int(Merch_DIB):
                floor = chkhgt
                chkhgt = ceiling - ((ceiling - floor) // 2)
                
            else:
                ceiling = chkhgt
                chkhgt = ceiling - ((ceiling - floor) // 2)
                       
        return chkhgt - 1


    
    def calc_log_stem(self, Previous_Log_Stem_Height, Merch_Height, Preferred_Log_Length, Minimum_Log_Length):
        mchk = Previous_Log_Stem_Height + Minimum_Log_Length + 1
        
        if mchk > Merch_Height - 2:
            return None
        else:    
            if Previous_Log_Stem_Height + 1 + Preferred_Log_Length <= Merch_Height:
                return Previous_Log_Stem_Height + Preferred_Log_Length + 1
            else:
                return Merch_Height
            

    def calc_log_length(self, Previous_Log_Stem_Height, Current_Log_Stem_Height):
        return (Current_Log_Stem_Height - Previous_Log_Stem_Height - 1) // 2 * 2


    def calc_board_feet(self, Log_Length, Scribner_Coefficient):
        return math.floor(Log_Length * Scribner_Coefficient)


    def calc_cubic_feet(self, Log_Length, DIB):
        if Log_Length < 17:
            x = Log_Length * 0.67
        else:
            x = Log_Length + 1
        return (.005454 * x) * (((2 * ((DIB + 0.7) ** 2)) + (2 * (DIB + 0.7))) / 3)


    def calc_log_grade(self, Log_DIB, Log_Length):
        for i in self.OFFICIAL_GRADES[self.SPP]:
            if Log_DIB >= i[0] and Log_Length >= i[1]:
                return i[2]
            else:
                next

    def calc_scribner(self, DIB, Log_Length):
        if DIB in range(6, 12):
            if Log_Length > 0 and Log_Length < 16:
                return self.SCRIBNER_DICT[DIB][0]
            elif Log_Length >= 16 and Log_Length < 32:
                return self.SCRIBNER_DICT[DIB][1]
            else:
                return self.SCRIBNER_DICT[DIB][2]
        else:
            return self.SCRIBNER_DICT[DIB]
        


    ## FUNCTIONS FOR A GETTING TREE DATA LISTS
    def stem_heights(self, Merch_Height, Preferred_Log_Length, Minimum_Log_Length):
        master = [1]
        for i in range(401):
            if self.calc_log_stem(master[i], Merch_Height, Preferred_Log_Length, Minimum_Log_Length) is None:
                break
            else:
                master.append(self.calc_log_stem(master[i], Merch_Height, Preferred_Log_Length, Minimum_Log_Length))
        return master



    def compile_tree_dict_data(self, Merch_DIB, Preferred_Log_Length, Minimum_Log_Length):
        merch_height = self.calc_merch_height(int(Merch_DIB))
        stem_height_list = self.stem_heights(merch_height, Preferred_Log_Length, Minimum_Log_Length)        
        dib_list = [self.get_any_dib(stem_height_list[i]) for i in range(1, len(stem_height_list))]        
        length_list = [self.calc_log_length(stem_height_list[i-1], stem_height_list[i]) for i in range(1, len(stem_height_list))]
        board_feet_list = [self.calc_board_feet(length, self.calc_scribner(dib, length)) for (dib, length) in zip(dib_list, length_list)]
        cubic_feet_list = [self.calc_cubic_feet(length, dib) for (dib, length) in zip(dib_list, length_list)]

        return merch_height, sum(board_feet_list), sum(cubic_feet_list)       
        


    def compile_log_lists(self, Merch_DIB, Preferred_Log_Length, Minimum_Log_Length):
        stem_height_list = self.stem_heights(self.calc_merch_height(int(Merch_DIB)), Preferred_Log_Length, Minimum_Log_Length)        
        dib_list = [self.get_any_dib(stem_height_list[i]) for i in range(1, len(stem_height_list))]        
        length_list = [self.calc_log_length(stem_height_list[i-1], stem_height_list[i]) for i in range(1, len(stem_height_list))]        
        grade_list = [self.calc_log_grade(dib, length) for (dib, length) in zip(dib_list, length_list)]        
        board_feet_list = [self.calc_board_feet(length, self.calc_scribner(dib, length)) for (dib, length) in zip(dib_list, length_list)]        
        cubic_feet_list = [self.calc_cubic_feet(length, dib) for (dib, length) in zip(dib_list, length_list)]
        
        stem_height_list.pop(0)

        return stem_height_list, dib_list, length_list, grade_list, board_feet_list, cubic_feet_list






##### EXAMPLE OF HOW TO USE LIBRARY

if __name__ == ('__main__'):
    
    #data_list = [Species Code, DBH, Total Height, Preferred Log Length, Minimum Log Length, Plot Factor]
    data_list = ['DF', 25.5, 125, 40, 16, 33.3]

    tree = Timber(data_list[0], data_list[1], data_list[2])

    merch_dib = tree.merch_dib()

    print('Tree Single Dict:\n', tree.tree_single(merch_dib, data_list[3], data_list[4]), '\n')

    print('Tree Acre Dict:\n', tree.tree_acre(merch_dib, data_list[3], data_list[4], data_list[5]), '\n')

    print('Log Single Dict:\n', tree.log_single(merch_dib, data_list[3], data_list[4]), '\n')

    print('Log Acre Dict:\n', tree.log_acre(merch_dib, data_list[3], data_list[4], data_list[5]), '\n')



    #### DICT KEYS:
            #TREE SINGLE:
                #SPP -      (Species Code, Species Common Name)
                #DBH -      Diameter at Breast Height (inches)
                #M_DIB -    Merchantble Diameter Inside Bark (inches)
                #T_HGT -    Total Height (feet)
                #M_HGT -    Merchantble Height (feet)
                #HDR -      Height to Diameter Ratio
                #BA -       Basal Area (square feet)
                #RD -       Relative Density
                #BF -       Total Board Feet
                #CF -       Total Cubic Feet
                #VBAR -     Volume to Basal Area Ratio (board feet per 1 sqft of basal area)

            #TREE ACRE:
                #TPA -      Trees per Acre
                #BA_AC -    Basal Area per acre
                #RD_AC -    Relative Density per acre
                #BF_AC -    Total Board Feet per acre
                #CF_AC -    Total Cubic Feet per acre

            #LOG SINGLE:
                #S_HGT -    Stem Height of the top of the log (feet)
                #DIB -      Diameter Inside Bark at the top of the log (inches)
                #L_LGT -    Length of log (feet)
                #L_GRD -    (Grade Code, Grade Name) of the log
                #L_BF -     Board Feet of the log
                #L_CF -     Cubic Feet of the log

            #LOG ACRE:
                #*Same as Log Single plus...
                #L_BF_AC -  Board Feet per acre of the log
                #L_CF_AC -  Cubic Feet per acre of the log
                #L_CT_AC -  Logs per acre



















    



        






    

