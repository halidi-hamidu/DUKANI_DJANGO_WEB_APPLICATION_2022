import soup

#_Civil_registration_numbers
try:
  get_is_there_a_need_to_collect_civil_registration_numbers_on_the_deceased = soup.find('id10069').text
except:
  get_is_there_a_need_to_collect_civil_registration_numbers_on_the_deceased = "None"

try:
  get_do_you_have_a_death_certificate_from_the_civil_registry = soup.find('id10069_a').text
except:
  get_do_you_have_a_death_certificate_from_the_civil_registry = "None"

try:
  get_death_registration_number_or_certificate = soup.find('id10070').text
except:
  get_death_registration_number_or_certificate = "None"

try:
  get_is_the_date_of_registration_available = soup.find('id10071_check').text
except:
  get_is_the_date_of_registration_available = "None"

try:
  get_date_of_registration = soup.find('id10071').text
except:
  get_date_of_registration = "None"


try:
  get_place_of_registration = soup.find('id10072').text
except:
  get_place_of_registration = "None"

try:
  get_national_identification_number_of_deceased = soup.find('id10073').text
except:
  get_national_identification_number_of_deceased = "None"

try:
  get_national_identification_number_of_deceased = soup.find('id10073').text
except:
  get_national_identification_number_of_deceased = "None"

# Community death
try:
  get_did_the_baby_ever_cry = soup.find('id10104').text
except:
  get_did_the_baby_ever_cry = "None"

try:
  get_did_the_baby_cry_immediately_after_birth_even_if_only_a_little_bit = soup.find('id10105').text
except:
  get_did_the_baby_cry_immediately_after_birth_even_if_only_a_little_bit = "None"

try:
  get_how_many_minutes_after_birth_did_the_baby_first_cry = soup.find('id10106').text
except:
  get_how_many_minutes_after_birth_did_the_baby_first_cry = "None"

try:
  get_did_the_baby_stop_being_able_to_cry = soup.find('id10107').text
except:
  get_did_the_baby_stop_being_able_to_cry = "None"

try:
  get_how_many_hours_before_death_did_the_baby_stop_crying = soup.find('id10108').text
except:
  get_how_many_hours_before_death_did_the_baby_stop_crying = "None"

try:
  get_did_the_baby_ever_move = soup.find('id10109').text
except:
  get_did_the_baby_ever_move = "None"

try:
  get_did_the_baby_ever_breathe = soup.find('id101010').text
except:
  get_did_the_baby_ever_breathe = "None"

try:
  get_did_the_baby_breathe_immediately_after_birth_even_a_little = soup.find('id101011').text
except:
  get_did_the_baby_breathe_immediately_after_birth_even_a_little = "None"

try:
  get_did_the_baby_have_a_breathing_problem = soup.find('id101012').text
except:
  get_did_the_baby_have_a_breathing_problem = "None"

try:
  get_was_the_baby_given_assistance_to_breathe_at_birth = soup.find('id101013').text
except:
  get_was_the_baby_given_assistance_to_breathe_at_birth = "None"

try:
  get_if_the_baby_did_not_show_any_sign_of_life_was_it_born_dead = soup.find('id101014').text
except:
  get_if_the_baby_did_not_show_any_sign_of_life_was_it_born_dead = "None"

try:
  get_were_there_any_bruises_or_signs_of_injury_on_babys_body_after_the_birth = soup.find('id101015').text
except:
  get_were_there_any_bruises_or_signs_of_injury_on_babys_body_after_the_birth = "None"

try:
  get_was_the_babys_body_soft_pulpy_and_discoloured_and_the_skin_peeling_away = soup.find('id101016').text
except:
  get_was_the_babys_body_soft_pulpy_and_discoloured_and_the_skin_peeling_away = "None"

# history of injuries_accidents
try:
  get_did_she_or_he_suffer_from_any_injury_or_accident_that_led_to_her_his_death = soup.find('id10077').text
except:
  get_did_she_or_he_suffer_from_any_injury_or_accident_that_led_to_her_his_death = "None"

# injuries and accidents detail
try:
  get_was_it_a_road_traffic_accident = soup.find('id10079').text
except:
  get_was_it_a_road_traffic_accident = "None"

try:
  get_what_was_her_his_role_in_the_road_traffic_accident = soup.find('id10080').text
except:
  get_what_was_her_his_role_in_the_road_traffic_accident = "None"

try:
  get_what_was_the_counterpart_that_was_hit_during_the_road_traffic_accident = soup.find('id10081').text
except:
  get_what_was_the_counterpart_that_was_hit_during_the_road_traffic_accident  = "None"

try:
  get_was_she_or_he_injured_in_a_non_road_transport_accident = soup.find('id10082').text
except:
  get_was_she_or_he_injured_in_a_non_road_transport_accident  = "None"

try:
  get_was_she_or_he_injured_in_a_fall = soup.find('id10083').text
except:
  get_was_she_or_he_injured_in_a_fall  = "None"

try:
  get_was_there_any_poisoning = soup.find('id10084').text
except:
  get_was_there_any_poisoning  = "None"

try:
  get_did_she_or_he_die_of_drowning = soup.find('id10085').text
except:
  get_did_she_or_he_die_of_drowning  = "None"

try:
  get_was_she_or_injured_by_a_bite_or_sting_by_venomous_animal = soup.find('id10086').text
except:
  get_was_she_or_injured_by_a_bite_or_sting_by_venomous_animal  = "None"

try:
  get_was_she_or_he_injured_by_an_animal_or_insect_non_venomous = soup.find('id10087').text
except:
  get_was_she_or_he_injured_by_an_animal_or_insect_non_venomous  = "None"

try:
  get_what_was_the_animal_insect = soup.find('id10088').text
except:
  get_what_was_the_animal_insect  = "None"

try:
  get_was_she_or_he_injured_by_burns_fire = soup.find('id10089').text
except:
  get_was_she_or_he_injured_by_burns_fire  = "None"

try:
  get_was_she_or_he_subject_to_violence_suicide_homicide_abuse = soup.find('id10090').text
except:
  get_was_she_or_he_subject_to_violence_suicide_homicide_abuse  = "None"

try:
  get_was_she_or_he_injured_by_a_firearm = soup.find('id10091').text
except:
  get_was_she_or_he_injured_by_a_firearm  = "None"

try:
  get_was_she_or_he_stabbed_cut_or_pierced = soup.find('id10092').text
except:
  get_was_she_or_he_stabbed_cut_or_pierced  = "None"

try:
  get_was_she_or_he_strangled = soup.find('id10093').text
except:
  get_was_she_or_he_strangled  = "None"

try:
  get_was_she_or_he_injured_by_a_blunt_force = soup.find('id10094').text
except:
  get_was_she_or_he_injured_by_a_blunt_force  = "None"

try:
  get_was_she_or_he_injured_by_a_force_of_nature = soup.find('id10095').text
except:
  get_was_she_or_he_injured_by_a_force_of_nature  = "None"

try:
  get_was_it_electrocution = soup.find('id10096').text
except:
  get_was_it_electrocution  = "None"

try:
  get_did_she_or_he_encounter_any_other_injury = soup.find('id10097').text
except:
  get_did_she_or_he_encounter_any_other_injury  = "None"

try:
  get_was_the_injury_accidental = soup.find('id10098').text
except:
  get_was_the_injury_accidental  = "None"

try:
  get_was_the_injury_self_inflicted = soup.find('id10099').text
except:
  get_was_the_injury_self_inflicted  = "None"

try:
  get_was_the_injury_intentionally_inflicted_by_someone_else = soup.find('id100100').text
except:
  get_was_the_injury_intentionally_inflicted_by_someone_else  = "None" 

# health history
try:
  get_how_many_days_old_was_the_baby_when_the_fatal_illness_started = soup.find('id10351').text
except:
  get_how_many_days_old_was_the_baby_when_the_fatal_illness_started  = "None" 

try:
  get_before_the_illness_that_led_to_death_was_the_baby_the_child_growing_normally = soup.find('id10408').text
except:
  get_before_the_illness_that_led_to_death_was_the_baby_the_child_growing_normally  = "None" 

# duration of illness
try:
  get_for_how_many_days_was_or_he_she_ill_before_death = soup.find('id10120_0').text
except:
  get_for_how_many_days_was_or_he_she_ill_before_death  = "None" 

try:
  get_for_how_lon_was_she_or_he_ill_before_death = soup.find('id10120_unit').text
except:
  get_for_how_lon_was_she_or_he_ill_before_death  = "None" 

try:
  get_months = soup.find('id10121').text
except:
  get_months  = "None" 

try:
  get_years = soup.find('id10122').text
except:
  get_years  = "None"

try:
  get_days = soup.find('id10120_1').text
except:
  get_days  = "None"

try:
  get_calculated_number_of_days_with_illness = soup.find('id10120').text
except:
  get_calculated_number_of_days_with_illness  = "None" 


try:
  get_did_she_or_he_die_suddenly = soup.find('id10123').text
except:
  get_did_she_or_he_die_suddenly  = "None" 



# Medical history associated with final illness
try:
  get_was_there_any_diagnosis_by_a_health_professional_of_tuberculosis = soup.find('id10125').text
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_tuberculosis  = "None" 

try:
  get_was_an_hiV_test_ever_positive = soup.find('id10126').text
except:
  get_was_an_hiV_test_ever_positive  = "None" 

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_AidS = soup.find('id10127').text
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_AiDS  = "None" 


try:
  get_did_she_or_he_have_a_recent_positive_test_by_a_health_professional_for_malaria = soup.find('id10128').text
except:
  get_did_she_or_he_have_a_recent_positive_test_by_a_health_professional_for_malaria  = "None" 

try:
  get_did_she_or_he_have_a_recent_negative_test_by_a_health_professional_for_malaria = soup.find('id10129').text
except:
  get_did_she_or_he_have_a_recent_negative_test_by_a_health_professional_for_malaria  = "None" 

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_dengue_fever =  soup.find('id10130').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_dengue_fever = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_measles =  soup.find('id10131').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_measles = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_high_blood_pressure =  soup.find('id10132').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_high_blood_pressure = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_heart_disease = soup.find('id10133').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_heart_disease = 'None'


try:
  get_was_there_any_diagnosis_by_a_health_professional_of_diabetes = soup.find('id10134').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_diabetes = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_asthma = soup.find('id10135').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_asthma = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_epilepsy = soup.find('id10136').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_epilepsy = 'None'


try:
  get_was_there_any_diagnosis_by_a_health_professional_of_cancer = soup.find('id10137').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_cancer = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_Chronic_Obstructive_Pulmonary_Disease_COPD = soup.find('id10138').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_Chronic_Obstructive_Pulmonary_Disease_COPD = 'None'


try:
  get_was_there_any_diagnosis_by_a_health_professional_of_dementia = soup.find('id10139').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_dementia = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_depression = soup.find('id10140').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_depression = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_stroke = soup.find('id10141').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_stroke = 'None'


try:
  get_was_there_any_diagnosis_by_a_health_professional_of_sickle_cell_disease = soup.find('id10142').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_sickle_cell_disease = 'None'

try:
  get_was_there_any_diagnosis_by_a_health_professional_of_kidney_disease = soup.find('id10143').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_kidney_disease = 'None'


try:
  get_was_there_any_diagnosis_by_a_health_professional_of_liver_disease = soup.find('id10144').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_liver_disease = 'None'


try:
  get_was_there_any_diagnosis_by_a_health_professional_of_COViD_19 = soup.find('id10482').text 
except:
  get_was_there_any_diagnosis_by_a_health_professional_of_COViD_19 = 'None'

try:
  get_did_she_or_he_have_a_recent_test_by_a_health_professional_for_COViD_19 = soup.find('id10483').text 
except:
  get_did_she_or_he_have_a_recent_test_by_a_health_professional_for_COViD_19 = 'None'


try:
  get_what_was_the_result = soup.find('id10484').text 
except:
  get_what_was_the_result = 'None'

# General signs and symptoms associated with final illness
try:
  get_did_she_or_he_have_a_fever = soup.find('id10147').text 
except:
  get_did_she_or_he_have_a_fever = 'None'

try:
  get_how_many_days_did_the_fever_last = soup.find('id10148_a').text 
except:
  get_how_many_days_did_the_fever_last = 'None'

try:
  get_how_long_did_the_fever_last = soup.find('id10148_units').text 
except:
  get_how_long_did_the_fever_last = 'None'

try:
  get_enter_how_long_the_fever_lasted_in_days = soup.find('id10148_b').text 
except:
  get_enter_how_long_the_fever_lasted_in_days = 'None'

try:
  get_enter_how_long_the_fever_lasted_in_months = soup.find('id10148_c').text 
except:
  get_enter_how_long_the_fever_lasted_in_months = 'None'

try:
  get_how_many_days_did_the_fever_last = soup.find('id10148').text 
except:
  get_how_many_days_did_the_fever_last = 'None'

try:
  get_did_the_fever_continue_until_death = soup.find('id10149').text 
except:
  get_did_the_fever_continue_until_death = 'None'

try:
  get_how_severe_was_the_fever = soup.find('id10150').text 
except:
  get_how_severe_was_the_fever = 'None'

try:
  get_what_was_the_pattern_of_the_fever = soup.find('id10151').text 
except:
  get_what_was_the_pattern_of_the_fever = 'None'

try:
  get_did_she_or_he_have_night_sweats = soup.find('id10152').text 
except:
  get_did_she_or_he_have_night_sweats = 'None'

try:
  get_did_she_or_he_have_a_cough = soup.find('id10153').text 
except:
  get_did_she_or_he_have_a_cough = 'None'

try:
  get_for_how__long_did_she_or_he_have_a_cough = soup.find('id10154_units').text 
except:
  get_for_how__long_did_she_or_he_have_a_cough = 'None'

try:
  get_enter_how_long_she_or_he_had_a_cough_in_days = soup.find('id10154_a').text 
except:
  get_enter_how_long_she_or_he_had_a_cough_in_days = 'None'

try:
  get_enter_how_long_she_or_he_had_a_cough_in_months = soup.find('id10154_b').text 
except:
  get_enter_how_long_she_or_he_had_a_cough_in_months = 'None'

try:
  get_for_how__many_days_did_she_or_he_have_a_cough = soup.find('id10154').text 
except:
  get_for_how__many_days_did_she_or_he_have_a_cough = 'None'


try:
  get_was_the_cough_productive_with_sputum = soup.find('id10155').text 
except:
  get_was_the_cough_productive_with_sputum = 'None'

try:
  get_was_the_cough_very_severe = soup.find('id10156').text 
except:
  get_was_the_cough_very_severe = 'None'

try:
  get_did_she_or_he_cough_up_blood = soup.find('id10157').text 
except:
  get_did_she_or_he_cough_up_blood = 'None'

try:
  get_did_she_or_he_make_a_whooping_sound_when_coughing = soup.find('id10158').text 
except:
  get_did_she_or_he_make_a_whooping_sound_when_coughing = 'None'

try:
  get_did_she_or_he_have_any_difficulty_breathing = soup.find('id10159').text 
except:
  get_did_she_or_he_have_any_difficulty_breathing = 'None'
 
# duration of breathing_difficulty
try:
  get_for_how_many_days_did_the_difficulty_breathing_last = soup.find('id10161_0').text 
except:
  get_for_how_many_days_did_the_difficulty_breathing_last = 'None'

try:
  get_for_how_long_did_the_difficult_breathing_last = soup.find('id10161_unit').text 
except:
  get_for_how_long_did_the_difficult_breathing_last = 'None'

try:
  get_enter_how_long_the_difficult_breathing_lasted_in_days = soup.find('id10161_1').text 
except:
  get_enter_how_long_the_difficult_breathing_lasted_in_days = 'None'

try:
  get_enter_how_long_the_difficult_breathing_lasted_in_months = soup.find('id10162').text 
except:
  get_enter_how_long_the_difficult_breathing_lasted_in_months = 'None'

try:
  get_enter_how_long_the_difficult_breathing_lasted_in_years = soup.find('id10163').text 
except:
  get_enter_how_long_the_difficult_breathing_lasted_in_years = 'None'
try:
  get_calculated_number_of_days_with_illness = soup.find('id10161').text 
except:
  get_calculated_number_of_days_with_illness = 'None'


try:
  get_was_the_difficulty_continuous_or_on_and_off = soup.find('id10165').text 
except:
  get_was_the_difficulty_continuous_or_on_and_off = 'None'

try:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_fast_breathing = soup.find('id10166').text 
except:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_fast_breathing = 'None'

try:
  get_for_how_many_days_did_the_fast_breathing_last = soup.find('id10167_a').text 
except:
  get_for_how_many_days_did_the_fast_breathing_last = 'None'

try:
  get_how_long_did_the_fast_breathing_last = soup.find('id10167_units').text 
except:
  get_how_long_did_the_fast_breathing_last = 'None'

try:
  get_enter_how_long_the_fast_breathing_lasted_in_days = soup.find('id10167_b').text 
except:
  get_enter_how_long_the_fast_breathing_lasted_in_days = 'None'

try:
  get_enter_how_long_the_fast_breathing_lasted_in_months = soup.find('id10167_c').text 
except:
  get_enter_how_long_the_fast_breathing_lasted_in_months = 'None'

try:
  get_how_long_did_the_fast_breathing_last = soup.find('id10167').text 
except:
  get_how_long_did_the_fast_breathing_last = 'None'

try:
  get_did_she_or_he_have_breathlessness = soup.find('id10168').text 
except:
  get_did_she_or_he_have_breathlessness = 'None'

try:
  get_for_how_many_days_did_she_or_he_have_breathlessness = soup.find('id10169_a').text 
except:
  get_for_how_many_days_did_she_or_he_have_breathlessness = 'None'

try:
  get_how_long_did_she_or_he_have_breathlessness = soup.find('id10169_units').text 
except:
  get_how_long_did_she_or_he_have_breathlessness = 'None'
  
try:
  get_enter_how_long_she_or_he_had_breathlessness_in_days = soup.find('id10169_b').text 
except:
  get_enter_how_long_she_or_he_had_breathlessness_in_days = 'None'

try:
  get_enter_how_long_she_or_he_had_breathlessness_in_months = soup.find('id10169_c').text 
except:
  get_enter_how_long_she_or_he_had_breathlessness_in_months = 'None'

try:
  get_how_long_did_she_or_he_have_breathlessness = soup.find('id10169').text 
except:
  get_how_long_did_she_or_he_have_breathlessness = 'None'

try:
  get_was_she_or_he_unable_to_carry_out_daily_routines_due_to_breathlessness = soup.find('id10170').text 
except:
  get_was_she_or_he_unable_to_carry_out_daily_routines_due_to_breathlessness = 'None'


try:
  get_was_she_or_he_breathless_while_lying_flat = soup.find('id10171').text 
except:
  get_was_she_or_he_breathless_while_lying_flat = 'None'

try:
  get_did_you_see_the_lower_chest_wall_ribs_being_pulled_in_as_the_child_breathed_in = soup.find('id10172').text 
except:
  get_did_you_see_the_lower_chest_wall_ribs_being_pulled_in_as_the_child_breathed_in = 'None'


try:
  get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following = soup.find('id10173_nc').text 
except:
  get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following = 'None'

# (id10173_check)_it_is_not_possible_to_select_don't_know_or_refuse_together_with_other_options._Please_go_back_and_correct_the_selection._
try:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_wheezing = soup.find('id10173_a').text 
except:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_wheezing = 'None'

try:
  get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following = soup.find('id10173').text 
except:
  get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following = 'None'

