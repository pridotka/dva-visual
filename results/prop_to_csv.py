# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:30:45 2018

@author: prido
"""

import pandas as pd
import requests
import time
import json

API_KEY = "DON'T PUSH"

results = []
#number of rows
rng = 430000
'''I Split the PROP file into smaller ones named filexx
the file num below grabs them to make more manageable calls to geocode'''
file_num = '00'
start_time = time.time()

path = r'C:\Desktop\CSE 6242 Data & Visual Analytics\proj_git\dva-visual\data\PROP.TXT'
colnames = ['prop_id', 'prop_type_cd', 'prop_val_yr', 'sup_num', 'sup_action', 'sup_cd', 'sup_desc', 'geo_id', 'py_owner_id', 'py_owner_name', 'partial_owner', 'udi_group', 'filler', 'py_addr_line1', 'py_addr_line2', 'py_addr_line3', 'py_addr_city', 'py_addr_state', 'py_addr_country', 'py_addr_zip', 'py_addr_zip_cass', 'py_addr_zip_rt', 'py_confidential_flag', 'py_address_suppress_flag', 'filler', 'py_addr_ml_deliverable', 'filler', 'situs_street_prefx', 'situs_street', 'situs_street_suffix', 'situs_city', 'situs_zip', 'legal_desc', 'legal_desc2', 'legal_acreage', 'abs_subdv_cd', 'hood_cd', 'block', 'tract_or_lot', 'land_hstd_val', 'land_non_hstd_val', 'imprv_hstd_val', 'imprv_non_hstd_val', 'ag_use_val', 'ag_market', 'timber_use', 'timber_market', 'appraised_val', 'ten_percent_cap', 'assessed_val', 'filler', 'arb_protest_flag', 'filler', 'deed_book_id', 'deed_book_page', 'deed_dt', 'mortgage_co_id', 'mortage_co_name', 'mortgage_acct_id', 'jan1_owner_id', 'jan1_owner_name', 'jan1_addr_line1', 'jan1_addr_line2', 'jan1_addr_line3', 'jan1_addr_city', 'jan1_addr_state', 'jan1_addr_country', 'jan1_addr_zip', 'jan1_addr_zip_cass', 'jan1_addr_zip_rt', 'jan1_confidential_flag', 'jan1_address_suppress_flag', 'filler', 'jan1_ml_deliverable', 'hs_exempt', 'ov65_exempt', 'ov65_prorate_begin', 'ov65_prorate_end', 'ov65s_exempt', 'dp_exempt', 'dv1_exempt', 'dv1s_exempt', 'dv2_exempt', 'dv2s_exempt', 'dv3_exempt', 'dv3s_exempt', 'dv4_exempt', 'dv4s_exempt', 'ex_exempt', 'ex_prorate_begin', 'ex_prorate_end', 'lve_exempt', 'ab_exempt', 'en_exempt', 'fr_exempt', 'ht_exempt', 'pro_exempt', 'pc_exempt', 'so_exempt', 'ex366_exempt', 'ch_exempt', 'imprv_state_cd', 'land_state_cd', 'personal_state_cd', 'mineral_state_cd', 'land_acres', 'entity_agent_id', 'entity_agent_name', 'entity_agent_addr_line1', 'entity_agent_addr_line2', 'entity_agent_addr_line3', 'entity_agent_city', 'entity_agent_state', 'entity_agent_country', 'entity_agent_zip', 'entity_agent_cass', 'entity_agent_rt', 'filler', 'ca_agent_id', 'ca_agent_name', 'ca_agent_addr_line1', 'ca_agent_addr_line2', 'ca_agent_addr_line3', 'ca_agent_city', 'ca_agent_state', 'ca_agent_country', 'ca_agent_zip', 'ca_agent_zip_cass', 'ca_agent_zip_rt', 'filler', 'arb_agent_id', 'arb_agent_name', 'arb_agent_addr_line1', 'arb_agent_addr_line2', 'arb_agent_addr_line3', 'arb_agent_city', 'arb_agent_state', 'arb_agent_country', 'arb_agent_zip', 'arb_agent_zip_cass', 'arb_agent_zip_rt', 'filler', 'mineral_type_of_int', 'mineral_int_pct', 'productivity_use_code', 'filler', 'timber_78_market', 'ag_late_loss', 'late_freeport_penalty', 'filler', 'filler', 'filler', 'dba', 'filler', 'market_value', 'filler', 'filler', 'filler', 'filler', 'filler', 'filler', 'ov65_deferral_date', 'dp_deferral_date', 'ref_id1', 'ref_id2', 'situs_num', 'situs_unit', 'appr_owner_id', 'appr_owner_name', 'appr_addr_line1', 'appr_addr_line2', 'appr_addr_line3', 'appr_addr_city', 'appr_addr_state', 'appr_addr_country', 'appr_addr_zip', 'appr_addr_zip_cass', 'appr_addr_zip_cass_route', 'appr_ml_deliverable', 'appr_confidential_flag', 'appr_address_suppress_flag', 'appr_confidential_name', 'py_confidential_name', 'jan1_confidential_name', 'filler', 'rendition_filed', 'rendition_date', 'rendition_penalty', 'rendition_penalty_date_paid', 'rendition_fraud_penalty', 'rendition_fraud_penalty_date_paid', 'filler', 'entities', 'eco_exempt', 'dataset_id', 'deed_num', 'chodo_exempt', 'local_option_pct_only_flag_hs', 'local_option_pct_only_flag_ov65', 'local_option_pct_only_flag_ov65s', 'local_option_pct_only_flag_dp', 'freeze_only_flag_ov65', 'freeze_only_flag_ov65s', 'freeze_only_flag_dp', 'apply_percent_exemption_flag', 'exemption_percentage', 'vit_flag', 'lih_exempt', 'git_exempt', 'dps_exempt', 'dps_deferral_date', 'local_option_pct_only_flag_dps', 'freeze_only_flag_dps', 'dvhs_exempt', 'hs_qualify_yr', 'ov65_qualify_yr', 'ov65s_qualify_yr', 'dp_qualify_yr', 'dps_qualify_yr', 'dv1_qualify_yr', 'dv1s_qualify_yr', 'dv2_qualify_yr', 'dv2s_qualify_yr', 'dv3_qualify_yr', 'dv3s_qualify_yr', 'dv4_qualify_yr', 'dv4s_qualify_yr', 'dvhs_qualify_yr', 'ex_qualify_yr', 'ab_qualify_yr', 'en_qualify_yr', 'fr_qualify_yr', 'ht_qualify_yr', 'pro_qualify_yr', 'pc_qualify_yr', 'so_qualify_yr', 'ex366_qualify_yr', 'ch_qualify_yr', 'eco_qualify_yr', 'chodo_qualify_yr', 'lih_qualify_yr', 'git_qualify_yr', 'mortgage_addr_line1', 'mortgage_addr_line2', 'mortgage_addr_line3', 'mortgage_addr_city', 'mortgage_addr_state', 'mortgage_addr_country', 'mortgage_addr_zip', 'mortgage_addr_zip_cass', 'mortgage_addr_zip_rt', 'mortgage_addr_ml_deliverable', 'sic_code', 'omitted_property_flag', 'hs_prorate_begin', 'hs_prorate_end', 'ov65s_prorate_begin', 'ov65s_prorate_end', 'dp_prorate_begin', 'dp_prorate_end', 'dv1_prorate_begin', 'dv1_prorate_end', 'dv1s_prorate_begin', 'dv1s_prorate_end', 'dv2_prorate_begin', 'dv2_prorate_end', 'dv2s_prorate_begin', 'dv2s_prorate_end', 'dv3_prorate_begin', 'dv3_prorate_end', 'dv3s_prorate_begin', 'dv3s_prorate_end', 'dv4_prorate_begin', 'dv4_prorate_end', 'dv4s_prorate_begin', 'dv4s_prorate_end', 'lve_prorate_begin', 'lve_prorate_end', 'ab_prorate_begin', 'ab_prorate_end', 'en_prorate_begin', 'en_prorate_end', 'fr_prorate_begin', 'fr_prorate_end', 'ht_prorate_begin', 'ht_prorate_end', 'pro_prorate_begin', 'pro_prorate_end', 'pc_prorate_begin', 'pc_prorate_end', 'so_prorate_begin', 'so_prorate_end', 'ex366_prorate_begin', 'ex366_prorate_end', 'ch_prorate_begin', 'ch_prorate_end', 'dps_prorate_begin', 'dps_prorate_end', 'eco_prorate_begin', 'eco_prorate_end', 'chodo_prorate_begin', 'chodo_prorate_end', 'lih_prorate_begin', 'lih_prorate_end', 'git_prorate_begin', 'git_prorate_end', 'clt_exempt', 'clt_prorate_begin', 'clt_prorate_end', 'clt_qualify_yr', 'dvhss_exempt', 'dvhss_prorate_begin', 'dvhss_prorate_end', 'dvhss_qualify_yr', 'omitted_imprv_hstd_val', 'omitted_imprv_non_hstd_val', 'dvhs_prorate_begin', 'dvhs_prorate_end', 'ex_xd_exempt', 'ex_xd_qualify_yr', 'ex_xd_prorate_begin', 'ex_xd_prorate_end', 'ex_xf_exempt', 'ex_xf_qualify_yr', 'ex_xf_prorate_begin', 'ex_xf_prorate_end', 'ex_xg_exempt', 'ex_xg_qualify_yr', 'ex_xg_prorate_begin', 'ex_xg_prorate_end', 'ex_xh_exempt', 'ex_xh_qualify_yr', 'ex_xh_prorate_begin', 'ex_xh_prorate_end', 'ex_xi_exempt', 'ex_xi_qualify_yr', 'ex_xi_prorate_begin', 'ex_xi_prorate_end', 'ex_xj_exempt', 'ex_xj_qualify_yr', 'ex_xj_prorate_begin', 'ex_xj_prorate_end', 'ex_xl_exempt', 'ex_xl_qualify_yr', 'ex_xl_prorate_begin', 'ex_xl_prorate_end', 'ex_xm_exempt', 'ex_xm_qualify_yr', 'ex_xm_prorate_begin', 'ex_xm_prorate_end', 'ex_xn_exempt', 'ex_xn_qualify_yr', 'ex_xn_prorate_begin', 'ex_xn_prorate_end', 'ex_xo_exempt', 'ex_xo_qualify_yr', 'ex_xo_prorate_begin', 'ex_xo_prorate_end', 'ex_xp_exempt', 'ex_xp_qualify_yr', 'ex_xp_prorate_begin', 'ex_xp_prorate_end', 'ex_xq_exempt', 'ex_xq_qualify_yr', 'ex_xq_prorate_begin', 'ex_xq_prorate_end', 'ex_xr_exempt', 'ex_xr_qualify_yr', 'ex_xr_prorate_begin', 'ex_xr_prorate_end', 'ex_xs_exempt', 'ex_xs_qualify_yr', 'ex_xs_prorate_begin', 'ex_xs_prorate_end', 'ex_xt_exempt', 'ex_xt_qualify_yr', 'ex_xt_prorate_begin', 'ex_xt_prorate_end', 'ex_xu_exempt', 'ex_xu_qualify_yr', 'ex_xu_prorate_begin', 'ex_xu_prorate_end', 'ex_xv_exempt', 'ex_xv_qualify_yr', 'ex_xv_prorate_begin', 'ex_xv_prorate_end', 'ex_xa_exempt', 'ex_xa_qualify_yr', 'ex_xa_prorate_begin', 'ex_xa_prorate_end', 'lve_qualify_yr', 'ppv_exempt', 'ppv_qualify_yr', 'ppv_prorate_begin', 'ppv_prorate_end', 'dvch_exempt', 'dvch_qualify_yr', 'dvch_prorate_begin', 'dvch_prorate_end', 'dvchs_exempt', 'dvchs_qualify_yr', 'dvchs_prorate_begin', 'dvchs_prorate_end', 'masss_exempt', 'masss_qualify_yr', 'masss_prorate_begin', 'masss_prorate_end', 'pp_late_interstate_allocation_val']
col_specification = [(0, 12), (12, 17), (17, 22), (22, 34), (34, 36), (36, 46), (46, 546), (546, 596), (596, 608), (608, 678), (678, 679), (679, 691), (691, 693), (693, 753), (753, 813), (813, 873), (873, 923), (923, 973), (973, 978), (978, 983), (983, 987), (987, 989), (989, 990), (990, 991), (991, 1011), (1011, 1012), (1012, 1039), (1039, 1049), (1049, 1099), (1099, 1109), (1109, 1139), (1139, 1149), (1149, 1404), (1404, 1659), (1659, 1675), (1675, 1685), (1685, 1695), (1695, 1745), (1745, 1795), (1795, 1810), (1810, 1825), (1825, 1840), (1840, 1855), (1855, 1870), (1870, 1885), (1885, 1900), (1900, 1915), (1915, 1930), (1930, 1945), (1945, 1960), (1960, 1980), (1980, 1981), (1981, 1993), (1993, 2013), (2013, 2033), (2033, 2058), (2058, 2070), (2070, 2140), (2140, 2190), (2190, 2202), (2202, 2272), (2272, 2332), (2332, 2392), (2392, 2452), (2452, 2502), (2502, 2552), (2552, 2557), (2557, 2562), (2562, 2566), (2566, 2568), (2568, 2569), (2569, 2570), (2570, 2607), (2607, 2608), (2608, 2609), (2609, 2610), (2610, 2635), (2635, 2660), (2660, 2661), (2661, 2662), (2662, 2663), (2663, 2664), (2664, 2665), (2665, 2666), (2666, 2667), (2667, 2668), (2668, 2669), (2669, 2670), (2670, 2671), (2671, 2696), (2696, 2721), (2721, 2722), (2722, 2723), (2723, 2724), (2724, 2725), (2725, 2726), (2726, 2727), (2727, 2728), (2728, 2729), (2729, 2730), (2730, 2731), (2731, 2741), (2741, 2751), (2751, 2761), (2761, 2771), (2771, 2791), (2791, 2803), (2803, 2873), (2873, 2933), (2933, 2993), (2993, 3053), (3053, 3103), (3103, 3153), (3153, 3158), (3158, 3163), (3163, 3167), (3167, 3169), (3169, 3203), (3203, 3215), (3215, 3285), (3285, 3345), (3345, 3405), (3405, 3465), (3465, 3515), (3515, 3565), (3565, 3570), (3570, 3575), (3575, 3579), (3579, 3581), (3581, 3615), (3615, 3627), (3627, 3697), (3697, 3757), (3757, 3817), (3817, 3877), (3877, 3927), (3927, 3977), (3977, 3982), (3982, 3987), (3987, 3991), (3991, 3993), (3993, 4027), (4027, 4032), (4032, 4047), (4047, 4050), (4050, 4090), (4090, 4102), (4102, 4114), (4114, 4126), (4126, 4128), (4128, 4133), (4133, 4135), (4135, 4175), (4175, 4213), (4213, 4227), (4227, 4247), (4247, 4267), (4267, 4287), (4287, 4288), (4288, 4289), (4289, 4359), (4359, 4384), (4384, 4409), (4409, 4434), (4434, 4459), (4459, 4474), (4474, 4479), (4479, 4491), (4491, 4561), (4561, 4621), (4621, 4681), (4681, 4741), (4741, 4791), (4791, 4841), (4841, 4846), (4846, 4851), (4851, 4855), (4855, 4857), (4857, 4858), (4858, 4859), (4859, 4860), (4860, 4930), (4930, 5000), (5000, 5070), (5070, 5075), (5075, 5076), (5076, 5101), (5101, 5116), (5116, 5141), (5141, 5156), (5156, 5181), (5181, 5201), (5201, 5341), (5341, 5342), (5342, 5357), (5357, 5407), (5407, 5408), (5408, 5409), (5409, 5410), (5410, 5411), (5411, 5412), (5412, 5413), (5413, 5414), (5414, 5415), (5415, 5416), (5416, 5431), (5431, 5432), (5432, 5433), (5433, 5434), (5434, 5435), (5435, 5460), (5460, 5461), (5461, 5462), (5462, 5463), (5463, 5467), (5467, 5471), (5471, 5475), (5475, 5479), (5479, 5483), (5483, 5487), (5487, 5491), (5491, 5495), (5495, 5499), (5499, 5503), (5503, 5507), (5507, 5511), (5511, 5515), (5515, 5519), (5519, 5523), (5523, 5527), (5527, 5531), (5531, 5535), (5535, 5539), (5539, 5543), (5543, 5547), (5547, 5551), (5551, 5555), (5555, 5559), (5559, 5563), (5563, 5567), (5567, 5571), (5571, 5575), (5575, 5635), (5635, 5695), (5695, 5755), (5755, 5805), (5805, 5855), (5855, 5860), (5860, 5865), (5865, 5869), (5869, 5871), (5871, 5872), (5872, 5882), (5882, 5883), (5883, 5908), (5908, 5933), (5933, 5958), (5958, 5983), (5983, 6008), (6008, 6033), (6033, 6058), (6058, 6083), (6083, 6108), (6108, 6133), (6133, 6158), (6158, 6183), (6183, 6208), (6208, 6233), (6233, 6258), (6258, 6283), (6283, 6308), (6308, 6333), (6333, 6358), (6358, 6383), (6383, 6408), (6408, 6433), (6433, 6458), (6458, 6483), (6483, 6508), (6508, 6533), (6533, 6558), (6558, 6583), (6583, 6608), (6608, 6633), (6633, 6658), (6658, 6683), (6683, 6708), (6708, 6733), (6733, 6758), (6758, 6783), (6783, 6808), (6808, 6833), (6833, 6858), (6858, 6883), (6883, 6908), (6908, 6933), (6933, 6958), (6958, 6983), (6983, 7008), (7008, 7033), (7033, 7058), (7058, 7083), (7083, 7108), (7108, 7133), (7133, 7158), (7158, 7183), (7183, 7184), (7184, 7209), (7209, 7234), (7234, 7238), (7238, 7239), (7239, 7264), (7264, 7289), (7289, 7293), (7293, 7308), (7308, 7323), (7323, 7348), (7348, 7373), (7373, 7374), (7374, 7378), (7378, 7403), (7403, 7428), (7428, 7429), (7429, 7433), (7433, 7458), (7458, 7483), (7483, 7484), (7484, 7488), (7488, 7513), (7513, 7538), (7538, 7539), (7539, 7543), (7543, 7568), (7568, 7593), (7593, 7594), (7594, 7598), (7598, 7623), (7623, 7648), (7648, 7649), (7649, 7653), (7653, 7678), (7678, 7703), (7703, 7704), (7704, 7708), (7708, 7733), (7733, 7758), (7758, 7759), (7759, 7763), (7763, 7788), (7788, 7813), (7813, 7814), (7814, 7818), (7818, 7843), (7843, 7868), (7868, 7869), (7869, 7873), (7873, 7898), (7898, 7923), (7923, 7924), (7924, 7928), (7928, 7953), (7953, 7978), (7978, 7979), (7979, 7983), (7983, 8008), (8008, 8033), (8033, 8034), (8034, 8038), (8038, 8063), (8063, 8088), (8088, 8089), (8089, 8093), (8093, 8118), (8118, 8143), (8143, 8144), (8144, 8148), (8148, 8173), (8173, 8198), (8198, 8199), (8199, 8203), (8203, 8228), (8228, 8253), (8253, 8254), (8254, 8258), (8258, 8283), (8283, 8308), (8308, 8309), (8309, 8313), (8313, 8338), (8338, 8363), (8363, 8367), (8367, 8368), (8368, 8372), (8372, 8397), (8397, 8422), (8422, 8423), (8423, 8427), (8427, 8452), (8452, 8477), (8477, 8478), (8478, 8482), (8482, 8507), (8507, 8532), (8532, 8533), (8533, 8537), (8537, 8562), (8562, 8587), (8587, 8602)]

PROP = pd.read_fwf(path, colspecs=col_specification, names = colnames, nrows=rng)

PROP['situs_street_prefx'].fillna('', inplace=True)
PROP['situs_num'].fillna('0', inplace=True)

for i in range(rng):
    #print(int(PROP['situs_num'][i]), PROP['situs_street_prefx'][i], PROP['situs_street'][i], PROP['situs_street_suffix'][i], PROP['situs_zip'][i])
    #st_num = str(int(PROP['situs_num'][i])) 
    #st_prefix = PROP['situs_street_prefx'][i] 
    #st_name = PROP['situs_street'][i] 
    #st_suffix = PROP['situs_street_suffix'][i] 
    #zipcode = str(PROP['situs_zip'][i])
    
    
    #print(PROP['situs_num'][i], PROP['situs_street_prefx'][i] , PROP['situs_street'][i], PROP['situs_street_suffix'][i], PROP['situs_zip'][i])
    '''try:
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + \
                                str(int(PROP['situs_num'][i])) + "+" \
                                + PROP['situs_street_prefx'][i] + "+" \
                                + PROP['situs_street'][i] + "+" \
                                + PROP['situs_street_suffix'][i] + ",+" \
                                + str(PROP['situs_zip'][i]) + \
                                "&key=" + API_KEY)
    except:
        pass
    data = response.json()
    #formatted_address = data['results'][0].get("formatted_address")
    #lat = data['results'][0].get("geometry").get("location").get("lat")
    #lng = data['results'][0].get("geometry").get("location").get("lng")
    
    #append address, lat, long
    #just gonna skip for now...
    try:
        results.append([PROP['prop_id'][i], data['results'][0].get("formatted_address"),\
                        data['results'][0].get("geometry").get("location").get("lat"),\
                        data['results'][0].get("geometry").get("location").get("lng")])    
    except:
        pass'''
        
#this is used to write relevant info to file...
    try:
        results.append([PROP['prop_id'][i], \
                        str(int(PROP['situs_num'][i])),\
                        PROP['situs_street_prefx'][i],\
                        PROP['situs_street'][i],\
                        PROP['situs_street_suffix'][i],\
                        str(PROP['situs_zip'][i])])    
    except:
        pass   
        
 #50 requests per second max, don't think I'll hit
print(str(rng) + " results in --- %s seconds ---" % (time.time() - start_time))
print("Writing to results file...")

#the file we write results to in the directory
f = open("results"+ file_num + ".csv", "w+")
#Write Source,Target so we can use in Gephi for post-processing
#f.write("ID,Address,City,State,Country,Lat,Long\n")
#f.write("ID,Address,City,State,Country,Lat,Long\n")

for x in results:
    f.write(str(x[0]) + ',' + str(x[1]) + ',' + str(x[2]) + ',' + str(x[3]) + ',' + str(x[4]) +',' + str(x[5]) + "\n")
    #f.write(str(x[0]) + ',' + str(x[1]) + ',' + str(x[2]) + str(x[3]) + ',' + str(x[4]) + "\n")
f.close()


