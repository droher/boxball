# Boxball
    ## retrosheet
            ### code_event
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### code_field_park
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### code_method_record
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### code_pitches_record
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### code_precip_park
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### code_sky_park
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### code_wind_direction_park
                    <detail>
                      <summary>&#128273; **code** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**description** : (varchar(30))</summary>

                      
                    </detail>
            ### comment
                    <detail>
                      <summary>&#128273; **dummy_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**game_id** : (char(12))</summary>

                      Game ID (home team ID + YYYYMMDD + doubleheader flag
                    </detail>
                    <detail>
                      <summary>**event_id** : (smallint)</summary>

                      Commented event number
                    </detail>
                    <detail>
                      <summary>**comment** : (varchar(1638))</summary>

                      Comment text
                    </detail>
                    <detail>
                      <summary>**ejected_person_id** : (varchar(256))</summary>

                      ID of ejected person
                    </detail>
                    <detail>
                      <summary>**ejected_person_role_cd** : (varchar(256))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**eject_umpire_id** : (varchar(256))</summary>

                      ID of umpire who ejected person
                    </detail>
                    <detail>
                      <summary>**eject_reason** : (varchar(1639))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**umpchange_inning** : (varchar(256))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**umpchange_position** : (varchar(256))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**umpchange_person_id** : (varchar(256))</summary>

                      ID of new umpire
                    </detail>
            ### daily
                    <detail>
                      <summary>&#128273; **dummy_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**game_id** : (char(12))</summary>

                      Game ID (home team ID + YYYYMMDD + doubleheader flag
                    </detail>
                    <detail>
                      <summary>**game_dt** : (date)</summary>

                      Game date
                    </detail>
                    <detail>
                      <summary>**game_ct** : (smallint)</summary>

                      Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
                    </detail>
                    <detail>
                      <summary>**appearance_dt** : (date)</summary>

                      Player appearance date. Can be different from game date if the game was suspended and the player entered the game at the later date
                    </detail>
                    <detail>
                      <summary>**team_id** : (char(3))</summary>

                      Team ID of player
                    </detail>
                    <detail>
                      <summary>**player_id** : (char(8))</summary>

                      Player ID
                    </detail>
                    <detail>
                      <summary>**slot_ct** : (smallint)</summary>

                      Player lineup position
                    </detail>
                    <detail>
                      <summary>**seq_ct** : (smallint)</summary>

                      Player is nth person of game to play in that lineup slot
                    </detail>
                    <detail>
                      <summary>**home_fl** : (boolean)</summary>

                      Player is playing at home
                    </detail>
                    <detail>
                      <summary>**opponent_id** : (char(3))</summary>

                      Team opponent ID
                    </detail>
                    <detail>
                      <summary>**park_id** : (char(5))</summary>

                      Park ID
                    </detail>
                    <detail>
                      <summary>**b_g** : (smallint)</summary>

                      Games played
                    </detail>
                    <detail>
                      <summary>**b_pa** : (smallint)</summary>

                      Plate appearances
                    </detail>
                    <detail>
                      <summary>**b_ab** : (smallint)</summary>

                      At bats
                    </detail>
                    <detail>
                      <summary>**b_r** : (smallint)</summary>

                      Runs scored
                    </detail>
                    <detail>
                      <summary>**b_h** : (smallint)</summary>

                      Hits
                    </detail>
                    <detail>
                      <summary>**b_tb** : (smallint)</summary>

                      Total bases
                    </detail>
                    <detail>
                      <summary>**b_2b** : (smallint)</summary>

                      Doubles
                    </detail>
                    <detail>
                      <summary>**b_3b** : (smallint)</summary>

                      Triples
                    </detail>
                    <detail>
                      <summary>**b_hr** : (smallint)</summary>

                      Home runs
                    </detail>
                    <detail>
                      <summary>**b_hr4** : (smallint)</summary>

                      Grand slams
                    </detail>
                    <detail>
                      <summary>**b_rbi** : (smallint)</summary>

                      Runs batted in
                    </detail>
                    <detail>
                      <summary>**b_gw** : (smallint)</summary>

                      Game winning RBI
                    </detail>
                    <detail>
                      <summary>**b_bb** : (smallint)</summary>

                      Walks
                    </detail>
                    <detail>
                      <summary>**b_ibb** : (smallint)</summary>

                      Intentional walks
                    </detail>
                    <detail>
                      <summary>**b_so** : (smallint)</summary>

                      Strikeouts
                    </detail>
                    <detail>
                      <summary>**b_gdp** : (smallint)</summary>

                      Grounded into double plays
                    </detail>
                    <detail>
                      <summary>**b_hp** : (smallint)</summary>

                      Hit by pitches
                    </detail>
                    <detail>
                      <summary>**b_sh** : (smallint)</summary>

                      Sacrifice hits
                    </detail>
                    <detail>
                      <summary>**b_sf** : (smallint)</summary>

                      Sacrifice files
                    </detail>
                    <detail>
                      <summary>**b_sb** : (smallint)</summary>

                      Stolen bases
                    </detail>
                    <detail>
                      <summary>**b_cs** : (smallint)</summary>

                      Caught stealing
                    </detail>
                    <detail>
                      <summary>**b_xi** : (smallint)</summary>

                      Reached on interference
                    </detail>
                    <detail>
                      <summary>**b_g_dh** : (smallint)</summary>

                      Games as DH
                    </detail>
                    <detail>
                      <summary>**b_g_ph** : (smallint)</summary>

                      Games as pinch hitter
                    </detail>
                    <detail>
                      <summary>**b_g_pr** : (smallint)</summary>

                      Games as pinch runner
                    </detail>
                    <detail>
                      <summary>**p_g** : (smallint)</summary>

                      Games pitched
                    </detail>
                    <detail>
                      <summary>**p_gs** : (smallint)</summary>

                      Games as starting pitcher
                    </detail>
                    <detail>
                      <summary>**p_cg** : (smallint)</summary>

                      Complete games
                    </detail>
                    <detail>
                      <summary>**p_sho** : (smallint)</summary>

                      Shutouts
                    </detail>
                    <detail>
                      <summary>**p_gf** : (smallint)</summary>

                      Games finished
                    </detail>
                    <detail>
                      <summary>**p_w** : (smallint)</summary>

                      Wins
                    </detail>
                    <detail>
                      <summary>**p_l** : (smallint)</summary>

                      Losses
                    </detail>
                    <detail>
                      <summary>**p_sv** : (smallint)</summary>

                      Saves
                    </detail>
                    <detail>
                      <summary>**p_out** : (smallint)</summary>

                      Outs recorded
                    </detail>
                    <detail>
                      <summary>**p_tbf** : (smallint)</summary>

                      Total batters faced
                    </detail>
                    <detail>
                      <summary>**p_ab** : (smallint)</summary>

                      At bats against
                    </detail>
                    <detail>
                      <summary>**p_r** : (smallint)</summary>

                      Runs allowed
                    </detail>
                    <detail>
                      <summary>**p_er** : (smallint)</summary>

                      Earned runs allowed
                    </detail>
                    <detail>
                      <summary>**p_h** : (smallint)</summary>

                      Hits allowed
                    </detail>
                    <detail>
                      <summary>**p_tb** : (smallint)</summary>

                      Total bases allowed
                    </detail>
                    <detail>
                      <summary>**p_2b** : (smallint)</summary>

                      Doubles allowed
                    </detail>
                    <detail>
                      <summary>**p_3b** : (smallint)</summary>

                      Triples allowed
                    </detail>
                    <detail>
                      <summary>**p_hr** : (smallint)</summary>

                      Home runs allowed
                    </detail>
                    <detail>
                      <summary>**p_hr4** : (smallint)</summary>

                      Grand slams allowed
                    </detail>
                    <detail>
                      <summary>**p_bb** : (smallint)</summary>

                      Walks allowed
                    </detail>
                    <detail>
                      <summary>**p_ibb** : (smallint)</summary>

                      Intentional walks allowed
                    </detail>
                    <detail>
                      <summary>**p_so** : (smallint)</summary>

                      Strikeouts against
                    </detail>
                    <detail>
                      <summary>**p_gdp** : (smallint)</summary>

                      Grounded into double plays against
                    </detail>
                    <detail>
                      <summary>**p_hp** : (smallint)</summary>

                      Hit by pitches allowed
                    </detail>
                    <detail>
                      <summary>**p_sh** : (smallint)</summary>

                      Sacrifice hits allowed
                    </detail>
                    <detail>
                      <summary>**p_sf** : (smallint)</summary>

                      Sacrifice flies allowed
                    </detail>
                    <detail>
                      <summary>**p_xi** : (smallint)</summary>

                      Reached on interference allowed
                    </detail>
                    <detail>
                      <summary>**p_wp** : (smallint)</summary>

                      Wild pitches allowed
                    </detail>
                    <detail>
                      <summary>**p_bk** : (smallint)</summary>

                      Balks allowed
                    </detail>
                    <detail>
                      <summary>**p_ir** : (smallint)</summary>

                      Inherited runners
                    </detail>
                    <detail>
                      <summary>**p_irs** : (smallint)</summary>

                      Inherited runners scored
                    </detail>
                    <detail>
                      <summary>**p_go** : (smallint)</summary>

                      Groundouts recorded
                    </detail>
                    <detail>
                      <summary>**p_ao** : (smallint)</summary>

                      Fly ball outs recorded
                    </detail>
                    <detail>
                      <summary>**p_pitch** : (smallint)</summary>

                      Pitches thrown
                    </detail>
                    <detail>
                      <summary>**p_strike** : (smallint)</summary>

                      Strikes thrown
                    </detail>
                    <detail>
                      <summary>**f_p_g** : (smallint)</summary>

                      Appearances at pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_gs** : (smallint)</summary>

                      Starts at pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_out** : (smallint)</summary>

                      Outs played as pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_tc** : (smallint)</summary>

                      Total chances as pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_po** : (smallint)</summary>

                      Putouts as pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_a** : (smallint)</summary>

                      Assists as pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_e** : (smallint)</summary>

                      Errors as pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_dp** : (smallint)</summary>

                      Double plays turned as pitcher
                    </detail>
                    <detail>
                      <summary>**f_p_tp** : (smallint)</summary>

                      Triple pays turned as pitcher
                    </detail>
                    <detail>
                      <summary>**f_c_g** : (smallint)</summary>

                      Appearances at catcher
                    </detail>
                    <detail>
                      <summary>**f_c_gs** : (smallint)</summary>

                      Starts at catcher
                    </detail>
                    <detail>
                      <summary>**f_c_out** : (smallint)</summary>

                      Outs played as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_tc** : (smallint)</summary>

                      Total chances as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_po** : (smallint)</summary>

                      Putouts as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_a** : (smallint)</summary>

                      Assists as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_e** : (smallint)</summary>

                      Errors as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_dp** : (smallint)</summary>

                      Double plays turned as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_tp** : (smallint)</summary>

                      Triple pays turned as catcher
                    </detail>
                    <detail>
                      <summary>**f_c_pb** : (smallint)</summary>

                      Passed balls
                    </detail>
                    <detail>
                      <summary>**f_c_xi** : (smallint)</summary>

                      Catcher's interference
                    </detail>
                    <detail>
                      <summary>**f_1b_g** : (smallint)</summary>

                      Appearances at first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_gs** : (smallint)</summary>

                      Starts at first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_out** : (smallint)</summary>

                      Outs played as first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_tc** : (smallint)</summary>

                      Total chances as first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_po** : (smallint)</summary>

                      Putouts as first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_a** : (smallint)</summary>

                      Assists as first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_e** : (smallint)</summary>

                      Errors as first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_dp** : (smallint)</summary>

                      Double plays turned as first baseman
                    </detail>
                    <detail>
                      <summary>**f_1b_tp** : (smallint)</summary>

                      Triple pays turned as first baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_g** : (smallint)</summary>

                      Appearances at second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_gs** : (smallint)</summary>

                      Starts at second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_out** : (smallint)</summary>

                      Outs played as second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_tc** : (smallint)</summary>

                      Total chances as second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_po** : (smallint)</summary>

                      Putouts as second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_a** : (smallint)</summary>

                      Assists as second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_e** : (smallint)</summary>

                      Errors as second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_dp** : (smallint)</summary>

                      Double plays turned as second baseman
                    </detail>
                    <detail>
                      <summary>**f_2b_tp** : (smallint)</summary>

                      Triple pays turned as second baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_g** : (smallint)</summary>

                      Appearances at third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_gs** : (smallint)</summary>

                      Starts at third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_out** : (smallint)</summary>

                      Outs played as third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_tc** : (smallint)</summary>

                      Total chances as third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_po** : (smallint)</summary>

                      Putouts as third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_a** : (smallint)</summary>

                      Assists as third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_e** : (smallint)</summary>

                      Errors as third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_dp** : (smallint)</summary>

                      Double plays turned as third baseman
                    </detail>
                    <detail>
                      <summary>**f_3b_tp** : (smallint)</summary>

                      Triple pays turned as third baseman
                    </detail>
                    <detail>
                      <summary>**f_ss_g** : (smallint)</summary>

                      Appearances at shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_gs** : (smallint)</summary>

                      Starts at shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_out** : (smallint)</summary>

                      Outs played as shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_tc** : (smallint)</summary>

                      Total chances as shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_po** : (smallint)</summary>

                      Putouts as shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_a** : (smallint)</summary>

                      Assists as shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_e** : (smallint)</summary>

                      Errors as shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_dp** : (smallint)</summary>

                      Double plays turned as shortstop
                    </detail>
                    <detail>
                      <summary>**f_ss_tp** : (smallint)</summary>

                      Triple pays turned as shortstop
                    </detail>
                    <detail>
                      <summary>**f_lf_g** : (smallint)</summary>

                      Appearances at left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_gs** : (smallint)</summary>

                      Starts at left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_out** : (smallint)</summary>

                      Outs played as left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_tc** : (smallint)</summary>

                      Total chances as left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_po** : (smallint)</summary>

                      Putouts as left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_a** : (smallint)</summary>

                      Assists as left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_e** : (smallint)</summary>

                      Errors as left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_dp** : (smallint)</summary>

                      Double plays turned as left fielder
                    </detail>
                    <detail>
                      <summary>**f_lf_tp** : (smallint)</summary>

                      Triple pays turned as left fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_g** : (smallint)</summary>

                      Appearances at center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_gs** : (smallint)</summary>

                      Starts at center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_out** : (smallint)</summary>

                      Outs played as center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_tc** : (smallint)</summary>

                      Total chances as center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_po** : (smallint)</summary>

                      Putouts as center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_a** : (smallint)</summary>

                      Assists as center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_e** : (smallint)</summary>

                      Errors as center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_dp** : (smallint)</summary>

                      Double plays turned as center fielder
                    </detail>
                    <detail>
                      <summary>**f_cf_tp** : (smallint)</summary>

                      Triple pays turned as center fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_g** : (smallint)</summary>

                      Appearances at right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_gs** : (smallint)</summary>

                      Starts at right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_out** : (smallint)</summary>

                      Outs played as right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_tc** : (smallint)</summary>

                      Total chances as right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_po** : (smallint)</summary>

                      Putouts as right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_a** : (smallint)</summary>

                      Assists as right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_e** : (smallint)</summary>

                      Errors as right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_dp** : (smallint)</summary>

                      Double plays turned as right fielder
                    </detail>
                    <detail>
                      <summary>**f_rf_tp** : (smallint)</summary>

                      Triple pays turned as right fielder
                    </detail>
            ### deduced_game
                    <detail>
                      <summary>&#128273; **game_id** : (char(12))</summary>

                      Game ID (home team ID + YYYYMMDD + doubleheader flag
                    </detail>
            ### event
                    <detail>
                      <summary>&#128273; **game_id** : (char(12))</summary>

                      Game ID (home team ID + YYYYMMDD + doubleheader flag
                    </detail>
                    <detail>
                      <summary>&#128273; **event_id** : (integer)</summary>

                      Event number of game
                    </detail>
                    <detail>
                      <summary>**away_team_id** : (char(3))</summary>

                      Visiting Team
                    </detail>
                    <detail>
                      <summary>**inn_ct** : (smallint)</summary>

                      Inning
                    </detail>
                    <detail>
                      <summary>**bat_home_id** : (boolean)</summary>

                      Home team is batting
                    </detail>
                    <detail>
                      <summary>**outs_ct** : (smallint)</summary>

                      Outs (0-2)
                    </detail>
                    <detail>
                      <summary>**balls_ct** : (smallint)</summary>

                      Balls (0-3)
                    </detail>
                    <detail>
                      <summary>**strikes_ct** : (smallint)</summary>

                      Strikes (0-2
                    </detail>
                    <detail>
                      <summary>**pitch_seq_tx** : (varchar(30))</summary>

                      Pitch sequence
                    </detail>
                    <detail>
                      <summary>**away_score_ct** : (smallint)</summary>

                      Away score
                    </detail>
                    <detail>
                      <summary>**home_score_ct** : (smallint)</summary>

                      Home score
                    </detail>
                    <detail>
                      <summary>**bat_id** : (char(8))</summary>

                      Batter ID
                    </detail>
                    <detail>
                      <summary>**bat_hand_cd** : (char(1))</summary>

                      Batter handedness
                    </detail>
                    <detail>
                      <summary>**resp_bat_id** : (char(8))</summary>

                      ID of batter charged with event
                    </detail>
                    <detail>
                      <summary>**resp_bat_hand_cd** : (char(1))</summary>

                      Handedness of batter charged with event
                    </detail>
                    <detail>
                      <summary>**pit_id** : (char(8))</summary>

                      Pitcher ID
                    </detail>
                    <detail>
                      <summary>**pit_hand_cd** : (char(1))</summary>

                      Pitcher handedness
                    </detail>
                    <detail>
                      <summary>**resp_pit_id** : (char(8))</summary>

                      ID of pitcher charged with event
                    </detail>
                    <detail>
                      <summary>**resp_pit_hand_cd** : (char(1))</summary>

                      Handedness of pitcher charged with event
                    </detail>
                    <detail>
                      <summary>**pos2_fld_id** : (char(8))</summary>

                      Catcher ID
                    </detail>
                    <detail>
                      <summary>**pos3_fld_id** : (char(8))</summary>

                      First baseman ID
                    </detail>
                    <detail>
                      <summary>**pos4_fld_id** : (char(8))</summary>

                      Second baseman ID
                    </detail>
                    <detail>
                      <summary>**pos5_fld_id** : (char(8))</summary>

                      Third baseman ID
                    </detail>
                    <detail>
                      <summary>**pos6_fld_id** : (char(8))</summary>

                      Shortstop ID
                    </detail>
                    <detail>
                      <summary>**pos7_fld_id** : (char(8))</summary>

                      Left fielder ID
                    </detail>
                    <detail>
                      <summary>**pos8_fld_id** : (char(8))</summary>

                      Center fielder ID
                    </detail>
                    <detail>
                      <summary>**pos9_fld_id** : (char(8))</summary>

                      Right fielder ID
                    </detail>
                    <detail>
                      <summary>**base1_run_id** : (char(8))</summary>

                      ID of runner on first
                    </detail>
                    <detail>
                      <summary>**base2_run_id** : (char(8))</summary>

                      ID of runner on second
                    </detail>
                    <detail>
                      <summary>**base3_run_id** : (char(8))</summary>

                      ID of runner on third
                    </detail>
                    <detail>
                      <summary>**event_tx** : (varchar(128))</summary>

                      Event text (in scoring shorthand
                    </detail>
                    <detail>
                      <summary>**leadoff_fl** : (boolean)</summary>

                      Batter is leading off the inning
                    </detail>
                    <detail>
                      <summary>**ph_fl** : (boolean)</summary>

                      Batter is pinch-hitting
                    </detail>
                    <detail>
                      <summary>**bat_fld_cd** : (smallint)</summary>

                      Defensive position of batter (10 for DH, 11 for PH, 12 for PR
                    </detail>
                    <detail>
                      <summary>**bat_lineup_id** : (smallint)</summary>

                      Lineup position (1-9)
                    </detail>
                    <detail>
                      <summary>**event_cd** : (smallint)</summary>

                      Event code (join table `code_event` for descriptions
                    </detail>
                    <detail>
                      <summary>**bat_event_fl** : (boolean)</summary>

                      Event is related to the batter
                    </detail>
                    <detail>
                      <summary>**ab_fl** : (boolean)</summary>

                      Event is an at-bat
                    </detail>
                    <detail>
                      <summary>**h_fl** : (smallint)</summary>

                      Event is a hit
                    </detail>
                    <detail>
                      <summary>**sh_fl** : (boolean)</summary>

                      Event is a sacrifice hit
                    </detail>
                    <detail>
                      <summary>**sf_fl** : (boolean)</summary>

                      Event is a sacrifice fly
                    </detail>
                    <detail>
                      <summary>**event_outs_ct** : (smallint)</summary>

                      Outs recorded on event (0-3)
                    </detail>
                    <detail>
                      <summary>**dp_fl** : (boolean)</summary>

                      Event is a double play
                    </detail>
                    <detail>
                      <summary>**tp_fl** : (boolean)</summary>

                      Event is a triple play
                    </detail>
                    <detail>
                      <summary>**rbi_ct** : (smallint)</summary>

                      Runs batted in on event
                    </detail>
                    <detail>
                      <summary>**wp_fl** : (boolean)</summary>

                      Event is a wild pitch
                    </detail>
                    <detail>
                      <summary>**pb_fl** : (boolean)</summary>

                      Event is a passed ball
                    </detail>
                    <detail>
                      <summary>**fld_cd** : (smallint)</summary>

                      Position id of event fielder
                    </detail>
                    <detail>
                      <summary>**battedball_cd** : (char(1))</summary>

                      Batted ball code (P - pop-up, G - ground ball, F - fly ball, L - line drive
                    </detail>
                    <detail>
                      <summary>**bunt_fl** : (boolean)</summary>

                      Event is a bunt
                    </detail>
                    <detail>
                      <summary>**foul_fl** : (boolean)</summary>

                      Event is a foul ball
                    </detail>
                    <detail>
                      <summary>**battedball_loc_tx** : (varchar(5))</summary>

                      Hit location code (see https://www.retrosheet.org/location.htm)
                    </detail>
                    <detail>
                      <summary>**err_ct** : (smallint)</summary>

                      Number of errors recorded during event
                    </detail>
                    <detail>
                      <summary>**err1_fld_cd** : (smallint)</summary>

                      Position code of fielder committing first error during event
                    </detail>
                    <detail>
                      <summary>**err1_cd** : (char(1))</summary>

                      First error type (T - throwing, F - fielding)
                    </detail>
                    <detail>
                      <summary>**err2_fld_cd** : (smallint)</summary>

                      Position code of fielder committing second error during event
                    </detail>
                    <detail>
                      <summary>**err2_cd** : (char(1))</summary>

                      Second error type (T - throwing, F - fielding)
                    </detail>
                    <detail>
                      <summary>**err3_fld_cd** : (smallint)</summary>

                      Position code of fielder committing third error during event
                    </detail>
                    <detail>
                      <summary>**err3_cd** : (char(1))</summary>

                      Third error type (T - throwing, F - fielding)
                    </detail>
                    <detail>
                      <summary>**bat_dest_id** : (smallint)</summary>

                      Destination of batter after event (0 - putout, 1-3 - bases, 4 - scored asearned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
                    </detail>
                    <detail>
                      <summary>**run1_dest_id** : (smallint)</summary>

                      Destination of runner on first after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
                    </detail>
                    <detail>
                      <summary>**run2_dest_id** : (smallint)</summary>

                      Destination of runner on second after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
                    </detail>
                    <detail>
                      <summary>**run3_dest_id** : (smallint)</summary>

                      Destination of runner on third after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
                    </detail>
                    <detail>
                      <summary>**bat_play_tx** : (varchar(15))</summary>

                      Fielding play on batter
                    </detail>
                    <detail>
                      <summary>**run1_play_tx** : (varchar(15))</summary>

                      Fielding play on runner on first
                    </detail>
                    <detail>
                      <summary>**run2_play_tx** : (varchar(15))</summary>

                      Fielding play on runner on second
                    </detail>
                    <detail>
                      <summary>**run3_play_tx** : (varchar(15))</summary>

                      Fielding play on runner on third
                    </detail>
                    <detail>
                      <summary>**run1_sb_fl** : (boolean)</summary>

                      Runner on first steals base
                    </detail>
                    <detail>
                      <summary>**run2_sb_fl** : (boolean)</summary>

                      Runner on second steals base
                    </detail>
                    <detail>
                      <summary>**run3_sb_fl** : (boolean)</summary>

                      Runner on third steals base
                    </detail>
                    <detail>
                      <summary>**run1_cs_fl** : (boolean)</summary>

                      Runner on first caught stealing
                    </detail>
                    <detail>
                      <summary>**run2_cs_fl** : (boolean)</summary>

                      Runner on second caught stealing
                    </detail>
                    <detail>
                      <summary>**run3_cs_fl** : (boolean)</summary>

                      Runner on third caught stealing
                    </detail>
                    <detail>
                      <summary>**run1_pk_fl** : (boolean)</summary>

                      Runner on first picked off
                    </detail>
                    <detail>
                      <summary>**run2_pk_fl** : (boolean)</summary>

                      Runner on second picked off
                    </detail>
                    <detail>
                      <summary>**run3_pk_fl** : (boolean)</summary>

                      Runner on third picked off
                    </detail>
                    <detail>
                      <summary>**run1_resp_pit_id** : (char(8))</summary>

                      ID of pitcher charged with runner on first
                    </detail>
                    <detail>
                      <summary>**run2_resp_pit_id** : (char(8))</summary>

                      ID of pitcher charged with runner on second
                    </detail>
                    <detail>
                      <summary>**run3_resp_pit_id** : (char(8))</summary>

                      ID of pitcher charged with runner on third
                    </detail>
                    <detail>
                      <summary>**game_new_fl** : (boolean)</summary>

                      Start of game flag
                    </detail>
                    <detail>
                      <summary>**game_end_fl** : (boolean)</summary>

                      End of game flag
                    </detail>
                    <detail>
                      <summary>**pr_run1_fl** : (boolean)</summary>

                      Pinch-runner on first
                    </detail>
                    <detail>
                      <summary>**pr_run2_fl** : (boolean)</summary>

                      Pinch-runner on second
                    </detail>
                    <detail>
                      <summary>**pr_run3_fl** : (boolean)</summary>

                      Runner on third
                    </detail>
                    <detail>
                      <summary>**removed_for_pr_run1_id** : (char(8))</summary>

                      ID of former runner on first removed for pinch-runner
                    </detail>
                    <detail>
                      <summary>**removed_for_pr_run2_id** : (char(8))</summary>

                      ID of former runner on second removed for pinch-runner
                    </detail>
                    <detail>
                      <summary>**removed_for_pr_run3_id** : (char(8))</summary>

                      ID of former runner on third removed for pinch-runner
                    </detail>
                    <detail>
                      <summary>**removed_for_ph_bat_id** : (char(8))</summary>

                      ID of former batter removed for pinch-hitter
                    </detail>
                    <detail>
                      <summary>**removed_for_ph_bat_fld_cd** : (integer)</summary>

                      Position code of batter removed for pinch-hitter
                    </detail>
                    <detail>
                      <summary>**po1_fld_cd** : (smallint)</summary>

                      Position code of fielder with first putout
                    </detail>
                    <detail>
                      <summary>**po2_fld_cd** : (smallint)</summary>

                      Position code of fielder with second putout
                    </detail>
                    <detail>
                      <summary>**po3_fld_cd** : (smallint)</summary>

                      Position code of fielder with third putout
                    </detail>
                    <detail>
                      <summary>**ass1_fld_cd** : (smallint)</summary>

                      Position code of fielder with first assist
                    </detail>
                    <detail>
                      <summary>**ass2_fld_cd** : (smallint)</summary>

                      Position code of fielder with second assist
                    </detail>
                    <detail>
                      <summary>**ass3_fld_cd** : (smallint)</summary>

                      Position code of fielder with third assist
                    </detail>
                    <detail>
                      <summary>**ass4_fld_cd** : (smallint)</summary>

                      Position code of fielder with fourth assist
                    </detail>
                    <detail>
                      <summary>**ass5_fld_cd** : (smallint)</summary>

                      Position code of fielder with fifth assist
                    </detail>
                    <detail>
                      <summary>**home_team_id** : (char(3))</summary>

                      Home team ID
                    </detail>
                    <detail>
                      <summary>**bat_team_id** : (char(3))</summary>

                      Batting team ID
                    </detail>
                    <detail>
                      <summary>**fld_team_id** : (char(3))</summary>

                      Fielding team ID
                    </detail>
                    <detail>
                      <summary>**bat_last_id** : (smallint)</summary>

                      Half inning (differs from batting team if home team bats first)
                    </detail>
                    <detail>
                      <summary>**inn_new_fl** : (boolean)</summary>

                      Start of half-inning flag
                    </detail>
                    <detail>
                      <summary>**inn_end_fl** : (boolean)</summary>

                      End of half-inning flag
                    </detail>
                    <detail>
                      <summary>**start_bat_score_ct** : (smallint)</summary>

                      Runs scored by batting team (prior to this event)
                    </detail>
                    <detail>
                      <summary>**start_fld_score_ct** : (smallint)</summary>

                      Runs scored by fielding team
                    </detail>
                    <detail>
                      <summary>**inn_runs_ct** : (smallint)</summary>

                      Runs scored in this half-inning (prior to this event)
                    </detail>
                    <detail>
                      <summary>**game_pa_ct** : (smallint)</summary>

                      Batting team PA total (prior to this event)
                    </detail>
                    <detail>
                      <summary>**inn_pa_ct** : (smallint)</summary>

                      Half-inning PA total (prior to this event)
                    </detail>
                    <detail>
                      <summary>**pa_new_fl** : (boolean)</summary>

                      Event is the start of a plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_trunc_fl** : (boolean)</summary>

                      Event is a truncated plate appearance
                    </detail>
                    <detail>
                      <summary>**start_bases_cd** : (smallint)</summary>

                      Base state at start of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
                    </detail>
                    <detail>
                      <summary>**end_bases_cd** : (smallint)</summary>

                      Base state end of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
                    </detail>
                    <detail>
                      <summary>**bat_start_fl** : (boolean)</summary>

                      Batter started game
                    </detail>
                    <detail>
                      <summary>**resp_bat_start_fl** : (boolean)</summary>

                      Result-charged batter is a starter
                    </detail>
                    <detail>
                      <summary>**bat_on_deck_id** : (char(8))</summary>

                      ID of batter on deck
                    </detail>
                    <detail>
                      <summary>**bat_in_hold_id** : (char(8))</summary>

                      Id of batter in the hole
                    </detail>
                    <detail>
                      <summary>**pit_start_fl** : (boolean)</summary>

                      Pitcher started game
                    </detail>
                    <detail>
                      <summary>**resp_pit_start_fl** : (boolean)</summary>

                      Result-charged pitcher started game
                    </detail>
                    <detail>
                      <summary>**run1_fld_cd** : (smallint)</summary>

                      Defensive position code of runner on first
                    </detail>
                    <detail>
                      <summary>**run1_lineup_cd** : (smallint)</summary>

                      Lineup position of runner on first
                    </detail>
                    <detail>
                      <summary>**run1_origin_event_id** : (smallint)</summary>

                      Event number on which runner on first reached base
                    </detail>
                    <detail>
                      <summary>**run2_fld_cd** : (smallint)</summary>

                      Defensive position code of runner on second
                    </detail>
                    <detail>
                      <summary>**run2_lineup_cd** : (smallint)</summary>

                      Lineup position of runner on second
                    </detail>
                    <detail>
                      <summary>**run2_origin_event_id** : (smallint)</summary>

                      Event number on which runner on second reached base
                    </detail>
                    <detail>
                      <summary>**run3_fld_cd** : (smallint)</summary>

                      Defensive position code of runner on third
                    </detail>
                    <detail>
                      <summary>**run3_lineup_cd** : (smallint)</summary>

                      Lineup position of runner on third
                    </detail>
                    <detail>
                      <summary>**run3_origin_event_id** : (smallint)</summary>

                      Event number on which runner on third reached base
                    </detail>
                    <detail>
                      <summary>**run1_resp_cat_id** : (char(8))</summary>

                      ID of responsible catcher for runner on first
                    </detail>
                    <detail>
                      <summary>**run2_resp_cat_id** : (char(8))</summary>

                      ID of responsible catcher for runner on second
                    </detail>
                    <detail>
                      <summary>**run3_resp_cat_id** : (char(8))</summary>

                      ID of responsible catcher for runner on third
                    </detail>
                    <detail>
                      <summary>**pa_ball_ct** : (smallint)</summary>

                      Number of balls in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_called_ball_ct** : (smallint)</summary>

                      Number of called balls in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_intent_ball_ct** : (smallint)</summary>

                      Number of intentional balls in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_pitchout_ball_ct** : (smallint)</summary>

                      Number of pitchouts in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_hitbatter_ball_ct** : (smallint)</summary>

                      Number of pitches hitting batter in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_other_ball_ct** : (smallint)</summary>

                      Number of other balls in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_strike_ct** : (smallint)</summary>

                      Number of strikes in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_called_strike_ct** : (smallint)</summary>

                      Number of called strikes in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_swingmiss_strike_ct** : (smallint)</summary>

                      Number of swing-and-miss strikes in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_foul_strike_ct** : (smallint)</summary>

                      Number of foul balls in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_inplay_strike_ct** : (smallint)</summary>

                      Number of balls in play in plate appearance
                    </detail>
                    <detail>
                      <summary>**pa_other_strike_ct** : (smallint)</summary>

                      Number of other strikes in plate appearance
                    </detail>
                    <detail>
                      <summary>**event_runs_ct** : (smallint)</summary>

                      Number of runs on play
                    </detail>
                    <detail>
                      <summary>**fld_id** : (char(8))</summary>

                      ID of player fielding batted ball
                    </detail>
                    <detail>
                      <summary>**base2_force_fl** : (boolean)</summary>

                      Event has force play at second
                    </detail>
                    <detail>
                      <summary>**base3_force_fl** : (boolean)</summary>

                      Event has force play at third
                    </detail>
                    <detail>
                      <summary>**base4_force_fl** : (boolean)</summary>

                      Event has force play at home
                    </detail>
                    <detail>
                      <summary>**bat_safe_err_fl** : (boolean)</summary>

                      Event has batter safe on an error
                    </detail>
                    <detail>
                      <summary>**bat_fate_id** : (smallint)</summary>

                      Ultimate fate of batter (see `dest_id` cols for code meaning
                    </detail>
                    <detail>
                      <summary>**run1_fate_id** : (smallint)</summary>

                      Ultimate fate of runner on first (see `dest_id` cols for code meaning
                    </detail>
                    <detail>
                      <summary>**run2_fate_id** : (smallint)</summary>

                      Ultimate fate of runner on second (see `dest_id` cols for code meaning
                    </detail>
                    <detail>
                      <summary>**run3_fate_id** : (smallint)</summary>

                      Ultimate fate of runner on third (see `dest_id` cols for code meaning
                    </detail>
                    <detail>
                      <summary>**fate_runs_ct** : (smallint)</summary>

                      Additional runs scored in half inning after this event
                    </detail>
                    <detail>
                      <summary>**ass6_fld_cd** : (smallint)</summary>

                      Position code of fielder with sixth assist
                    </detail>
                    <detail>
                      <summary>**ass7_fld_cd** : (smallint)</summary>

                      Position code of fielder with seventh assist
                    </detail>
                    <detail>
                      <summary>**ass8_fld_cd** : (smallint)</summary>

                      Position code of fielder with eighth assist
                    </detail>
                    <detail>
                      <summary>**ass9_fld_cd** : (smallint)</summary>

                      Position code of fielder with ninth assist
                    </detail>
                    <detail>
                      <summary>**ass10_fld_cd** : (smallint)</summary>

                      Position code of fielder with tenth assist
                    </detail>
                    <detail>
                      <summary>**unknown_out_exc_fl** : (boolean)</summary>

                      Unknown fielding credit flag
                    </detail>
                    <detail>
                      <summary>**uncertain_play_exc_fl** : (boolean)</summary>

                      Uncertain play flag
                    </detail>
            ### game
                    <detail>
                      <summary>&#128273; **game_id** : (char(12))</summary>

                      Game ID (home team ID + YYYYMMDD + doubleheader flag
                    </detail>
                    <detail>
                      <summary>**game_dt** : (date)</summary>

                      Game date
                    </detail>
                    <detail>
                      <summary>**game_ct** : (smallint)</summary>

                      Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
                    </detail>
                    <detail>
                      <summary>**game_dy** : (varchar(9))</summary>

                      Day of week
                    </detail>
                    <detail>
                      <summary>**start_game_tm** : (smallint)</summary>

                      Game start time (12HMM coded as integer, eg 1015 for 10:15 PM)
                    </detail>
                    <detail>
                      <summary>**dh_fl** : (varchar(1))</summary>

                      DH used
                    </detail>
                    <detail>
                      <summary>**daynight_park_cd** : (varchar(1))</summary>

                      D - day game, N - night game
                    </detail>
                    <detail>
                      <summary>**away_team_id** : (char(3))</summary>

                      Away team ID
                    </detail>
                    <detail>
                      <summary>**home_team_id** : (char(3))</summary>

                      Home team ID
                    </detail>
                    <detail>
                      <summary>**park_id** : (varchar(5))</summary>

                      Park ID
                    </detail>
                    <detail>
                      <summary>**away_start_pit_id** : (char(8))</summary>

                      Away team starting pitcher ID
                    </detail>
                    <detail>
                      <summary>**home_start_pit_id** : (char(8))</summary>

                      Home team starting pitcher ID
                    </detail>
                    <detail>
                      <summary>**base4_ump_id** : (varchar(32))</summary>

                      Home plate umpire ID
                    </detail>
                    <detail>
                      <summary>**base1_ump_id** : (varchar(32))</summary>

                      First base umpire ID
                    </detail>
                    <detail>
                      <summary>**base2_ump_id** : (varchar(32))</summary>

                      Second base umpire ID
                    </detail>
                    <detail>
                      <summary>**base3_ump_id** : (varchar(32))</summary>

                      Third base umpire ID
                    </detail>
                    <detail>
                      <summary>**lf_ump_id** : (char(8))</summary>

                      Left field umpire ID
                    </detail>
                    <detail>
                      <summary>**rf_ump_id** : (char(8))</summary>

                      Right field umpire ID
                    </detail>
                    <detail>
                      <summary>**attend_park_ct** : (integer)</summary>

                      Attendance
                    </detail>
                    <detail>
                      <summary>**scorer_record_id** : (varchar(50))</summary>

                      Scorekeeper
                    </detail>
                    <detail>
                      <summary>**translator_record_id** : (varchar(50))</summary>

                      Translator
                    </detail>
                    <detail>
                      <summary>**inputter_record_id** : (varchar(50))</summary>

                      Inputter
                    </detail>
                    <detail>
                      <summary>**input_record_ts** : (varchar(20))</summary>

                      Date and time of record input
                    </detail>
                    <detail>
                      <summary>**edit_record_ts** : (varchar(20))</summary>

                      Date and time of Most recent record edit
                    </detail>
                    <detail>
                      <summary>**method_record_cd** : (varchar(1))</summary>

                      How the game was scored (join `code_method_record` for details
                    </detail>
                    <detail>
                      <summary>**pitches_record_cd** : (varchar(1))</summary>

                      Highest detail of pitches recorded (join `code_pitches_record` for details). Note that many games with pitch detail do not have that info for all events, so pitch totals may not be accurate.
                    </detail>
                    <detail>
                      <summary>**temp_park_ct** : (smallint)</summary>

                      Park temperature in degrees F (0 if unknown)
                    </detail>
                    <detail>
                      <summary>**wind_direction_park_cd** : (smallint)</summary>

                      Wind direction park code (join `code_wind_direction_park` for details)
                    </detail>
                    <detail>
                      <summary>**wind_speed_park_ct** : (smallint)</summary>

                      Wind speed in miles per hour (-1 if unknown)
                    </detail>
                    <detail>
                      <summary>**field_park_cd** : (smallint)</summary>

                      Park field condition code (join `code_field_park` for details)
                    </detail>
                    <detail>
                      <summary>**precip_park_cd** : (smallint)</summary>

                      Park precipitation code (join `code_precip_park` for details
                    </detail>
                    <detail>
                      <summary>**sky_park_cd** : (smallint)</summary>

                      Park sky condition code (join `code_sky_park` for details
                    </detail>
                    <detail>
                      <summary>**minutes_game_ct** : (smallint)</summary>

                      Length of game in minutes
                    </detail>
                    <detail>
                      <summary>**inn_ct** : (smallint)</summary>

                      Length of game in innings
                    </detail>
                    <detail>
                      <summary>**away_score_ct** : (smallint)</summary>

                      Away team final score
                    </detail>
                    <detail>
                      <summary>**home_score_ct** : (smallint)</summary>

                      Home team final score
                    </detail>
                    <detail>
                      <summary>**away_hits_ct** : (smallint)</summary>

                      Away team hits
                    </detail>
                    <detail>
                      <summary>**home_hits_ct** : (smallint)</summary>

                      Home team hits
                    </detail>
                    <detail>
                      <summary>**away_err_ct** : (smallint)</summary>

                      Away team errors
                    </detail>
                    <detail>
                      <summary>**home_err_ct** : (smallint)</summary>

                      Home team errors
                    </detail>
                    <detail>
                      <summary>**away_lob_ct** : (smallint)</summary>

                      Away team left on base
                    </detail>
                    <detail>
                      <summary>**home_lob_ct** : (smallint)</summary>

                      Home team left on base
                    </detail>
                    <detail>
                      <summary>**win_pit_id** : (char(8))</summary>

                      ID of winning pitcher
                    </detail>
                    <detail>
                      <summary>**lose_pit_id** : (char(8))</summary>

                      ID of losing pitcher
                    </detail>
                    <detail>
                      <summary>**save_pit_id** : (char(8))</summary>

                      ID of saving pitcher
                    </detail>
                    <detail>
                      <summary>**gwrbi_bat_id** : (char(8))</summary>

                      ID of batter wit game-winning RBI
                    </detail>
                    <detail>
                      <summary>**away_lineup1_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 1
                    </detail>
                    <detail>
                      <summary>**away_lineup1_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 1
                    </detail>
                    <detail>
                      <summary>**away_lineup2_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 2
                    </detail>
                    <detail>
                      <summary>**away_lineup2_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 2
                    </detail>
                    <detail>
                      <summary>**away_lineup3_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 3
                    </detail>
                    <detail>
                      <summary>**away_lineup3_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 3
                    </detail>
                    <detail>
                      <summary>**away_lineup4_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 4
                    </detail>
                    <detail>
                      <summary>**away_lineup4_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 4
                    </detail>
                    <detail>
                      <summary>**away_lineup5_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 5
                    </detail>
                    <detail>
                      <summary>**away_lineup5_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 5
                    </detail>
                    <detail>
                      <summary>**away_lineup6_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 6
                    </detail>
                    <detail>
                      <summary>**away_lineup6_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 6
                    </detail>
                    <detail>
                      <summary>**away_lineup7_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 7
                    </detail>
                    <detail>
                      <summary>**away_lineup7_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 7
                    </detail>
                    <detail>
                      <summary>**away_lineup8_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 8
                    </detail>
                    <detail>
                      <summary>**away_lineup8_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 8
                    </detail>
                    <detail>
                      <summary>**away_lineup9_bat_id** : (char(8))</summary>

                      ID of away team starting batter in lineup position 9
                    </detail>
                    <detail>
                      <summary>**away_lineup9_fld_cd** : (smallint)</summary>

                      Fielding position code of away team starting batter in lineup position 9
                    </detail>
                    <detail>
                      <summary>**home_lineup1_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 1
                    </detail>
                    <detail>
                      <summary>**home_lineup1_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 1
                    </detail>
                    <detail>
                      <summary>**home_lineup2_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 2
                    </detail>
                    <detail>
                      <summary>**home_lineup2_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 2
                    </detail>
                    <detail>
                      <summary>**home_lineup3_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 3
                    </detail>
                    <detail>
                      <summary>**home_lineup3_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 3
                    </detail>
                    <detail>
                      <summary>**home_lineup4_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 4
                    </detail>
                    <detail>
                      <summary>**home_lineup4_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 4
                    </detail>
                    <detail>
                      <summary>**home_lineup5_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 5
                    </detail>
                    <detail>
                      <summary>**home_lineup5_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 5
                    </detail>
                    <detail>
                      <summary>**home_lineup6_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 6
                    </detail>
                    <detail>
                      <summary>**home_lineup6_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 6
                    </detail>
                    <detail>
                      <summary>**home_lineup7_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 7
                    </detail>
                    <detail>
                      <summary>**home_lineup7_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 7
                    </detail>
                    <detail>
                      <summary>**home_lineup8_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 8
                    </detail>
                    <detail>
                      <summary>**home_lineup8_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 8
                    </detail>
                    <detail>
                      <summary>**home_lineup9_bat_id** : (char(8))</summary>

                      ID of home team starting batter in lineup position 9
                    </detail>
                    <detail>
                      <summary>**home_lineup9_fld_cd** : (smallint)</summary>

                      Fielding position code of home team starting batter in lineup position 9
                    </detail>
                    <detail>
                      <summary>**away_finish_pit_id** : (char(8))</summary>

                      Away team finishing pitcher
                    </detail>
                    <detail>
                      <summary>**home_finish_pit_id** : (char(8))</summary>

                      Home team finishing pitcher
                    </detail>
                    <detail>
                      <summary>**away_team_league_id** : (char(1))</summary>

                      Away team league (1 char ID)
                    </detail>
                    <detail>
                      <summary>**home_team_league_id** : (char(1))</summary>

                      Home team league (1 char ID)
                    </detail>
                    <detail>
                      <summary>**away_team_game_ct** : (smallint)</summary>

                      Away team game number
                    </detail>
                    <detail>
                      <summary>**home_team_game_ct** : (smallint)</summary>

                      Home team game number
                    </detail>
                    <detail>
                      <summary>**outs_ct** : (smallint)</summary>

                      Length of game in outs
                    </detail>
                    <detail>
                      <summary>**completion_tx** : (varchar(26))</summary>

                      Information on completion of game
                    </detail>
                    <detail>
                      <summary>**forfeit_tx** : (varchar(26))</summary>

                      Information on forfeit of game
                    </detail>
                    <detail>
                      <summary>**protest_tx** : (varchar(26))</summary>

                      Information on protest of game
                    </detail>
                    <detail>
                      <summary>**away_line_tx** : (varchar(26))</summary>

                      Away team linescore
                    </detail>
                    <detail>
                      <summary>**home_line_tx** : (varchar(26))</summary>

                      Home team linescore
                    </detail>
                    <detail>
                      <summary>**away_ab_ct** : (smallint)</summary>

                      Away team at bats
                    </detail>
                    <detail>
                      <summary>**away_2b_ct** : (smallint)</summary>

                      Away team doubles
                    </detail>
                    <detail>
                      <summary>**away_3b_ct** : (smallint)</summary>

                      Away team triples
                    </detail>
                    <detail>
                      <summary>**away_hr_ct** : (smallint)</summary>

                      Away team home runs
                    </detail>
                    <detail>
                      <summary>**away_bi_ct** : (smallint)</summary>

                      Away team runs batted in
                    </detail>
                    <detail>
                      <summary>**away_sh_ct** : (smallint)</summary>

                      Away team sacrifice hits
                    </detail>
                    <detail>
                      <summary>**away_sf_ct** : (smallint)</summary>

                      Away team sacrifice flies
                    </detail>
                    <detail>
                      <summary>**away_hp_ct** : (smallint)</summary>

                      Away team hit by pitches
                    </detail>
                    <detail>
                      <summary>**away_bb_ct** : (smallint)</summary>

                      Away team walks
                    </detail>
                    <detail>
                      <summary>**away_ibb_ct** : (smallint)</summary>

                      Away team intentional walks
                    </detail>
                    <detail>
                      <summary>**away_so_ct** : (smallint)</summary>

                      Away team strikeouts
                    </detail>
                    <detail>
                      <summary>**away_sb_ct** : (smallint)</summary>

                      Away team stolen bases
                    </detail>
                    <detail>
                      <summary>**away_cs_ct** : (smallint)</summary>

                      Away team caught stealing
                    </detail>
                    <detail>
                      <summary>**away_gdp_ct** : (smallint)</summary>

                      Away team grounded into double plays
                    </detail>
                    <detail>
                      <summary>**away_xi_ct** : (smallint)</summary>

                      Away team reached on interference
                    </detail>
                    <detail>
                      <summary>**away_pitcher_ct** : (smallint)</summary>

                      Away team number of pitchers used
                    </detail>
                    <detail>
                      <summary>**away_er_ct** : (smallint)</summary>

                      Away team individual earned runs
                    </detail>
                    <detail>
                      <summary>**away_ter_ct** : (smallint)</summary>

                      Away team team earned runs
                    </detail>
                    <detail>
                      <summary>**away_wp_ct** : (smallint)</summary>

                      Away team wild pitches
                    </detail>
                    <detail>
                      <summary>**away_bk_ct** : (smallint)</summary>

                      Away team balks
                    </detail>
                    <detail>
                      <summary>**away_po_ct** : (smallint)</summary>

                      Away team putouts
                    </detail>
                    <detail>
                      <summary>**away_a_ct** : (smallint)</summary>

                      Away team assists
                    </detail>
                    <detail>
                      <summary>**away_pb_ct** : (smallint)</summary>

                      Away team passed balls
                    </detail>
                    <detail>
                      <summary>**away_dp_ct** : (smallint)</summary>

                      Away team double plays turned
                    </detail>
                    <detail>
                      <summary>**away_tp_ct** : (smallint)</summary>

                      Away team triple plays turned
                    </detail>
                    <detail>
                      <summary>**home_ab_ct** : (smallint)</summary>

                      Home team at bats
                    </detail>
                    <detail>
                      <summary>**home_2b_ct** : (smallint)</summary>

                      Home team doubles
                    </detail>
                    <detail>
                      <summary>**home_3b_ct** : (smallint)</summary>

                      Home team triples
                    </detail>
                    <detail>
                      <summary>**home_hr_ct** : (smallint)</summary>

                      Home team home runs
                    </detail>
                    <detail>
                      <summary>**home_bi_ct** : (smallint)</summary>

                      Home team runs batted in
                    </detail>
                    <detail>
                      <summary>**home_sh_ct** : (smallint)</summary>

                      Home team sacrifice hits
                    </detail>
                    <detail>
                      <summary>**home_sf_ct** : (smallint)</summary>

                      Home team sacrifice flies
                    </detail>
                    <detail>
                      <summary>**home_hp_ct** : (smallint)</summary>

                      Home team hit by pitches
                    </detail>
                    <detail>
                      <summary>**home_bb_ct** : (smallint)</summary>

                      Home team walks
                    </detail>
                    <detail>
                      <summary>**home_ibb_ct** : (smallint)</summary>

                      Home team intentional walks
                    </detail>
                    <detail>
                      <summary>**home_so_ct** : (smallint)</summary>

                      Home team strikeouts
                    </detail>
                    <detail>
                      <summary>**home_sb_ct** : (smallint)</summary>

                      Home team stolen bases
                    </detail>
                    <detail>
                      <summary>**home_cs_ct** : (smallint)</summary>

                      Home team caught stealing
                    </detail>
                    <detail>
                      <summary>**home_gdp_ct** : (smallint)</summary>

                      Home team grounded into double plays
                    </detail>
                    <detail>
                      <summary>**home_xi_ct** : (smallint)</summary>

                      Home team reached on interference
                    </detail>
                    <detail>
                      <summary>**home_pitcher_ct** : (smallint)</summary>

                      Home team number of pitchers used
                    </detail>
                    <detail>
                      <summary>**home_er_ct** : (smallint)</summary>

                      Home team individual earned runs
                    </detail>
                    <detail>
                      <summary>**home_ter_ct** : (smallint)</summary>

                      Home team team earned runs
                    </detail>
                    <detail>
                      <summary>**home_wp_ct** : (smallint)</summary>

                      Home team wild pitches
                    </detail>
                    <detail>
                      <summary>**home_bk_ct** : (smallint)</summary>

                      Home team balks
                    </detail>
                    <detail>
                      <summary>**home_po_ct** : (smallint)</summary>

                      Home team putouts
                    </detail>
                    <detail>
                      <summary>**home_a_ct** : (smallint)</summary>

                      Home team assists
                    </detail>
                    <detail>
                      <summary>**home_pb_ct** : (smallint)</summary>

                      Home team passed balls
                    </detail>
                    <detail>
                      <summary>**home_dp_ct** : (smallint)</summary>

                      Home team double plays turned
                    </detail>
                    <detail>
                      <summary>**home_tp_ct** : (smallint)</summary>

                      Home team triple plays turned
                    </detail>
                    <detail>
                      <summary>**ump_home_name_tx** : (varchar(26))</summary>

                      Home plate umpire name
                    </detail>
                    <detail>
                      <summary>**ump_1b_name_tx** : (varchar(26))</summary>

                      First base umpire name
                    </detail>
                    <detail>
                      <summary>**ump_2b_name_tx** : (varchar(26))</summary>

                      Second base umpire name
                    </detail>
                    <detail>
                      <summary>**ump_3b_name_tx** : (varchar(26))</summary>

                      Third base umpire name
                    </detail>
                    <detail>
                      <summary>**ump_lf_name_tx** : (varchar(26))</summary>

                      Left field umpire name
                    </detail>
                    <detail>
                      <summary>**ump_rf_name_tx** : (varchar(26))</summary>

                      Right field umpire name
                    </detail>
                    <detail>
                      <summary>**away_manager_id** : (char(8))</summary>

                      Away manager ID
                    </detail>
                    <detail>
                      <summary>**away_manager_name_tx** : (varchar(26))</summary>

                      Away manager name
                    </detail>
                    <detail>
                      <summary>**home_manager_id** : (char(8))</summary>

                      Home manager ID
                    </detail>
                    <detail>
                      <summary>**home_manager_name_tx** : (varchar(26))</summary>

                      Home manager name
                    </detail>
                    <detail>
                      <summary>**win_pit_name_tx** : (varchar(26))</summary>

                      Wining pitcher name
                    </detail>
                    <detail>
                      <summary>**lose_pit_name_tx** : (varchar(26))</summary>

                      Losing pitcher name
                    </detail>
                    <detail>
                      <summary>**save_pit_name_tx** : (varchar(26))</summary>

                      Saving pitcher name
                    </detail>
                    <detail>
                      <summary>**goahead_rbi_id** : (char(8))</summary>

                      ID of batter with goahead RBI
                    </detail>
                    <detail>
                      <summary>**goahead_rbi_name_tx** : (varchar(26))</summary>

                      Name of batter with goahead RBI
                    </detail>
                    <detail>
                      <summary>**away_lineup1_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 1
                    </detail>
                    <detail>
                      <summary>**away_lineup2_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 2
                    </detail>
                    <detail>
                      <summary>**away_lineup3_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 3
                    </detail>
                    <detail>
                      <summary>**away_lineup4_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 4
                    </detail>
                    <detail>
                      <summary>**away_lineup5_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 5
                    </detail>
                    <detail>
                      <summary>**away_lineup6_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 6
                    </detail>
                    <detail>
                      <summary>**away_lineup7_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 7
                    </detail>
                    <detail>
                      <summary>**away_lineup8_bat_name_tx** : (varchar(26))</summary>

                      Name of away team batter in lineup position 8
                    </detail>
                    <detail>
                      <summary>**away_lineup9_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 9
                    </detail>
                    <detail>
                      <summary>**home_lineup1_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 1
                    </detail>
                    <detail>
                      <summary>**home_lineup2_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 2
                    </detail>
                    <detail>
                      <summary>**home_lineup3_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 3
                    </detail>
                    <detail>
                      <summary>**home_lineup4_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 4
                    </detail>
                    <detail>
                      <summary>**home_lineup5_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 5
                    </detail>
                    <detail>
                      <summary>**home_lineup6_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 6
                    </detail>
                    <detail>
                      <summary>**home_lineup7_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 7
                    </detail>
                    <detail>
                      <summary>**home_lineup8_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 8
                    </detail>
                    <detail>
                      <summary>**home_lineup9_bat_name_tx** : (varchar(26))</summary>

                      Name of home team batter in lineup position 9
                    </detail>
                    <detail>
                      <summary>**add_info_tx** : (varchar(26))</summary>

                      Additional information
                    </detail>
                    <detail>
                      <summary>**acq_info_tx** : (varchar(26))</summary>

                      Acquisition information
                    </detail>
            ### gamelog
                    <detail>
                      <summary>&#128273; **date** : (date)</summary>

                      Game date
                    </detail>
                    <detail>
                      <summary>&#128273; **double_header** : (char(1))</summary>

                      Number of game:
 "0" -- a single game
 "1" -- the first game of a double (or triple) header
        including separate admission doubleheaders
 "2" -- the second game of a double (or triple) header
        including separate admission doubleheaders
 "3" -- the third game of a triple-header
 "A" -- the first game of a double-header involving 3 teams
 "B" -- the second game of a double-header involving 3 teams
 
                    </detail>
                    <detail>
                      <summary>&#128273; **visiting_team** : (char(3))</summary>

                      Visiting team ID
                    </detail>
                    <detail>
                      <summary>&#128273; **home_team** : (char(3))</summary>

                      Home team ID
                    </detail>
                    <detail>
                      <summary>**day_of_week** : (char(3))</summary>

                      Day of week (3 char abbreviation)
                    </detail>
                    <detail>
                      <summary>**visiting_team_league** : (char(2))</summary>

                      Away team league ID
                    </detail>
                    <detail>
                      <summary>**visiting_team_game_number** : (smallint)</summary>

                      Away team game number
                    </detail>
                    <detail>
                      <summary>**home_team_league** : (char(2))</summary>

                      Home team league ID
                    </detail>
                    <detail>
                      <summary>**home_team_game_number** : (smallint)</summary>

                      Home team game number
                    </detail>
                    <detail>
                      <summary>**visitor_runs_scored** : (smallint)</summary>

                      Away team runs scored
                    </detail>
                    <detail>
                      <summary>**home_runs_score** : (smallint)</summary>

                      Home team runs scored
                    </detail>
                    <detail>
                      <summary>**length_in_outs** : (smallint)</summary>

                      Game length in outs
                    </detail>
                    <detail>
                      <summary>**day_night** : (char(1))</summary>

                      D - day game, N - night game
                    </detail>
                    <detail>
                      <summary>**completion_info** : (varchar(23))</summary>

                      Completion information.  If the game was completed at a
later date (either due to a suspension or an upheld protest)
this field will include:
    "yyyymmdd,park,vs,hs,len" Where
yyyymmdd -- the date the game was completed
park -- the park ID where the game was completed
vs -- the visitor score at the time of interruption
hs -- the home score at the time of interruption
len -- the length of the game in outs at time of interruption
All the rest of the information in the record refers to the
entire game.
                    </detail>
                    <detail>
                      <summary>**forfeit_info** : (varchar(3))</summary>

                      V - forfeited to away team, H - forfeited to home team, T - ruled a no-decision
                    </detail>
                    <detail>
                      <summary>**protest_info** : (varchar(3))</summary>

                      P - protested by unidentified team, V - disallowed protest by away team, H - disallowed protest by home team, X - upheld protest by away team, Y - upheld protest by home team
                    </detail>
                    <detail>
                      <summary>**park_id** : (char(5))</summary>

                      Park ID
                    </detail>
                    <detail>
                      <summary>**attendance** : (integer)</summary>

                      Attendance
                    </detail>
                    <detail>
                      <summary>**duration** : (smallint)</summary>

                      Time of game in minutes
                    </detail>
                    <detail>
                      <summary>**vistor_line_score** : (varchar(26))</summary>

                      Away team line score, e.g. 010000(10)0x
                    </detail>
                    <detail>
                      <summary>**home_line_score** : (varchar(26))</summary>

                      Home team line score, e.g. 010000(10)0x
                    </detail>
                    <detail>
                      <summary>**visitor_ab** : (smallint)</summary>

                      Away team at bats
                    </detail>
                    <detail>
                      <summary>**visitor_h** : (smallint)</summary>

                      Away team hits
                    </detail>
                    <detail>
                      <summary>**visitor_d** : (smallint)</summary>

                      Away team doubles
                    </detail>
                    <detail>
                      <summary>**visitor_t** : (smallint)</summary>

                      Away team triples
                    </detail>
                    <detail>
                      <summary>**visitor_hr** : (smallint)</summary>

                      Away team home runs
                    </detail>
                    <detail>
                      <summary>**visitor_rbi** : (smallint)</summary>

                      Away team runs batted in
                    </detail>
                    <detail>
                      <summary>**visitor_sh** : (smallint)</summary>

                      Away team sacrifice hits (may include sac flies before 1954)
                    </detail>
                    <detail>
                      <summary>**visitor_sf** : (smallint)</summary>

                      Away team sacrifice flies (since 1954)
                    </detail>
                    <detail>
                      <summary>**visitor_hbp** : (smallint)</summary>

                      Away team hit by pitches
                    </detail>
                    <detail>
                      <summary>**visitor_bb** : (smallint)</summary>

                      Away team walks
                    </detail>
                    <detail>
                      <summary>**visitor_ibb** : (smallint)</summary>

                      Away team intentional walks
                    </detail>
                    <detail>
                      <summary>**visitor_k** : (smallint)</summary>

                      Away team strikeouts
                    </detail>
                    <detail>
                      <summary>**visitor_sb** : (smallint)</summary>

                      Away team stolen bases
                    </detail>
                    <detail>
                      <summary>**visitor_cs** : (smallint)</summary>

                      Away team caught stealing
                    </detail>
                    <detail>
                      <summary>**visitor_gdp** : (smallint)</summary>

                      Away team grounded into double plays
                    </detail>
                    <detail>
                      <summary>**visitor_ci** : (smallint)</summary>

                      Away team reached on interference
                    </detail>
                    <detail>
                      <summary>**visitor_lob** : (smallint)</summary>

                      Away team left on base
                    </detail>
                    <detail>
                      <summary>**visitor_pitchers** : (smallint)</summary>

                      Away team pitchers used
                    </detail>
                    <detail>
                      <summary>**visitor_er** : (smallint)</summary>

                      Away team individual earned runs allowed
                    </detail>
                    <detail>
                      <summary>**visitor_ter** : (smallint)</summary>

                      Away team team earned runs allowed
                    </detail>
                    <detail>
                      <summary>**visitor_wp** : (smallint)</summary>

                      Away team wild pitches allowed
                    </detail>
                    <detail>
                      <summary>**visitor_balks** : (smallint)</summary>

                      Away team balks allowed
                    </detail>
                    <detail>
                      <summary>**visitor_po** : (smallint)</summary>

                      Away team putouts
                    </detail>
                    <detail>
                      <summary>**visitor_a** : (smallint)</summary>

                      Away team assists
                    </detail>
                    <detail>
                      <summary>**visitor_e** : (smallint)</summary>

                      Away team errors
                    </detail>
                    <detail>
                      <summary>**visitor_passed** : (smallint)</summary>

                      Away team passed balls
                    </detail>
                    <detail>
                      <summary>**visitor_db** : (smallint)</summary>

                      Away team double plays turned
                    </detail>
                    <detail>
                      <summary>**visitor_tp** : (smallint)</summary>

                      Away team triple plays turned
                    </detail>
                    <detail>
                      <summary>**home_ab** : (smallint)</summary>

                      Home team at bats
                    </detail>
                    <detail>
                      <summary>**home_h** : (smallint)</summary>

                      Home team hits
                    </detail>
                    <detail>
                      <summary>**home_d** : (smallint)</summary>

                      Home team doubles
                    </detail>
                    <detail>
                      <summary>**home_t** : (smallint)</summary>

                      Home team triples
                    </detail>
                    <detail>
                      <summary>**home_hr** : (smallint)</summary>

                      Home team home runs
                    </detail>
                    <detail>
                      <summary>**home_rbi** : (smallint)</summary>

                      Home team runs batted in
                    </detail>
                    <detail>
                      <summary>**home_sh** : (smallint)</summary>

                      Home team sacrifice hits (may include sac flies before 1954)
                    </detail>
                    <detail>
                      <summary>**home_sf** : (smallint)</summary>

                      Home team sacrifice flies (since 1954)
                    </detail>
                    <detail>
                      <summary>**home_hbp** : (smallint)</summary>

                      Home team hit by pitches
                    </detail>
                    <detail>
                      <summary>**home_bb** : (smallint)</summary>

                      Home team walks
                    </detail>
                    <detail>
                      <summary>**home_ibb** : (smallint)</summary>

                      Home team intentional walks
                    </detail>
                    <detail>
                      <summary>**home_k** : (smallint)</summary>

                      Home team strikeouts
                    </detail>
                    <detail>
                      <summary>**home_sb** : (smallint)</summary>

                      Home team stolen bases
                    </detail>
                    <detail>
                      <summary>**home_cs** : (smallint)</summary>

                      Home team caught stealing
                    </detail>
                    <detail>
                      <summary>**home_gdp** : (smallint)</summary>

                      Home team grounded into double plays
                    </detail>
                    <detail>
                      <summary>**home_ci** : (smallint)</summary>

                      Home team reached on interference
                    </detail>
                    <detail>
                      <summary>**home_lob** : (smallint)</summary>

                      Home team left on base
                    </detail>
                    <detail>
                      <summary>**home_pitchers** : (smallint)</summary>

                      Home team pitchers used
                    </detail>
                    <detail>
                      <summary>**home_er** : (smallint)</summary>

                      Home team individual earned runs allowed
                    </detail>
                    <detail>
                      <summary>**home_ter** : (smallint)</summary>

                      Home team team earned runs allowed
                    </detail>
                    <detail>
                      <summary>**home_wp** : (smallint)</summary>

                      Home team wild pitches allowed
                    </detail>
                    <detail>
                      <summary>**home_balks** : (smallint)</summary>

                      Home team balks allowed
                    </detail>
                    <detail>
                      <summary>**home_po** : (smallint)</summary>

                      Home team putouts
                    </detail>
                    <detail>
                      <summary>**home_a** : (smallint)</summary>

                      Home team assists
                    </detail>
                    <detail>
                      <summary>**home_e** : (smallint)</summary>

                      Home team errors
                    </detail>
                    <detail>
                      <summary>**home_passed** : (smallint)</summary>

                      Home team passed balls
                    </detail>
                    <detail>
                      <summary>**home_db** : (smallint)</summary>

                      Home team double plays turned
                    </detail>
                    <detail>
                      <summary>**home_tp** : (smallint)</summary>

                      Home team triple plays turned
                    </detail>
                    <detail>
                      <summary>**umpire_h_id** : (char(8))</summary>

                      Home plate umpire ID
                    </detail>
                    <detail>
                      <summary>**umpire_h_name** : (varchar(32))</summary>

                      Home plate umpire name
                    </detail>
                    <detail>
                      <summary>**umpire_1b_id** : (char(8))</summary>

                      First base umpire ID
                    </detail>
                    <detail>
                      <summary>**umpire_1b_name** : (varchar(32))</summary>

                      First base umpire name
                    </detail>
                    <detail>
                      <summary>**umpire_2b_id** : (char(8))</summary>

                      Second base umpire ID
                    </detail>
                    <detail>
                      <summary>**umpire_2b_name** : (varchar(32))</summary>

                      Second base umpire name
                    </detail>
                    <detail>
                      <summary>**umpire_3b_id** : (char(8))</summary>

                      Third base umpire ID
                    </detail>
                    <detail>
                      <summary>**umpire_3b_name** : (varchar(32))</summary>

                      Third base umpire name
                    </detail>
                    <detail>
                      <summary>**umpire_lf_id** : (char(8))</summary>

                      Left field umpire ID
                    </detail>
                    <detail>
                      <summary>**umpire_lf_name** : (varchar(32))</summary>

                      Left field umpire name
                    </detail>
                    <detail>
                      <summary>**umpire_rf_id** : (char(8))</summary>

                      Right field umpire ID
                    </detail>
                    <detail>
                      <summary>**umpire_rf_name** : (varchar(32))</summary>

                      Right field umpire name
                    </detail>
                    <detail>
                      <summary>**visitor_manager_id** : (char(8))</summary>

                      Away team manager ID
                    </detail>
                    <detail>
                      <summary>**visitor_manager_name** : (varchar(32))</summary>

                      Away team manager name
                    </detail>
                    <detail>
                      <summary>**home_manager_id** : (char(8))</summary>

                      Home team manager ID
                    </detail>
                    <detail>
                      <summary>**home_manager_name** : (varchar(32))</summary>

                      Home team manager name
                    </detail>
                    <detail>
                      <summary>**winning_pitcher_id** : (char(8))</summary>

                      Winning pitcher ID
                    </detail>
                    <detail>
                      <summary>**winning_pitcher_name** : (varchar(32))</summary>

                      Winning pitcher name
                    </detail>
                    <detail>
                      <summary>**losing_pitcher_id** : (char(8))</summary>

                      Losing pitcher ID
                    </detail>
                    <detail>
                      <summary>**losing_pitcher_name** : (varchar(32))</summary>

                      Losing pitcher name
                    </detail>
                    <detail>
                      <summary>**saving_pitcher_id** : (char(8))</summary>

                      Saving pitcher ID
                    </detail>
                    <detail>
                      <summary>**saving_pitcher_name** : (varchar(32))</summary>

                      Saving pitcher name
                    </detail>
                    <detail>
                      <summary>**game_winning_rbi_id** : (char(8))</summary>

                      Game-winning RBI ID
                    </detail>
                    <detail>
                      <summary>**game_winning_rbi_name** : (varchar(32))</summary>

                      Game-winning RBI name
                    </detail>
                    <detail>
                      <summary>**visitor_starting_pitcher_id** : (char(8))</summary>

                      Away team starting pitcher ID
                    </detail>
                    <detail>
                      <summary>**visitor_starting_pitcher_name** : (varchar(32))</summary>

                      Away team starting pitcher name
                    </detail>
                    <detail>
                      <summary>**home_starting_pitcher_id** : (char(8))</summary>

                      Home team starting pitcher ID
                    </detail>
                    <detail>
                      <summary>**home_starting_pitcher_name** : (varchar(32))</summary>

                      Home team starting pitcher name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_1_player_id** : (char(8))</summary>

                      Away team lineup slot 1 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_1_name** : (varchar(32))</summary>

                      Away team lineup slot 1 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_1_position** : (smallint)</summary>

                      Away team lineup slot 1 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_2_player_id** : (char(8))</summary>

                      Away team lineup slot 2 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_2_name** : (varchar(32))</summary>

                      Away team lineup slot 2 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_2_position** : (smallint)</summary>

                      Away team lineup slot 2 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_3_player_id** : (char(8))</summary>

                      Away team lineup slot 3 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_3_name** : (varchar(32))</summary>

                      Away team lineup slot 3 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_3_position** : (smallint)</summary>

                      Away team lineup slot 3 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_4_player_id** : (char(8))</summary>

                      Away team lineup slot 4 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_4_name** : (varchar(32))</summary>

                      Away team lineup slot 4 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_4_position** : (smallint)</summary>

                      Away team lineup slot 4 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_5_player_id** : (char(8))</summary>

                      Away team lineup slot 5 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_5_name** : (varchar(32))</summary>

                      Away team lineup slot 5 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_5_position** : (smallint)</summary>

                      Away team lineup slot 5 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_6_player_id** : (char(8))</summary>

                      Away team lineup slot 6 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_6_name** : (varchar(32))</summary>

                      Away team lineup slot 6 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_6_position** : (smallint)</summary>

                      Away team lineup slot 6 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_7_player_id** : (char(8))</summary>

                      Away team lineup slot 7 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_7_name** : (varchar(32))</summary>

                      Away team lineup slot 7 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_7_position** : (smallint)</summary>

                      Away team lineup slot 7 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_8_player_id** : (char(8))</summary>

                      Away team lineup slot 8 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_8_name** : (varchar(32))</summary>

                      Away team lineup slot 8 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_8_position** : (smallint)</summary>

                      Away team lineup slot 8 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**visitor_batting_9_player_id** : (char(8))</summary>

                      Away team lineup slot 9 starting player ID
                    </detail>
                    <detail>
                      <summary>**visitor_batting_9_name** : (varchar(32))</summary>

                      Away team lineup slot 9 starting player name
                    </detail>
                    <detail>
                      <summary>**visitor_batting_9_position** : (smallint)</summary>

                      Away team lineup slot 9 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_1_player_id** : (char(8))</summary>

                      Home team lineup slot 1 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_1_name** : (varchar(32))</summary>

                      Home team lineup slot 1 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_1_position** : (smallint)</summary>

                      Home team lineup slot 1 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_2_player_id** : (char(8))</summary>

                      Home team lineup slot 2 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_2_name** : (varchar(32))</summary>

                      Home team lineup slot 2 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_2_position** : (smallint)</summary>

                      Home team lineup slot 2 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_3_player_id** : (char(8))</summary>

                      Home team lineup slot 3 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_3_name** : (varchar(32))</summary>

                      Home team lineup slot 3 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_3_position** : (smallint)</summary>

                      Home team lineup slot 3 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_4_player_id** : (char(8))</summary>

                      Home team lineup slot 4 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_4_name** : (varchar(32))</summary>

                      Home team lineup slot 4 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_4_position** : (smallint)</summary>

                      Home team lineup slot 4 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_5_player_id** : (char(8))</summary>

                      Home team lineup slot 5 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_5_name** : (varchar(32))</summary>

                      Home team lineup slot 5 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_5_position** : (smallint)</summary>

                      Home team lineup slot 5 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_6_player_id** : (char(8))</summary>

                      Home team lineup slot 6 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_6_name** : (varchar(32))</summary>

                      Home team lineup slot 6 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_6_position** : (smallint)</summary>

                      Home team lineup slot 6 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_7_player_id** : (char(8))</summary>

                      Home team lineup slot 7 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_7_name** : (varchar(32))</summary>

                      Home team lineup slot 7 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_7_position** : (smallint)</summary>

                      Home team lineup slot 7 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_8_player_id** : (char(8))</summary>

                      Home team lineup slot 8 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_8_name** : (varchar(32))</summary>

                      Home team lineup slot 8 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_8_position** : (smallint)</summary>

                      Home team lineup slot 8 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**home_batting_9_player_id** : (char(8))</summary>

                      Home team lineup slot 9 starting player ID
                    </detail>
                    <detail>
                      <summary>**home_batting_9_name** : (varchar(32))</summary>

                      Home team lineup slot 9 starting player name
                    </detail>
                    <detail>
                      <summary>**home_batting_9_position** : (smallint)</summary>

                      Home team lineup slot 9 starting player fielding position
                    </detail>
                    <detail>
                      <summary>**additional_info** : (varchar(128))</summary>

                      Additional information.  This is a grab-bag of informational
      items that might not warrant a field on their own.  The field
      is alpha-numeric. Some items are represented by tokens such as:
         "HTBF" -- home team batted first.
         Note: if "HTBF" is specified it would be possible to see
         something like "01002000x" in the visitor's line score.
      Changes in umpire positions during a game will also appear in
      this field.  These will be in the form:
         umpchange,inning,umpPosition,umpid with the latter three
         repeated for each umpire.
      These changes occur with umpire injuries, late arrival of
      umpires or changes from completion of suspended games. Details
      of suspended games are in field `completion_information`.
                    </detail>
                    <detail>
                      <summary>**acquisition_info** : (char(1))</summary>

                      Y - complete game information, N - no game information, D - game derived from box score and game story, P - portions of game information
                    </detail>
            ### park
                    <detail>
                      <summary>&#128273; **park_id** : (char(5))</summary>

                      Park ID
                    </detail>
                    <detail>
                      <summary>**name** : (varchar(41))</summary>

                      Park name
                    </detail>
                    <detail>
                      <summary>**aka** : (varchar(55))</summary>

                      Common park alias
                    </detail>
                    <detail>
                      <summary>**city** : (varchar(17))</summary>

                      City
                    </detail>
                    <detail>
                      <summary>**state** : (varchar(9))</summary>

                      State
                    </detail>
                    <detail>
                      <summary>**start_date** : (varchar(10))</summary>

                      First game
                    </detail>
                    <detail>
                      <summary>**end_date** : (varchar(10))</summary>

                      Last game
                    </detail>
                    <detail>
                      <summary>**league** : (char(2))</summary>

                      League ID
                    </detail>
                    <detail>
                      <summary>**notes** : (varchar(54))</summary>

                      Misc. notes
                    </detail>
            ### roster
                    <detail>
                      <summary>&#128273; **year** : (integer)</summary>

                      Year of roster
                    </detail>
                    <detail>
                      <summary>&#128273; **player_id** : (char(8))</summary>

                      Player ID
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (char(3))</summary>

                      Team ID
                    </detail>
                    <detail>
                      <summary>&#128273; **position** : (varchar(2))</summary>

                      Primary fielding position
                    </detail>
                    <detail>
                      <summary>**last_name** : (varchar(32))</summary>

                      Player last name
                    </detail>
                    <detail>
                      <summary>**first_name** : (varchar(32))</summary>

                      Player first name
                    </detail>
                    <detail>
                      <summary>**bats** : (char(1))</summary>

                      Bat handedness
                    </detail>
                    <detail>
                      <summary>**throws** : (char(1))</summary>

                      Throw handedness
                    </detail>
            ### schedule
                    <detail>
                      <summary>&#128273; **date** : (date)</summary>

                      Scheduled game date
                    </detail>
                    <detail>
                      <summary>&#128273; **home_team** : (char(3))</summary>

                      Home team ID
                    </detail>
                    <detail>
                      <summary>&#128273; **home_team_game_number** : (integer)</summary>

                      Home team game number
                    </detail>
                    <detail>
                      <summary>**double_header** : (smallint)</summary>

                      Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
                    </detail>
                    <detail>
                      <summary>**day_of_week** : (char(3))</summary>

                      Day of week (3 letter abbreviation
                    </detail>
                    <detail>
                      <summary>**visiting_team** : (char(3))</summary>

                      Away team ID
                    </detail>
                    <detail>
                      <summary>**visiting_team_league** : (char(2))</summary>

                      Away team league ID
                    </detail>
                    <detail>
                      <summary>**visiting_team_game_number** : (smallint)</summary>

                      Away team game number
                    </detail>
                    <detail>
                      <summary>**home_team_league** : (char(2))</summary>

                      Home team league ID
                    </detail>
                    <detail>
                      <summary>**day_night** : (char(1))</summary>

                      D - day, N - night
                    </detail>
                    <detail>
                      <summary>**postponement_indicator** : (varchar(120))</summary>

                      This field will contain one or more phrases related to the game if it was
not played as scheduled. If there is more than one phrase, they are separated
by a semi-colon (";"). There are three possible outcomes for games not played
on the originally scheduled date:
-- The game was played on another date
-- The game was played on the original date but at another site
-- The game was not played
                    </detail>
                    <detail>
                      <summary>**makeup_dates** : (varchar(120))</summary>

                      This field will contain a makeup date if the postponed game was played at
another time or place. If an attempt was known to have been made on a date but
postponed again, that date will be listed. In that case, there will be a second
date for the date when the game was actually played, in this form: "20150428;
20150528" For the note about a team folding, the team code is one of the
standard Retrosheet team IDs. The same is true for the team played as note.
Often, the two of these are combined in one field.
                    </detail>
            ### sub
                    <detail>
                      <summary>&#128273; **dummy_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**game_id** : (char(12))</summary>

                      Game ID (home team ID + YYYYMMDD + doubleheader flag
                    </detail>
                    <detail>
                      <summary>**inn_ct** : (smallint)</summary>

                      Inning of substitution
                    </detail>
                    <detail>
                      <summary>**bat_home_id** : (smallint)</summary>

                      Is home team batting (-1 for N/A)
                    </detail>
                    <detail>
                      <summary>**sub_id** : (char(8))</summary>

                      Player ID of substitute
                    </detail>
                    <detail>
                      <summary>**sub_home_id** : (boolean)</summary>

                      Is the home team making the substitution
                    </detail>
                    <detail>
                      <summary>**sub_lineup_id** : (smallint)</summary>

                      Lineup position of substitution
                    </detail>
                    <detail>
                      <summary>**sub_fld_cd** : (smallint)</summary>

                      Fielding position of substitution
                    </detail>
                    <detail>
                      <summary>**removed_id** : (char(8))</summary>

                      ID of removed player
                    </detail>
                    <detail>
                      <summary>**removed_fld_cd** : (smallint)</summary>

                      Fielding position of removed player
                    </detail>
                    <detail>
                      <summary>**event_id** : (smallint)</summary>

                      Event number in which substitution occurred
                    </detail>
    ## baseballdatabank
            ### allstar_full
                    <detail>
                      <summary>&#128273; **dummy_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**game_num** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**game_id** : (varchar(12))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**starting_pos** : (smallint)</summary>

                      
                    </detail>
            ### appearances
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_all** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_batting** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_defense** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_p** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_c** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_1b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_2b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_3b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_ss** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_lf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_cf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_rf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_of** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_dh** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_ph** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_pr** : (smallint)</summary>

                      
                    </detail>
            ### awards_managers
                    <detail>
                      <summary>&#128273; **dummy_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**player_id** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**award_id** : (varchar(75))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**tie** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**notes** : (varchar(100))</summary>

                      
                    </detail>
            ### awards_players
                    <detail>
                      <summary>&#128273; **dummy_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**award_id** : (varchar(255))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**tie** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**notes** : (varchar(100))</summary>

                      
                    </detail>
            ### awards_share_managers
                    <detail>
                      <summary>&#128273; **award_id** : (varchar(25))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**points_won** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**points_max** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**votes_first** : (integer)</summary>

                      
                    </detail>
            ### awards_share_players
                    <detail>
                      <summary>&#128273; **award_id** : (varchar(25))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**points_won** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**points_max** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**votes_first** : (float)</summary>

                      
                    </detail>
            ### batting
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **stint** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ab** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**r** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**h** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**_2b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**_3b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hr** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**rbi** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**so** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ibb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hbp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sh** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gidp** : (smallint)</summary>

                      
                    </detail>
            ### batting_post
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **round** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ab** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**r** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**h** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**_2b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**_3b** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hr** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**rbi** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**so** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ibb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hbp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sh** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gidp** : (smallint)</summary>

                      
                    </detail>
            ### college_playing
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **school_id** : (varchar(15))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
            ### fielding
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **stint** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **pos** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**inn_outs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**po** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**a** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**e** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**dp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**pb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**wp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**zr** : (float)</summary>

                      
                    </detail>
            ### fielding_of
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **stint** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_lf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_cf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_rf** : (smallint)</summary>

                      
                    </detail>
            ### fielding_of_split
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **stint** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **pos** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**inn_outs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**po** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**a** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**e** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**dp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**pb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**wp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**zr** : (float)</summary>

                      
                    </detail>
            ### fielding_post
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **round** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **pos** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**inn_outs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**po** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**a** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**e** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**dp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**tp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**pb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cs** : (smallint)</summary>

                      
                    </detail>
            ### hall_of_fame
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **voted_by** : (varchar(64))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ballots** : (varchar(64))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**needed** : (varchar(64))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**votes** : (varchar(64))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**inducted** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**category** : (varchar(20))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**needed_note** : (varchar(25))</summary>

                      
                    </detail>
            ### home_games
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **park_id** : (varchar(5))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**first_game** : (date)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**last_game** : (date)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**games** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**openings** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**attendance** : (integer)</summary>

                      
                    </detail>
            ### managers
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **inseason** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**player_id** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**w** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**l** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**rank** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**plyr_mgr** : (varchar(1))</summary>

                      
                    </detail>
            ### managers_half
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **half** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**inseason** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**w** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**l** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**rank** : (smallint)</summary>

                      
                    </detail>
            ### parks
                    <detail>
                      <summary>&#128273; **park_id** : (varchar(5))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**park_name** : (varchar(40))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**park_alias** : (varchar(55))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**city** : (varchar(25))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**state** : (varchar(16))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**country** : (varchar(2))</summary>

                      
                    </detail>
            ### people
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**birth_year** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**birth_month** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**birth_day** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**birth_country** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**birth_state** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**birth_city** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**death_year** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**death_month** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**death_day** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**death_country** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**death_state** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**death_city** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**name_first** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**name_last** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**name_given** : (varchar(255))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**weight** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**height** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bats** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**throws** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**debut** : (date)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**final_game** : (date)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**retro_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bbref_id** : (varchar(9))</summary>

                      
                    </detail>
            ### pitching
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **stint** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**w** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**l** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cg** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sho** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sv** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ip_outs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**h** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**er** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hr** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**so** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ba_opp** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**era** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ibb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**wp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hbp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bk** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bfp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**r** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sh** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gidp** : (smallint)</summary>

                      
                    </detail>
            ### pitching_post
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **round** : (varchar(10))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**w** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**l** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cg** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sho** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sv** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ip_outs** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**h** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**er** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hr** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**so** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ba_opp** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**era** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ibb** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**wp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hbp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bk** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bfp** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**r** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sh** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sf** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**gidp** : (smallint)</summary>

                      
                    </detail>
            ### salaries
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **player_id** : (varchar(9))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**salary** : (float)</summary>

                      
                    </detail>
            ### schools
                    <detail>
                      <summary>&#128273; **school_id** : (varchar(15))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**name_full** : (varchar(255))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**city** : (varchar(55))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**state** : (varchar(55))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**country** : (varchar(55))</summary>

                      
                    </detail>
            ### series_post
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **round** : (varchar(5))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id_winner** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id_winner** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id_loser** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_id_loser** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**wins** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**losses** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ties** : (smallint)</summary>

                      
                    </detail>
            ### teams
                    <detail>
                      <summary>&#128273; **year_id** : (smallint)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**franch_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**div_id** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**rank** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g_home** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**w** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**l** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**div_win** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**wc_win** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**lg_win** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ws_win** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**r** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ab** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**h** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**_2b** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**_3b** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hr** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bb** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**so** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sb** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cs** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hbp** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sf** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ra** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**er** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**era** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**cg** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sho** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**sv** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ip_outs** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**h_a** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**hr_a** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bb_a** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**so_a** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**e** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**dp** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**fp** : (float)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**name** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**park** : (varchar(255))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**attendance** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**bpf** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**ppf** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id_br** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id_lahman45** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**team_id_retro** : (varchar(3))</summary>

                      
                    </detail>
            ### teams_franchises
                    <detail>
                      <summary>&#128273; **franch_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**franch_name** : (varchar(50))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**active** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**na_assoc** : (varchar(3))</summary>

                      
                    </detail>
            ### teams_half
                    <detail>
                      <summary>&#128273; **year_id** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **lg_id** : (varchar(2))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **team_id** : (varchar(3))</summary>

                      
                    </detail>
                    <detail>
                      <summary>&#128273; **half** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**div_id** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**div_win** : (varchar(1))</summary>

                      
                    </detail>
                    <detail>
                      <summary>**rank** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**g** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**w** : (integer)</summary>

                      
                    </detail>
                    <detail>
                      <summary>**l** : (integer)</summary>

                      
                    </detail>