try:
  get_did_she_or_he_have_chest_pain = soup.find('id10174').text 
except:
  get_did_she_or_he_have_chest_pain = 'None'

try:
  get_was_the_chest_pain_severe = soup.find('id10175').text 
except:
  get_was_the_chest_pain_severe = 'None'
  
try:
  get_how_many_days_before_death_did_she_or_he_have_chest_pain = soup.find('id10176').text 
except:
  get_how_many_days_before_death_did_she_or_he_have_chest_pain = 'None'

#_duration_of_the_chest_pain

try:
  get_how_long_did_the_chest_pain_last_ = soup.find('id10178_unit').text 
except:
  get_how_long_did_the_chest_pain_last_ = 'None'

try:
  get_enter_how_long_the_chest_pain_lasted_in_minutes = soup.find('id10178').text 
except:
  get_enter_how_long_the_chest_pain_lasted_in_minutes = 'None'

try:
  get_enter_how_long_the_chest_pain_lasted_in_hours = soup.find('id10179').text 
except:
  get_enter_how_long_the_chest_pain_lasted_in_hours = 'None'

try:
  get_enter_how_long_the_chest_pain_lasted_in_days = soup.find('id10179_1').text 
except:
  get_enter_how_long_the_chest_pain_lasted_in_days = 'None'

try:
  get_did_she_or_he_have_more_frequent_loose_or_liquid_stools_than_usual = soup.find('id10181').text 
except:
  get_did_she_or_he_have_more_frequent_loose_or_liquid_stools_than_usual = 'None'


try:
  get_how_long_did_she_or_he_have_frequent_loose_or_liquid_stools = soup.find('id10182_units').text 
except:
  get_how_long_did_she_or_he_have_frequent_loose_or_liquid_stools = 'None'

try:
  get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_days = soup.find('id10182_a').text 
except:
  get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_days = 'None'


try:
  get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_months = soup.find('id10182_b').text 
except:
  get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_months = 'None'

try:
  get_for_how_many_days_did_she_or_he_have_frequent_loose_or_liquid_stools = soup.find('id10182').text 
except:
  get_for_how_many_days_did_she_or_he_have_frequent_loose_or_liquid_stools = 'None'
  
try:
  get_how_many_stools_did_the_baby_or_child_have_on_the_day_that_loose_liquid_stools_were_most_frequent = soup.find('id10183').text 
except:
  get_how_many_stools_did_the_baby_or_child_have_on_the_day_that_loose_liquid_stools_were_most_frequent = 'None'


try:
  get_how_many_days_before_death_did_the_frequent_loose_or_liquid_stools_start = soup.find('id10184_a').text 
except:
  get_how_many_days_before_death_did_the_frequent_loose_or_liquid_stools_start = 'None'


try:
  get_how_long_before_death_did_the_frequent_loose_or_liquid_stools_start = soup.find('id10184_units').text 
except:
  get_how_long_before_death_did_the_frequent_loose_or_liquid_stools_start = 'None'


try:
  get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_days = soup.find('id10184_b').text 
except:
  get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_days = 'None'

try:
  get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_months = soup.find('id10184_c').text 
except:
  get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_months = 'None'


try:
  get_did_the_frequent_loose_or_liquid_stools_continue_until_death = soup.find('id10185').text 
except:
  get_did_the_frequent_loose_or_liquid_stools_continue_until_death = 'None'

try:
  get_at_any_time_during_the_final_illness_was_there_blood_in_the_stools = soup.find('id10186').text 
except:
  get_at_any_time_during_the_final_illness_was_there_blood_in_the_stools = 'None'

try:
  get_was_there_blood_in_the_stool_up_until_death = soup.find('id10187').text 
except:
  get_was_there_blood_in_the_stool_up_until_death = 'None'

try:
  get_did_she_or_he_vomit = soup.find('id10188').text 
except:
  get_did_she_or_he_vomit = 'None'

try:
  get_to_clarify_did_she_or_he_vomit_in_the_week_preceding_the_death = soup.find('id10189').text 
except:
  get_to_clarify_did_she_or_he_vomit_in_the_week_preceding_the_death = 'None'

try:
  get_how_long_before_death_did_she_or_he_vomit = soup.find('id10190_units').text 
except:
  get_how_long_before_death_did_she_or_he_vomit = 'None'

try:
  get_enter_how_long_before_deathshe_or_he_vomited_in_days = soup.find('id10190_a').text 
except:
  get_enter_how_long_before_deathshe_or_he_vomited_in_days = 'None'


try:
  get_enter_how_long_before_deathshe_or_he_vomited_in_months = soup.find('id10190_b').text 
except:
  get_enter_how_long_before_deathshe_or_he_vomited_in_months = 'None'


try:
  get_was_there_blood_in_the_vomit = soup.find('id10191').text 
except:
  get_was_there_blood_in_the_vomit = 'None'


try:
  get_was_the_vomit_black = soup.find('id10192').text 
except:
  get_was_the_vomit_black = 'None'

try:
  get_did_she_or_he_have_any_belly_abdominal_problem = soup.find('id10193').text 
except:
  get_did_she_or_he_have_any_belly_abdominal_problem = 'None'

try:
  get_did_she_or_he_have_belly_abdominal_pain = soup.find('id10194').text 
except:
  get_did_she_or_he_have_belly_abdominal_pain = 'None'

  
try:
  get_was_the_belly_abdominal_pain_severe = soup.find('id10195').text 
except:
  get_was_the_belly_abdominal_pain_severe = 'None'

#_Belly_pain  
try:
  get_for_how_long_did_she_or_he_have_belly_abdominal_pain_ = soup.find('id10196_unit').text 
except:
  get_for_how_long_did_she_or_he_have_belly_abdominal_pain_ = 'None'


try:
  get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_hours = soup.find('id10196').text 
except:
  get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_hours = 'None'

try:
  get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_days = soup.find('id10197_a').text 
except:
  get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_days = 'None'

try:
  get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_months = soup.find('id10198').text 
except:
  get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_months = 'None'

try:
  get_Calculated_number_of_days_with_belly_pain = soup.find('id10197').text 
except:
  get_Calculated_number_of_days_with_belly_pain = 'None'
  
try:
  get_was_the_pain_in_the_upper_or_lower_belly_abdomen = soup.find('id10199').text 
except:
  get_was_the_pain_in_the_upper_or_lower_belly_abdomen = 'None'

try:
  get_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen = soup.find('id10200').text 
except:
  get_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen = 'None'

try:
  get_for_how_long_before_death_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen = soup.find('id10201_unit').text 
except:
  get_for_how_long_before_death_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen = 'None'

try:
  get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_days = soup.find('id10201_a').text 
except:
  get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_days = 'None'

try:
  get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_months = soup.find('id10202').text 
except:
  get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_months = 'None'

try:
  get_Calculated_number_of_days_with_protruding_belly_abdomen = soup.find('id10201').text 
except:
  get_Calculated_number_of_days_with_protruding_belly_abdomen = 'None'

try:
  get_how_rapidly_did_she_or_he_develop_the_protruding_belly_abdomen = soup.find('id10203').text 
except:
  get_how_rapidly_did_she_or_he_develop_the_protruding_belly_abdomen = 'None'

try:
  get_did_she_or_he_have_any_mass_in_the_belly_abdomen = soup.find('id10204').text 
except:
  get_did_she_or_he_have_any_mass_in_the_belly_abdomen = 'None'

try:
  get_for_how_long_did_she_or_he_have_a_mass_in_the_belly_abdomen = soup.find('id10205_unit').text 
except:
  get_for_how_long_did_she_or_he_have_a_mass_in_the_belly_abdomen = 'None'

try:
  get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_days = soup.find('id10205_a').text 
except:
  get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_days = 'None'

try:
  get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_months = soup.find('id10206').text 
except:
  get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_months = 'None'

try:
  get_Calculated_number_of_days_with_a_mass_in_the_belly_abdomen = soup.find('id10205').text 
except:
  get_Calculated_number_of_days_with_a_mass_in_the_belly_abdomen = 'None'

try:
  get_did_she_or_he_have_a_severe_headache = soup.find('id10207').text 
except:
  get_did_she_or_he_have_a_severe_headache = 'None'


try:
  get_did_she_or_he_have_a_stiff_neck_during_illness_that_led_to_death = soup.find('id10208').text 
except:
  get_did_she_or_he_have_a_stiff_neck_during_illness_that_led_to_death = 'None'


try:
  get_how_long_before_death_did_she_or_he_have_stiff_neck = soup.find('id10209_units').text 
except:
  get_how_long_before_death_did_she_or_he_have_stiff_neck = 'None'

try:
  get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_days = soup.find('id10209_a').text 
except:
  get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_days = 'None'


try:
  get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_months = soup.find('id10209_b').text 
except:
  get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_months = 'None'

try:
  get_for_how_many_days_before_death_did_she_or_he_have_stiff_neck = soup.find('id10209').text 
except:
  get_for_how_many_days_before_death_did_she_or_he_have_stiff_neck = 'None'

try:
  get_did_she_or_he_have_a_painful_neck_during_the_illness_that_led_to_death = soup.find('id10210').text 
except:
  get_did_she_or_he_have_a_painful_neck_during_the_illness_that_led_to_death = 'None'
 
try:
  get_how_long_before_death_did_she_or_he_have_a_painful_neck = soup.find('id10211_units').text 
except:
  get_how_long_before_death_did_she_or_he_have_a_painful_neck = 'None'
 
try:
  get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_days = soup.find('id10211_a').text 
except:
  get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_days = 'None'
 
try:
  get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_months = soup.find('id10211_b').text 
except:
  get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_months = 'None'

try:
  get_for_how_many_days_before_death_did_she_or_he_have_a_painful_neck = soup.find('id10211').text 
except:
  get_for_how_many_days_before_death_did_she_or_he_have_a_painful_neck = 'None'
 
try:
  get_did_she_or_he_have_mental_confusion = soup.find('id10212').text 
except:
  get_did_she_or_he_have_mental_confusion = 'None'
 
try:
  get_how_long_did_she_or_he_have_mental_confusion = soup.find('id10213_units').text 
except:
  get_how_long_did_she_or_he_have_mental_confusion = 'None'
 
try:
  get_enter_how_long_she_or_he_had_mental_confusion_in_days = soup.find('id10213_a').text 
except:
  get_enter_how_long_she_or_he_had_mental_confusion_in_days = 'None'
 
try:
  get_enter_how_long_she_or_he_had_mental_confusion_in_months = soup.find('id10213_b').text 
except:
  get_enter_how_long_she_or_he_had_mental_confusion_in_months = 'None'
 
try:
  get_for_how_many_months_did_she_or_he_have_mental_confusion = soup.find('id10213').text 
except:
  get_for_how_many_months_did_she_or_he_have_mental_confusion = 'None'

try:
  get_was_she_or_he_unconscious_during_the_illness_thatledto_death = soup.find('id10214').text 
except:
  get_was_she_or_he_unconscious_during_the_illness_thatledto_death = 'None'
 
try:
  get_was_she_or_he_unconscious_for_more_than_24_hours_before_death = soup.find('id10215').text 
except:
  get_was_she_or_he_unconscious_for_more_than_24_hours_before_death = 'None'

try:
  get_how_long_before_death_did_unconsciousness_start = soup.find('id10216_units').text 
except:
  get_how_long_before_death_did_unconsciousness_start = 'None'

try:
  get_enter_how_long_before_death_unconsciousness_started_in_hours = soup.find('id10216_a').text 
except:
  get_enter_how_long_before_death_unconsciousness_started_in_hours = 'None'

try:
  get_enter_how_long_before_death_unconsciousness_started_in_days = soup.find('id10216_b').text 
except:
  get_enter_how_long_before_death_unconsciousness_started_in_days = 'None'
 
try:
  get_how_many_hours_before_death_did_unconsciousness_start = soup.find('id10216').text 
except:
  get_how_many_hours_before_death_did_unconsciousness_start = 'None'
 
try:
  get_did_the_unconsciousness_start_suddenly_quickly_at_least_within_a_single_day = soup.find('id10217').text 
except:
  get_did_the_unconsciousness_start_suddenly_quickly_at_least_within_a_single_day = 'None'
 
try:
  get_did_the_unconsciousness_continue_until_death = soup.find('id10218').text 
except:
  get_did_the_unconsciousness_continue_until_death = 'None'
 
try:
  get_did_she_or_he_have_convulsions = soup.find('id10219').text 
except:
  get_did_she_or_he_have_convulsions = 'None'

try:
  get_did_she_or_he_experience_any_generalized_convulsions_or_fits_during_the_illness_that_led_to_death = soup.find('id10220').text 
except:
  get_did_she_or_he_experience_any_generalized_convulsions_or_fits_during_the_illness_that_led_to_death = 'None'
 
try:
  get_for_how_many_minutes_did_the_convulsions_last = soup.find('id10221').text 
except:
  get_for_how_many_minutes_did_the_convulsions_last = 'None'
 
try:
  get_did_she_or_he_become_unconscious_immediately_after_the_convulsion = soup.find('id10222').text 
except:
  get_did_she_or_he_become_unconscious_immediately_after_the_convulsion = 'None'
 
try:
  get_did_she_or_he_have_any_urine_problems = soup.find('id10223').text 
except:
  get_did_she_or_he_have_any_urine_problems = 'None'
 
try:
  get_did_she_or_he_go_to_urinate_more_often_than_usual = soup.find('id10225').text 
except:
  get_did_she_or_he_go_to_urinate_more_often_than_usual = 'None'
 
try:
  get_during_the_final_illness_did_she_or_he_ever_pass_blood_in_the_urine = soup.find('id10226').text 
except:
  get_during_the_final_illness_did_she_or_he_ever_pass_blood_in_the_urine = 'None'
 
try:
  get_did_she_or_he_stop_urinating = soup.find('id10224').text 
except:
  get_did_she_or_he_stop_urinating = 'None'
 
try:
  get_did_she_or_he_have_sores_or_ulcers_anywhere_on_the_body = soup.find('id10227').text 
except:
  get_did_she_or_he_have_sores_or_ulcers_anywhere_on_the_body = 'None'

try:
  get_did_she_or_he_have_sores = soup.find('id10228').text 
except:
  get_did_she_or_he_have_sores = 'None'

try:
  get_did_the_sores_have_clear_fluid_or_pus = soup.find('id10229').text 
except:
  get_did_the_sores_have_clear_fluid_or_pus = 'None'
 
try:
  get_did_she_or_he_have_an_ulcer_pit_on_the_foot = soup.find('id10230').text 
except:
  get_did_she_or_he_have_an_ulcer_pit_on_the_foot = 'None'
 
 
try:
  get_did_the_ulcer_on_the_foot_ooze_pus = soup.find('id10231').text 
except:
  get_did_the_ulcer_on_the_foot_ooze_pus = 'None'
 
try:
  get_how_long__did_the_ulcer_on_the_foot_ooze_pus = soup.find('id10232_units').text 
except:
  get_how_long__did_the_ulcer_on_the_foot_ooze_pus = 'None'
 
try:
  get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_days = soup.find('id10232_a').text 
except:
  get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_days = 'None'
 
try:
  get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_months = soup.find('id10232_b').text 
except:
  get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_months = 'None'
 
try:
  get_for_how_many_days_did_the_ulcer_on_the_foot_ooze_pus = soup.find('id10232').text 
except:
  get_for_how_many_days_did_the_ulcer_on_the_foot_ooze_pus = 'None'
 
try:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_any_skin_rash = soup.find('id10233').text 
except:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_any_skin_rash = 'None'
 

try:
  get_for_how_many_days_did_she_or_he_have_the_skin_rash = soup.find('id10234').text 
except:
  get_for_how_many_days_did_she_or_he_have_the_skin_rash = 'None'
 
try:
  get_where_was_the_rash = soup.find('id10235').text 
except:
  get_where_was_the_rash = 'None'
 

# (id10235_check)_it_is_not_possible_to_select_doesn't_Know_or_Refused_to_answer_together_with_other_options._Please_go_back_and_correct_the_selection._
try:
  get_did_she_or_he_have_measles_rash_use_local_term = soup.find('id10236').text 
except:
  get_did_she_or_he_have_measles_rash_use_local_term = 'None'
 
try:
  get_did_she_or_he_ever_have_shingles_or_herpes_zoster = soup.find('id10237').text 
except:
  get_did_she_or_he_ever_have_shingles_or_herpes_zoster = 'None'
 
try:
  get_during_the_illness_that_led_to_death_did_her_his_skin_flake_off_in_patches = soup.find('id10238').text 
except:
  get_during_the_illness_that_led_to_death_did_her_his_skin_flake_off_in_patches = 'None'
 
try:
  get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_that_turned_black = soup.find('id10239').text 
except:
  get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_that_turned_black = 'None'
 
try:
  get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_with_redness_and_swelling = soup.find('id10240').text 
except:
  get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_with_redness_and_swelling = 'None'
 
try:
  get_during_the_illness_that_led_to_death_did_she_or_he_bleed_from_anywhere = soup.find('id10241').text 
except:
  get_during_the_illness_that_led_to_death_did_she_or_he_bleed_from_anywhere = 'None'
 
try:
  get_did_she_or_he_bleed_from_the_nose_mouth_or_anus = soup.find('id10242').text 
except:
  get_did_she_or_he_bleed_from_the_nose_mouth_or_anus = 'None'
 
try:
  get_did_she_or_he_have_noticeable_weight_loss = soup.find('id10243').text 
except:
  get_did_she_or_he_have_noticeable_weight_loss = 'None'
 
try:
  get_was_she_or_he_severely_thin_or_wasted = soup.find('id10244').text 
except:
  get_was_she_or_he_severely_thin_or_wasted = 'None'
 
try:
  get_during_the_illness_that_led_to_death_did_s_he_have_a_whitish_rash_inside_the_mouth_or_on_the_tongue = soup.find('id10245').text 
except:
  get_during_the_illness_that_led_to_death_did_s_he_have_a_whitish_rash_inside_the_mouth_or_on_the_tongue = 'None'

try:
  get_did_she_or_he_have_stiffness_of_the_whole_body_or_was_unable_to_open_the_mouth = soup.find('id10246').text 
except:
  get_did_she_or_he_have_stiffness_of_the_whole_body_or_was_unable_to_open_the_mouth = 'None'
  
try:
  get_did_she_or_he_have_puffiness_of_the_face = soup.find('id10247').text 
except:
  get_did_she_or_he_have_puffiness_of_the_face = 'None'
  
 
try:
  get_how_long_did_she_or_he_have_puffiness_of_the_face = soup.find('id10248_units').text 
except:
  get_how_long_did_she_or_he_have_puffiness_of_the_face = 'None'
  
 
try:
  get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_days = soup.find('id10248_a').text 
except:
  get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_days = 'None'
  
 
try:
  get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_months = soup.find('id10248_b').text 
except:
  get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_months = 'None'
  
 
try:
  get_for_how_many_days_did_she_or_he_have_puffiness_of_the_face = soup.find('id10248').text 
except:
  get_for_how_many_days_did_she_or_he_have_puffiness_of_the_face = 'None'
  
 
try:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_swollen_legs_or_feet = soup.find('id10249').text 
except:
  get_during_the_illness_that_led_to_death_did_she_or_he_have_swollen_legs_or_feet = 'None'
  
try:
  get_how_long_did_the_swelling_last = soup.find('id10250_units').text 
except:
  get_how_long_did_the_swelling_last = 'None'
  
try:
  get_enter_how_long_the_swelling_lasted_in_days = soup.find('id10250_a').text 
except:
  get_enter_how_long_the_swelling_lasted_in_days = 'None'
  
