# retrosheet
## code_event
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## code_field_park
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## code_method_record
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## code_pitches_record
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## code_precip_park
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## code_sky_park
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## code_wind_direction_park
### **code**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### description
- Type: VARCHAR(30)
- Description: No description
## comment
### **dummy_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### game_id
- Type: CHAR(12)
- Description: Game ID (home team ID + YYYYMMDD + doubleheader flag
### event_id
- Type: SMALLINT
- Description: Commented event number
### comment
- Type: VARCHAR(1638)
- Description: Comment text
### ejected_person_id
- Type: VARCHAR(256)
- Description: ID of ejected person
### ejected_person_role_cd
- Type: VARCHAR(256)
- Description: No description
### eject_umpire_id
- Type: VARCHAR(256)
- Description: ID of umpire who ejected person
### eject_reason
- Type: VARCHAR(1639)
- Description: No description
### umpchange_inning
- Type: VARCHAR(256)
- Description: No description
### umpchange_position
- Type: VARCHAR(256)
- Description: No description
### umpchange_person_id
- Type: VARCHAR(256)
- Description: ID of new umpire
## daily
### **dummy_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### game_id
- Type: CHAR(12)
- Description: Game ID (home team ID + YYYYMMDD + doubleheader flag
### game_dt
- Type: DATE
- Description: Game date
### game_ct
- Type: SMALLINT
- Description: Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
### appearance_dt
- Type: DATE
- Description: Player appearance date. Can be different from game date if the game was suspended and the player entered the game at the later date
### team_id
- Type: CHAR(3)
- Description: Team ID of player
### player_id
- Type: CHAR(8)
- Description: Player ID
### slot_ct
- Type: SMALLINT
- Description: Player lineup position
### seq_ct
- Type: SMALLINT
- Description: Player is nth person of game to play in that lineup slot
### home_fl
- Type: BOOLEAN
- Description: Player is playing at home
### opponent_id
- Type: CHAR(3)
- Description: Team opponent ID
### park_id
- Type: CHAR(5)
- Description: Park ID
### b_g
- Type: SMALLINT
- Description: Games played
### b_pa
- Type: SMALLINT
- Description: Plate appearances
### b_ab
- Type: SMALLINT
- Description: At bats
### b_r
- Type: SMALLINT
- Description: Runs scored
### b_h
- Type: SMALLINT
- Description: Hits
### b_tb
- Type: SMALLINT
- Description: Total bases
### b_2b
- Type: SMALLINT
- Description: Doubles
### b_3b
- Type: SMALLINT
- Description: Triples
### b_hr
- Type: SMALLINT
- Description: Home runs
### b_hr4
- Type: SMALLINT
- Description: Grand slams
### b_rbi
- Type: SMALLINT
- Description: Runs batted in
### b_gw
- Type: SMALLINT
- Description: Game winning RBI
### b_bb
- Type: SMALLINT
- Description: Walks
### b_ibb
- Type: SMALLINT
- Description: Intentional walks
### b_so
- Type: SMALLINT
- Description: Strikeouts
### b_gdp
- Type: SMALLINT
- Description: Grounded into double plays
### b_hp
- Type: SMALLINT
- Description: Hit by pitches
### b_sh
- Type: SMALLINT
- Description: Sacrifice hits
### b_sf
- Type: SMALLINT
- Description: Sacrifice files
### b_sb
- Type: SMALLINT
- Description: Stolen bases
### b_cs
- Type: SMALLINT
- Description: Caught stealing
### b_xi
- Type: SMALLINT
- Description: Reached on interference
### b_g_dh
- Type: SMALLINT
- Description: Games as DH
### b_g_ph
- Type: SMALLINT
- Description: Games as pinch hitter
### b_g_pr
- Type: SMALLINT
- Description: Games as pinch runner
### p_g
- Type: SMALLINT
- Description: Games pitched
### p_gs
- Type: SMALLINT
- Description: Games as starting pitcher
### p_cg
- Type: SMALLINT
- Description: Complete games
### p_sho
- Type: SMALLINT
- Description: Shutouts
### p_gf
- Type: SMALLINT
- Description: Games finished
### p_w
- Type: SMALLINT
- Description: Wins
### p_l
- Type: SMALLINT
- Description: Losses
### p_sv
- Type: SMALLINT
- Description: Saves
### p_out
- Type: SMALLINT
- Description: Outs recorded
### p_tbf
- Type: SMALLINT
- Description: Total batters faced
### p_ab
- Type: SMALLINT
- Description: At bats against
### p_r
- Type: SMALLINT
- Description: Runs allowed
### p_er
- Type: SMALLINT
- Description: Earned runs allowed
### p_h
- Type: SMALLINT
- Description: Hits allowed
### p_tb
- Type: SMALLINT
- Description: Total bases allowed
### p_2b
- Type: SMALLINT
- Description: Doubles allowed
### p_3b
- Type: SMALLINT
- Description: Triples allowed
### p_hr
- Type: SMALLINT
- Description: Home runs allowed
### p_hr4
- Type: SMALLINT
- Description: Grand slams allowed
### p_bb
- Type: SMALLINT
- Description: Walks allowed
### p_ibb
- Type: SMALLINT
- Description: Intentional walks allowed
### p_so
- Type: SMALLINT
- Description: Strikeouts against
### p_gdp
- Type: SMALLINT
- Description: Grounded into double plays against
### p_hp
- Type: SMALLINT
- Description: Hit by pitches allowed
### p_sh
- Type: SMALLINT
- Description: Sacrifice hits allowed
### p_sf
- Type: SMALLINT
- Description: Sacrifice flies allowed
### p_xi
- Type: SMALLINT
- Description: Reached on interference allowed
### p_wp
- Type: SMALLINT
- Description: Wild pitches allowed
### p_bk
- Type: SMALLINT
- Description: Balks allowed
### p_ir
- Type: SMALLINT
- Description: Inherited runners
### p_irs
- Type: SMALLINT
- Description: Inherited runners scored
### p_go
- Type: SMALLINT
- Description: Groundouts recorded
### p_ao
- Type: SMALLINT
- Description: Fly ball outs recorded
### p_pitch
- Type: SMALLINT
- Description: Pitches thrown
### p_strike
- Type: SMALLINT
- Description: Strikes thrown
### f_p_g
- Type: SMALLINT
- Description: Appearances at pitcher
### f_p_gs
- Type: SMALLINT
- Description: Starts at pitcher
### f_p_out
- Type: SMALLINT
- Description: Outs played as pitcher
### f_p_tc
- Type: SMALLINT
- Description: Total chances as pitcher
### f_p_po
- Type: SMALLINT
- Description: Putouts as pitcher
### f_p_a
- Type: SMALLINT
- Description: Assists as pitcher
### f_p_e
- Type: SMALLINT
- Description: Errors as pitcher
### f_p_dp
- Type: SMALLINT
- Description: Double plays turned as pitcher
### f_p_tp
- Type: SMALLINT
- Description: Triple pays turned as pitcher
### f_c_g
- Type: SMALLINT
- Description: Appearances at catcher
### f_c_gs
- Type: SMALLINT
- Description: Starts at catcher
### f_c_out
- Type: SMALLINT
- Description: Outs played as catcher
### f_c_tc
- Type: SMALLINT
- Description: Total chances as catcher
### f_c_po
- Type: SMALLINT
- Description: Putouts as catcher
### f_c_a
- Type: SMALLINT
- Description: Assists as catcher
### f_c_e
- Type: SMALLINT
- Description: Errors as catcher
### f_c_dp
- Type: SMALLINT
- Description: Double plays turned as catcher
### f_c_tp
- Type: SMALLINT
- Description: Triple pays turned as catcher
### f_c_pb
- Type: SMALLINT
- Description: Passed balls
### f_c_xi
- Type: SMALLINT
- Description: Catcher's interference
### f_1b_g
- Type: SMALLINT
- Description: Appearances at first baseman
### f_1b_gs
- Type: SMALLINT
- Description: Starts at first baseman
### f_1b_out
- Type: SMALLINT
- Description: Outs played as first baseman
### f_1b_tc
- Type: SMALLINT
- Description: Total chances as first baseman
### f_1b_po
- Type: SMALLINT
- Description: Putouts as first baseman
### f_1b_a
- Type: SMALLINT
- Description: Assists as first baseman
### f_1b_e
- Type: SMALLINT
- Description: Errors as first baseman
### f_1b_dp
- Type: SMALLINT
- Description: Double plays turned as first baseman
### f_1b_tp
- Type: SMALLINT
- Description: Triple pays turned as first baseman
### f_2b_g
- Type: SMALLINT
- Description: Appearances at second baseman
### f_2b_gs
- Type: SMALLINT
- Description: Starts at second baseman
### f_2b_out
- Type: SMALLINT
- Description: Outs played as second baseman
### f_2b_tc
- Type: SMALLINT
- Description: Total chances as second baseman
### f_2b_po
- Type: SMALLINT
- Description: Putouts as second baseman
### f_2b_a
- Type: SMALLINT
- Description: Assists as second baseman
### f_2b_e
- Type: SMALLINT
- Description: Errors as second baseman
### f_2b_dp
- Type: SMALLINT
- Description: Double plays turned as second baseman
### f_2b_tp
- Type: SMALLINT
- Description: Triple pays turned as second baseman
### f_3b_g
- Type: SMALLINT
- Description: Appearances at third baseman
### f_3b_gs
- Type: SMALLINT
- Description: Starts at third baseman
### f_3b_out
- Type: SMALLINT
- Description: Outs played as third baseman
### f_3b_tc
- Type: SMALLINT
- Description: Total chances as third baseman
### f_3b_po
- Type: SMALLINT
- Description: Putouts as third baseman
### f_3b_a
- Type: SMALLINT
- Description: Assists as third baseman
### f_3b_e
- Type: SMALLINT
- Description: Errors as third baseman
### f_3b_dp
- Type: SMALLINT
- Description: Double plays turned as third baseman
### f_3b_tp
- Type: SMALLINT
- Description: Triple pays turned as third baseman
### f_ss_g
- Type: SMALLINT
- Description: Appearances at shortstop
### f_ss_gs
- Type: SMALLINT
- Description: Starts at shortstop
### f_ss_out
- Type: SMALLINT
- Description: Outs played as shortstop
### f_ss_tc
- Type: SMALLINT
- Description: Total chances as shortstop
### f_ss_po
- Type: SMALLINT
- Description: Putouts as shortstop
### f_ss_a
- Type: SMALLINT
- Description: Assists as shortstop
### f_ss_e
- Type: SMALLINT
- Description: Errors as shortstop
### f_ss_dp
- Type: SMALLINT
- Description: Double plays turned as shortstop
### f_ss_tp
- Type: SMALLINT
- Description: Triple pays turned as shortstop
### f_lf_g
- Type: SMALLINT
- Description: Appearances at left fielder
### f_lf_gs
- Type: SMALLINT
- Description: Starts at left fielder
### f_lf_out
- Type: SMALLINT
- Description: Outs played as left fielder
### f_lf_tc
- Type: SMALLINT
- Description: Total chances as left fielder
### f_lf_po
- Type: SMALLINT
- Description: Putouts as left fielder
### f_lf_a
- Type: SMALLINT
- Description: Assists as left fielder
### f_lf_e
- Type: SMALLINT
- Description: Errors as left fielder
### f_lf_dp
- Type: SMALLINT
- Description: Double plays turned as left fielder
### f_lf_tp
- Type: SMALLINT
- Description: Triple pays turned as left fielder
### f_cf_g
- Type: SMALLINT
- Description: Appearances at center fielder
### f_cf_gs
- Type: SMALLINT
- Description: Starts at center fielder
### f_cf_out
- Type: SMALLINT
- Description: Outs played as center fielder
### f_cf_tc
- Type: SMALLINT
- Description: Total chances as center fielder
### f_cf_po
- Type: SMALLINT
- Description: Putouts as center fielder
### f_cf_a
- Type: SMALLINT
- Description: Assists as center fielder
### f_cf_e
- Type: SMALLINT
- Description: Errors as center fielder
### f_cf_dp
- Type: SMALLINT
- Description: Double plays turned as center fielder
### f_cf_tp
- Type: SMALLINT
- Description: Triple pays turned as center fielder
### f_rf_g
- Type: SMALLINT
- Description: Appearances at right fielder
### f_rf_gs
- Type: SMALLINT
- Description: Starts at right fielder
### f_rf_out
- Type: SMALLINT
- Description: Outs played as right fielder
### f_rf_tc
- Type: SMALLINT
- Description: Total chances as right fielder
### f_rf_po
- Type: SMALLINT
- Description: Putouts as right fielder
### f_rf_a
- Type: SMALLINT
- Description: Assists as right fielder
### f_rf_e
- Type: SMALLINT
- Description: Errors as right fielder
### f_rf_dp
- Type: SMALLINT
- Description: Double plays turned as right fielder
### f_rf_tp
- Type: SMALLINT
- Description: Triple pays turned as right fielder
## deduced_game
### **game_id**
- Type: CHAR(12)
- Description: Game ID (home team ID + YYYYMMDD + doubleheader flag
- Primary Key: Yes
## event
### **game_id**
- Type: CHAR(12)
- Description: Game ID (home team ID + YYYYMMDD + doubleheader flag
- Primary Key: Yes
### **event_id**
- Type: INTEGER
- Description: Event number of game
- Primary Key: Yes
### away_team_id
- Type: CHAR(3)
- Description: Visiting Team
### inn_ct
- Type: SMALLINT
- Description: Inning
### bat_home_id
- Type: BOOLEAN
- Description: Home team is batting
### outs_ct
- Type: SMALLINT
- Description: Outs (0-2)
### balls_ct
- Type: SMALLINT
- Description: Balls (0-3)
### strikes_ct
- Type: SMALLINT
- Description: Strikes (0-2
### pitch_seq_tx
- Type: VARCHAR(30)
- Description: Pitch sequence
### away_score_ct
- Type: SMALLINT
- Description: Away score
### home_score_ct
- Type: SMALLINT
- Description: Home score
### bat_id
- Type: CHAR(8)
- Description: Batter ID
### bat_hand_cd
- Type: CHAR(1)
- Description: Batter handedness
### resp_bat_id
- Type: CHAR(8)
- Description: ID of batter charged with event
### resp_bat_hand_cd
- Type: CHAR(1)
- Description: Handedness of batter charged with event
### pit_id
- Type: CHAR(8)
- Description: Pitcher ID
### pit_hand_cd
- Type: CHAR(1)
- Description: Pitcher handedness
### resp_pit_id
- Type: CHAR(8)
- Description: ID of pitcher charged with event
### resp_pit_hand_cd
- Type: CHAR(1)
- Description: Handedness of pitcher charged with event
### pos2_fld_id
- Type: CHAR(8)
- Description: Catcher ID
### pos3_fld_id
- Type: CHAR(8)
- Description: First baseman ID
### pos4_fld_id
- Type: CHAR(8)
- Description: Second baseman ID
### pos5_fld_id
- Type: CHAR(8)
- Description: Third baseman ID
### pos6_fld_id
- Type: CHAR(8)
- Description: Shortstop ID
### pos7_fld_id
- Type: CHAR(8)
- Description: Left fielder ID
### pos8_fld_id
- Type: CHAR(8)
- Description: Center fielder ID
### pos9_fld_id
- Type: CHAR(8)
- Description: Right fielder ID
### base1_run_id
- Type: CHAR(8)
- Description: ID of runner on first
### base2_run_id
- Type: CHAR(8)
- Description: ID of runner on second
### base3_run_id
- Type: CHAR(8)
- Description: ID of runner on third
### event_tx
- Type: VARCHAR(128)
- Description: Event text (in scoring shorthand
### leadoff_fl
- Type: BOOLEAN
- Description: Batter is leading off the inning
### ph_fl
- Type: BOOLEAN
- Description: Batter is pinch-hitting
### bat_fld_cd
- Type: SMALLINT
- Description: Defensive position of batter (10 for DH, 11 for PH, 12 for PR
### bat_lineup_id
- Type: SMALLINT
- Description: Lineup position (1-9)
### event_cd
- Type: SMALLINT
- Description: Event code (join table `code_event` for descriptions
### bat_event_fl
- Type: BOOLEAN
- Description: Event is related to the batter
### ab_fl
- Type: BOOLEAN
- Description: Event is an at-bat
### h_fl
- Type: SMALLINT
- Description: Event is a hit
### sh_fl
- Type: BOOLEAN
- Description: Event is a sacrifice hit
### sf_fl
- Type: BOOLEAN
- Description: Event is a sacrifice fly
### event_outs_ct
- Type: SMALLINT
- Description: Outs recorded on event (0-3)
### dp_fl
- Type: BOOLEAN
- Description: Event is a double play
### tp_fl
- Type: BOOLEAN
- Description: Event is a triple play
### rbi_ct
- Type: SMALLINT
- Description: Runs batted in on event
### wp_fl
- Type: BOOLEAN
- Description: Event is a wild pitch
### pb_fl
- Type: BOOLEAN
- Description: Event is a passed ball
### fld_cd
- Type: SMALLINT
- Description: Position id of event fielder
### battedball_cd
- Type: CHAR(1)
- Description: Batted ball code (P - pop-up, G - ground ball, F - fly ball, L - line drive
### bunt_fl
- Type: BOOLEAN
- Description: Event is a bunt
### foul_fl
- Type: BOOLEAN
- Description: Event is a foul ball
### battedball_loc_tx
- Type: VARCHAR(5)
- Description: Hit location code (see https://www.retrosheet.org/location.htm)
### err_ct
- Type: SMALLINT
- Description: Number of errors recorded during event
### err1_fld_cd
- Type: SMALLINT
- Description: Position code of fielder committing first error during event
### err1_cd
- Type: CHAR(1)
- Description: First error type (T - throwing, F - fielding)
### err2_fld_cd
- Type: SMALLINT
- Description: Position code of fielder committing second error during event
### err2_cd
- Type: CHAR(1)
- Description: Second error type (T - throwing, F - fielding)
### err3_fld_cd
- Type: SMALLINT
- Description: Position code of fielder committing third error during event
### err3_cd
- Type: CHAR(1)
- Description: Third error type (T - throwing, F - fielding)
### bat_dest_id
- Type: SMALLINT
- Description: Destination of batter after event (0 - putout, 1-3 - bases, 4 - scored asearned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
### run1_dest_id
- Type: SMALLINT
- Description: Destination of runner on first after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
### run2_dest_id
- Type: SMALLINT
- Description: Destination of runner on second after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
### run3_dest_id
- Type: SMALLINT
- Description: Destination of runner on third after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
### bat_play_tx
- Type: VARCHAR(15)
- Description: Fielding play on batter
### run1_play_tx
- Type: VARCHAR(15)
- Description: Fielding play on runner on first
### run2_play_tx
- Type: VARCHAR(15)
- Description: Fielding play on runner on second
### run3_play_tx
- Type: VARCHAR(15)
- Description: Fielding play on runner on third
### run1_sb_fl
- Type: BOOLEAN
- Description: Runner on first steals base
### run2_sb_fl
- Type: BOOLEAN
- Description: Runner on second steals base
### run3_sb_fl
- Type: BOOLEAN
- Description: Runner on third steals base
### run1_cs_fl
- Type: BOOLEAN
- Description: Runner on first caught stealing
### run2_cs_fl
- Type: BOOLEAN
- Description: Runner on second caught stealing
### run3_cs_fl
- Type: BOOLEAN
- Description: Runner on third caught stealing
### run1_pk_fl
- Type: BOOLEAN
- Description: Runner on first picked off
### run2_pk_fl
- Type: BOOLEAN
- Description: Runner on second picked off
### run3_pk_fl
- Type: BOOLEAN
- Description: Runner on third picked off
### run1_resp_pit_id
- Type: CHAR(8)
- Description: ID of pitcher charged with runner on first
### run2_resp_pit_id
- Type: CHAR(8)
- Description: ID of pitcher charged with runner on second
### run3_resp_pit_id
- Type: CHAR(8)
- Description: ID of pitcher charged with runner on third
### game_new_fl
- Type: BOOLEAN
- Description: Start of game flag
### game_end_fl
- Type: BOOLEAN
- Description: End of game flag
### pr_run1_fl
- Type: BOOLEAN
- Description: Pinch-runner on first
### pr_run2_fl
- Type: BOOLEAN
- Description: Pinch-runner on second
### pr_run3_fl
- Type: BOOLEAN
- Description: Runner on third
### removed_for_pr_run1_id
- Type: CHAR(8)
- Description: ID of former runner on first removed for pinch-runner
### removed_for_pr_run2_id
- Type: CHAR(8)
- Description: ID of former runner on second removed for pinch-runner
### removed_for_pr_run3_id
- Type: CHAR(8)
- Description: ID of former runner on third removed for pinch-runner
### removed_for_ph_bat_id
- Type: CHAR(8)
- Description: ID of former batter removed for pinch-hitter
### removed_for_ph_bat_fld_cd
- Type: INTEGER
- Description: Position code of batter removed for pinch-hitter
### po1_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with first putout
### po2_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with second putout
### po3_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with third putout
### ass1_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with first assist
### ass2_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with second assist
### ass3_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with third assist
### ass4_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with fourth assist
### ass5_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with fifth assist
### home_team_id
- Type: CHAR(3)
- Description: Home team ID
### bat_team_id
- Type: CHAR(3)
- Description: Batting team ID
### fld_team_id
- Type: CHAR(3)
- Description: Fielding team ID
### bat_last_id
- Type: SMALLINT
- Description: Half inning (differs from batting team if home team bats first)
### inn_new_fl
- Type: BOOLEAN
- Description: Start of half-inning flag
### inn_end_fl
- Type: BOOLEAN
- Description: End of half-inning flag
### start_bat_score_ct
- Type: SMALLINT
- Description: Runs scored by batting team (prior to this event)
### start_fld_score_ct
- Type: SMALLINT
- Description: Runs scored by fielding team
### inn_runs_ct
- Type: SMALLINT
- Description: Runs scored in this half-inning (prior to this event)
### game_pa_ct
- Type: SMALLINT
- Description: Batting team PA total (prior to this event)
### inn_pa_ct
- Type: SMALLINT
- Description: Half-inning PA total (prior to this event)
### pa_new_fl
- Type: BOOLEAN
- Description: Event is the start of a plate appearance
### pa_trunc_fl
- Type: BOOLEAN
- Description: Event is a truncated plate appearance
### start_bases_cd
- Type: SMALLINT
- Description: Base state at start of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
### end_bases_cd
- Type: SMALLINT
- Description: Base state end of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
### bat_start_fl
- Type: BOOLEAN
- Description: Batter started game
### resp_bat_start_fl
- Type: BOOLEAN
- Description: Result-charged batter is a starter
### bat_on_deck_id
- Type: CHAR(8)
- Description: ID of batter on deck
### bat_in_hold_id
- Type: CHAR(8)
- Description: Id of batter in the hole
### pit_start_fl
- Type: BOOLEAN
- Description: Pitcher started game
### resp_pit_start_fl
- Type: BOOLEAN
- Description: Result-charged pitcher started game
### run1_fld_cd
- Type: SMALLINT
- Description: Defensive position code of runner on first
### run1_lineup_cd
- Type: SMALLINT
- Description: Lineup position of runner on first
### run1_origin_event_id
- Type: SMALLINT
- Description: Event number on which runner on first reached base
### run2_fld_cd
- Type: SMALLINT
- Description: Defensive position code of runner on second
### run2_lineup_cd
- Type: SMALLINT
- Description: Lineup position of runner on second
### run2_origin_event_id
- Type: SMALLINT
- Description: Event number on which runner on second reached base
### run3_fld_cd
- Type: SMALLINT
- Description: Defensive position code of runner on third
### run3_lineup_cd
- Type: SMALLINT
- Description: Lineup position of runner on third
### run3_origin_event_id
- Type: SMALLINT
- Description: Event number on which runner on third reached base
### run1_resp_cat_id
- Type: CHAR(8)
- Description: ID of responsible catcher for runner on first
### run2_resp_cat_id
- Type: CHAR(8)
- Description: ID of responsible catcher for runner on second
### run3_resp_cat_id
- Type: CHAR(8)
- Description: ID of responsible catcher for runner on third
### pa_ball_ct
- Type: SMALLINT
- Description: Number of balls in plate appearance
### pa_called_ball_ct
- Type: SMALLINT
- Description: Number of called balls in plate appearance
### pa_intent_ball_ct
- Type: SMALLINT
- Description: Number of intentional balls in plate appearance
### pa_pitchout_ball_ct
- Type: SMALLINT
- Description: Number of pitchouts in plate appearance
### pa_hitbatter_ball_ct
- Type: SMALLINT
- Description: Number of pitches hitting batter in plate appearance
### pa_other_ball_ct
- Type: SMALLINT
- Description: Number of other balls in plate appearance
### pa_strike_ct
- Type: SMALLINT
- Description: Number of strikes in plate appearance
### pa_called_strike_ct
- Type: SMALLINT
- Description: Number of called strikes in plate appearance
### pa_swingmiss_strike_ct
- Type: SMALLINT
- Description: Number of swing-and-miss strikes in plate appearance
### pa_foul_strike_ct
- Type: SMALLINT
- Description: Number of foul balls in plate appearance
### pa_inplay_strike_ct
- Type: SMALLINT
- Description: Number of balls in play in plate appearance
### pa_other_strike_ct
- Type: SMALLINT
- Description: Number of other strikes in plate appearance
### event_runs_ct
- Type: SMALLINT
- Description: Number of runs on play
### fld_id
- Type: CHAR(8)
- Description: ID of player fielding batted ball
### base2_force_fl
- Type: BOOLEAN
- Description: Event has force play at second
### base3_force_fl
- Type: BOOLEAN
- Description: Event has force play at third
### base4_force_fl
- Type: BOOLEAN
- Description: Event has force play at home
### bat_safe_err_fl
- Type: BOOLEAN
- Description: Event has batter safe on an error
### bat_fate_id
- Type: SMALLINT
- Description: Ultimate fate of batter (see `dest_id` cols for code meaning
### run1_fate_id
- Type: SMALLINT
- Description: Ultimate fate of runner on first (see `dest_id` cols for code meaning
### run2_fate_id
- Type: SMALLINT
- Description: Ultimate fate of runner on second (see `dest_id` cols for code meaning
### run3_fate_id
- Type: SMALLINT
- Description: Ultimate fate of runner on third (see `dest_id` cols for code meaning
### fate_runs_ct
- Type: SMALLINT
- Description: Additional runs scored in half inning after this event
### ass6_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with sixth assist
### ass7_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with seventh assist
### ass8_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with eighth assist
### ass9_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with ninth assist
### ass10_fld_cd
- Type: SMALLINT
- Description: Position code of fielder with tenth assist
### unknown_out_exc_fl
- Type: BOOLEAN
- Description: Unknown fielding credit flag
### uncertain_play_exc_fl
- Type: BOOLEAN
- Description: Uncertain play flag
## game
### **game_id**
- Type: CHAR(12)
- Description: Game ID (home team ID + YYYYMMDD + doubleheader flag
- Primary Key: Yes
### game_dt
- Type: DATE
- Description: Game date
### game_ct
- Type: SMALLINT
- Description: Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
### game_dy
- Type: VARCHAR(9)
- Description: Day of week
### start_game_tm
- Type: SMALLINT
- Description: Game start time (12HMM coded as integer, eg 1015 for 10:15 PM)
### dh_fl
- Type: VARCHAR(1)
- Description: DH used
### daynight_park_cd
- Type: VARCHAR(1)
- Description: D - day game, N - night game
### away_team_id
- Type: CHAR(3)
- Description: Away team ID
### home_team_id
- Type: CHAR(3)
- Description: Home team ID
### park_id
- Type: VARCHAR(5)
- Description: Park ID
### away_start_pit_id
- Type: CHAR(8)
- Description: Away team starting pitcher ID
### home_start_pit_id
- Type: CHAR(8)
- Description: Home team starting pitcher ID
### base4_ump_id
- Type: VARCHAR(32)
- Description: Home plate umpire ID
### base1_ump_id
- Type: VARCHAR(32)
- Description: First base umpire ID
### base2_ump_id
- Type: VARCHAR(32)
- Description: Second base umpire ID
### base3_ump_id
- Type: VARCHAR(32)
- Description: Third base umpire ID
### lf_ump_id
- Type: CHAR(8)
- Description: Left field umpire ID
### rf_ump_id
- Type: CHAR(8)
- Description: Right field umpire ID
### attend_park_ct
- Type: INTEGER
- Description: Attendance
### scorer_record_id
- Type: VARCHAR(50)
- Description: Scorekeeper
### translator_record_id
- Type: VARCHAR(50)
- Description: Translator
### inputter_record_id
- Type: VARCHAR(50)
- Description: Inputter
### input_record_ts
- Type: VARCHAR(20)
- Description: Date and time of record input
### edit_record_ts
- Type: VARCHAR(20)
- Description: Date and time of Most recent record edit
### method_record_cd
- Type: VARCHAR(1)
- Description: How the game was scored (join `code_method_record` for details
### pitches_record_cd
- Type: VARCHAR(1)
- Description: Highest detail of pitches recorded (join `code_pitches_record` for details). Note that many games with pitch detail do not have that info for all events, so pitch totals may not be accurate.
### temp_park_ct
- Type: SMALLINT
- Description: Park temperature in degrees F (0 if unknown)
### wind_direction_park_cd
- Type: SMALLINT
- Description: Wind direction park code (join `code_wind_direction_park` for details)
### wind_speed_park_ct
- Type: SMALLINT
- Description: Wind speed in miles per hour (-1 if unknown)
### field_park_cd
- Type: SMALLINT
- Description: Park field condition code (join `code_field_park` for details)
### precip_park_cd
- Type: SMALLINT
- Description: Park precipitation code (join `code_precip_park` for details
### sky_park_cd
- Type: SMALLINT
- Description: Park sky condition code (join `code_sky_park` for details
### minutes_game_ct
- Type: SMALLINT
- Description: Length of game in minutes
### inn_ct
- Type: SMALLINT
- Description: Length of game in innings
### away_score_ct
- Type: SMALLINT
- Description: Away team final score
### home_score_ct
- Type: SMALLINT
- Description: Home team final score
### away_hits_ct
- Type: SMALLINT
- Description: Away team hits
### home_hits_ct
- Type: SMALLINT
- Description: Home team hits
### away_err_ct
- Type: SMALLINT
- Description: Away team errors
### home_err_ct
- Type: SMALLINT
- Description: Home team errors
### away_lob_ct
- Type: SMALLINT
- Description: Away team left on base
### home_lob_ct
- Type: SMALLINT
- Description: Home team left on base
### win_pit_id
- Type: CHAR(8)
- Description: ID of winning pitcher
### lose_pit_id
- Type: CHAR(8)
- Description: ID of losing pitcher
### save_pit_id
- Type: CHAR(8)
- Description: ID of saving pitcher
### gwrbi_bat_id
- Type: CHAR(8)
- Description: ID of batter wit game-winning RBI
### away_lineup1_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 1
### away_lineup1_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 1
### away_lineup2_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 2
### away_lineup2_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 2
### away_lineup3_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 3
### away_lineup3_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 3
### away_lineup4_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 4
### away_lineup4_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 4
### away_lineup5_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 5
### away_lineup5_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 5
### away_lineup6_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 6
### away_lineup6_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 6
### away_lineup7_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 7
### away_lineup7_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 7
### away_lineup8_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 8
### away_lineup8_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 8
### away_lineup9_bat_id
- Type: CHAR(8)
- Description: ID of away team starting batter in lineup position 9
### away_lineup9_fld_cd
- Type: SMALLINT
- Description: Fielding position code of away team starting batter in lineup position 9
### home_lineup1_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 1
### home_lineup1_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 1
### home_lineup2_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 2
### home_lineup2_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 2
### home_lineup3_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 3
### home_lineup3_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 3
### home_lineup4_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 4
### home_lineup4_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 4
### home_lineup5_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 5
### home_lineup5_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 5
### home_lineup6_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 6
### home_lineup6_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 6
### home_lineup7_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 7
### home_lineup7_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 7
### home_lineup8_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 8
### home_lineup8_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 8
### home_lineup9_bat_id
- Type: CHAR(8)
- Description: ID of home team starting batter in lineup position 9
### home_lineup9_fld_cd
- Type: SMALLINT
- Description: Fielding position code of home team starting batter in lineup position 9
### away_finish_pit_id
- Type: CHAR(8)
- Description: Away team finishing pitcher
### home_finish_pit_id
- Type: CHAR(8)
- Description: Home team finishing pitcher
### away_team_league_id
- Type: CHAR(1)
- Description: Away team league (1 char ID)
### home_team_league_id
- Type: CHAR(1)
- Description: Home team league (1 char ID)
### away_team_game_ct
- Type: SMALLINT
- Description: Away team game number
### home_team_game_ct
- Type: SMALLINT
- Description: Home team game number
### outs_ct
- Type: SMALLINT
- Description: Length of game in outs
### completion_tx
- Type: VARCHAR(26)
- Description: Information on completion of game
### forfeit_tx
- Type: VARCHAR(26)
- Description: Information on forfeit of game
### protest_tx
- Type: VARCHAR(26)
- Description: Information on protest of game
### away_line_tx
- Type: VARCHAR(26)
- Description: Away team linescore
### home_line_tx
- Type: VARCHAR(26)
- Description: Home team linescore
### away_ab_ct
- Type: SMALLINT
- Description: Away team at bats
### away_2b_ct
- Type: SMALLINT
- Description: Away team doubles
### away_3b_ct
- Type: SMALLINT
- Description: Away team triples
### away_hr_ct
- Type: SMALLINT
- Description: Away team home runs
### away_bi_ct
- Type: SMALLINT
- Description: Away team runs batted in
### away_sh_ct
- Type: SMALLINT
- Description: Away team sacrifice hits
### away_sf_ct
- Type: SMALLINT
- Description: Away team sacrifice flies
### away_hp_ct
- Type: SMALLINT
- Description: Away team hit by pitches
### away_bb_ct
- Type: SMALLINT
- Description: Away team walks
### away_ibb_ct
- Type: SMALLINT
- Description: Away team intentional walks
### away_so_ct
- Type: SMALLINT
- Description: Away team strikeouts
### away_sb_ct
- Type: SMALLINT
- Description: Away team stolen bases
### away_cs_ct
- Type: SMALLINT
- Description: Away team caught stealing
### away_gdp_ct
- Type: SMALLINT
- Description: Away team grounded into double plays
### away_xi_ct
- Type: SMALLINT
- Description: Away team reached on interference
### away_pitcher_ct
- Type: SMALLINT
- Description: Away team number of pitchers used
### away_er_ct
- Type: SMALLINT
- Description: Away team individual earned runs
### away_ter_ct
- Type: SMALLINT
- Description: Away team team earned runs
### away_wp_ct
- Type: SMALLINT
- Description: Away team wild pitches
### away_bk_ct
- Type: SMALLINT
- Description: Away team balks
### away_po_ct
- Type: SMALLINT
- Description: Away team putouts
### away_a_ct
- Type: SMALLINT
- Description: Away team assists
### away_pb_ct
- Type: SMALLINT
- Description: Away team passed balls
### away_dp_ct
- Type: SMALLINT
- Description: Away team double plays turned
### away_tp_ct
- Type: SMALLINT
- Description: Away team triple plays turned
### home_ab_ct
- Type: SMALLINT
- Description: Home team at bats
### home_2b_ct
- Type: SMALLINT
- Description: Home team doubles
### home_3b_ct
- Type: SMALLINT
- Description: Home team triples
### home_hr_ct
- Type: SMALLINT
- Description: Home team home runs
### home_bi_ct
- Type: SMALLINT
- Description: Home team runs batted in
### home_sh_ct
- Type: SMALLINT
- Description: Home team sacrifice hits
### home_sf_ct
- Type: SMALLINT
- Description: Home team sacrifice flies
### home_hp_ct
- Type: SMALLINT
- Description: Home team hit by pitches
### home_bb_ct
- Type: SMALLINT
- Description: Home team walks
### home_ibb_ct
- Type: SMALLINT
- Description: Home team intentional walks
### home_so_ct
- Type: SMALLINT
- Description: Home team strikeouts
### home_sb_ct
- Type: SMALLINT
- Description: Home team stolen bases
### home_cs_ct
- Type: SMALLINT
- Description: Home team caught stealing
### home_gdp_ct
- Type: SMALLINT
- Description: Home team grounded into double plays
### home_xi_ct
- Type: SMALLINT
- Description: Home team reached on interference
### home_pitcher_ct
- Type: SMALLINT
- Description: Home team number of pitchers used
### home_er_ct
- Type: SMALLINT
- Description: Home team individual earned runs
### home_ter_ct
- Type: SMALLINT
- Description: Home team team earned runs
### home_wp_ct
- Type: SMALLINT
- Description: Home team wild pitches
### home_bk_ct
- Type: SMALLINT
- Description: Home team balks
### home_po_ct
- Type: SMALLINT
- Description: Home team putouts
### home_a_ct
- Type: SMALLINT
- Description: Home team assists
### home_pb_ct
- Type: SMALLINT
- Description: Home team passed balls
### home_dp_ct
- Type: SMALLINT
- Description: Home team double plays turned
### home_tp_ct
- Type: SMALLINT
- Description: Home team triple plays turned
### ump_home_name_tx
- Type: VARCHAR(26)
- Description: Home plate umpire name
### ump_1b_name_tx
- Type: VARCHAR(26)
- Description: First base umpire name
### ump_2b_name_tx
- Type: VARCHAR(26)
- Description: Second base umpire name
### ump_3b_name_tx
- Type: VARCHAR(26)
- Description: Third base umpire name
### ump_lf_name_tx
- Type: VARCHAR(26)
- Description: Left field umpire name
### ump_rf_name_tx
- Type: VARCHAR(26)
- Description: Right field umpire name
### away_manager_id
- Type: CHAR(8)
- Description: Away manager ID
### away_manager_name_tx
- Type: VARCHAR(26)
- Description: Away manager name
### home_manager_id
- Type: CHAR(8)
- Description: Home manager ID
### home_manager_name_tx
- Type: VARCHAR(26)
- Description: Home manager name
### win_pit_name_tx
- Type: VARCHAR(26)
- Description: Wining pitcher name
### lose_pit_name_tx
- Type: VARCHAR(26)
- Description: Losing pitcher name
### save_pit_name_tx
- Type: VARCHAR(26)
- Description: Saving pitcher name
### goahead_rbi_id
- Type: CHAR(8)
- Description: ID of batter with goahead RBI
### goahead_rbi_name_tx
- Type: VARCHAR(26)
- Description: Name of batter with goahead RBI
### away_lineup1_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 1
### away_lineup2_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 2
### away_lineup3_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 3
### away_lineup4_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 4
### away_lineup5_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 5
### away_lineup6_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 6
### away_lineup7_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 7
### away_lineup8_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of away team batter in lineup position 8
### away_lineup9_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 9
### home_lineup1_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 1
### home_lineup2_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 2
### home_lineup3_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 3
### home_lineup4_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 4
### home_lineup5_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 5
### home_lineup6_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 6
### home_lineup7_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 7
### home_lineup8_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 8
### home_lineup9_bat_name_tx
- Type: VARCHAR(26)
- Description: Name of home team batter in lineup position 9
### add_info_tx
- Type: VARCHAR(26)
- Description: Additional information
### acq_info_tx
- Type: VARCHAR(26)
- Description: Acquisition information
## gamelog
### **date**
- Type: DATE
- Description: Game date
- Primary Key: Yes
### **double_header**
- Type: CHAR(1)
- Description: 
        Number of game:
         "0" -- a single game
         "1" -- the first game of a double (or triple) header
                including separate admission doubleheaders
         "2" -- the second game of a double (or triple) header
                including separate admission doubleheaders
         "3" -- the third game of a triple-header
         "A" -- the first game of a double-header involving 3 teams
         "B" -- the second game of a double-header involving 3 teams
         
- Primary Key: Yes
### **visiting_team**
- Type: CHAR(3)
- Description: Visiting team ID
- Primary Key: Yes
### **home_team**
- Type: CHAR(3)
- Description: Home team ID
- Primary Key: Yes
### day_of_week
- Type: CHAR(3)
- Description: Day of week (3 char abbreviation)
### visiting_team_league
- Type: CHAR(2)
- Description: Away team league ID
### visiting_team_game_number
- Type: SMALLINT
- Description: Away team game number
### home_team_league
- Type: CHAR(2)
- Description: Home team league ID
### home_team_game_number
- Type: SMALLINT
- Description: Home team game number
### visitor_runs_scored
- Type: SMALLINT
- Description: Away team runs scored
### home_runs_score
- Type: SMALLINT
- Description: Home team runs scored
### length_in_outs
- Type: SMALLINT
- Description: Game length in outs
### day_night
- Type: CHAR(1)
- Description: D - day game, N - night game
### completion_info
- Type: VARCHAR(23)
- Description: 
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
        
### forfeit_info
- Type: VARCHAR(3)
- Description: V - forfeited to away team, H - forfeited to home team, T - ruled a no-decision
### protest_info
- Type: VARCHAR(3)
- Description: P - protested by unidentified team, V - disallowed protest by away team, H - disallowed protest by home team, X - upheld protest by away team, Y - upheld protest by home team
### park_id
- Type: CHAR(5)
- Description: Park ID
### attendance
- Type: INTEGER
- Description: Attendance
### duration
- Type: SMALLINT
- Description: Time of game in minutes
### vistor_line_score
- Type: VARCHAR(26)
- Description: Away team line score, e.g. 010000(10)0x
### home_line_score
- Type: VARCHAR(26)
- Description: Home team line score, e.g. 010000(10)0x
### visitor_ab
- Type: SMALLINT
- Description: Away team at bats
### visitor_h
- Type: SMALLINT
- Description: Away team hits
### visitor_d
- Type: SMALLINT
- Description: Away team doubles
### visitor_t
- Type: SMALLINT
- Description: Away team triples
### visitor_hr
- Type: SMALLINT
- Description: Away team home runs
### visitor_rbi
- Type: SMALLINT
- Description: Away team runs batted in
### visitor_sh
- Type: SMALLINT
- Description: Away team sacrifice hits (may include sac flies before 1954)
### visitor_sf
- Type: SMALLINT
- Description: Away team sacrifice flies (since 1954)
### visitor_hbp
- Type: SMALLINT
- Description: Away team hit by pitches
### visitor_bb
- Type: SMALLINT
- Description: Away team walks
### visitor_ibb
- Type: SMALLINT
- Description: Away team intentional walks
### visitor_k
- Type: SMALLINT
- Description: Away team strikeouts
### visitor_sb
- Type: SMALLINT
- Description: Away team stolen bases
### visitor_cs
- Type: SMALLINT
- Description: Away team caught stealing
### visitor_gdp
- Type: SMALLINT
- Description: Away team grounded into double plays
### visitor_ci
- Type: SMALLINT
- Description: Away team reached on interference
### visitor_lob
- Type: SMALLINT
- Description: Away team left on base
### visitor_pitchers
- Type: SMALLINT
- Description: Away team pitchers used
### visitor_er
- Type: SMALLINT
- Description: Away team individual earned runs allowed
### visitor_ter
- Type: SMALLINT
- Description: Away team team earned runs allowed
### visitor_wp
- Type: SMALLINT
- Description: Away team wild pitches allowed
### visitor_balks
- Type: SMALLINT
- Description: Away team balks allowed
### visitor_po
- Type: SMALLINT
- Description: Away team putouts
### visitor_a
- Type: SMALLINT
- Description: Away team assists
### visitor_e
- Type: SMALLINT
- Description: Away team errors
### visitor_passed
- Type: SMALLINT
- Description: Away team passed balls
### visitor_db
- Type: SMALLINT
- Description: Away team double plays turned
### visitor_tp
- Type: SMALLINT
- Description: Away team triple plays turned
### home_ab
- Type: SMALLINT
- Description: Home team at bats
### home_h
- Type: SMALLINT
- Description: Home team hits
### home_d
- Type: SMALLINT
- Description: Home team doubles
### home_t
- Type: SMALLINT
- Description: Home team triples
### home_hr
- Type: SMALLINT
- Description: Home team home runs
### home_rbi
- Type: SMALLINT
- Description: Home team runs batted in
### home_sh
- Type: SMALLINT
- Description: Home team sacrifice hits (may include sac flies before 1954)
### home_sf
- Type: SMALLINT
- Description: Home team sacrifice flies (since 1954)
### home_hbp
- Type: SMALLINT
- Description: Home team hit by pitches
### home_bb
- Type: SMALLINT
- Description: Home team walks
### home_ibb
- Type: SMALLINT
- Description: Home team intentional walks
### home_k
- Type: SMALLINT
- Description: Home team strikeouts
### home_sb
- Type: SMALLINT
- Description: Home team stolen bases
### home_cs
- Type: SMALLINT
- Description: Home team caught stealing
### home_gdp
- Type: SMALLINT
- Description: Home team grounded into double plays
### home_ci
- Type: SMALLINT
- Description: Home team reached on interference
### home_lob
- Type: SMALLINT
- Description: Home team left on base
### home_pitchers
- Type: SMALLINT
- Description: Home team pitchers used
### home_er
- Type: SMALLINT
- Description: Home team individual earned runs allowed
### home_ter
- Type: SMALLINT
- Description: Home team team earned runs allowed
### home_wp
- Type: SMALLINT
- Description: Home team wild pitches allowed
### home_balks
- Type: SMALLINT
- Description: Home team balks allowed
### home_po
- Type: SMALLINT
- Description: Home team putouts
### home_a
- Type: SMALLINT
- Description: Home team assists
### home_e
- Type: SMALLINT
- Description: Home team errors
### home_passed
- Type: SMALLINT
- Description: Home team passed balls
### home_db
- Type: SMALLINT
- Description: Home team double plays turned
### home_tp
- Type: SMALLINT
- Description: Home team triple plays turned
### umpire_h_id
- Type: CHAR(8)
- Description: Home plate umpire ID
### umpire_h_name
- Type: VARCHAR(32)
- Description: Home plate umpire name
### umpire_1b_id
- Type: CHAR(8)
- Description: First base umpire ID
### umpire_1b_name
- Type: VARCHAR(32)
- Description: First base umpire name
### umpire_2b_id
- Type: CHAR(8)
- Description: Second base umpire ID
### umpire_2b_name
- Type: VARCHAR(32)
- Description: Second base umpire name
### umpire_3b_id
- Type: CHAR(8)
- Description: Third base umpire ID
### umpire_3b_name
- Type: VARCHAR(32)
- Description: Third base umpire name
### umpire_lf_id
- Type: CHAR(8)
- Description: Left field umpire ID
### umpire_lf_name
- Type: VARCHAR(32)
- Description: Left field umpire name
### umpire_rf_id
- Type: CHAR(8)
- Description: Right field umpire ID
### umpire_rf_name
- Type: VARCHAR(32)
- Description: Right field umpire name
### visitor_manager_id
- Type: CHAR(8)
- Description: Away team manager ID
### visitor_manager_name
- Type: VARCHAR(32)
- Description: Away team manager name
### home_manager_id
- Type: CHAR(8)
- Description: Home team manager ID
### home_manager_name
- Type: VARCHAR(32)
- Description: Home team manager name
### winning_pitcher_id
- Type: CHAR(8)
- Description: Winning pitcher ID
### winning_pitcher_name
- Type: VARCHAR(32)
- Description: Winning pitcher name
### losing_pitcher_id
- Type: CHAR(8)
- Description: Losing pitcher ID
### losing_pitcher_name
- Type: VARCHAR(32)
- Description: Losing pitcher name
### saving_pitcher_id
- Type: CHAR(8)
- Description: Saving pitcher ID
### saving_pitcher_name
- Type: VARCHAR(32)
- Description: Saving pitcher name
### game_winning_rbi_id
- Type: CHAR(8)
- Description: Game-winning RBI ID
### game_winning_rbi_name
- Type: VARCHAR(32)
- Description: Game-winning RBI name
### visitor_starting_pitcher_id
- Type: CHAR(8)
- Description: Away team starting pitcher ID
### visitor_starting_pitcher_name
- Type: VARCHAR(32)
- Description: Away team starting pitcher name
### home_starting_pitcher_id
- Type: CHAR(8)
- Description: Home team starting pitcher ID
### home_starting_pitcher_name
- Type: VARCHAR(32)
- Description: Home team starting pitcher name
### visitor_batting_1_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 1 starting player ID
### visitor_batting_1_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 1 starting player name
### visitor_batting_1_position
- Type: SMALLINT
- Description: Away team lineup slot 1 starting player fielding position
### visitor_batting_2_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 2 starting player ID
### visitor_batting_2_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 2 starting player name
### visitor_batting_2_position
- Type: SMALLINT
- Description: Away team lineup slot 2 starting player fielding position
### visitor_batting_3_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 3 starting player ID
### visitor_batting_3_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 3 starting player name
### visitor_batting_3_position
- Type: SMALLINT
- Description: Away team lineup slot 3 starting player fielding position
### visitor_batting_4_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 4 starting player ID
### visitor_batting_4_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 4 starting player name
### visitor_batting_4_position
- Type: SMALLINT
- Description: Away team lineup slot 4 starting player fielding position
### visitor_batting_5_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 5 starting player ID
### visitor_batting_5_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 5 starting player name
### visitor_batting_5_position
- Type: SMALLINT
- Description: Away team lineup slot 5 starting player fielding position
### visitor_batting_6_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 6 starting player ID
### visitor_batting_6_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 6 starting player name
### visitor_batting_6_position
- Type: SMALLINT
- Description: Away team lineup slot 6 starting player fielding position
### visitor_batting_7_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 7 starting player ID
### visitor_batting_7_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 7 starting player name
### visitor_batting_7_position
- Type: SMALLINT
- Description: Away team lineup slot 7 starting player fielding position
### visitor_batting_8_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 8 starting player ID
### visitor_batting_8_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 8 starting player name
### visitor_batting_8_position
- Type: SMALLINT
- Description: Away team lineup slot 8 starting player fielding position
### visitor_batting_9_player_id
- Type: CHAR(8)
- Description: Away team lineup slot 9 starting player ID
### visitor_batting_9_name
- Type: VARCHAR(32)
- Description: Away team lineup slot 9 starting player name
### visitor_batting_9_position
- Type: SMALLINT
- Description: Away team lineup slot 9 starting player fielding position
### home_batting_1_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 1 starting player ID
### home_batting_1_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 1 starting player name
### home_batting_1_position
- Type: SMALLINT
- Description: Home team lineup slot 1 starting player fielding position
### home_batting_2_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 2 starting player ID
### home_batting_2_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 2 starting player name
### home_batting_2_position
- Type: SMALLINT
- Description: Home team lineup slot 2 starting player fielding position
### home_batting_3_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 3 starting player ID
### home_batting_3_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 3 starting player name
### home_batting_3_position
- Type: SMALLINT
- Description: Home team lineup slot 3 starting player fielding position
### home_batting_4_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 4 starting player ID
### home_batting_4_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 4 starting player name
### home_batting_4_position
- Type: SMALLINT
- Description: Home team lineup slot 4 starting player fielding position
### home_batting_5_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 5 starting player ID
### home_batting_5_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 5 starting player name
### home_batting_5_position
- Type: SMALLINT
- Description: Home team lineup slot 5 starting player fielding position
### home_batting_6_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 6 starting player ID
### home_batting_6_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 6 starting player name
### home_batting_6_position
- Type: SMALLINT
- Description: Home team lineup slot 6 starting player fielding position
### home_batting_7_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 7 starting player ID
### home_batting_7_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 7 starting player name
### home_batting_7_position
- Type: SMALLINT
- Description: Home team lineup slot 7 starting player fielding position
### home_batting_8_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 8 starting player ID
### home_batting_8_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 8 starting player name
### home_batting_8_position
- Type: SMALLINT
- Description: Home team lineup slot 8 starting player fielding position
### home_batting_9_player_id
- Type: CHAR(8)
- Description: Home team lineup slot 9 starting player ID
### home_batting_9_name
- Type: VARCHAR(32)
- Description: Home team lineup slot 9 starting player name
### home_batting_9_position
- Type: SMALLINT
- Description: Home team lineup slot 9 starting player fielding position
### additional_info
- Type: VARCHAR(128)
- Description: 
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
        
### acquisition_info
- Type: CHAR(1)
- Description: Y - complete game information, N - no game information, D - game derived from box score and game story, P - portions of game information
## park
### **park_id**
- Type: CHAR(5)
- Description: Park ID
- Primary Key: Yes
### name
- Type: VARCHAR(41)
- Description: Park name
### aka
- Type: VARCHAR(55)
- Description: Common park alias
### city
- Type: VARCHAR(17)
- Description: City
### state
- Type: VARCHAR(9)
- Description: State
### start_date
- Type: VARCHAR(10)
- Description: First game
### end_date
- Type: VARCHAR(10)
- Description: Last game
### league
- Type: CHAR(2)
- Description: League ID
### notes
- Type: VARCHAR(54)
- Description: Misc. notes
## roster
### **year**
- Type: INTEGER
- Description: Year of roster
- Primary Key: Yes
### **player_id**
- Type: CHAR(8)
- Description: Player ID
- Primary Key: Yes
### **team_id**
- Type: CHAR(3)
- Description: Team ID
- Primary Key: Yes
### **position**
- Type: VARCHAR(2)
- Description: Primary fielding position
- Primary Key: Yes
### last_name
- Type: VARCHAR(32)
- Description: Player last name
### first_name
- Type: VARCHAR(32)
- Description: Player first name
### bats
- Type: CHAR(1)
- Description: Bat handedness
### throws
- Type: CHAR(1)
- Description: Throw handedness
## schedule
### **date**
- Type: DATE
- Description: Scheduled game date
- Primary Key: Yes
### **home_team**
- Type: CHAR(3)
- Description: Home team ID
- Primary Key: Yes
### **home_team_game_number**
- Type: INTEGER
- Description: Home team game number
- Primary Key: Yes
### double_header
- Type: SMALLINT
- Description: Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
### day_of_week
- Type: CHAR(3)
- Description: Day of week (3 letter abbreviation
### visiting_team
- Type: CHAR(3)
- Description: Away team ID
### visiting_team_league
- Type: CHAR(2)
- Description: Away team league ID
### visiting_team_game_number
- Type: SMALLINT
- Description: Away team game number
### home_team_league
- Type: CHAR(2)
- Description: Home team league ID
### day_night
- Type: CHAR(1)
- Description: D - day, N - night
### postponement_indicator
- Type: VARCHAR(120)
- Description: 
        This field will contain one or more phrases related to the game if it was
        not played as scheduled. If there is more than one phrase, they are separated
        by a semi-colon (";"). There are three possible outcomes for games not played
        on the originally scheduled date:
        -- The game was played on another date
        -- The game was played on the original date but at another site
        -- The game was not played
        
### makeup_dates
- Type: VARCHAR(120)
- Description: 
        This field will contain a makeup date if the postponed game was played at
        another time or place. If an attempt was known to have been made on a date but
        postponed again, that date will be listed. In that case, there will be a second
        date for the date when the game was actually played, in this form: "20150428;
        20150528" For the note about a team folding, the team code is one of the
        standard Retrosheet team IDs. The same is true for the team played as note.
        Often, the two of these are combined in one field.
        
## sub
### **dummy_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### game_id
- Type: CHAR(12)
- Description: Game ID (home team ID + YYYYMMDD + doubleheader flag
### inn_ct
- Type: SMALLINT
- Description: Inning of substitution
### bat_home_id
- Type: SMALLINT
- Description: Is home team batting (-1 for N/A)
### sub_id
- Type: CHAR(8)
- Description: Player ID of substitute
### sub_home_id
- Type: BOOLEAN
- Description: Is the home team making the substitution
### sub_lineup_id
- Type: SMALLINT
- Description: Lineup position of substitution
### sub_fld_cd
- Type: SMALLINT
- Description: Fielding position of substitution
### removed_id
- Type: CHAR(8)
- Description: ID of removed player
### removed_fld_cd
- Type: SMALLINT
- Description: Fielding position of removed player
### event_id
- Type: SMALLINT
- Description: Event number in which substitution occurred


# baseballdatabank
## allstar_full
### **dummy_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### player_id
- Type: VARCHAR(9)
- Description: No description
### year_id
- Type: SMALLINT
- Description: No description
### game_num
- Type: SMALLINT
- Description: No description
### game_id
- Type: VARCHAR(12)
- Description: No description
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### gp
- Type: SMALLINT
- Description: No description
### starting_pos
- Type: SMALLINT
- Description: No description
## appearances
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g_all
- Type: SMALLINT
- Description: No description
### gs
- Type: SMALLINT
- Description: No description
### g_batting
- Type: SMALLINT
- Description: No description
### g_defense
- Type: SMALLINT
- Description: No description
### g_p
- Type: SMALLINT
- Description: No description
### g_c
- Type: SMALLINT
- Description: No description
### g_1b
- Type: SMALLINT
- Description: No description
### g_2b
- Type: SMALLINT
- Description: No description
### g_3b
- Type: SMALLINT
- Description: No description
### g_ss
- Type: SMALLINT
- Description: No description
### g_lf
- Type: SMALLINT
- Description: No description
### g_cf
- Type: SMALLINT
- Description: No description
### g_rf
- Type: SMALLINT
- Description: No description
### g_of
- Type: SMALLINT
- Description: No description
### g_dh
- Type: SMALLINT
- Description: No description
### g_ph
- Type: SMALLINT
- Description: No description
### g_pr
- Type: SMALLINT
- Description: No description
## awards_managers
### **dummy_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### player_id
- Type: VARCHAR(10)
- Description: No description
### award_id
- Type: VARCHAR(75)
- Description: No description
### year_id
- Type: SMALLINT
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### tie
- Type: VARCHAR(1)
- Description: No description
### notes
- Type: VARCHAR(100)
- Description: No description
## awards_players
### **dummy_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### player_id
- Type: VARCHAR(9)
- Description: No description
### award_id
- Type: VARCHAR(255)
- Description: No description
### year_id
- Type: SMALLINT
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### tie
- Type: VARCHAR(1)
- Description: No description
### notes
- Type: VARCHAR(100)
- Description: No description
## awards_share_managers
### **award_id**
- Type: VARCHAR(25)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### **player_id**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### lg_id
- Type: VARCHAR(2)
- Description: No description
### points_won
- Type: INTEGER
- Description: No description
### points_max
- Type: INTEGER
- Description: No description
### votes_first
- Type: INTEGER
- Description: No description
## awards_share_players
### **award_id**
- Type: VARCHAR(25)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### lg_id
- Type: VARCHAR(2)
- Description: No description
### points_won
- Type: FLOAT
- Description: No description
### points_max
- Type: INTEGER
- Description: No description
### votes_first
- Type: FLOAT
- Description: No description
## batting
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **stint**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### ab
- Type: SMALLINT
- Description: No description
### r
- Type: SMALLINT
- Description: No description
### h
- Type: SMALLINT
- Description: No description
### _2b
- Type: SMALLINT
- Description: No description
### _3b
- Type: SMALLINT
- Description: No description
### hr
- Type: SMALLINT
- Description: No description
### rbi
- Type: SMALLINT
- Description: No description
### sb
- Type: SMALLINT
- Description: No description
### cs
- Type: SMALLINT
- Description: No description
### bb
- Type: SMALLINT
- Description: No description
### so
- Type: SMALLINT
- Description: No description
### ibb
- Type: SMALLINT
- Description: No description
### hbp
- Type: SMALLINT
- Description: No description
### sh
- Type: SMALLINT
- Description: No description
### sf
- Type: SMALLINT
- Description: No description
### gidp
- Type: SMALLINT
- Description: No description
## batting_post
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **round**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### ab
- Type: SMALLINT
- Description: No description
### r
- Type: SMALLINT
- Description: No description
### h
- Type: SMALLINT
- Description: No description
### _2b
- Type: SMALLINT
- Description: No description
### _3b
- Type: SMALLINT
- Description: No description
### hr
- Type: SMALLINT
- Description: No description
### rbi
- Type: SMALLINT
- Description: No description
### sb
- Type: SMALLINT
- Description: No description
### cs
- Type: SMALLINT
- Description: No description
### bb
- Type: SMALLINT
- Description: No description
### so
- Type: SMALLINT
- Description: No description
### ibb
- Type: SMALLINT
- Description: No description
### hbp
- Type: SMALLINT
- Description: No description
### sh
- Type: SMALLINT
- Description: No description
### sf
- Type: SMALLINT
- Description: No description
### gidp
- Type: SMALLINT
- Description: No description
## college_playing
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **school_id**
- Type: VARCHAR(15)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
## fielding
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **stint**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **pos**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### gs
- Type: SMALLINT
- Description: No description
### inn_outs
- Type: SMALLINT
- Description: No description
### po
- Type: SMALLINT
- Description: No description
### a
- Type: SMALLINT
- Description: No description
### e
- Type: SMALLINT
- Description: No description
### dp
- Type: SMALLINT
- Description: No description
### pb
- Type: SMALLINT
- Description: No description
### wp
- Type: SMALLINT
- Description: No description
### sb
- Type: SMALLINT
- Description: No description
### cs
- Type: SMALLINT
- Description: No description
### zr
- Type: FLOAT
- Description: No description
## fielding_of
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **stint**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### g_lf
- Type: SMALLINT
- Description: No description
### g_cf
- Type: SMALLINT
- Description: No description
### g_rf
- Type: SMALLINT
- Description: No description
## fielding_of_split
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **stint**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **pos**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### gs
- Type: SMALLINT
- Description: No description
### inn_outs
- Type: SMALLINT
- Description: No description
### po
- Type: SMALLINT
- Description: No description
### a
- Type: SMALLINT
- Description: No description
### e
- Type: SMALLINT
- Description: No description
### dp
- Type: SMALLINT
- Description: No description
### pb
- Type: SMALLINT
- Description: No description
### wp
- Type: SMALLINT
- Description: No description
### sb
- Type: SMALLINT
- Description: No description
### cs
- Type: SMALLINT
- Description: No description
### zr
- Type: FLOAT
- Description: No description
## fielding_post
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **round**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### **pos**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### gs
- Type: SMALLINT
- Description: No description
### inn_outs
- Type: SMALLINT
- Description: No description
### po
- Type: SMALLINT
- Description: No description
### a
- Type: SMALLINT
- Description: No description
### e
- Type: SMALLINT
- Description: No description
### dp
- Type: SMALLINT
- Description: No description
### tp
- Type: SMALLINT
- Description: No description
### pb
- Type: SMALLINT
- Description: No description
### sb
- Type: SMALLINT
- Description: No description
### cs
- Type: SMALLINT
- Description: No description
## hall_of_fame
### **player_id**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **voted_by**
- Type: VARCHAR(64)
- Description: No description
- Primary Key: Yes
### ballots
- Type: VARCHAR(64)
- Description: No description
### needed
- Type: VARCHAR(64)
- Description: No description
### votes
- Type: VARCHAR(64)
- Description: No description
### inducted
- Type: VARCHAR(1)
- Description: No description
### category
- Type: VARCHAR(20)
- Description: No description
### needed_note
- Type: VARCHAR(25)
- Description: No description
## home_games
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **lg_id**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### **park_id**
- Type: VARCHAR(5)
- Description: No description
- Primary Key: Yes
### first_game
- Type: DATE
- Description: No description
### last_game
- Type: DATE
- Description: No description
### games
- Type: SMALLINT
- Description: No description
### openings
- Type: SMALLINT
- Description: No description
### attendance
- Type: INTEGER
- Description: No description
## managers
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### **inseason**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### player_id
- Type: VARCHAR(10)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### w
- Type: SMALLINT
- Description: No description
### l
- Type: SMALLINT
- Description: No description
### rank
- Type: SMALLINT
- Description: No description
### plyr_mgr
- Type: VARCHAR(1)
- Description: No description
## managers_half
### **player_id**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### **half**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### lg_id
- Type: VARCHAR(2)
- Description: No description
### inseason
- Type: SMALLINT
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### w
- Type: SMALLINT
- Description: No description
### l
- Type: SMALLINT
- Description: No description
### rank
- Type: SMALLINT
- Description: No description
## parks
### **park_id**
- Type: VARCHAR(5)
- Description: No description
- Primary Key: Yes
### park_name
- Type: VARCHAR(40)
- Description: No description
### park_alias
- Type: VARCHAR(55)
- Description: No description
### city
- Type: VARCHAR(25)
- Description: No description
### state
- Type: VARCHAR(16)
- Description: No description
### country
- Type: VARCHAR(2)
- Description: No description
## people
### **player_id**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### birth_year
- Type: SMALLINT
- Description: No description
### birth_month
- Type: SMALLINT
- Description: No description
### birth_day
- Type: SMALLINT
- Description: No description
### birth_country
- Type: VARCHAR(50)
- Description: No description
### birth_state
- Type: VARCHAR(50)
- Description: No description
### birth_city
- Type: VARCHAR(50)
- Description: No description
### death_year
- Type: SMALLINT
- Description: No description
### death_month
- Type: SMALLINT
- Description: No description
### death_day
- Type: SMALLINT
- Description: No description
### death_country
- Type: VARCHAR(50)
- Description: No description
### death_state
- Type: VARCHAR(50)
- Description: No description
### death_city
- Type: VARCHAR(50)
- Description: No description
### name_first
- Type: VARCHAR(50)
- Description: No description
### name_last
- Type: VARCHAR(50)
- Description: No description
### name_given
- Type: VARCHAR(255)
- Description: No description
### weight
- Type: SMALLINT
- Description: No description
### height
- Type: FLOAT
- Description: No description
### bats
- Type: VARCHAR(1)
- Description: No description
### throws
- Type: VARCHAR(1)
- Description: No description
### debut
- Type: DATE
- Description: No description
### final_game
- Type: DATE
- Description: No description
### retro_id
- Type: VARCHAR(9)
- Description: No description
### bbref_id
- Type: VARCHAR(9)
- Description: No description
## pitching
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **stint**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### w
- Type: SMALLINT
- Description: No description
### l
- Type: SMALLINT
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### gs
- Type: SMALLINT
- Description: No description
### cg
- Type: SMALLINT
- Description: No description
### sho
- Type: SMALLINT
- Description: No description
### sv
- Type: SMALLINT
- Description: No description
### ip_outs
- Type: SMALLINT
- Description: No description
### h
- Type: SMALLINT
- Description: No description
### er
- Type: SMALLINT
- Description: No description
### hr
- Type: SMALLINT
- Description: No description
### bb
- Type: SMALLINT
- Description: No description
### so
- Type: SMALLINT
- Description: No description
### ba_opp
- Type: FLOAT
- Description: No description
### era
- Type: FLOAT
- Description: No description
### ibb
- Type: SMALLINT
- Description: No description
### wp
- Type: SMALLINT
- Description: No description
### hbp
- Type: SMALLINT
- Description: No description
### bk
- Type: SMALLINT
- Description: No description
### bfp
- Type: SMALLINT
- Description: No description
### gf
- Type: SMALLINT
- Description: No description
### r
- Type: SMALLINT
- Description: No description
### sh
- Type: SMALLINT
- Description: No description
### sf
- Type: SMALLINT
- Description: No description
### gidp
- Type: SMALLINT
- Description: No description
## pitching_post
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **round**
- Type: VARCHAR(10)
- Description: No description
- Primary Key: Yes
### team_id
- Type: VARCHAR(3)
- Description: No description
### lg_id
- Type: VARCHAR(2)
- Description: No description
### w
- Type: SMALLINT
- Description: No description
### l
- Type: SMALLINT
- Description: No description
### g
- Type: SMALLINT
- Description: No description
### gs
- Type: SMALLINT
- Description: No description
### cg
- Type: SMALLINT
- Description: No description
### sho
- Type: SMALLINT
- Description: No description
### sv
- Type: SMALLINT
- Description: No description
### ip_outs
- Type: SMALLINT
- Description: No description
### h
- Type: SMALLINT
- Description: No description
### er
- Type: SMALLINT
- Description: No description
### hr
- Type: SMALLINT
- Description: No description
### bb
- Type: SMALLINT
- Description: No description
### so
- Type: SMALLINT
- Description: No description
### ba_opp
- Type: FLOAT
- Description: No description
### era
- Type: FLOAT
- Description: No description
### ibb
- Type: SMALLINT
- Description: No description
### wp
- Type: SMALLINT
- Description: No description
### hbp
- Type: SMALLINT
- Description: No description
### bk
- Type: SMALLINT
- Description: No description
### bfp
- Type: SMALLINT
- Description: No description
### gf
- Type: SMALLINT
- Description: No description
### r
- Type: SMALLINT
- Description: No description
### sh
- Type: SMALLINT
- Description: No description
### sf
- Type: SMALLINT
- Description: No description
### gidp
- Type: SMALLINT
- Description: No description
## salaries
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### **lg_id**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### **player_id**
- Type: VARCHAR(9)
- Description: No description
- Primary Key: Yes
### salary
- Type: FLOAT
- Description: No description
## schools
### **school_id**
- Type: VARCHAR(15)
- Description: No description
- Primary Key: Yes
### name_full
- Type: VARCHAR(255)
- Description: No description
### city
- Type: VARCHAR(55)
- Description: No description
### state
- Type: VARCHAR(55)
- Description: No description
### country
- Type: VARCHAR(55)
- Description: No description
## series_post
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **round**
- Type: VARCHAR(5)
- Description: No description
- Primary Key: Yes
### team_id_winner
- Type: VARCHAR(3)
- Description: No description
### lg_id_winner
- Type: VARCHAR(2)
- Description: No description
### team_id_loser
- Type: VARCHAR(3)
- Description: No description
### lg_id_loser
- Type: VARCHAR(2)
- Description: No description
### wins
- Type: SMALLINT
- Description: No description
### losses
- Type: SMALLINT
- Description: No description
### ties
- Type: SMALLINT
- Description: No description
## teams
### **year_id**
- Type: SMALLINT
- Description: No description
- Primary Key: Yes
### **lg_id**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### franch_id
- Type: VARCHAR(3)
- Description: No description
### div_id
- Type: VARCHAR(1)
- Description: No description
### rank
- Type: INTEGER
- Description: No description
### g
- Type: INTEGER
- Description: No description
### g_home
- Type: INTEGER
- Description: No description
### w
- Type: INTEGER
- Description: No description
### l
- Type: INTEGER
- Description: No description
### div_win
- Type: VARCHAR(1)
- Description: No description
### wc_win
- Type: VARCHAR(1)
- Description: No description
### lg_win
- Type: VARCHAR(1)
- Description: No description
### ws_win
- Type: VARCHAR(1)
- Description: No description
### r
- Type: INTEGER
- Description: No description
### ab
- Type: INTEGER
- Description: No description
### h
- Type: INTEGER
- Description: No description
### _2b
- Type: INTEGER
- Description: No description
### _3b
- Type: INTEGER
- Description: No description
### hr
- Type: INTEGER
- Description: No description
### bb
- Type: INTEGER
- Description: No description
### so
- Type: INTEGER
- Description: No description
### sb
- Type: INTEGER
- Description: No description
### cs
- Type: INTEGER
- Description: No description
### hbp
- Type: INTEGER
- Description: No description
### sf
- Type: INTEGER
- Description: No description
### ra
- Type: INTEGER
- Description: No description
### er
- Type: INTEGER
- Description: No description
### era
- Type: FLOAT
- Description: No description
### cg
- Type: INTEGER
- Description: No description
### sho
- Type: INTEGER
- Description: No description
### sv
- Type: INTEGER
- Description: No description
### ip_outs
- Type: INTEGER
- Description: No description
### h_a
- Type: INTEGER
- Description: No description
### hr_a
- Type: INTEGER
- Description: No description
### bb_a
- Type: INTEGER
- Description: No description
### so_a
- Type: INTEGER
- Description: No description
### e
- Type: INTEGER
- Description: No description
### dp
- Type: INTEGER
- Description: No description
### fp
- Type: FLOAT
- Description: No description
### name
- Type: VARCHAR(50)
- Description: No description
### park
- Type: VARCHAR(255)
- Description: No description
### attendance
- Type: INTEGER
- Description: No description
### bpf
- Type: INTEGER
- Description: No description
### ppf
- Type: INTEGER
- Description: No description
### team_id_br
- Type: VARCHAR(3)
- Description: No description
### team_id_lahman45
- Type: VARCHAR(3)
- Description: No description
### team_id_retro
- Type: VARCHAR(3)
- Description: No description
## teams_franchises
### **franch_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### franch_name
- Type: VARCHAR(50)
- Description: No description
### active
- Type: VARCHAR(2)
- Description: No description
### na_assoc
- Type: VARCHAR(3)
- Description: No description
## teams_half
### **year_id**
- Type: INTEGER
- Description: No description
- Primary Key: Yes
### **lg_id**
- Type: VARCHAR(2)
- Description: No description
- Primary Key: Yes
### **team_id**
- Type: VARCHAR(3)
- Description: No description
- Primary Key: Yes
### **half**
- Type: VARCHAR(1)
- Description: No description
- Primary Key: Yes
### div_id
- Type: VARCHAR(1)
- Description: No description
### div_win
- Type: VARCHAR(1)
- Description: No description
### rank
- Type: INTEGER
- Description: No description
### g
- Type: INTEGER
- Description: No description
### w
- Type: INTEGER
- Description: No description
### l
- Type: INTEGER
- Description: No description
