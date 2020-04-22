# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:00:37 2019

@author: seongpar
"""
#import os
#import pandas as pd

Base = { 'Scen_Name'               : 'Base',
         'IR_Stress_Type'          : 'Parallel' ,
         'IR_Parallel_Shift_bps'   : 0,
         'Credit_Spread_Shock_bps' : {'AAA': 0, # AIG Derived Rating
                                      'AA' : 0,
                                      'A'  : 0,
                                      'BBB': 0,
                                      'BB' : 0,
                                      'B'  : 0,
                                      'CCC': 0,
                                      'CC' : 0,
                                      'C'  : 0,
                                      'D'  : 0,
                                  'Average': 0},     
         'Alts_Retrun'             : 0,
         'MLIII_Return'            : 0,
         'PC_PYD'                  : 0,
         'Liab_Spread_Beta'        : 0.65,
         'LT_Reserve'              : 0,
         'Longevity shock'         : 0,
         'Mortality shock'         : 0,	
         'Expense shock_Permanent' : 0,	
         'Expense shock_Inflation' : 0,	
         'Lapse shock'             : 0,	
         'Morbidity shock'         : 0,	
         'Longevity Trend shock'   : 0
        }

Comp = { 'Scen_Name'               : 'Comprehensive',
         'IR_Stress_Type'          : 'Parallel' ,
         'IR_Parallel_Shift_bps'   : -59,
         'Credit_Spread_Shock_bps' : {'AAA': 34,
                                      'AA' : 55.20,
                                      'A'  : 62.8,
                                      'BBB': 70,
                                      'BB' : 112.4,
                                      'B'  : 192,
                                      'CCC': 342.4,
                                      'CC' : 342.4,
                                      'C'  : 342.4,
                                      'D'  : 342.4,
                                  'Average': 0},
         'Alts_Retrun'             : -0.1395174,
         'MLIII_Return'            : -0.142767256132,
         'PC_PYD'                  : 0.076405094,
         'Liab_Spread_Beta'        : 0.65,
         'LT_Reserve'              : 0,
         'Longevity shock'         : 0,
         'Mortality shock'         : 0,	
         'Expense shock_Permanent' : 0.05,	
         'Expense shock_Inflation' : 0.03,
         'Lapse shock'             : 0,	
         'Morbidity shock'         : 0,	
         'Longevity Trend shock'   : 0
        }

SFP = { 'Scen_Name'                : 'SFP',     # No.993
         'IR_Stress_Type'          : 'Parallel' ,
         'IR_Parallel_Shift_bps'   : -30.483628,
         'Credit_Spread_Shock_bps' : {'AAA': 124.2,
                                      'AA' : 106.8,
                                      'A'  : 136.8,
                                      'BBB': 214.2,
                                      'BB' : 290.4,
                                      'B'  : 442.8,
                                      'CCC': 1095.6,
                                      'CC' : 1095.6,
                                      'C'  : 1095.6,
                                      'D'  : 1095.6,
                                  'Average': 0},
         'Alts_Retrun'             : -0.216120785143862,
         'MLIII_Return'            : -0.225209905055905,
         'PC_PYD'                  : 0,
         'Liab_Spread_Beta'        : 0.65,
         'LT_Reserve'              : 0,
         'Longevity shock'         : 0,
         'Mortality shock'         : 0,	
         'Expense shock_Permanent' : 0,	
         'Expense shock_Inflation' : 0,
         'Lapse shock'             : 0,	
         'Morbidity shock'         : 0,	
         'Longevity Trend shock'   : 0
        }

Today_March_6th = { 'Scen_Name'                : 'March_6th',     
                     'IR_Stress_Type'          : 'Parallel' ,
                     'IR_Parallel_Shift_bps'   : -120,
                     'Credit_Spread_Shock_bps' : {'AAA': 40,
                                                  'AA' : 40,
                                                  'A'  : 40,
                                                  'BBB': 40,
                                                  'BB' : 40,
                                                  'B'  : 40,
                                                  'CCC': 40,
                                                  'CC' : 40,
                                                  'C'  : 40,
                                                  'D'  : 40,
                                              'Average': 0},
                     'Alts_Retrun'             : 0,
                     'MLIII_Return'            : 0,
                     'PC_PYD'                  : 0,
                     'Liab_Spread_Beta'        : 0.65,
                     'LT_Reserve'              : 0,
                     'Longevity shock'         : 0,
                     'Mortality shock'         : 0,	
                     'Expense shock_Permanent' : 0,	
                     'Expense shock_Inflation' : 0,
                     'Lapse shock'             : 0,	
                     'Morbidity shock'         : 0,	
                     'Longevity Trend shock'   : 0
                    }

Today_March_10th = { 'Scen_Name'               : 'March_10th',     
                     'IR_Stress_Type'          : 'Parallel' ,
                     'IR_Parallel_Shift_bps'   : -115,
                     'Credit_Spread_Shock_bps' : {'AAA': 63.92,
                                                  'AA' : 63.92,
                                                  'A'  : 63.92,
                                                  'BBB': 63.92,
                                                  'BB' : 63.92,
                                                  'B'  : 63.92,
                                                  'CCC': 63.92,
                                                  'CC' : 63.92,
                                                  'C'  : 63.92,
                                                  'D'  : 63.92,
                                              'Average': 0},
                     'Alts_Retrun'             : 0,
                     'MLIII_Return'            : 0,
                     'PC_PYD'                  : 0,
                     'Liab_Spread_Beta'        : 0.65,
                     'LT_Reserve'              : 0,
                     'Longevity shock'         : 0,
                     'Mortality shock'         : 0,	
                     'Expense shock_Permanent' : 0,	
                     'Expense shock_Inflation' : 0,
                     'Lapse shock'             : 0,	
                     'Morbidity shock'         : 0,	
                     'Longevity Trend shock'   : 0
                    }
    
        
ERM_Longevity_1_in_100 = {'Scen_Name'              : 'ERM_Longevity_1_in_100', # No.908
                         'IR_Stress_Type'          : 'Parallel' ,
                         'IR_Parallel_Shift_bps'   : 0,
                         'Credit_Spread_Shock_bps' : {'AAA': 0,
                                                      'AA' : 0,
                                                      'A'  : 0,
                                                      'BBB': 0,
                                                      'BB' : 0,
                                                      'B'  : 0,
                                                      'CCC': 0,
                                                      'CC' : 0,
                                                      'C'  : 0,
                                                      'D'  : 0,
                                                  'Average': 0},     
                         'Alts_Retrun'             : 0,
                         'MLIII_Return'            : 0,
                         'PC_PYD'                  : 0,
                         'Liab_Spread_Beta'        : 0.65,
                         'LT_Reserve'              : 0,
                         'Longevity shock'         : 0.0109013126,
                         'Mortality shock'         : 0,	
                         'Expense shock_Permanent' : 0,	
                         'Expense shock_Inflation' : 0,	
                         'Lapse shock'             : 0,	
                         'Morbidity shock'         : 0,	
                         'Longevity Trend shock'   : 0
                        } 

ERM_PC_1_in_100 = {'Scen_Name'                     : 'ERM_PC_1_in_100', # No.913
                         'IR_Stress_Type'          : 'Parallel' ,
                         'IR_Parallel_Shift_bps'   : 0,
                         'Credit_Spread_Shock_bps' : {'AAA': 0,
                                                      'AA' : 0,
                                                      'A'  : 0,
                                                      'BBB': 0,
                                                      'BB' : 0,
                                                      'B'  : 0,
                                                      'CCC': 0,
                                                      'CC' : 0,
                                                      'C'  : 0,
                                                      'D'  : 0,
                                                  'Average': 0},     
                         'Alts_Retrun'             : 0,
                         'MLIII_Return'            : 0,
                         'PC_PYD'                  : 0.18211921,
                         'Liab_Spread_Beta'        : 0.65,
                         'LT_Reserve'              : 0,
                         'Longevity shock'         : 0,
                         'Mortality shock'         : 0,	
                         'Expense shock_Permanent' : 0,	
                         'Expense shock_Inflation' : 0,	
                         'Lapse shock'             : 0,	
                         'Morbidity shock'         : 0,	
                         'Longevity Trend shock'   : 0
                        } 

ERM_IR_1_in_100_up = {  'Scen_Name'                : 'ERM_IR_1_in_100_up', # No.923
                         'IR_Stress_Type'          : 'Parallel' ,
                         'IR_Parallel_Shift_bps'   : 204,
                         'Credit_Spread_Shock_bps' : {'AAA': 0,
                                                      'AA' : 0,
                                                      'A'  : 0,
                                                      'BBB': 0,
                                                      'BB' : 0,
                                                      'B'  : 0,
                                                      'CCC': 0,
                                                      'CC' : 0,
                                                      'C'  : 0,
                                                      'D'  : 0,
                                                  'Average': 0},     
                         'Alts_Retrun'             : 0,
                         'MLIII_Return'            : 0,
                         'PC_PYD'                  : 0,
                         'Liab_Spread_Beta'        : 0.65,
                         'LT_Reserve'              : 0,
                         'Longevity shock'         : 0,
                         'Mortality shock'         : 0,	
                         'Expense shock_Permanent' : 0,	
                         'Expense shock_Inflation' : 0,	
                         'Lapse shock'             : 0,	
                         'Morbidity shock'         : 0,	
                         'Longevity Trend shock'   : 0                    
                        } 

ERM_IR_1_in_100_dn = { 'Scen_Name'                 : 'ERM_IR_1_in_100_dn', # No.918
                         'IR_Stress_Type'          : 'Parallel' ,
                         'IR_Parallel_Shift_bps'   : -202,
                         'Credit_Spread_Shock_bps' : {'AAA': 0,
                                                      'AA' : 0,
                                                      'A'  : 0,
                                                      'BBB': 0,
                                                      'BB' : 0,
                                                      'B'  : 0,
                                                      'CCC': 0,
                                                      'CC' : 0,
                                                      'C'  : 0,
                                                      'D'  : 0,
                                                  'Average': 0},     
                         'Alts_Retrun'             : 0,
                         'MLIII_Return'            : 0,
                         'PC_PYD'                  : 0,
                         'Liab_Spread_Beta'        : 0.65,
                         'LT_Reserve'              : 0,
                         'Longevity shock'         : 0,
                         'Mortality shock'         : 0,	
                         'Expense shock_Permanent' : 0,	
                         'Expense shock_Inflation' : 0,	
                         'Lapse shock'             : 0,	
                         'Morbidity shock'         : 0,	
                         'Longevity Trend shock'   : 0                    
                        } 

ERM_CS_1_in_100_up = {  'Scen_Name'                : 'ERM_CS_1_in_100_up', # No.931
                         'IR_Stress_Type'          : 'Parallel' ,
                         'IR_Parallel_Shift_bps'   : 0,
                         'Credit_Spread_Shock_bps' : {'AAA': 244,
                                                      'AA' : 267,
                                                      'A'  : 325,
                                                      'BBB': 501,
                                                      'BB' : 827,
                                                      'B'  : 1088,
                                                      'CCC': 2090,
                                                      'CC' : 2090,
                                                      'C'  : 2090,
                                                      'D'  : 2090,
                                                  'Average': 0},     
                         'Alts_Retrun'             : 0,
                         'MLIII_Return'            : 0,
                         'PC_PYD'                  : 0,
                         'Liab_Spread_Beta'        : 0.65,
                         'LT_Reserve'              : 0,
                         'Longevity shock'         : 0,
                         'Mortality shock'         : 0,	
                         'Expense shock_Permanent' : 0,	
                         'Expense shock_Inflation' : 0,	
                         'Lapse shock'             : 0,	
                         'Morbidity shock'         : 0,	
                         'Longevity Trend shock'   : 0                    
                        } 

ERM_CS_1_in_100_dn = {  'Scen_Name'                : 'ERM_CS_1_in_100_dn', # No.932
                         'IR_Stress_Type'          : 'Parallel' ,
                         'IR_Parallel_Shift_bps'   : 0,
                         'Credit_Spread_Shock_bps' : {'AAA': -41,
                                                      'AA' : -38,
                                                      'A'  : -53,
                                                      'BBB': -90,
                                                      'BB' : -127,
                                                      'B'  : -225,
                                                      'CCC': -703,
                                                      'CC' : -703,
                                                      'C'  : -703,
                                                      'D'  : -703,
                                                  'Average': 0}, 
                         'Alts_Retrun'             : 0,
                         'MLIII_Return'            : 0,
                         'PC_PYD'                  : 0,
                         'Liab_Spread_Beta'        : 0.65, 
                         'LT_Reserve'              : 0,
                         'Longevity shock'         : 0,
                         'Mortality shock'         : 0,	
                         'Expense shock_Permanent' : 0,	
                         'Expense shock_Inflation' : 0,	
                         'Lapse shock'             : 0,	
                         'Morbidity shock'         : 0,	
                         'Longevity Trend shock'   : 0                    
                        }