try:
  get_how_many_days_did_the_swelling_last = soup.find('id10250_b').text 
except:
  get_how_many_days_did_the_swelling_last = 'None'
  
try:
  get_did_she_or_he_have_both_feet_swollen = soup.find('id10251').text 
except:
  get_did_she_or_he_have_both_feet_swollen = 'None'
  
try:
  get_did_she_or_he_have_general_puffiness_all_over_his_her_body = soup.find('id10252').text 
except:
  get_did_she_or_he_have_general_puffiness_all_over_his_her_body = 'None'
  
try:
  get_did_she_or_he_have_any_lumps = soup.find('id10253').text 
except:
  get_did_she_or_he_have_any_lumps = 'None'
  
try:
  get_did_she_or_he_have_any_lumps_or_lesions_in_the_mouth = soup.find('id10254').text 
except:
  get_did_she_or_he_have_any_lumps_or_lesions_in_the_mouth = 'None'
  
try:
  get_did_she_or_he_have_any_lumps_on_the_neck = soup.find('id10255').text 
except:
  get_did_she_or_he_have_any_lumps_on_the_neck = 'None'
  
try:
  get_did_she_or_he_have_any_lumps_on_the_armpit = soup.find('id10256').text 
except:
  get_did_she_or_he_have_any_lumps_on_the_armpit = 'None'
  
try:
  get_did_she_or_he_have_any_lumps_on_the_groin = soup.find('id10257').text 
except:
  get_did_she_or_he_have_any_lumps_on_the_groin = 'None'
  
try:
  get_was_she_or_he_in_any_way_paralysed = soup.find('id10258').text 
except:
  get_was_she_or_he_in_any_way_paralysed = 'None'
  
try:
  get_did_she_or_he_have_paralysis_of_only_one_side_of_the_body = soup.find('id10259').text 
except:
  get_did_she_or_he_have_paralysis_of_only_one_side_of_the_body = 'None'
  
try:
  get_which_were_the_limbs_or_body_parts_paralysed = soup.find('id10260').text 
except:
  get_which_were_the_limbs_or_body_parts_paralysed = 'None'
  
  
# (id10260_check)_it_is_not_possible_to_select_only_one_side_paralysed_and_left_and_right_side_or__whole_body_together._Please_go_back_and_correct_the_selection._
# (id10260_check2)_it_is not possible to select doesn't Know or Refused_to_answer_together_with_other_options._Please_go_back_and_correct_the_selection._
try:
  get_did_she_or_he_have_difficulty_swallowing = soup.find('id10261').text 
except:
  get_did_she_or_he_have_difficulty_swallowing = 'None'
 
try:
  get_for_how_long_before_death_did_she_or_he_have_difficulty_swallowing = soup.find('id10262_units').text 
except:
  get_for_how_long_before_death_did_she_or_he_have_difficulty_swallowing = 'None'

try:
  get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_days = soup.find('id10262_a').text 
except:
  get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_days = 'None'

try:
  get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_months = soup.find('id10262_b').text 
except:
  get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_months = 'None'

try:
  get_for_how_many_days_before_death_did_she_or_he_have_difficulty_swallowing = soup.find('id10262').text 
except:
  get_for_how_many_days_before_death_did_she_or_he_have_difficulty_swallowing = 'None'

try:
  get_was_the_difficulty_with_swallowing_with_solids_liquids_or_both = soup.find('id10263').text 
except:
  get_was_the_difficulty_with_swallowing_with_solids_liquids_or_both = 'None'

try:
  get_did_she_or_he_have_pain_upon_swallowing = soup.find('id10264').text 
except:
  get_did_she_or_he_have_pain_upon_swallowing = 'None'

try:
  get_did_she_or_he_have_yellow_discoloration_of_the_eyes = soup.find('id10265').text 
except:
  get_did_she_or_he_have_yellow_discoloration_of_the_eyes = 'None'

try:
  get_for_how_long_did_she_or_he_have_the_yellow_discoloration = soup.find('id10266_units').text 
except:
  get_for_how_long_did_she_or_he_have_the_yellow_discoloration = 'None'

try:
  get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_days = soup.find('id10266_a').text 
except:
  get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_days = 'None'


 
try:
  get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_months = soup.find('id10266_b').text 
except:
  get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_months = 'None'

try:
  get_for_how_many_days_did_she_or_he_have_the_yellow_discoloration = soup.find('id10266').text 
except:
  get_for_how_many_days_did_she_or_he_have_the_yellow_discoloration = 'None'

try:
  get_did_her_his_hair_change_in_color_to_a_reddish_or_yellowish_color = soup.find('id10267').text 
except:
  get_did_her_his_hair_change_in_color_to_a_reddish_or_yellowish_color = 'None'

try:
  get_did_she_or_he_look_pale_thinning_lack_of_blood_or_have_pale_palms_eyes_or_nail_beds = soup.find('id10268').text 
except:
  get_did_she_or_he_look_pale_thinning_lack_of_blood_or_have_pale_palms_eyes_or_nail_beds = 'None'


 
try:
  get_did_she_or_he_have_sunken_eyes = soup.find('id10269').text 
except:
  get_did_she_or_he_have_sunken_eyes = 'None'

 
try:
  get_did_she_or_he_drink_a_lot_more_water_than_usual = soup.find('id10270').text 
except:
  get_did_she_or_he_drink_a_lot_more_water_than_usual = 'None'

 
try:
  get_was_the_baby_able_to_suckle_or_bottle_feed_within_the_first_24_hours_after_birth = soup.find('id10271').text 
except:
  get_was_the_baby_able_to_suckle_or_bottle_feed_within_the_first_24_hours_after_birth = 'None'

 
try:
  get_did_the_baby_ever_suckle_in_a_normal_way = soup.find('id10272').text 
except:
  get_did_the_baby_ever_suckle_in_a_normal_way = 'None'

try:
  get_did_the_baby_stop_suckling = soup.find('id10273').text 
except:
  get_did_the_baby_stop_suckling = 'None'

try:
  get_how_many_days_after_birth_did_the_baby_stop_suckling = soup.find('id10274_a').text 
except:
  get_how_many_days_after_birth_did_the_baby_stop_suckling = 'None'

try:
  get_how_long_after_birth_did_the_baby_stop_suckling = soup.find('id10274_units').text 
except:
  get_how_long_after_birth_did_the_baby_stop_suckling = 'None'

try:
  get_enter_how_long_after_birth__the_baby_stopped_suckling_in_days = soup.find('id10274_b').text 
except:
  get_enter_how_long_after_birth__the_baby_stopped_suckling_in_days = 'None'

try:
  get_enter_how_long_after_birth__the_baby_stopped_suckling_in_months = soup.find('id10274_c').text 
except:
  get_enter_how_long_after_birth__the_baby_stopped_suckling_in_months = 'None'

try:
  get_how_many_days_after_birth_did_the_baby_stop_suckling = soup.find('id10274').text 
except:
  get_how_many_days_after_birth_did_the_baby_stop_suckling = 'None'

try:
  get_did_the_baby_have_convulsions_starting_within_the_first_24_hours_of_life = soup.find('id10275').text 
except:
  get_did_the_baby_have_convulsions_starting_within_the_first_24_hours_of_life = 'None'

try:
  get_did_the_baby_have_convulsions_starting_more_than_24_hours_after_birth = soup.find('id10276').text 
except:
  get_did_the_baby_have_convulsions_starting_more_than_24_hours_after_birth = 'None'

try:
  get_did_the_babys_body_become_stiff_with_the_back_arched_backwards = soup.find('id10277').text 
except:
  get_did_the_babys_body_become_stiff_with_the_back_arched_backwards = 'None'

 
try:
  get_during_the_illness_that_led_to_death_did_the_baby_have_a_bulging_or_raised_fontanelle_ = soup.find('id10278').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_have_a_bulging_or_raised_fontanelle_ = 'None'

try:
  get_during_the_illness_that_led_to_death_did_the_baby_have_a_sunken_fontanelle = soup.find('id10279').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_have_a_sunken_fontanelle = 'None'

try:
  get_during_the_illness_that_led_to_death_did_the_baby_become_unresponsive_or_unconscious = soup.find('id10281').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_become_unresponsive_or_unconscious = 'None'

try:
  get_did_the_baby_become_unresponsive_or_unconscious_soon_after_birth_within_less_than_24_hours = soup.find('id10282').text 
except:
  get_did_the_baby_become_unresponsive_or_unconscious_soon_after_birth_within_less_than_24_hours = 'None'
 
#_Neonatal_child_questions_part_C
try:
  get_during_the_illness_that_led_to_death_did_the_baby_become_cold_to_touch = soup.find('id10284').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_become_cold_to_touch = 'None'

try:
  get_how_many_days_old_was_the_baby_when_it_started_feeling_cold_to_touch = soup.find('id10285').text 
except:
  get_how_many_days_old_was_the_baby_when_it_started_feeling_cold_to_touch = 'None'

try:
  get_during_the_illness_that_led_to_death_did_the_baby_become_lethargic_after_a_period_of_normal_activity = soup.find('id10286').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_become_lethargic_after_a_period_of_normal_activity = 'None'

try:
  get_did_the_baby_have_redness_or_pus_drainage_from_the_umbilical_cord_stump = soup.find('id10287').text 
except:
  get_did_the_baby_have_redness_or_pus_drainage_from_the_umbilical_cord_stump = 'None'


try:
  get_during_the_illness_that_led_to_death_did_the_baby_have_skin_ulcers_or_pits = soup.find('id10288').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_have_skin_ulcers_or_pits = 'None'

try:
  get_during_the_illness_that_led_to_death_did_the_baby_have_yellow_skin_palms_hand_or_soles_foot = soup.find('id10289').text 
except:
  get_during_the_illness_that_led_to_death_did_the_baby_have_yellow_skin_palms_hand_or_soles_foot = 'None'

try:
  get_did_the_baby_or_infant_appear_to_be_healthy_and_then_just_die_suddenly = soup.find('id10290').text 
except:
  get_did_the_baby_or_infant_appear_to_be_healthy_and_then_just_die_suddenly = 'None'



# pregnancy_women	Signs and symptoms associated with pregnancy and women
try:
  get_did_she_have_any_swelling_or_lump_in_the_breast = soup.find('Id10294').text 
except:
  get_did_she_have_any_swelling_or_lump_in_the_breast = 'None'

try:
  get_did_she_have_any_ulcers_pits_in_the_breast = soup.find('Id10295').text 
except:
  get_did_she_have_any_ulcers_pits_in_the_breast = 'None'

try:
  get_did_she_ever_have_a_period_or_menstruate = soup.find('Id10296').text 
except:
  get_did_she_ever_have_a_period_or_menstruate = 'None'

try:
  get_when_she_had_her_period_did_she_have_vaginal_bleeding_in_between_menstrual_periods = soup.find('Id10297').text 
except:
  get_when_she_had_her_period_did_she_have_vaginal_bleeding_in_between_menstrual_periods = 'None'

try:
  get_was_the_bleeding_excessive = soup.find('Id10298').text 
except:
  get_was_the_bleeding_excessive = 'None'

try:
  get_was_there_excessive_vaginal_bleeding_in_the_week_prior_to_death = soup.find('Id10301').text 
except:
  get_was_there_excessive_vaginal_bleeding_in_the_week_prior_to_death = 'None'

try:
  get_did_her_menstrual_period_stop_naturally_because_of_menopause_or_removal_of_uterus = soup.find('Id10299').text 
except:
  get_did_her_menstrual_period_stop_naturally_because_of_menopause_or_removal_of_uterus = 'None'

try:
  get_at_the_time_of_death_was_her_period_overdue = soup.find('Id10302').text 
except:
  get_at_the_time_of_death_was_her_period_overdue = 'None'

try:
  get_for_how_many_weeks_had_her_period_been_overdue = soup.find('Id10303').text 
except:
  get_for_how_many_weeks_had_her_period_been_overdue = 'None'

try:
  get_did_she_have_vaginal_bleeding_after_cessation_of_menstruation = soup.find('Id10300').text 
except:
  get_did_she_have_vaginal_bleeding_after_cessation_of_menstruation = 'None'

try:
  get_did_she_have_a_sharp_pain_in_her_belly_abdomen_shortly_before_death = soup.find('Id10304').text 
except:
  get_did_she_have_vaginal_bleeding_after_cessation_of_menstruation = 'None'

try:
  get_was_she_pregnant_or_in_labour_at_the_time_of_death = soup.find('Id10305').text 
except:
  get_was_she_pregnant_or_in_labour_at_the_time_of_death = 'None'

try:
  get_did_she_die_within_6_weeks_of_delivery_abortion_or_miscarriage = soup.find('Id10306').text 
except:
  get_did_she_die_within_6_weeks_of_delivery_abortion_or_miscarriage = 'None'

try:
  get_did_this_woman_die_more_than_6_weeks_after_being_pregnant_or_delivering_a_baby = soup.find('Id10307').text 
except:
  get_did_this_woman_die_more_than_6_weeks_after_being_pregnant_or_delivering_a_baby = 'None'

try:
  get_was_this_a_woman_who_died_less_than_1_year_after_being_pregnant_or_delivering_a_baby = soup.find('Id10308').text 
except:
  get_was_this_a_woman_who_died_less_than_1_year_after_being_pregnant_or_delivering_a_baby = 'None'

try:
  get_for_how_many_months_was_she_pregnant = soup.find('Id10309').text 
except:
  get_for_how_many_months_was_she_pregnant = 'None'

try:
  get_please_confirm_when_she_died_she_was_NEITHER_pregnant_NOR_had_delivered_had_an_abortion_or_miscarried_within_12_months_of_when_she_died_is_that_right = soup.find('Id10310').text 
except:
  get_please_confirm_when_she_died_she_was_NEITHER_pregnant_NOR_had_delivered_had_an_abortion_or_miscarried_within_12_months_of_when_she_died_is_that_right = 'None'

# Id10310_check	(Id10310_check) if_the_response_is_NO_DONT_KNOw_OR_REFUSED_it_indicates_some_uncertainty_as_to_whether_the_cause_of_death_could_have_been_a_maternal_or_pregnancy_related_cause_Go_back_to_the_question_did_she_ever_have_a_period_or_menstruate_and_follow_the_process_again_If_it_is_confirmed_that_the_death_was_related_to_pregnancy_proceed_with_the_next_question_did_she_die_during_labour_or_delivery_
#_group_maternal	Questions_about_possible_maternal_deaths
try:
  get_did_she_die_during_labour_or_delivery = soup.find('Id10312').text 
except:
  get_did_she_die_during_labour_or_delivery = 'None'

try:
  get_did_she_die_after_delivering_a_baby = soup.find('Id10313').text 
except:
  get_did_she_die_after_delivering_a_baby = 'None'

try:
  get_did_she_die_within_24_hours_after_delivery = soup.find('Id10314').text 
except:
  get_did_she_die_within_24_hours_after_delivery = 'None'

try:
  get_did_she_die_within_6_weeks_of_childbirth = soup.find('Id10315_a').text 
except:
  get_did_she_die_within_24_hours_after_delivery = 'None'

try:
  get_did_she_die_within_6_weeks_of_childbirth = soup.find('Id10315').text 
except:
  get_did_she_die_within_6_weeks_of_childbirth = 'None'

try:
  get_did_she_give_birth_to_a_live_baby_within_6_weeks_of_her_death = soup.find('Id10316').text 
except:
  get_did_she_give_birth_to_a_live_baby_within_6_weeks_of_her_death = 'None'

try:
  get_get_did_she_die_during_or_after_a_multiple_pregnancy = soup.find('Id10317').text 
except:
  get_get_did_she_die_during_or_after_a_multiple_pregnancy = 'None'

try:
  get_was_she_breastfeeding_the_child_in_the_days_before_death = soup.find('Id10318').text 
except:
  get_was_she_breastfeeding_the_child_in_the_days_before_death = 'None'

try:
  get_how_many_births_including_still_births_did_she_the_mother_have_before_this_baby = soup.find('Id10319').text 
except:
  get_how_many_births_including_still_births_did_she_the_mother_have_before_this_baby = 'None'

try:
  get_had_she_had_any_previous_Caesarean_section = soup.find('Id10320').text 
except:
  get_had_she_had_any_previous_Caesarean_section = 'None'

try:
  get_during_pregnancy_did_she_suffer_from_high_blood_pressure = soup.find('Id10321').text 
except:
  get_during_pregnancy_did_she_suffer_from_high_blood_pressure = 'None'

try:
  get_did_she_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery = soup.find('Id10322').text 
except:
  get_did_she_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery = 'None'

try:
  get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_convulsions = soup.find('Id10323').text 
except:
  get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_convulsions = 'None'

try:
  get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_blurred_vision = soup.find('Id10324').text 
except:
  get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_blurred_vision = 'None'

try:
  get_did_bleeding_occur_while_she_was_pregnant = soup.find('Id10325').text 
except:
  get_did_bleeding_occur_while_she_was_pregnant = 'None'

try:
  get_was_there_vaginal_bleeding_during_the_first_6_months_of_pregnancy = soup.find('Id10326').text 
except:
  get_was_there_vaginal_bleeding_during_the_first_6_months_of_pregnancy = 'None'

try:
  get_was_there_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started = soup.find('Id10327').text 
except:
  get_was_there_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started = 'None'


try:
  get_did_she_have_excessive_bleeding_during_labour_or_delivery = soup.find('Id10328').text 
except:
  get_did_she_have_excessive_bleeding_during_labour_or_delivery = 'None'

try:
  get_did_she_have_excessive_bleeding_after_delivery_or_abortion = soup.find('Id10329').text 
except:
  get_did_she_have_excessive_bleeding_after_delivery_or_abortion = 'None'

try:
  get_was_the_placenta_completely_delivered = soup.find('Id10330').text 
except:
  get_was_the_placenta_completely_delivered = 'None'

try:
  get_did_she_deliver_or_try_to_deliver_an_abnormally_positioned_baby = soup.find('Id10331').text 
except:
  get_did_she_deliver_or_try_to_deliver_an_abnormally_positioned_baby = 'None'

try:
  get_for_how_many_hours_was_she_in_labour = soup.find('Id10332').text 
except:
  get_for_how_many_hours_was_she_in_labour = 'None'

try:
  get_did_she_attempt_to_terminate_the_pregnancy = soup.find('Id10333').text 
except:
  get_did_she_attempt_to_terminate_the_pregnancy = 'None'

try:
  get_did_she_recently_have_a_pregnancy_that_ended_in_an_abortion_spontaneous_or_induced = soup.find('Id10334').text 
except:
  get_did_she_recently_have_a_pregnancy_that_ended_in_an_abortion_spontaneous_or_induced = 'None'

try:
  get_get_did_she_die_during_an_abortion = soup.find('Id10335').text 
except:
  get_get_did_she_die_during_an_abortion = 'None'

try:
  get_get_did_she_die_within_6_weeks_of_having_an_abortion = soup.find('Id10336').text 
except:
  get_get_did_she_die_within_6_weeks_of_having_an_abortion = 'None'

try:
  get_where_did_she_give_birth_complete_the_miscarriage_have_the_abortion = soup.find('Id10337').text 
except:
  get_where_did_she_give_birth_complete_the_miscarriage_have_the_abortion = 'None'

try:
  get_did_she_receive_professional_assistance_during_the_delivery = soup.find('Id10338').text 
except:
  get_did_she_receive_professional_assistance_during_the_delivery = 'None'

try:
  get_who_delivered_the_baby_completed_the_miscarriage___performed_the_abortion = soup.find('Id10339').text 
except:
  get_who_delivered_the_baby_completed_the_miscarriage___performed_the_abortion = 'None'
 
#_deliverytype	how_did_the_mother_deliver_her_baby
try:
  get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum = soup.find('Id10342').text 
except:
  get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum = 'None'
 
try:
  get_was_the_delivery_vaginal_with_forceps_or_vacuum = soup.find('Id10343').text 
except:
  get_was_the_delivery_vaginal_with_forceps_or_vacuum = 'None'
 
try:
  get_was_the_delivery_a_Caesarean_section = soup.find('Id10344').text 
except:
  get_was_the_delivery_a_Caesarean_section = 'None'
 
try:
  get_was_the_baby_born_more_than_one_month_early = soup.find('Id10347').text 
except:
  get_was_the_baby_born_more_than_one_month_early = 'None'
 
	
try:
  get_did_she_have_an_operation_to_remove_her_uterus_shortly_before_death = soup.find('Id10340').text 
except:
  get_did_she_have_an_operation_to_remove_her_uterus_shortly_before_death = 'None'
 
	
#_neonatal_child	Neonatal_and_child_history_signs_and_symptoms
try:
  get_how_old_was_the_child_when_the_fatal_illness_started = soup.find('Id10352_units').text 
except:
  get_how_old_was_the_child_when_the_fatal_illness_started = 'None'
 
	
try:
  get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_months = soup.find('Id10352_a').text 
except:
  get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_months = 'None'
 
	
try:
  get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_years = soup.find('Id10352_b').text 
except:
  get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_years = 'None'
 
	
try:
  get_how_many_years_old_was_the_child_when_the_fatal_illness_started = soup.find('Id10352').text 
except:
  get_how_many_years_old_was_the_child_when_the_fatal_illness_started = 'None'

#_neonatal_childA	Neonatal_child_questions_part_A
	
try:
  get_was_the_child_part_of_a_multiple__birth = soup.find('Id10354').text 
except:
  get_was_the_child_part_of_a_multiple__birth = 'None'

 
try:
  get_was_the_child_the_first_second_or_later_in_the_birth_order = soup.find('Id10355').text 
except:
  get_was_the_child_the_first_second_or_later_in_the_birth_order = 'None'

try:
  get_is_the_mother_still_alive = soup.find('Id10356').text 
except:
  get_is_the_mother_still_alive = 'None'

try:
  get_did_the_mother_die_before_during_or_after_the_delivery = soup.find('Id10357').text 
except:
  get_did_the_mother_die_before_during_or_after_the_delivery = 'None'


#_moth_death	Time_between_delivery_and_death_of_mother

try:
  get_how_long_after_the_delivery_did_the_mother_die = soup.find('Id10358_units').text 
except:
  get_how_long_after_the_delivery_did_the_mother_die = 'None'

try:
  get_how_many_months_after_the_delivery_did_the_mother_die = soup.find('Id10358').text 
except:
  get_how_many_months_after_the_delivery_did_the_mother_die = 'None'

try:
  get_how_many_days_after_the_delivery_did_the_mother_die = soup.find('Id10359').text 
except:
  get_how_many_days_after_the_delivery_did_the_mother_die = 'None'

try:
  get_how_many_weeks_after_the_delivery_did_the_mother_die = soup.find('Id10359_a').text 
except:
  get_how_many_weeks_after_the_delivery_did_the_mother_die = 'None'

	
try:
  get_where_was_the_deceased_born = soup.find('Id10360').text 
except:
  get_where_was_the_deceased_born = 'None'

	
try:
  get_did_you_the_mother_receive_professional_assistance_during_the_delivery = soup.find('Id10361').text 
except:
  get_did_you_the_mother_receive_professional_assistance_during_the_delivery = 'None'


	
try:
  get_at_birth_was_the_baby_of_usual_size = soup.find('Id10362').text 
except:
  get_at_birth_was_the_baby_of_usual_size = 'None'

	
try:
  get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg = soup.find('Id10363').text 
except:
  get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg = 'None'

	
try:
  get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg = soup.find('Id10363').text 
except:
  get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg = 'None'

	
try:
  get_at_birth_was_the_baby_very_much_smaller_than_usual_weighing_under_1_kg = soup.find('Id10364').text 
except:
  get_at_birth_was_the_baby_very_much_smaller_than_usual_weighing_under_1_kg = 'None'

	
try:
  get_at_birth_was_the_baby_larger_than_usual_weighing_over_4point5_kg = soup.find('Id10365').text 
except:
  get_at_birth_was_the_baby_larger_than_usual_weighing_over_4point5_kg = 'None'

#_id1036X_check	(id1036X_check)_it_is_not_possible_to_select_"No_usual_size_at_Birth"_"No_weighing_under_2.5_kg"_and_"No_weighing_over_4.5_kg"_together._Please_go_back_and_correct_the_selection._
	
try:
  get_what_was_the_weight_in_grammes_of_the_deceased_at_birth = soup.find('Id10366').text 
except:
  get_what_was_the_weight_in_grammes_of_the_deceased_at_birth = 'None'
	
try:
  get_how_many_months_long_was_the_pregnancy_before_the_child_was_born = soup.find('Id10367').text 
except:
  get_how_many_months_long_was_the_pregnancy_before_the_child_was_born = 'None'

try:
  get_were_there_any_complications_in_the_late_part_of_the_pregnancy_defined_as_the_last_3_months_before_labour = soup.find('Id10368').text 
except:
  get_were_there_any_complications_in_the_late_part_of_the_pregnancy_defined_as_the_last_3_months_before_labour = 'None'

try:
  get_were_there_any_complications_during_labour_or_delivery = soup.find('Id10369').text 
except:
  get_were_there_any_complications_during_labour_or_delivery = 'None'

try:
  get_was_any_part_of_the_baby_physically_abnormal_at_time_of_delivery_for_example_body_part_too_large_or_too_small_additional_growth_on_body = soup.find('Id10370').text 
except:
  get_was_any_part_of_the_baby_physically_abnormal_at_time_of_delivery_for_example_body_part_too_large_or_too_small_additional_growth_on_body = 'None'

try:
  get_did_the_baby_child_have_a_swelling_or_defect_on_the_back_at_time_of_birth = soup.find('Id10371').text 
except:
  get_did_the_baby_child_have_a_swelling_or_defect_on_the_back_at_time_of_birth = 'None'

try:
  get_did_the_baby_child_have_a_very_large_head_at_time_of_birth = soup.find('Id10372').text 
except:
  get_did_the_baby_child_have_a_very_large_head_at_time_of_birth = 'None'

try:
  get_did_the_baby_child_have_a_very_small_head_at_time_of_birth = soup.find('Id10373').text 
except:
  get_did_the_baby_child_have_a_very_small_head_at_time_of_birth = 'None'

try:
  get_how_many_births_including_stillbirths_did_the_babys_mother_have_before_this_baby = soup.find('Id10394').text 
except:
  get_how_many_births_including_stillbirths_did_the_babys_mother_have_before_this_baby = 'None'

#_neonatal_childB	(neonatal_childB)_Neonatal_child_questions_part_B

try:
  get_was_the_baby_moving_in_the_last_few_days_before_the_birth = soup.find('Id10376').text 
except:
  get_was_the_baby_moving_in_the_last_few_days_before_the_birth = 'None'

try:
  get_did_the_baby_stop_moving_in_the_womb_before_labour_started = soup.find('Id10377').text 
except:
  get_did_the_baby_stop_moving_in_the_womb_before_labour_started = 'None'
 
#_babmove	Baby_moving
try:
  get_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move = soup.find('Id10379_unit').text 
except:
  get_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move = 'None'
 
try:
  get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_days = soup.find('Id10379').text 
except:
  get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_days = 'None'
 
try:
  get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_hours = soup.find('Id10380').text 
except:
  get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_hours = 'None'
 
	
try:
  get_how_many_hours_did_labour_and_delivery_take = soup.find('Id10382').text 
except:
  get_how_many_hours_did_labour_and_delivery_take = 'None'
 
	
try:
  get_was_the_baby_born_24_hours_or_more_after_the_water_broke = soup.find('Id10383').text 
except:
  get_was_the_baby_born_24_hours_or_more_after_the_water_broke = 'None'
 
	
try:
  get_what_was_the_colour_of_the_liquor_when_the_water_broke = soup.find('Id10385').text 
except:
  get_what_was_the_colour_of_the_liquor_when_the_water_broke = 'None'
 
#_mother_deliv	(mother_deliv)_how_was_the_baby_delivered
try:
  get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum = soup.find('Id10387').text 
except:
  get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum = 'None'

try:
  get_was_the_delivery_vaginal_with_forceps_or_vacuum = soup.find('Id10388').text 
except:
  get_was_the_delivery_vaginal_with_forceps_or_vacuum = 'None'

try:
  get_was_the_delivery_a_Caesarean_section = soup.find('Id10389').text 
except:
  get_was_the_delivery_a_Caesarean_section = 'None'

try:
  get_was_the_delivery_a_Caesarean_section = soup.find('Id10389').text 
except:
  get_was_the_delivery_a_Caesarean_section = 'None'

# id10389_check	(id10389_check) it_is_not_possible_to_select_No_to_all_three_previous_questions._Please_go_back_and_review_the_answers._
try:
  get_did_you_the_mother_receive_any_vaccinations_since_reaching_adulthood_including_during_this_pregnancy = soup.find('Id10391').text 
except:
  get_did_you_the_mother_receive_any_vaccinations_since_reaching_adulthood_including_during_this_pregnancy = 'None'
   
try:
  get_how_many_doses = soup.find('Id10392').text 
except:
  get_how_many_doses = 'None'
   
try:
  get_did_you_the_mother_receive_tetanus_toxoid_TT_vaccine = soup.find('Id10393').text 
except:
  get_did_you_the_mother_receive_tetanus_toxoid_TT_vaccine = 'None'
   
try:
  get_during_labour_did_the_babys_mother_suffer_from_fever = soup.find('Id10395').text 
except:
  get_during_labour_did_the_babys_mother_suffer_from_fever = 'None'
   
try:
  get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_high_blood_pressure = soup.find('Id10396').text 
except:
  get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_high_blood_pressure = 'None'
   
try:
  get_did_you_the_babys_mother_have_diabetes_mellitus = soup.find('Id10397').text 
except:
  get_did_you_the_babys_mother_have_diabetes_mellitus = 'None'
   
try:
  get_did_you_the_babys_mother_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery = soup.find('Id10398').text 
except:
  get_did_you_the_babys_mother_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery = 'None'
   
 
try:
  get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_convulsions = soup.find('Id10399').text 
except:
  get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_convulsions = 'None'
   
 
try:
  get_during_the_last_3_months_of_pregnancy_did_you_the_babys_mother_suffer_from_blurred_vision = soup.find('Id10400').text 
except:
  get_during_the_last_3_months_of_pregnancy_did_you_the_babys_mother_suffer_from_blurred_vision = 'None'
 
try:
  get_did_you_the_babys_mother_have_severe_anemia = soup.find('Id10401').text 
except:
  get_did_you_the_babys_mother_have_severe_anemia = 'None'

try:
  get_did_you_the_babys_mother_have_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started = soup.find('Id10402').text 
except:
  get_did_you_the_babys_mother_have_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started = 'None'


try:
  get_did_the_babys_bottom_feet_arm_or_hand_come_out_of_the_vagina_before_its_head = soup.find('Id10403').text 
except:
  get_did_the_babys_bottom_feet_arm_or_hand_come_out_of_the_vagina_before_its_head = 'None'


try:
  get_was_the_umbilical_cord_wrapped_more_than_once_around_the_neck_of_the_child_at_birth = soup.find('Id10404').text 
except:
  get_was_the_umbilical_cord_wrapped_more_than_once_around_the_neck_of_the_child_at_birth = 'None'


try:
  get_was_the_umbilical_cord_delivered_first = soup.find('Id10405').text 
except:
  get_was_the_umbilical_cord_delivered_first = 'None'

try:
  get_was_the_baby_blue_in_colour_at_birth = soup.find('Id10406').text 
except:
  get_was_the_baby_blue_in_colour_at_birth = 'None'

#_risk_factors	Risk_factors

try:
  get_did_she_or_he__drink_alcohol = soup.find('Id10411').text 
except:
  get_did_she_or_he__drink_alcohol = 'None'

try:
  get_did_she_or_he__use_tobacco = soup.find('Id10412').text 
except:
  get_did_she_or_he__use_tobacco = 'None'

try:
  get_did_she_or_he__smoke_tobacco_cigarette_cigar_pipe_etc = soup.find('Id10413').text 
except:
  get_did_she_or_he__smoke_tobacco_cigarette_cigar_pipe_etc = 'None'

try:
  what_kind_of_tobacco_get_did_she_or_he__use = soup.find('Id10414').text 
except:
  what_kind_of_tobacco_get_did_she_or_he__use = 'None'

# id10414_check	(id10414_check)_it_is_not_possible_to_select_cigarettes_or_pipe_and_"no"_to_"get_did_she_or_he__smoke_tobacco"._Please_go_back_and_correct_the_selections.
try:
  get_how_many_cigarettes_get_did_she_or_he__smoke_daily = soup.find('Id10415').text 
except:
  get_how_many_cigarettes_get_did_she_or_he__smoke_daily = 'None'

 
try:
  get_how_many_times_didshe_or_he__use_tobacco_products_each_day = soup.find('Id10416').text 
except:
  get_how_many_times_didshe_or_he__use_tobacco_products_each_day = 'None'
	
#_health_service_utilization	Health_service_utilisation
try:
  get_did_she_or_he__receive_any_treatment_for_the_illness_that_led_to_death = soup.find('Id10418').text 
except:
  get_did_she_or_he__receive_any_treatment_for_the_illness_that_led_to_death = 'None'
	
try:
  get_did_she_or_he_receive_oral_rehydration_salts = soup.find('Id10419').text 
except:
  get_did_she_or_he_receive_oral_rehydration_salts = 'None'
	
try:
  get_did_she_or_he_receive_or_need_intravenous_fluids_drip_treatment = soup.find('Id10420').text 
except:
  get_did_she_or_he_receive_or_need_intravenous_fluids_drip_treatment = 'None'
	
try:
  get_did_she_or_he_receive_or_need_a_blood_transfusion = soup.find('Id10421').text 
except:
  get_did_she_or_he_receive_or_need_a_blood_transfusion = 'None'
	
try:
  get_did_she_or_he_receive_or_need_treatment_food_through_a_tube_passed_through_the_nose = soup.find('Id10422').text 
except:
  get_did_she_or_he_receive_or_need_treatment_food_through_a_tube_passed_through_the_nose = 'None'
	

try:
  get_did_she_or_he_receive_or_need_injectable_antibiotics = soup.find('Id10423').text 
except:
  get_did_she_or_he_receive_or_need_injectable_antibiotics = 'None'
	
try:
  get_did_she_or_he_receive_or_need_antiretroviral_therapy_ART = soup.find('Id10424').text 
except:
  get_did_she_or_he_receive_or_need_antiretroviral_therapy_ART = 'None'
	
try:
  get_did_she_or_he_have_or_need_an_operation_for_the_illness = soup.find('Id10425').text 
except:
  get_did_she_or_he_have_or_need_an_operation_for_the_illness = 'None'
	

try:
  get_did_she_or_he_have_the_operation_within_1_month_before_death = soup.find('Id10426').text 
except:
  get_did_she_or_he_have_the_operation_within_1_month_before_death = 'None'
	

try:
  get_was_she_or_he__discharged_from_hospital_very_ill = soup.find('Id10427').text 
except:
  get_was_she_or_he__discharged_from_hospital_very_ill = 'None'
	
try:
  get_did_she_or_he__receive_any_immunizations = soup.find('Id10428').text 
except:
  get_did_she_or_he__receive_any_immunizations = 'None'
	
try:
  get_do_you_have_the_childs_vaccination_card = soup.find('Id10429').text 
except:
  get_do_you_have_the_childs_vaccination_card = 'None'
	
try:
  get_can_i_see_the_vaccination_card_note_the_vaccines_the_child_received = soup.find('Id10430').text 
except:
  get_can_i_see_the_vaccination_card_note_the_vaccines_the_child_received = 'None'
	
try:
  get_select_EPI_vaccines_done = soup.find('Id10431').text 
except:
  get_select_EPI_vaccines_done = 'None'
	
# id10431_check	(id10431_check)_it_is_not_possible_to_select_"No_vaccines"_"don't_know"_or_"refuse"_together_with_other_options._Please_go_back_and_correct_the_selection._

try:
  get_was_care_sought_outside_the_home_while_she_or_he__had_this_illness = soup.find('Id10432').text 
except:
  get_was_care_sought_outside_the_home_while_she_or_he__had_this_illness = 'None'
	
try:
  get_where_or_from_whom_did_you_seek_care = soup.find('Id10433').text 
except:
  get_where_or_from_whom_did_you_seek_care = 'None'

# id10433_check	(id10433_check)_it_is_not_possible_to_select_"don't_know"_or_"refuse"_together_with_other_options._Please_go_back_and_correct_the_selection._
	
try:
  get_what_was_the_name_and_address_of_any_hospital_health_center_or_clinic_where_care_was_sought = soup.find('Id10434').text 
except:
  get_what_was_the_name_and_address_of_any_hospital_health_center_or_clinic_where_care_was_sought = 'None'

try:
  get_did_a_health_care_worker_tell_you_the_cause_of_death = soup.find('Id10435').text 
except:
  get_did_a_health_care_worker_tell_you_the_cause_of_death = 'None'

try:
  get_what_did_the_health_care_worker_say = soup.find('Id10436').text 
except:
  get_what_did_the_health_care_worker_say = 'None'

try:
  get_do_you_have_any_health_records_that_belonged_to_the_deceased = soup.find('Id10437').text 
except:
  get_do_you_have_any_health_records_that_belonged_to_the_deceased = 'None'

try:
  get_can_i_see_the_health_records = soup.find('Id10438').text 
except:
  get_can_i_see_the_health_records = 'None'


# Id10439_check	(Id10439_check)_is_the_date_of_the_most_recent_(last)_visit_available
try:
  get_record_the_date_of_the_most_recent_last_visit = soup.find('Id10439').text 
except:
  get_record_the_date_of_the_most_recent_last_visit = 'None'

# Id10440_check	(Id10440_check)_is_the_date_of_the_second_most_recent_visit_available
try:
  get_record_the_date_of_the_second_most_recent_visit = soup.find('Id10440').text 
except:
  get_record_the_date_of_the_second_most_recent_visit = 'None'

# Id10441_check	(Id10441_check)_is_the_date_of_the_last_note_on_the_health_records_available
try:
  get_record_the_date_of_the_last_note_on_the_health_records = soup.find('Id10441').text 
except:
  get_record_the_date_of_the_last_note_on_the_health_records = 'None'

try:
  get_record_the_weight_in_kilogrammes_written_at_the_most_recent_last_visit = soup.find('Id10442').text 
except:
  get_record_the_weight_in_kilogrammes_written_at_the_most_recent_last_visit = 'None'

try:
  get_record_the_weight_in_kilogrammes_written_at_the_second_most_recent_visit = soup.find('Id10443').text 
except:
  get_record_the_weight_in_kilogrammes_written_at_the_second_most_recent_visit = 'None'


try:
  get_transcribe_the_last_note_on_the_health_records = soup.find('Id10444').text 
except:
  get_transcribe_the_last_note_on_the_health_records = 'None'

try:
  get_has_the_deceaseds_biological_mother_ever_been_tested_for_HIV = soup.find('Id10445').text 
except:
  get_has_the_deceaseds_biological_mother_ever_been_tested_for_HIV = 'None'

try:
  get_has_the_deceaseds_biological_mother_ever_been_told_she_had_HIV_AIDS_by_a_health_worker = soup.find('Id10446').text 
except:
  get_has_the_deceaseds_biological_mother_ever_been_told_she_had_HIV_AIDS_by_a_health_worker = 'None'

#_back_context	Background_and_context
try:
  get_in_the_final_days_before_death_did_s_he_travel_to_a_hospital_or_health_facility = soup.find('Id10450').text 
except:
  get_in_the_final_days_before_death_did_s_he_travel_to_a_hospital_or_health_facility = 'None'

try:
  get_get_did_she_or_he__use_motorised_transport_to_get_to_the_hospital_or_health_facility = soup.find('Id10451').text 
except:
  get_get_did_she_or_he__use_motorised_transport_to_get_to_the_hospital_or_health_facility = 'None'

try:
  get_were_there_any_problems_during_admission_to_the_hospital_or_health_facility = soup.find('Id10452').text 
except:
  get_were_there_any_problems_during_admission_to_the_hospital_or_health_facility = 'None'


try:
  get_were_there_any_problems_with_the_way_she_or_he__was_treated_medical_treatment_procedures_interpersonal_attitudes_respect_dignity_in_the_hospital_or_health_facility = soup.find('Id10453').text 
except:
  get_were_there_any_problems_with_the_way_she_or_he__was_treated_medical_treatment_procedures_interpersonal_attitudes_respect_dignity_in_the_hospital_or_health_facility = 'None'

try:
  get_were_there_any_problems_getting_medications_or_diagnostic_tests_in_the_hospital_or_health_facility = soup.find('Id10454').text 
except:
  get_were_there_any_problems_getting_medications_or_diagnostic_tests_in_the_hospital_or_health_facility = 'None'

try:
  get_does_it_take_more_than_2_hours_to_get_to_the_nearest_hospital_or_health_facility_from_the_deceaseds_household = soup.find('Id10455').text 
except:
  get_does_it_take_more_than_2_hours_to_get_to_the_nearest_hospital_or_health_facility_from_the_deceaseds_household = 'None'

try:
  get_in_the_final_days_before_death_were_there_any_doubts_about_whether_medical_care_was_needed = soup.find('Id10456').text 
except:
  get_in_the_final_days_before_death_were_there_any_doubts_about_whether_medical_care_was_needed = 'None'

try:
  get_in_the_final_days_before_death_was_traditional_medicine_used = soup.find('Id10457').text 
except:
  get_in_the_final_days_before_death_was_traditional_medicine_used = 'None'

try:
  get_in_the_final_days_before_death_did_anyone_use_a_telephone_or_cell_phone_to_call_for_help = soup.find('Id10458').text 
except:
  get_in_the_final_days_before_death_did_anyone_use_a_telephone_or_cell_phone_to_call_for_help = 'None'

try:
  get_over_the_course_of_illness_did_the_total_costs_of_care_and_treatment_prohibit_other_household_payments = soup.find('Id10459').text 
except:
  get_over_the_course_of_illness_did_the_total_costs_of_care_and_treatment_prohibit_other_household_payments = 'None'


#_Health_ins	Health_insuarance
try:
  get_did_the_deceased_have_Health_insuarance = soup.find('TZ001').text 
except:
  get_did_the_deceased_have_Health_insuarance = 'None'

try:
  get_which_among_the_following_Health_insuarances_did_the_deceased_have = soup.find('TZ002').text 
except:
  get_which_among_the_following_Health_insuarances_did_the_deceased_have = 'None'

try:
  get_Other_Specify = soup.find('TZ002_other').text 
except:
  get_Other_Specify = 'None'

try:
  get_did_the_deceased_use_his_her_Health_insuarance_during_his_her_final_illness = soup.find('TZ003').text 
except:
  get_did_the_deceased_use_his_her_Health_insuarance_during_his_her_final_illness = 'None'


	
try:
  get_which_services_did_the_Health_insuarance_provide = soup.find('TZ004').text 
except:
  get_which_services_did_the_Health_insuarance_provide = 'None'

try:
  get_Other_Specify = soup.find('TZ004_other').text 
except:
  get_Other_Specify = 'None'

try:
  get_why_did_the_deceased_not_use_his_her_health_insuarance = soup.find('TZ005').text 
except:
  get_why_did_the_deceased_not_use_his_her_health_insuarance = 'None'

try:
  get_there_was_another_problem_with_using_the_insuarance_specify = soup.find('TZ005_a').text 
except:
  get_there_was_another_problem_with_using_the_insuarance_specify = 'None'


#_deathcert	Death_certificate_with_cause_of_death
try:
  get_was_a_medical_certificate_of_cause_of_death_issued = soup.find('Id10462').text 
except:
  get_was_a_medical_certificate_of_cause_of_death_issued = 'None'

try:
  get_can_I_see_the_medical_certificate_of_cause_of_death = soup.find('Id10463').text 
except:
  get_can_I_see_the_medical_certificate_of_cause_of_death = 'None'

try:
  get_record_the_immediate_cause_of_death_from_the_certificate_line_1a = soup.find('Id10464').text 
except:
  get_record_the_immediate_cause_of_death_from_the_certificate_line_1a = 'None'

try:
  get_duration_Ia = soup.find('Id10465').text 
except:
  get_duration_Ia = 'None'

try:
  get_record_the_first_antecedent_cause_of_death_from_the_certificate__line_1b = soup.find('Id10466').text 
except:
  get_record_the_first_antecedent_cause_of_death_from_the_certificate__line_1b = 'None'

try:
  get_duration_Ib = soup.find('Id10467').text 
except:
  get_duration_Ib = 'None'

try:
  get_record_the_second_antecedent_cause_of_death_from_the_certificate_line_1c = soup.find('Id10468').text 
except:
  get_record_the_second_antecedent_cause_of_death_from_the_certificate_line_1c = 'None'


try:
  get_duration_Ic = soup.find('Id10469').text 
except:
  get_duration_Ic = 'None'

try:
  get_record_the_third_antecedent_cause_of_death_from_the_certificate_line_1d = soup.find('Id10470').text 
except:
  get_record_the_third_antecedent_cause_of_death_from_the_certificate_line_1d = 'None'

try:
  get_duration_Id = soup.find('Id10471').text 
except:
  get_duration_Id = 'None'


try:
  get_record_the_contributing_causes_of_death_from_the_certificate_part_2 = soup.find('Id10472').text 
except:
  get_record_the_contributing_causes_of_death_from_the_certificate_part_2 = 'None'

try:
  get_duration_part2 = soup.find('Id10473').text 
except:
  get_duration_part2 = 'None'

#_narrat	Open_narrative
try:
  get_Thank_you_for_your_information_Now_can_you_please_tell_me_in_your_own_words_about_the_events_that_led_to_the_death = soup.find('Id10476').text 
except:
  get_Thank_you_for_your_information_Now_can_you_please_tell_me_in_your_own_words_about_the_events_that_led_to_the_death = 'None'

try:
  get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative = soup.find('Id10477').text 
except:
  get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative = 'None'

try:
  get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative = soup.find('Id10478').text 
except:
  get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative = 'None'

try:
  get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative = soup.find('Id10479').text 
except:
  get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative = 'None'


# id10477_check	(id10477_check)_it_is_not_possible_to_select_"don't_know"_or_"None_of_the_above"_together_with_other_options._Please_go_back_and_correct_the_selection._
# id10478_check	(id10478_check)_it_is_not_possible_to_select_"don't_know"_or_"None_of_the_above"_together_with_other_options._Please_go_back_and_correct_the_selection._
# id10479_check	(id10479_check)_it_is_not_possible_to_select_"don't_know"_or_"None_of_the_above"_together_with_other_options._Please_go_back_and_correct_the_selection._
try:
  get_End_time_of_the_interview = soup.find('Id10481').text 
except:
  get_End_time_of_the_interview = 'None'
	
#_comment	(comment)_Comment
try:
  get_Collect_the_GPS_coordinates_of_this_location = soup.find('gps_location').text 
except:
  get_End_time_of_the_interview = 'None'
	
try:
  get_the_GPS_coordinates_represents = soup.find('gps_details').text 
except:
  get_the_GPS_coordinates_represents = 'None'
	
	

dict = {
  
#_Civil_registration_numbers
'get_is_there_a_need_to_collect_civil_registration_numbers_on_the_deceased_id10069':get_is_there_a_need_to_collect_civil_registration_numbers_on_the_deceased,

'get_do_you_have_a_death_certificate_from_the_civil_registry_id10069_a':get_do_you_have_a_death_certificate_from_the_civil_registry,

'get_death_registration_number_or_certificate_id10070':get_death_registration_number_or_certificate,

'get_is_the_date_of_registration_available_id10071_check':get_is_the_date_of_registration_available,

'get_date_of_registration_id10071':get_date_of_registration,


'get_place_of_registration_id10072':get_place_of_registration,

'get_national_identification_number_of_deceased_id10073':get_national_identification_number_of_deceased,

'get_national_identification_number_of_deceased_id10073':get_national_identification_number_of_deceased,

# Community death
'get_did_the_baby_ever_cry_id10104':get_did_the_baby_ever_cry,

'get_did_the_baby_cry_immediately_after_birth_even_if_only_a_little_bit_id10105':get_did_the_baby_cry_immediately_after_birth_even_if_only_a_little_bit,

'get_how_many_minutes_after_birth_did_the_baby_first_cry_id10106':get_how_many_minutes_after_birth_did_the_baby_first_cry,

'get_did_the_baby_stop_being_able_to_cry_id10107':get_did_the_baby_stop_being_able_to_cry,

'get_how_many_hours_before_death_did_the_baby_stop_crying_id10108':get_how_many_hours_before_death_did_the_baby_stop_crying,

'get_did_the_baby_ever_move_id10109':get_did_the_baby_ever_move,

'get_did_the_baby_ever_breathe_id101010':get_did_the_baby_ever_breathe,

'get_did_the_baby_breathe_immediately_after_birth_even_a_little_id101011':get_did_the_baby_breathe_immediately_after_birth_even_a_little,

'get_did_the_baby_have_a_breathing_problem_id101012':get_did_the_baby_have_a_breathing_problem,

'get_was_the_baby_given_assistance_to_breathe_at_birth_id101013':get_was_the_baby_given_assistance_to_breathe_at_birth,

'get_if_the_baby_did_not_show_any_sign_of_life_was_it_born_dead_id101014':get_if_the_baby_did_not_show_any_sign_of_life_was_it_born_dead,

'get_were_there_any_bruises_or_signs_of_injury_on_babys_body_after_the_birth_id101015':get_were_there_any_bruises_or_signs_of_injury_on_babys_body_after_the_birth,

'get_was_the_babys_body_soft_pulpy_and_discoloured_and_the_skin_peeling_away_id101016':get_was_the_babys_body_soft_pulpy_and_discoloured_and_the_skin_peeling_away,

# history of injuries_accidents
'get_did_she_or_he_suffer_from_any_injury_or_accident_that_led_to_her_his_death_id10077':get_did_she_or_he_suffer_from_any_injury_or_accident_that_led_to_her_his_death,

# injuries and accidents detail
'get_was_it_a_road_traffic_accident_id10079':get_was_it_a_road_traffic_accident,

'get_what_was_her_his_role_in_the_road_traffic_accident_id10080':get_what_was_her_his_role_in_the_road_traffic_accident,

'get_what_was_the_counterpart_that_was_hit_during_the_road_traffic_accident_id10081':get_what_was_the_counterpart_that_was_hit_during_the_road_traffic_accident ,

'get_was_she_or_he_injured_in_a_non_road_transport_accident_id10082':get_was_she_or_he_injured_in_a_non_road_transport_accident ,

'get_was_she_or_he_injured_in_a_fall_id10083':get_was_she_or_he_injured_in_a_fall ,

'get_was_there_any_poisoning_id10084':get_was_there_any_poisoning ,

'get_did_she_or_he_die_of_drowning_id10085':get_did_she_or_he_die_of_drowning ,

'get_was_she_or_injured_by_a_bite_or_sting_by_venomous_animal_id10086':get_was_she_or_injured_by_a_bite_or_sting_by_venomous_animal ,

'get_was_she_or_he_injured_by_an_animal_or_insect_non_venomous_id10087':get_was_she_or_he_injured_by_an_animal_or_insect_non_venomous ,

'get_what_was_the_animal_insect_id10088':get_what_was_the_animal_insect ,

'get_was_she_or_he_injured_by_burns_fire_id10089':get_was_she_or_he_injured_by_burns_fire ,

'get_was_she_or_he_subject_to_violence_suicide_homicide_abuse_id10090':get_was_she_or_he_subject_to_violence_suicide_homicide_abuse ,

'get_was_she_or_he_injured_by_a_firearm_id10091':get_was_she_or_he_injured_by_a_firearm ,

'get_was_she_or_he_stabbed_cut_or_pierced_id10092':get_was_she_or_he_stabbed_cut_or_pierced ,

'get_was_she_or_he_strangled_id10093':get_was_she_or_he_strangled ,

'get_was_she_or_he_injured_by_a_blunt_force_id10094':get_was_she_or_he_injured_by_a_blunt_force ,

'get_was_she_or_he_injured_by_a_force_of_nature_id10095':get_was_she_or_he_injured_by_a_force_of_nature ,

'get_was_it_electrocution_id10096':get_was_it_electrocution ,

'get_did_she_or_he_encounter_any_other_injury_id10097':get_did_she_or_he_encounter_any_other_injury ,

'get_was_the_injury_accidental_id10098':get_was_the_injury_accidental ,

'get_was_the_injury_self_inflicted_id10099':get_was_the_injury_self_inflicted ,

'get_was_the_injury_intentionally_inflicted_by_someone_else_id100100':get_was_the_injury_intentionally_inflicted_by_someone_else , 

# health history
'get_how_many_days_old_was_the_baby_when_the_fatal_illness_started_id10351':get_how_many_days_old_was_the_baby_when_the_fatal_illness_started , 

'get_before_the_illness_that_led_to_death_was_the_baby_the_child_growing_normally_id10408':get_before_the_illness_that_led_to_death_was_the_baby_the_child_growing_normally , 

# duration of illness
'get_for_how_many_days_was_or_he_she_ill_before_death_id10120_0':get_for_how_many_days_was_or_he_she_ill_before_death , 

'get_for_how_lon_was_she_or_he_ill_before_death_id10120_unit':get_for_how_lon_was_she_or_he_ill_before_death , 

'get_months_id10121':get_months , 

'get_years_id10122':get_years ,

'get_days_id10120_1':get_days ,

'get_calculated_number_of_days_with_illness_id10120':get_calculated_number_of_days_with_illness , 


'get_did_she_or_he_die_suddenly_id10123':get_did_she_or_he_die_suddenly , 



# Medical history associated with final illness
'get_was_there_any_diagnosis_by_a_health_professional_of_tuberculosis_id10125':get_was_there_any_diagnosis_by_a_health_professional_of_tuberculosis , 

'get_was_an_hiV_test_ever_positive_id10126':get_was_an_hiV_test_ever_positive , 

'get_was_there_any_diagnosis_by_a_health_professional_of_AidS_id10127':get_was_there_any_diagnosis_by_a_health_professional_of_AiDS , 


'get_did_she_or_he_have_a_recent_positive_test_by_a_health_professional_for_malaria_id10128':get_did_she_or_he_have_a_recent_positive_test_by_a_health_professional_for_malaria , 

'get_did_she_or_he_have_a_recent_negative_test_by_a_health_professional_for_malaria_id10129':get_did_she_or_he_have_a_recent_negative_test_by_a_health_professional_for_malaria , 

'get_was_there_any_diagnosis_by_a_health_professional_of_dengue_fever_ id10130':get_was_there_any_diagnosis_by_a_health_professional_of_dengue_fever,

'get_was_there_any_diagnosis_by_a_health_professional_of_measles_ id10131':get_was_there_any_diagnosis_by_a_health_professional_of_measles,

'get_was_there_any_diagnosis_by_a_health_professional_of_high_blood_pressure_ id10132':get_was_there_any_diagnosis_by_a_health_professional_of_high_blood_pressure,

'get_was_there_any_diagnosis_by_a_health_professional_of_heart_disease_id10133':get_was_there_any_diagnosis_by_a_health_professional_of_heart_disease,


'get_was_there_any_diagnosis_by_a_health_professional_of_diabetes_id10134':get_was_there_any_diagnosis_by_a_health_professional_of_diabetes,

'get_was_there_any_diagnosis_by_a_health_professional_of_asthma_id10135':get_was_there_any_diagnosis_by_a_health_professional_of_asthma,

'get_was_there_any_diagnosis_by_a_health_professional_of_epilepsy_id10136':get_was_there_any_diagnosis_by_a_health_professional_of_epilepsy,


'get_was_there_any_diagnosis_by_a_health_professional_of_cancer_id10137':get_was_there_any_diagnosis_by_a_health_professional_of_cancer,

'get_was_there_any_diagnosis_by_a_health_professional_of_Chronic_Obstructive_Pulmonary_Disease_COPD_id10138':get_was_there_any_diagnosis_by_a_health_professional_of_Chronic_Obstructive_Pulmonary_Disease_COPD,


'get_was_there_any_diagnosis_by_a_health_professional_of_dementia_id10139':get_was_there_any_diagnosis_by_a_health_professional_of_dementia,

'get_was_there_any_diagnosis_by_a_health_professional_of_depression_id10140':get_was_there_any_diagnosis_by_a_health_professional_of_depression,

'get_was_there_any_diagnosis_by_a_health_professional_of_stroke_id10141':get_was_there_any_diagnosis_by_a_health_professional_of_stroke,


'get_was_there_any_diagnosis_by_a_health_professional_of_sickle_cell_disease_id10142':get_was_there_any_diagnosis_by_a_health_professional_of_sickle_cell_disease,

'get_was_there_any_diagnosis_by_a_health_professional_of_kidney_disease_id10143':get_was_there_any_diagnosis_by_a_health_professional_of_kidney_disease,


'get_was_there_any_diagnosis_by_a_health_professional_of_liver_disease_id10144':get_was_there_any_diagnosis_by_a_health_professional_of_liver_disease,


'get_was_there_any_diagnosis_by_a_health_professional_of_COViD_19_id10482':get_was_there_any_diagnosis_by_a_health_professional_of_COViD_19,

'get_did_she_or_he_have_a_recent_test_by_a_health_professional_for_COViD_19_id10483':get_did_she_or_he_have_a_recent_test_by_a_health_professional_for_COViD_19,


'get_what_was_the_result_id10484':get_what_was_the_result,

# General signs and symptoms associated with final illness
'get_did_she_or_he_have_a_fever_id10147':get_did_she_or_he_have_a_fever,

'get_how_many_days_did_the_fever_last_id10148_a':get_how_many_days_did_the_fever_last,

'get_how_long_did_the_fever_last_id10148_units':get_how_long_did_the_fever_last,

'get_enter_how_long_the_fever_lasted_in_days_id10148_b':get_enter_how_long_the_fever_lasted_in_days,

'get_enter_how_long_the_fever_lasted_in_months_id10148_c':get_enter_how_long_the_fever_lasted_in_months,

'get_how_many_days_did_the_fever_last_id10148':get_how_many_days_did_the_fever_last,

'get_did_the_fever_continue_until_death_id10149':get_did_the_fever_continue_until_death,

'get_how_severe_was_the_fever_id10150':get_how_severe_was_the_fever,

'get_what_was_the_pattern_of_the_fever_id10151':get_what_was_the_pattern_of_the_fever,

'get_did_she_or_he_have_night_sweats_id10152':get_did_she_or_he_have_night_sweats,

'get_did_she_or_he_have_a_cough_id10153':get_did_she_or_he_have_a_cough,

'get_for_how__long_did_she_or_he_have_a_cough_id10154_units':get_for_how__long_did_she_or_he_have_a_cough,

'get_enter_how_long_she_or_he_had_a_cough_in_days_id10154_a':get_enter_how_long_she_or_he_had_a_cough_in_days,

'get_enter_how_long_she_or_he_had_a_cough_in_months_id10154_b':get_enter_how_long_she_or_he_had_a_cough_in_months,

'get_for_how__many_days_did_she_or_he_have_a_cough_id10154':get_for_how__many_days_did_she_or_he_have_a_cough,


'get_was_the_cough_productive_with_sputum_id10155':get_was_the_cough_productive_with_sputum,

'get_was_the_cough_very_severe_id10156':get_was_the_cough_very_severe,

'get_did_she_or_he_cough_up_blood_id10157':get_did_she_or_he_cough_up_blood,

'get_did_she_or_he_make_a_whooping_sound_when_coughing_id10158':get_did_she_or_he_make_a_whooping_sound_when_coughing,

'get_did_she_or_he_have_any_difficulty_breathing_id10159':get_did_she_or_he_have_any_difficulty_breathing,
 
# duration of breathing_difficulty
'get_for_how_many_days_did_the_difficulty_breathing_last_id10161_0':get_for_how_many_days_did_the_difficulty_breathing_last,

'get_for_how_long_did_the_difficult_breathing_last_id10161_unit':get_for_how_long_did_the_difficult_breathing_last,

'get_enter_how_long_the_difficult_breathing_lasted_in_days_id10161_1':get_enter_how_long_the_difficult_breathing_lasted_in_days,

'get_enter_how_long_the_difficult_breathing_lasted_in_months_id10162':get_enter_how_long_the_difficult_breathing_lasted_in_months,

'get_enter_how_long_the_difficult_breathing_lasted_in_years_id10163':get_enter_how_long_the_difficult_breathing_lasted_in_years,
'get_calculated_number_of_days_with_illness_id10161':get_calculated_number_of_days_with_illness,


'get_was_the_difficulty_continuous_or_on_and_off_id10165':get_was_the_difficulty_continuous_or_on_and_off,

'get_during_the_illness_that_led_to_death_did_she_or_he_have_fast_breathing_id10166':get_during_the_illness_that_led_to_death_did_she_or_he_have_fast_breathing,

'get_for_how_many_days_did_the_fast_breathing_last_id10167_a':get_for_how_many_days_did_the_fast_breathing_last,

'get_how_long_did_the_fast_breathing_last_id10167_units':get_how_long_did_the_fast_breathing_last,

'get_enter_how_long_the_fast_breathing_lasted_in_days_id10167_b':get_enter_how_long_the_fast_breathing_lasted_in_days,

'get_enter_how_long_the_fast_breathing_lasted_in_months_id10167_c':get_enter_how_long_the_fast_breathing_lasted_in_months,

'get_how_long_did_the_fast_breathing_last_id10167':get_how_long_did_the_fast_breathing_last,

'get_did_she_or_he_have_breathlessness_id10168':get_did_she_or_he_have_breathlessness,

'get_for_how_many_days_did_she_or_he_have_breathlessness_id10169_a':get_for_how_many_days_did_she_or_he_have_breathlessness,

'get_how_long_did_she_or_he_have_breathlessness_id10169_units':get_how_long_did_she_or_he_have_breathlessness,
'get_enter_how_long_she_or_he_had_breathlessness_in_days_id10169_b':get_enter_how_long_she_or_he_had_breathlessness_in_days,

'get_enter_how_long_she_or_he_had_breathlessness_in_months_id10169_c':get_enter_how_long_she_or_he_had_breathlessness_in_months,

'get_how_long_did_she_or_he_have_breathlessness_id10169':get_how_long_did_she_or_he_have_breathlessness,

'get_was_she_or_he_unable_to_carry_out_daily_routines_due_to_breathlessness_id10170':get_was_she_or_he_unable_to_carry_out_daily_routines_due_to_breathlessness,


'get_was_she_or_he_breathless_while_lying_flat_id10171':get_was_she_or_he_breathless_while_lying_flat,

'get_did_you_see_the_lower_chest_wall_ribs_being_pulled_in_as_the_child_breathed_in_id10172':get_did_you_see_the_lower_chest_wall_ribs_being_pulled_in_as_the_child_breathed_in,


'get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following_id10173_nc':get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following,

# (id10173_check)_it_is_not_possible_to_select_don't_know_or_refuse_together_with_other_options._Please_go_back_and_correct_the_selection._
'get_during_the_illness_that_led_to_death_did_she_or_he_have_wheezing_id10173_a':get_during_the_illness_that_led_to_death_did_she_or_he_have_wheezing,

'get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following_id10173':get_during_the_illness_that_led_to_death_did_his_her_breathing_sound_like_any_of_the_following,

'get_did_she_or_he_have_chest_pain_id10174':get_did_she_or_he_have_chest_pain,

'get_was_the_chest_pain_severe_id10175':get_was_the_chest_pain_severe,
'get_how_many_days_before_death_did_she_or_he_have_chest_pain_id10176':get_how_many_days_before_death_did_she_or_he_have_chest_pain,

#_duration_of_the_chest_pain

'get_how_long_did_the_chest_pain_last__id10178_unit':get_how_long_did_the_chest_pain_last_,

'get_enter_how_long_the_chest_pain_lasted_in_minutes_id10178':get_enter_how_long_the_chest_pain_lasted_in_minutes,

'get_enter_how_long_the_chest_pain_lasted_in_hours_id10179':get_enter_how_long_the_chest_pain_lasted_in_hours,

'get_enter_how_long_the_chest_pain_lasted_in_days_id10179_1':get_enter_how_long_the_chest_pain_lasted_in_days,

'get_did_she_or_he_have_more_frequent_loose_or_liquid_stools_than_usual_id10181':get_did_she_or_he_have_more_frequent_loose_or_liquid_stools_than_usual,


'get_how_long_did_she_or_he_have_frequent_loose_or_liquid_stools_id10182_units':get_how_long_did_she_or_he_have_frequent_loose_or_liquid_stools,

'get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_days_id10182_a':get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_days,


'get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_months_id10182_b':get_enter_how_long_she_or_he_had_frequent_loose_or_liquid_stools_in_months,

'get_for_how_many_days_did_she_or_he_have_frequent_loose_or_liquid_stools_id10182':get_for_how_many_days_did_she_or_he_have_frequent_loose_or_liquid_stools,
'get_how_many_stools_did_the_baby_or_child_have_on_the_day_that_loose_liquid_stools_were_most_frequent_id10183':get_how_many_stools_did_the_baby_or_child_have_on_the_day_that_loose_liquid_stools_were_most_frequent,


'get_how_many_days_before_death_did_the_frequent_loose_or_liquid_stools_start_id10184_a':get_how_many_days_before_death_did_the_frequent_loose_or_liquid_stools_start,


'get_how_long_before_death_did_the_frequent_loose_or_liquid_stools_start_id10184_units':get_how_long_before_death_did_the_frequent_loose_or_liquid_stools_start,


'get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_days_id10184_b':get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_days,

'get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_months_id10184_c':get_enter_how_long_before_death_the_frequent_loose_or_liquid_stools_started_in_months,


'get_did_the_frequent_loose_or_liquid_stools_continue_until_death_id10185':get_did_the_frequent_loose_or_liquid_stools_continue_until_death,

'get_at_any_time_during_the_final_illness_was_there_blood_in_the_stools_id10186':get_at_any_time_during_the_final_illness_was_there_blood_in_the_stools,

'get_was_there_blood_in_the_stool_up_until_death_id10187':get_was_there_blood_in_the_stool_up_until_death,

'get_did_she_or_he_vomit_id10188':get_did_she_or_he_vomit,

'get_to_clarify_did_she_or_he_vomit_in_the_week_preceding_the_death_id10189':get_to_clarify_did_she_or_he_vomit_in_the_week_preceding_the_death,

'get_how_long_before_death_did_she_or_he_vomit_id10190_units':get_how_long_before_death_did_she_or_he_vomit,

'get_enter_how_long_before_deathshe_or_he_vomited_in_days_id10190_a':get_enter_how_long_before_deathshe_or_he_vomited_in_days,


'get_enter_how_long_before_deathshe_or_he_vomited_in_months_id10190_b':get_enter_how_long_before_deathshe_or_he_vomited_in_months,


'get_was_there_blood_in_the_vomit_id10191':get_was_there_blood_in_the_vomit,


'get_was_the_vomit_black_id10192':get_was_the_vomit_black,

'get_did_she_or_he_have_any_belly_abdominal_problem_id10193':get_did_she_or_he_have_any_belly_abdominal_problem,

'get_did_she_or_he_have_belly_abdominal_pain_id10194':get_did_she_or_he_have_belly_abdominal_pain,

'get_was_the_belly_abdominal_pain_severe_id10195':get_was_the_belly_abdominal_pain_severe,

#_Belly_pain  
'get_for_how_long_did_she_or_he_have_belly_abdominal_pain__id10196_unit':get_for_how_long_did_she_or_he_have_belly_abdominal_pain_,


'get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_hours_id10196':get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_hours,

'get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_days_id10197_a':get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_days,

'get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_months_id10198':get_enter_how_long_she_or_he_had__belly_abdominal_pain_in_months,

'get_Calculated_number_of_days_with_belly_pain_id10197':get_Calculated_number_of_days_with_belly_pain,
'get_was_the_pain_in_the_upper_or_lower_belly_abdomen_id10199':get_was_the_pain_in_the_upper_or_lower_belly_abdomen,

'get_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen_id10200':get_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen,

'get_for_how_long_before_death_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen_id10201_unit':get_for_how_long_before_death_did_she_or_he_have_a_more_than_usually_protruding_belly_abdomen,

'get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_days_id10201_a':get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_days,

'get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_months_id10202':get_enter_how_long_before_death_she_or_he_had_a_more_than_usually_protruding_belly_abdomen_in_months,

'get_Calculated_number_of_days_with_protruding_belly_abdomen_id10201':get_Calculated_number_of_days_with_protruding_belly_abdomen,

'get_how_rapidly_did_she_or_he_develop_the_protruding_belly_abdomen_id10203':get_how_rapidly_did_she_or_he_develop_the_protruding_belly_abdomen,

'get_did_she_or_he_have_any_mass_in_the_belly_abdomen_id10204':get_did_she_or_he_have_any_mass_in_the_belly_abdomen,

'get_for_how_long_did_she_or_he_have_a_mass_in_the_belly_abdomen_id10205_unit':get_for_how_long_did_she_or_he_have_a_mass_in_the_belly_abdomen,

'get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_days_id10205_a':get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_days,

'get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_months_id10206':get_enter_how_long_she_or_he_had_a_mass_in_the_belly_abdomen_in_months,

'get_Calculated_number_of_days_with_a_mass_in_the_belly_abdomen_id10205':get_Calculated_number_of_days_with_a_mass_in_the_belly_abdomen,

'get_did_she_or_he_have_a_severe_headache_id10207':get_did_she_or_he_have_a_severe_headache,


'get_did_she_or_he_have_a_stiff_neck_during_illness_that_led_to_death_id10208':get_did_she_or_he_have_a_stiff_neck_during_illness_that_led_to_death,


'get_how_long_before_death_did_she_or_he_have_stiff_neck_id10209_units':get_how_long_before_death_did_she_or_he_have_stiff_neck,

'get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_days_id10209_a':get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_days,


'get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_months_id10209_b':get_enter_how_long_before_death_did_she_or_he_have_stiff_neck_in_months,

'get_for_how_many_days_before_death_did_she_or_he_have_stiff_neck_id10209':get_for_how_many_days_before_death_did_she_or_he_have_stiff_neck,

'get_did_she_or_he_have_a_painful_neck_during_the_illness_that_led_to_death_id10210':get_did_she_or_he_have_a_painful_neck_during_the_illness_that_led_to_death,
 
'get_how_long_before_death_did_she_or_he_have_a_painful_neck_id10211_units':get_how_long_before_death_did_she_or_he_have_a_painful_neck,
 
'get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_days_id10211_a':get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_days,
 
'get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_months_id10211_b':get_enter_how_long_before_death_she_or_he_had_a_painful_neck_in_months,

'get_for_how_many_days_before_death_did_she_or_he_have_a_painful_neck_id10211':get_for_how_many_days_before_death_did_she_or_he_have_a_painful_neck,
 
'get_did_she_or_he_have_mental_confusion_id10212':get_did_she_or_he_have_mental_confusion,
 
'get_how_long_did_she_or_he_have_mental_confusion_id10213_units':get_how_long_did_she_or_he_have_mental_confusion,
 
'get_enter_how_long_she_or_he_had_mental_confusion_in_days_id10213_a':get_enter_how_long_she_or_he_had_mental_confusion_in_days,
 
'get_enter_how_long_she_or_he_had_mental_confusion_in_months_id10213_b':get_enter_how_long_she_or_he_had_mental_confusion_in_months,
 
'get_for_how_many_months_did_she_or_he_have_mental_confusion_id10213':get_for_how_many_months_did_she_or_he_have_mental_confusion,

'get_was_she_or_he_unconscious_during_the_illness_thatledto_death_id10214':get_was_she_or_he_unconscious_during_the_illness_thatledto_death,
 
'get_was_she_or_he_unconscious_for_more_than_24_hours_before_death_id10215':get_was_she_or_he_unconscious_for_more_than_24_hours_before_death,

'get_how_long_before_death_did_unconsciousness_start_id10216_units':get_how_long_before_death_did_unconsciousness_start,

'get_enter_how_long_before_death_unconsciousness_started_in_hours_id10216_a':get_enter_how_long_before_death_unconsciousness_started_in_hours,

'get_enter_how_long_before_death_unconsciousness_started_in_days_id10216_b':get_enter_how_long_before_death_unconsciousness_started_in_days,
 
'get_how_many_hours_before_death_did_unconsciousness_start_id10216':get_how_many_hours_before_death_did_unconsciousness_start,
 
'get_did_the_unconsciousness_start_suddenly_quickly_at_least_within_a_single_day_id10217':get_did_the_unconsciousness_start_suddenly_quickly_at_least_within_a_single_day,
 
'get_did_the_unconsciousness_continue_until_death_id10218':get_did_the_unconsciousness_continue_until_death,
 
'get_did_she_or_he_have_convulsions_id10219':get_did_she_or_he_have_convulsions,

'get_did_she_or_he_experience_any_generalized_convulsions_or_fits_during_the_illness_that_led_to_death_id10220':get_did_she_or_he_experience_any_generalized_convulsions_or_fits_during_the_illness_that_led_to_death,
 
'get_for_how_many_minutes_did_the_convulsions_last_id10221':get_for_how_many_minutes_did_the_convulsions_last,
 
'get_did_she_or_he_become_unconscious_immediately_after_the_convulsion_id10222':get_did_she_or_he_become_unconscious_immediately_after_the_convulsion,
 
'get_did_she_or_he_have_any_urine_problems_id10223':get_did_she_or_he_have_any_urine_problems,
 
'get_did_she_or_he_go_to_urinate_more_often_than_usual_id10225':get_did_she_or_he_go_to_urinate_more_often_than_usual,
 
'get_during_the_final_illness_did_she_or_he_ever_pass_blood_in_the_urine_id10226':get_during_the_final_illness_did_she_or_he_ever_pass_blood_in_the_urine,
 
'get_did_she_or_he_stop_urinating_id10224':get_did_she_or_he_stop_urinating,
 
'get_did_she_or_he_have_sores_or_ulcers_anywhere_on_the_body_id10227':get_did_she_or_he_have_sores_or_ulcers_anywhere_on_the_body,

'get_did_she_or_he_have_sores_id10228':get_did_she_or_he_have_sores,

'get_did_the_sores_have_clear_fluid_or_pus_id10229':get_did_the_sores_have_clear_fluid_or_pus,
 
'get_did_she_or_he_have_an_ulcer_pit_on_the_foot_id10230':get_did_she_or_he_have_an_ulcer_pit_on_the_foot,
 
 
'get_did_the_ulcer_on_the_foot_ooze_pus_id10231':get_did_the_ulcer_on_the_foot_ooze_pus,
 
'get_how_long__did_the_ulcer_on_the_foot_ooze_pus_id10232_units':get_how_long__did_the_ulcer_on_the_foot_ooze_pus,
 
'get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_days_id10232_a':get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_days,
 
'get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_months_id10232_b':get_enter_how_long_the_ulcer_on_the_foot_oozed_pus_in_months,
 
'get_for_how_many_days_did_the_ulcer_on_the_foot_ooze_pus_id10232':get_for_how_many_days_did_the_ulcer_on_the_foot_ooze_pus,
 
'get_during_the_illness_that_led_to_death_did_she_or_he_have_any_skin_rash_id10233':get_during_the_illness_that_led_to_death_did_she_or_he_have_any_skin_rash,
 

'get_for_how_many_days_did_she_or_he_have_the_skin_rash_id10234':get_for_how_many_days_did_she_or_he_have_the_skin_rash,
 
'get_where_was_the_rash_id10235':get_where_was_the_rash,
 

# (id10235_check)_it_is_not_possible_to_select_doesn't_Know_or_Refused_to_answer_together_with_other_options._Please_go_back_and_correct_the_selection._
'get_did_she_or_he_have_measles_rash_use_local_term_id10236':get_did_she_or_he_have_measles_rash_use_local_term,
 
'get_did_she_or_he_ever_have_shingles_or_herpes_zoster_id10237':get_did_she_or_he_ever_have_shingles_or_herpes_zoster,
 
'get_during_the_illness_that_led_to_death_did_her_his_skin_flake_off_in_patches_id10238':get_during_the_illness_that_led_to_death_did_her_his_skin_flake_off_in_patches,
 
'get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_that_turned_black_id10239':get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_that_turned_black,
 
'get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_with_redness_and_swelling_id10240':get_during_the_illness_that_led_to_death_did_he_she_have_areas_of_the_skin_with_redness_and_swelling,
 
'get_during_the_illness_that_led_to_death_did_she_or_he_bleed_from_anywhere_id10241':get_during_the_illness_that_led_to_death_did_she_or_he_bleed_from_anywhere,
 
'get_did_she_or_he_bleed_from_the_nose_mouth_or_anus_id10242':get_did_she_or_he_bleed_from_the_nose_mouth_or_anus,
 
'get_did_she_or_he_have_noticeable_weight_loss_id10243':get_did_she_or_he_have_noticeable_weight_loss,
 
'get_was_she_or_he_severely_thin_or_wasted_id10244':get_was_she_or_he_severely_thin_or_wasted,
 
'get_during_the_illness_that_led_to_death_did_s_he_have_a_whitish_rash_inside_the_mouth_or_on_the_tongue_id10245':get_during_the_illness_that_led_to_death_did_s_he_have_a_whitish_rash_inside_the_mouth_or_on_the_tongue,

'get_did_she_or_he_have_stiffness_of_the_whole_body_or_was_unable_to_open_the_mouth_id10246':get_did_she_or_he_have_stiffness_of_the_whole_body_or_was_unable_to_open_the_mouth,
'get_did_she_or_he_have_puffiness_of_the_face_id10247':get_did_she_or_he_have_puffiness_of_the_face,
 
'get_how_long_did_she_or_he_have_puffiness_of_the_face_id10248_units':get_how_long_did_she_or_he_have_puffiness_of_the_face,
 
'get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_days_id10248_a':get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_days,
 
'get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_months_id10248_b':get_enter_how_long_she_or_he_had_puffiness_of_the_face_in_months,
 
'get_for_how_many_days_did_she_or_he_have_puffiness_of_the_face_id10248':get_for_how_many_days_did_she_or_he_have_puffiness_of_the_face,
 
'get_during_the_illness_that_led_to_death_did_she_or_he_have_swollen_legs_or_feet_id10249':get_during_the_illness_that_led_to_death_did_she_or_he_have_swollen_legs_or_feet,
'get_how_long_did_the_swelling_last_id10250_units':get_how_long_did_the_swelling_last,
'get_enter_how_long_the_swelling_lasted_in_days_id10250_a':get_enter_how_long_the_swelling_lasted_in_days,
'get_how_many_days_did_the_swelling_last_id10250_b':get_how_many_days_did_the_swelling_last,
'get_did_she_or_he_have_both_feet_swollen_id10251':get_did_she_or_he_have_both_feet_swollen,
'get_did_she_or_he_have_general_puffiness_all_over_his_her_body_id10252':get_did_she_or_he_have_general_puffiness_all_over_his_her_body,
'get_did_she_or_he_have_any_lumps_id10253':get_did_she_or_he_have_any_lumps,
'get_did_she_or_he_have_any_lumps_or_lesions_in_the_mouth_id10254':get_did_she_or_he_have_any_lumps_or_lesions_in_the_mouth,
'get_did_she_or_he_have_any_lumps_on_the_neck_id10255':get_did_she_or_he_have_any_lumps_on_the_neck,
'get_did_she_or_he_have_any_lumps_on_the_armpit_id10256':get_did_she_or_he_have_any_lumps_on_the_armpit,
'get_did_she_or_he_have_any_lumps_on_the_groin_id10257':get_did_she_or_he_have_any_lumps_on_the_groin,
'get_was_she_or_he_in_any_way_paralysed_id10258':get_was_she_or_he_in_any_way_paralysed,
'get_did_she_or_he_have_paralysis_of_only_one_side_of_the_body_id10259':get_did_she_or_he_have_paralysis_of_only_one_side_of_the_body,
'get_which_were_the_limbs_or_body_parts_paralysed_id10260':get_which_were_the_limbs_or_body_parts_paralysed,
# (id10260_check)_it_is_not_possible_to_select_only_one_side_paralysed_and_left_and_right_side_or__whole_body_together._Please_go_back_and_correct_the_selection._
# (id10260_check2)_it_is not possible to select doesn't Know or Refused_to_answer_together_with_other_options._Please_go_back_and_correct_the_selection._
'get_did_she_or_he_have_difficulty_swallowing_id10261':get_did_she_or_he_have_difficulty_swallowing,
 
'get_for_how_long_before_death_did_she_or_he_have_difficulty_swallowing_id10262_units':get_for_how_long_before_death_did_she_or_he_have_difficulty_swallowing,

'get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_days_id10262_a':get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_days,

'get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_months_id10262_b':get_enter_how_long_before_death_she_or_he_had_difficulty_swallowing_in_months,

'get_for_how_many_days_before_death_did_she_or_he_have_difficulty_swallowing_id10262':get_for_how_many_days_before_death_did_she_or_he_have_difficulty_swallowing,

'get_was_the_difficulty_with_swallowing_with_solids_liquids_or_both_id10263':get_was_the_difficulty_with_swallowing_with_solids_liquids_or_both,

'get_did_she_or_he_have_pain_upon_swallowing_id10264':get_did_she_or_he_have_pain_upon_swallowing,

'get_did_she_or_he_have_yellow_discoloration_of_the_eyes_id10265':get_did_she_or_he_have_yellow_discoloration_of_the_eyes,

'get_for_how_long_did_she_or_he_have_the_yellow_discoloration_id10266_units':get_for_how_long_did_she_or_he_have_the_yellow_discoloration,

'get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_days_id10266_a':get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_days,


 
'get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_months_id10266_b':get_enter_how_long_she_or_he_had_the_yellow_discoloration_in_months,

'get_for_how_many_days_did_she_or_he_have_the_yellow_discoloration_id10266':get_for_how_many_days_did_she_or_he_have_the_yellow_discoloration,

'get_did_her_his_hair_change_in_color_to_a_reddish_or_yellowish_color_id10267':get_did_her_his_hair_change_in_color_to_a_reddish_or_yellowish_color,

'get_did_she_or_he_look_pale_thinning_lack_of_blood_or_have_pale_palms_eyes_or_nail_beds_id10268':get_did_she_or_he_look_pale_thinning_lack_of_blood_or_have_pale_palms_eyes_or_nail_beds,


 
'get_did_she_or_he_have_sunken_eyes_id10269':get_did_she_or_he_have_sunken_eyes,

 
'get_did_she_or_he_drink_a_lot_more_water_than_usual_id10270':get_did_she_or_he_drink_a_lot_more_water_than_usual,

 
'get_was_the_baby_able_to_suckle_or_bottle_feed_within_the_first_24_hours_after_birth_id10271':get_was_the_baby_able_to_suckle_or_bottle_feed_within_the_first_24_hours_after_birth,

 
'get_did_the_baby_ever_suckle_in_a_normal_way_id10272':get_did_the_baby_ever_suckle_in_a_normal_way,

'get_did_the_baby_stop_suckling_id10273':get_did_the_baby_stop_suckling,

'get_how_many_days_after_birth_did_the_baby_stop_suckling_id10274_a':get_how_many_days_after_birth_did_the_baby_stop_suckling,

'get_how_long_after_birth_did_the_baby_stop_suckling_id10274_units':get_how_long_after_birth_did_the_baby_stop_suckling,

'get_enter_how_long_after_birth__the_baby_stopped_suckling_in_days_id10274_b':get_enter_how_long_after_birth__the_baby_stopped_suckling_in_days,

'get_enter_how_long_after_birth__the_baby_stopped_suckling_in_months_id10274_c':get_enter_how_long_after_birth__the_baby_stopped_suckling_in_months,

'get_how_many_days_after_birth_did_the_baby_stop_suckling_id10274':get_how_many_days_after_birth_did_the_baby_stop_suckling,

'get_did_the_baby_have_convulsions_starting_within_the_first_24_hours_of_life_id10275':get_did_the_baby_have_convulsions_starting_within_the_first_24_hours_of_life,

'get_did_the_baby_have_convulsions_starting_more_than_24_hours_after_birth_id10276':get_did_the_baby_have_convulsions_starting_more_than_24_hours_after_birth,

'get_did_the_babys_body_become_stiff_with_the_back_arched_backwards_id10277':get_did_the_babys_body_become_stiff_with_the_back_arched_backwards,

 
'get_during_the_illness_that_led_to_death_did_the_baby_have_a_bulging_or_raised_fontanelle__id10278':get_during_the_illness_that_led_to_death_did_the_baby_have_a_bulging_or_raised_fontanelle_,

'get_during_the_illness_that_led_to_death_did_the_baby_have_a_sunken_fontanelle_id10279':get_during_the_illness_that_led_to_death_did_the_baby_have_a_sunken_fontanelle,

'get_during_the_illness_that_led_to_death_did_the_baby_become_unresponsive_or_unconscious_id10281':get_during_the_illness_that_led_to_death_did_the_baby_become_unresponsive_or_unconscious,

'get_did_the_baby_become_unresponsive_or_unconscious_soon_after_birth_within_less_than_24_hours_id10282':get_did_the_baby_become_unresponsive_or_unconscious_soon_after_birth_within_less_than_24_hours,
 
#_Neonatal_child_questions_part_C
'get_during_the_illness_that_led_to_death_did_the_baby_become_cold_to_touch_id10284':get_during_the_illness_that_led_to_death_did_the_baby_become_cold_to_touch,

'get_how_many_days_old_was_the_baby_when_it_started_feeling_cold_to_touch_id10285':get_how_many_days_old_was_the_baby_when_it_started_feeling_cold_to_touch,

'get_during_the_illness_that_led_to_death_did_the_baby_become_lethargic_after_a_period_of_normal_activity_id10286':get_during_the_illness_that_led_to_death_did_the_baby_become_lethargic_after_a_period_of_normal_activity,

'get_did_the_baby_have_redness_or_pus_drainage_from_the_umbilical_cord_stump_id10287':get_did_the_baby_have_redness_or_pus_drainage_from_the_umbilical_cord_stump,


'get_during_the_illness_that_led_to_death_did_the_baby_have_skin_ulcers_or_pits_id10288':get_during_the_illness_that_led_to_death_did_the_baby_have_skin_ulcers_or_pits,

'get_during_the_illness_that_led_to_death_did_the_baby_have_yellow_skin_palms_hand_or_soles_foot_id10289':get_during_the_illness_that_led_to_death_did_the_baby_have_yellow_skin_palms_hand_or_soles_foot,

'get_did_the_baby_or_infant_appear_to_be_healthy_and_then_just_die_suddenly_id10290':get_did_the_baby_or_infant_appear_to_be_healthy_and_then_just_die_suddenly,



# pregnancy_women	Signs and symptoms associated with pregnancy and women
'get_did_she_have_any_swelling_or_lump_in_the_breast_Id10294':get_did_she_have_any_swelling_or_lump_in_the_breast,

'get_did_she_have_any_ulcers_pits_in_the_breast_Id10295':get_did_she_have_any_ulcers_pits_in_the_breast,

'get_did_she_ever_have_a_period_or_menstruate_Id10296':get_did_she_ever_have_a_period_or_menstruate,

'get_when_she_had_her_period_did_she_have_vaginal_bleeding_in_between_menstrual_periods_Id10297':get_when_she_had_her_period_did_she_have_vaginal_bleeding_in_between_menstrual_periods,

'get_was_the_bleeding_excessive_Id10298':get_was_the_bleeding_excessive,

'get_was_there_excessive_vaginal_bleeding_in_the_week_prior_to_death_Id10301':get_was_there_excessive_vaginal_bleeding_in_the_week_prior_to_death,

'get_did_her_menstrual_period_stop_naturally_because_of_menopause_or_removal_of_uterus_Id10299':get_did_her_menstrual_period_stop_naturally_because_of_menopause_or_removal_of_uterus,

'get_at_the_time_of_death_was_her_period_overdue_Id10302':get_at_the_time_of_death_was_her_period_overdue,

'get_for_how_many_weeks_had_her_period_been_overdue_Id10303':get_for_how_many_weeks_had_her_period_been_overdue,

'get_did_she_have_vaginal_bleeding_after_cessation_of_menstruation_Id10300':get_did_she_have_vaginal_bleeding_after_cessation_of_menstruation,

'get_did_she_have_a_sharp_pain_in_her_belly_abdomen_shortly_before_death_Id10304':get_did_she_have_vaginal_bleeding_after_cessation_of_menstruation,

'get_was_she_pregnant_or_in_labour_at_the_time_of_death_Id10305':get_was_she_pregnant_or_in_labour_at_the_time_of_death,

'get_did_she_die_within_6_weeks_of_delivery_abortion_or_miscarriage_Id10306':get_did_she_die_within_6_weeks_of_delivery_abortion_or_miscarriage,

'get_did_this_woman_die_more_than_6_weeks_after_being_pregnant_or_delivering_a_baby_Id10307':get_did_this_woman_die_more_than_6_weeks_after_being_pregnant_or_delivering_a_baby,

'get_was_this_a_woman_who_died_less_than_1_year_after_being_pregnant_or_delivering_a_baby_Id10308':get_was_this_a_woman_who_died_less_than_1_year_after_being_pregnant_or_delivering_a_baby,

'get_for_how_many_months_was_she_pregnant_Id10309':get_for_how_many_months_was_she_pregnant,

'get_please_confirm_when_she_died_she_was_NEITHER_pregnant_NOR_had_delivered_had_an_abortion_or_miscarried_within_12_months_of_when_she_died_is_that_right_Id10310':get_please_confirm_when_she_died_she_was_NEITHER_pregnant_NOR_had_delivered_had_an_abortion_or_miscarried_within_12_months_of_when_she_died_is_that_right,

# Id10310_check	(Id10310_check) if_the_response_is_NO_DONT_KNOw_OR_REFUSED_it_indicates_some_uncertainty_as_to_whether_the_cause_of_death_could_have_been_a_maternal_or_pregnancy_related_cause_Go_back_to_the_question_did_she_ever_have_a_period_or_menstruate_and_follow_the_process_again_If_it_is_confirmed_that_the_death_was_related_to_pregnancy_proceed_with_the_next_question_did_she_die_during_labour_or_delivery_
#_group_maternal	Questions_about_possible_maternal_deaths
'get_did_she_die_during_labour_or_delivery_Id10312':get_did_she_die_during_labour_or_delivery,

'get_did_she_die_after_delivering_a_baby_Id10313':get_did_she_die_after_delivering_a_baby,

'get_did_she_die_within_24_hours_after_delivery_Id10314':get_did_she_die_within_24_hours_after_delivery,

'get_did_she_die_within_6_weeks_of_childbirth_Id10315_a':get_did_she_die_within_24_hours_after_delivery,

'get_did_she_die_within_6_weeks_of_childbirth_Id10315':get_did_she_die_within_6_weeks_of_childbirth,

'get_did_she_give_birth_to_a_live_baby_within_6_weeks_of_her_death_Id10316':get_did_she_give_birth_to_a_live_baby_within_6_weeks_of_her_death,

'get_get_did_she_die_during_or_after_a_multiple_pregnancy_Id10317':get_get_did_she_die_during_or_after_a_multiple_pregnancy,

'get_was_she_breastfeeding_the_child_in_the_days_before_death_Id10318':get_was_she_breastfeeding_the_child_in_the_days_before_death,

'get_how_many_births_including_still_births_did_she_the_mother_have_before_this_baby_Id10319':get_how_many_births_including_still_births_did_she_the_mother_have_before_this_baby,

'get_had_she_had_any_previous_Caesarean_section_Id10320':get_had_she_had_any_previous_Caesarean_section,

'get_during_pregnancy_did_she_suffer_from_high_blood_pressure_Id10321':get_during_pregnancy_did_she_suffer_from_high_blood_pressure,

'get_did_she_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery_Id10322':get_did_she_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery,

'get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_convulsions_Id10323':get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_convulsions,

'get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_blurred_vision_Id10324':get_during_the_last_3_months_of_pregnancy_did_she_suffer_from_blurred_vision,

'get_did_bleeding_occur_while_she_was_pregnant_Id10325':get_did_bleeding_occur_while_she_was_pregnant,

'get_was_there_vaginal_bleeding_during_the_first_6_months_of_pregnancy_Id10326':get_was_there_vaginal_bleeding_during_the_first_6_months_of_pregnancy,

'get_was_there_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started_Id10327':get_was_there_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started,


'get_did_she_have_excessive_bleeding_during_labour_or_delivery_Id10328':get_did_she_have_excessive_bleeding_during_labour_or_delivery,

'get_did_she_have_excessive_bleeding_after_delivery_or_abortion_Id10329':get_did_she_have_excessive_bleeding_after_delivery_or_abortion,

'get_was_the_placenta_completely_delivered_Id10330':get_was_the_placenta_completely_delivered,

'get_did_she_deliver_or_try_to_deliver_an_abnormally_positioned_baby_Id10331':get_did_she_deliver_or_try_to_deliver_an_abnormally_positioned_baby,

'get_for_how_many_hours_was_she_in_labour_Id10332':get_for_how_many_hours_was_she_in_labour,

'get_did_she_attempt_to_terminate_the_pregnancy_Id10333':get_did_she_attempt_to_terminate_the_pregnancy,

'get_did_she_recently_have_a_pregnancy_that_ended_in_an_abortion_spontaneous_or_induced_Id10334':get_did_she_recently_have_a_pregnancy_that_ended_in_an_abortion_spontaneous_or_induced,

'get_get_did_she_die_during_an_abortion_Id10335':get_get_did_she_die_during_an_abortion,

'get_get_did_she_die_within_6_weeks_of_having_an_abortion_Id10336':get_get_did_she_die_within_6_weeks_of_having_an_abortion,

'get_where_did_she_give_birth_complete_the_miscarriage_have_the_abortion_Id10337':get_where_did_she_give_birth_complete_the_miscarriage_have_the_abortion,

'get_did_she_receive_professional_assistance_during_the_delivery_Id10338':get_did_she_receive_professional_assistance_during_the_delivery,

'get_who_delivered_the_baby_completed_the_miscarriage___performed_the_abortion_Id10339':get_who_delivered_the_baby_completed_the_miscarriage___performed_the_abortion,
 
#_deliverytype	how_did_the_mother_deliver_her_baby
'get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum_Id10342':get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum,
 
'get_was_the_delivery_vaginal_with_forceps_or_vacuum_Id10343':get_was_the_delivery_vaginal_with_forceps_or_vacuum,
 
'get_was_the_delivery_a_Caesarean_section_Id10344':get_was_the_delivery_a_Caesarean_section,
 
'get_was_the_baby_born_more_than_one_month_early_Id10347':get_was_the_baby_born_more_than_one_month_early,
 
	
'get_did_she_have_an_operation_to_remove_her_uterus_shortly_before_death_Id10340':get_did_she_have_an_operation_to_remove_her_uterus_shortly_before_death,
 
	
#_neonatal_child	Neonatal_and_child_history_signs_and_symptoms
'get_how_old_was_the_child_when_the_fatal_illness_started_Id10352_units':get_how_old_was_the_child_when_the_fatal_illness_started,
 
	
'get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_months_Id10352_a':get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_months,
 
	
'get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_years_Id10352_b':get_Enter_how_old_the_child_was__when_the_fatal_illness_started_in_years,
 
	
'get_how_many_years_old_was_the_child_when_the_fatal_illness_started_Id10352':get_how_many_years_old_was_the_child_when_the_fatal_illness_started,

#_neonatal_childA	Neonatal_child_questions_part_A
	
'get_was_the_child_part_of_a_multiple__birth_Id10354':get_was_the_child_part_of_a_multiple__birth,

 
'get_was_the_child_the_first_second_or_later_in_the_birth_order_Id10355':get_was_the_child_the_first_second_or_later_in_the_birth_order,

'get_is_the_mother_still_alive_Id10356':get_is_the_mother_still_alive,

'get_did_the_mother_die_before_during_or_after_the_delivery_Id10357':get_did_the_mother_die_before_during_or_after_the_delivery,


#_moth_death	Time_between_delivery_and_death_of_mother

'get_how_long_after_the_delivery_did_the_mother_die_Id10358_units':get_how_long_after_the_delivery_did_the_mother_die,

'get_how_many_months_after_the_delivery_did_the_mother_die_Id10358':get_how_many_months_after_the_delivery_did_the_mother_die,

'get_how_many_days_after_the_delivery_did_the_mother_die_Id10359':get_how_many_days_after_the_delivery_did_the_mother_die,

'get_how_many_weeks_after_the_delivery_did_the_mother_die_Id10359_a':get_how_many_weeks_after_the_delivery_did_the_mother_die,

	
'get_where_was_the_deceased_born_Id10360':get_where_was_the_deceased_born,

	
'get_did_you_the_mother_receive_professional_assistance_during_the_delivery_Id10361':get_did_you_the_mother_receive_professional_assistance_during_the_delivery,


	
'get_at_birth_was_the_baby_of_usual_size_Id10362':get_at_birth_was_the_baby_of_usual_size,

	
'get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg_Id10363':get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg,

	
'get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg_Id10363':get_at_birth_was_the_baby_smaller_than_usual_weighing_under_2point5_kg,

	
'get_at_birth_was_the_baby_very_much_smaller_than_usual_weighing_under_1_kg_Id10364':get_at_birth_was_the_baby_very_much_smaller_than_usual_weighing_under_1_kg,

	
'get_at_birth_was_the_baby_larger_than_usual_weighing_over_4point5_kg_Id10365':get_at_birth_was_the_baby_larger_than_usual_weighing_over_4point5_kg,

#_id1036X_check	(id1036X_check)_it_is_not_possible_to_select_"No_usual_size_at_Birth"_"No_weighing_under_2.5_kg"_and_"No_weighing_over_4.5_kg"_together._Please_go_back_and_correct_the_selection._
	
'get_what_was_the_weight_in_grammes_of_the_deceased_at_birth_Id10366':get_what_was_the_weight_in_grammes_of_the_deceased_at_birth,
	
'get_how_many_months_long_was_the_pregnancy_before_the_child_was_born_Id10367':get_how_many_months_long_was_the_pregnancy_before_the_child_was_born,

'get_were_there_any_complications_in_the_late_part_of_the_pregnancy_defined_as_the_last_3_months_before_labour_Id10368':get_were_there_any_complications_in_the_late_part_of_the_pregnancy_defined_as_the_last_3_months_before_labour,

'get_were_there_any_complications_during_labour_or_delivery_Id10369':get_were_there_any_complications_during_labour_or_delivery,

'get_was_any_part_of_the_baby_physically_abnormal_at_time_of_delivery_for_example_body_part_too_large_or_too_small_additional_growth_on_body_Id10370':get_was_any_part_of_the_baby_physically_abnormal_at_time_of_delivery_for_example_body_part_too_large_or_too_small_additional_growth_on_body,

'get_did_the_baby_child_have_a_swelling_or_defect_on_the_back_at_time_of_birth_Id10371':get_did_the_baby_child_have_a_swelling_or_defect_on_the_back_at_time_of_birth,

'get_did_the_baby_child_have_a_very_large_head_at_time_of_birth_Id10372':get_did_the_baby_child_have_a_very_large_head_at_time_of_birth,

'get_did_the_baby_child_have_a_very_small_head_at_time_of_birth_Id10373':get_did_the_baby_child_have_a_very_small_head_at_time_of_birth,

'get_how_many_births_including_stillbirths_did_the_babys_mother_have_before_this_baby_Id10394':get_how_many_births_including_stillbirths_did_the_babys_mother_have_before_this_baby,

#_neonatal_childB	(neonatal_childB)_Neonatal_child_questions_part_B

'get_was_the_baby_moving_in_the_last_few_days_before_the_birth_Id10376':get_was_the_baby_moving_in_the_last_few_days_before_the_birth,

'get_did_the_baby_stop_moving_in_the_womb_before_labour_started_Id10377':get_did_the_baby_stop_moving_in_the_womb_before_labour_started,
 
#_babmove	Baby_moving
'get_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_Id10379_unit':get_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move,
 
'get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_days_Id10379':get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_days,
 
'get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_hours_Id10380':get_Enter_how_long_before_labour_did_you_the_mother_last_feel_the_baby_move_in_hours,
 
	
'get_how_many_hours_did_labour_and_delivery_take_Id10382':get_how_many_hours_did_labour_and_delivery_take,
 
	
'get_was_the_baby_born_24_hours_or_more_after_the_water_broke_Id10383':get_was_the_baby_born_24_hours_or_more_after_the_water_broke,
 
	
'get_what_was_the_colour_of_the_liquor_when_the_water_broke_Id10385':get_what_was_the_colour_of_the_liquor_when_the_water_broke,
 
#_mother_deliv	(mother_deliv)_how_was_the_baby_delivered
'get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum_Id10387':get_was_the_delivery_normal_vaginal_without_forceps_or_vacuum,

'get_was_the_delivery_vaginal_with_forceps_or_vacuum_Id10388':get_was_the_delivery_vaginal_with_forceps_or_vacuum,

'get_was_the_delivery_a_Caesarean_section_Id10389':get_was_the_delivery_a_Caesarean_section,

'get_was_the_delivery_a_Caesarean_section_Id10389':get_was_the_delivery_a_Caesarean_section,

# id10389_check	(id10389_check) it_is_not_possible_to_select_No_to_all_three_previous_questions._Please_go_back_and_review_the_answers._
'get_did_you_the_mother_receive_any_vaccinations_since_reaching_adulthood_including_during_this_pregnancy_Id10391':get_did_you_the_mother_receive_any_vaccinations_since_reaching_adulthood_including_during_this_pregnancy, 
'get_how_many_doses_Id10392':get_how_many_doses, 
'get_did_you_the_mother_receive_tetanus_toxoid_TT_vaccine_Id10393':get_did_you_the_mother_receive_tetanus_toxoid_TT_vaccine, 
'get_during_labour_did_the_babys_mother_suffer_from_fever_Id10395':get_during_labour_did_the_babys_mother_suffer_from_fever, 
'get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_high_blood_pressure_Id10396':get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_high_blood_pressure, 
'get_did_you_the_babys_mother_have_diabetes_mellitus_Id10397':get_did_you_the_babys_mother_have_diabetes_mellitus, 
'get_did_you_the_babys_mother_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery_Id10398':get_did_you_the_babys_mother_have_foul_smelling_vaginal_discharge_during_pregnancy_or_after_delivery, 
 
'get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_convulsions_Id10399':get_during_the_last_3_months_of_pregnancy_labour_or_delivery_did_you_the_babys_mother_suffer_from_convulsions, 
 
'get_during_the_last_3_months_of_pregnancy_did_you_the_babys_mother_suffer_from_blurred_vision_Id10400':get_during_the_last_3_months_of_pregnancy_did_you_the_babys_mother_suffer_from_blurred_vision,
 
'get_did_you_the_babys_mother_have_severe_anemia_Id10401':get_did_you_the_babys_mother_have_severe_anemia,

'get_did_you_the_babys_mother_have_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started_Id10402':get_did_you_the_babys_mother_have_vaginal_bleeding_during_the_last_3_months_of_pregnancy_but_before_labour_started,


'get_did_the_babys_bottom_feet_arm_or_hand_come_out_of_the_vagina_before_its_head_Id10403':get_did_the_babys_bottom_feet_arm_or_hand_come_out_of_the_vagina_before_its_head,


'get_was_the_umbilical_cord_wrapped_more_than_once_around_the_neck_of_the_child_at_birth_Id10404':get_was_the_umbilical_cord_wrapped_more_than_once_around_the_neck_of_the_child_at_birth,


'get_was_the_umbilical_cord_delivered_first_Id10405':get_was_the_umbilical_cord_delivered_first,

'get_was_the_baby_blue_in_colour_at_birth_Id10406':get_was_the_baby_blue_in_colour_at_birth,

#_risk_factors	Risk_factors

'get_did_she_or_he__drink_alcohol_Id10411':get_did_she_or_he__drink_alcohol,

'get_did_she_or_he__use_tobacco_Id10412':get_did_she_or_he__use_tobacco,

'get_did_she_or_he__smoke_tobacco_cigarette_cigar_pipe_etc_Id10413':get_did_she_or_he__smoke_tobacco_cigarette_cigar_pipe_etc,

'what_kind_of_tobacco_get_did_she_or_he__use_Id10414':what_kind_of_tobacco_get_did_she_or_he__use,

# id10414_check	(id10414_check)_it_is_not_possible_to_select_cigarettes_or_pipe_and_"no"_to_"get_did_she_or_he__smoke_tobacco"._Please_go_back_and_correct_the_selections.
'get_how_many_cigarettes_get_did_she_or_he__smoke_daily_Id10415':get_how_many_cigarettes_get_did_she_or_he__smoke_daily,

 
'get_how_many_times_didshe_or_he__use_tobacco_products_each_day_Id10416':get_how_many_times_didshe_or_he__use_tobacco_products_each_day,
	
#_health_service_utilization	Health_service_utilisation
'get_did_she_or_he__receive_any_treatment_for_the_illness_that_led_to_death_Id10418':get_did_she_or_he__receive_any_treatment_for_the_illness_that_led_to_death,
	
'get_did_she_or_he_receive_oral_rehydration_salts_Id10419':get_did_she_or_he_receive_oral_rehydration_salts,
	
'get_did_she_or_he_receive_or_need_intravenous_fluids_drip_treatment_Id10420':get_did_she_or_he_receive_or_need_intravenous_fluids_drip_treatment,
	
'get_did_she_or_he_receive_or_need_a_blood_transfusion_Id10421':get_did_she_or_he_receive_or_need_a_blood_transfusion,
	
'get_did_she_or_he_receive_or_need_treatment_food_through_a_tube_passed_through_the_nose_Id10422':get_did_she_or_he_receive_or_need_treatment_food_through_a_tube_passed_through_the_nose,
	

'get_did_she_or_he_receive_or_need_injectable_antibiotics_Id10423':get_did_she_or_he_receive_or_need_injectable_antibiotics,
	
'get_did_she_or_he_receive_or_need_antiretroviral_therapy_ART_Id10424':get_did_she_or_he_receive_or_need_antiretroviral_therapy_ART,
	
'get_did_she_or_he_have_or_need_an_operation_for_the_illness_Id10425':get_did_she_or_he_have_or_need_an_operation_for_the_illness,
	

'get_did_she_or_he_have_the_operation_within_1_month_before_death_Id10426':get_did_she_or_he_have_the_operation_within_1_month_before_death,
	

'get_was_she_or_he__discharged_from_hospital_very_ill_Id10427':get_was_she_or_he__discharged_from_hospital_very_ill,
	
'get_did_she_or_he__receive_any_immunizations_Id10428':get_did_she_or_he__receive_any_immunizations,
	
'get_do_you_have_the_childs_vaccination_card_Id10429':get_do_you_have_the_childs_vaccination_card,
	
'get_can_i_see_the_vaccination_card_note_the_vaccines_the_child_received_Id10430':get_can_i_see_the_vaccination_card_note_the_vaccines_the_child_received,
	
'get_select_EPI_vaccines_done_Id10431':get_select_EPI_vaccines_done,
	
# id10431_check	(id10431_check)_it_is_not_possible_to_select_"No_vaccines"_"don't_know"_or_"refuse"_together_with_other_options._Please_go_back_and_correct_the_selection._

'get_was_care_sought_outside_the_home_while_she_or_he__had_this_illness_Id10432':get_was_care_sought_outside_the_home_while_she_or_he__had_this_illness,
	
'get_where_or_from_whom_did_you_seek_care_Id10433':get_where_or_from_whom_did_you_seek_care,

# id10433_check	(id10433_check)_it_is_not_possible_to_select_"don't_know"_or_"refuse"_together_with_other_options._Please_go_back_and_correct_the_selection._
	
'get_what_was_the_name_and_address_of_any_hospital_health_center_or_clinic_where_care_was_sought_Id10434':get_what_was_the_name_and_address_of_any_hospital_health_center_or_clinic_where_care_was_sought,

'get_did_a_health_care_worker_tell_you_the_cause_of_death_Id10435':get_did_a_health_care_worker_tell_you_the_cause_of_death,

'get_what_did_the_health_care_worker_say_Id10436':get_what_did_the_health_care_worker_say,

'get_do_you_have_any_health_records_that_belonged_to_the_deceased_Id10437':get_do_you_have_any_health_records_that_belonged_to_the_deceased,

'get_can_i_see_the_health_records_Id10438':get_can_i_see_the_health_records,


# Id10439_check	(Id10439_check)_is_the_date_of_the_most_recent_(last)_visit_available
'get_record_the_date_of_the_most_recent_last_visit_Id10439':get_record_the_date_of_the_most_recent_last_visit,

# Id10440_check	(Id10440_check)_is_the_date_of_the_second_most_recent_visit_available
'get_record_the_date_of_the_second_most_recent_visit_Id10440':get_record_the_date_of_the_second_most_recent_visit,

# Id10441_check	(Id10441_check)_is_the_date_of_the_last_note_on_the_health_records_available
'get_record_the_date_of_the_last_note_on_the_health_records_Id10441':get_record_the_date_of_the_last_note_on_the_health_records,

'get_record_the_weight_in_kilogrammes_written_at_the_most_recent_last_visit_Id10442':get_record_the_weight_in_kilogrammes_written_at_the_most_recent_last_visit,

'get_record_the_weight_in_kilogrammes_written_at_the_second_most_recent_visit_Id10443':get_record_the_weight_in_kilogrammes_written_at_the_second_most_recent_visit,


'get_transcribe_the_last_note_on_the_health_records_Id10444':get_transcribe_the_last_note_on_the_health_records,

'get_has_the_deceaseds_biological_mother_ever_been_tested_for_HIV_Id10445':get_has_the_deceaseds_biological_mother_ever_been_tested_for_HIV,

'get_has_the_deceaseds_biological_mother_ever_been_told_she_had_HIV_AIDS_by_a_health_worker_Id10446':get_has_the_deceaseds_biological_mother_ever_been_told_she_had_HIV_AIDS_by_a_health_worker,

#_back_context	Background_and_context
'get_in_the_final_days_before_death_did_s_he_travel_to_a_hospital_or_health_facility_Id10450':get_in_the_final_days_before_death_did_s_he_travel_to_a_hospital_or_health_facility,

'get_get_did_she_or_he__use_motorised_transport_to_get_to_the_hospital_or_health_facility_Id10451':get_get_did_she_or_he__use_motorised_transport_to_get_to_the_hospital_or_health_facility,

'get_were_there_any_problems_during_admission_to_the_hospital_or_health_facility_Id10452':get_were_there_any_problems_during_admission_to_the_hospital_or_health_facility,


'get_were_there_any_problems_with_the_way_she_or_he__was_treated_medical_treatment_procedures_interpersonal_attitudes_respect_dignity_in_the_hospital_or_health_facility_Id10453':get_were_there_any_problems_with_the_way_she_or_he__was_treated_medical_treatment_procedures_interpersonal_attitudes_respect_dignity_in_the_hospital_or_health_facility,

'get_were_there_any_problems_getting_medications_or_diagnostic_tests_in_the_hospital_or_health_facility_Id10454':get_were_there_any_problems_getting_medications_or_diagnostic_tests_in_the_hospital_or_health_facility,

'get_does_it_take_more_than_2_hours_to_get_to_the_nearest_hospital_or_health_facility_from_the_deceaseds_household_Id10455':get_does_it_take_more_than_2_hours_to_get_to_the_nearest_hospital_or_health_facility_from_the_deceaseds_household,

'get_in_the_final_days_before_death_were_there_any_doubts_about_whether_medical_care_was_needed_Id10456':get_in_the_final_days_before_death_were_there_any_doubts_about_whether_medical_care_was_needed,

'get_in_the_final_days_before_death_was_traditional_medicine_used_Id10457':get_in_the_final_days_before_death_was_traditional_medicine_used,

'get_in_the_final_days_before_death_did_anyone_use_a_telephone_or_cell_phone_to_call_for_help_Id10458':get_in_the_final_days_before_death_did_anyone_use_a_telephone_or_cell_phone_to_call_for_help,

'get_over_the_course_of_illness_did_the_total_costs_of_care_and_treatment_prohibit_other_household_payments_Id10459':get_over_the_course_of_illness_did_the_total_costs_of_care_and_treatment_prohibit_other_household_payments,


#_Health_ins	Health_insuarance
'get_did_the_deceased_have_Health_insuarance_TZ001':get_did_the_deceased_have_Health_insuarance,

'get_which_among_the_following_Health_insuarances_did_the_deceased_have_TZ002':get_which_among_the_following_Health_insuarances_did_the_deceased_have,

'get_Other_Specify_TZ002_other':get_Other_Specify,

'get_did_the_deceased_use_his_her_Health_insuarance_during_his_her_final_illness_TZ003':get_did_the_deceased_use_his_her_Health_insuarance_during_his_her_final_illness,


	
'get_which_services_did_the_Health_insuarance_provide_TZ004':get_which_services_did_the_Health_insuarance_provide,

'get_Other_Specify_TZ004_other':get_Other_Specify,

'get_why_did_the_deceased_not_use_his_her_health_insuarance_TZ005':get_why_did_the_deceased_not_use_his_her_health_insuarance,

'get_there_was_another_problem_with_using_the_insuarance_specify_TZ005_a':get_there_was_another_problem_with_using_the_insuarance_specify,


#_deathcert	Death_certificate_with_cause_of_death
'get_was_a_medical_certificate_of_cause_of_death_issued_Id10462':get_was_a_medical_certificate_of_cause_of_death_issued,

'get_can_I_see_the_medical_certificate_of_cause_of_death_Id10463':get_can_I_see_the_medical_certificate_of_cause_of_death,

'get_record_the_immediate_cause_of_death_from_the_certificate_line_1a_Id10464':get_record_the_immediate_cause_of_death_from_the_certificate_line_1a,

'get_duration_Ia_Id10465':get_duration_Ia,

'get_record_the_first_antecedent_cause_of_death_from_the_certificate__line_1b_Id10466':get_record_the_first_antecedent_cause_of_death_from_the_certificate__line_1b,

'get_duration_Ib_Id10467':get_duration_Ib,

'get_record_the_second_antecedent_cause_of_death_from_the_certificate_line_1c_Id10468':get_record_the_second_antecedent_cause_of_death_from_the_certificate_line_1c,


'get_duration_Ic_Id10469':get_duration_Ic,

'get_record_the_third_antecedent_cause_of_death_from_the_certificate_line_1d_Id10470':get_record_the_third_antecedent_cause_of_death_from_the_certificate_line_1d,

'get_duration_Id_Id10471':get_duration_Id,


'get_record_the_contributing_causes_of_death_from_the_certificate_part_2_Id10472':get_record_the_contributing_causes_of_death_from_the_certificate_part_2,

'get_duration_part2_Id10473':get_duration_part2,

#_narrat	Open_narrative
'get_Thank_you_for_your_information_Now_can_you_please_tell_me_in_your_own_words_about_the_events_that_led_to_the_death_Id10476':get_Thank_you_for_your_information_Now_can_you_please_tell_me_in_your_own_words_about_the_events_that_led_to_the_death,

'get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative_Id10477':get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative,

'get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative_Id10478':get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative,

'get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative_Id10479':get_select_any_of_the_following_words_that_were_mentioned_as_present_in_the_narrative,


# id10477_check	(id10477_check)_it_is_not_possible_to_select_"don't_know"_or_"None_of_the_above"_together_with_other_options._Please_go_back_and_correct_the_selection._
# id10478_check	(id10478_check)_it_is_not_possible_to_select_"don't_know"_or_"None_of_the_above"_together_with_other_options._Please_go_back_and_correct_the_selection._
# id10479_check	(id10479_check)_it_is_not_possible_to_select_"don't_know"_or_"None_of_the_above"_together_with_other_options._Please_go_back_and_correct_the_selection._
'get_End_time_of_the_interview_Id10481':get_End_time_of_the_interview,
	
#_comment	(comment)_Comment
'get_Collect_the_GPS_coordinates_of_this_location_gps_location':get_End_time_of_the_interview,
	
'get_the_GPS_coordinates_represents_gps_details':get_the_GPS_coordinates_represents,
}	
