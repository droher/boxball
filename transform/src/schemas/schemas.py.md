# Boxball Schemas
[TOC]
## retrosheet
### code_event

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### code_field_park

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### code_method_record

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### code_pitches_record

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### code_precip_park

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### code_sky_park

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### code_wind_direction_park

??? keycolumnstyle "code    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "description    (varchar(30))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### comment

??? keycolumnstyle "dummy_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "game_id    (char(12))"
    ```{.codeblock}
    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "event_id    (smallint)"
    ```{.codeblock}
    Commented event number
    ```
    

??? columnstyle "comment    (varchar(1638))"
    ```{.codeblock}
    Comment text
    ```
    

??? columnstyle "ejected_person_id    (varchar(256))"
    ```{.codeblock}
    ID of ejected person
    ```
    

??? columnstyle "ejected_person_role_cd    (varchar(256))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "eject_umpire_id    (varchar(256))"
    ```{.codeblock}
    ID of umpire who ejected person
    ```
    

??? columnstyle "eject_reason    (varchar(1639))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "umpchange_inning    (varchar(256))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "umpchange_position    (varchar(256))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "umpchange_person_id    (varchar(256))"
    ```{.codeblock}
    ID of new umpire
    ```
    



### daily

??? keycolumnstyle "dummy_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "game_id    (char(12))"
    ```{.codeblock}
    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "game_dt    (date)"
    ```{.codeblock}
    Game date
    ```
    

??? columnstyle "game_ct    (smallint)"
    ```{.codeblock}
    Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
    ```
    

??? columnstyle "appearance_dt    (date)"
    ```{.codeblock}
    Player appearance date. Can be different from game date if the game was suspended and the player entered the game at the later date
    ```
    

??? columnstyle "team_id    (char(3))"
    ```{.codeblock}
    Team ID of player
    ```
    

??? columnstyle "player_id    (char(8))"
    ```{.codeblock}
    Player ID
    ```
    

??? columnstyle "slot_ct    (smallint)"
    ```{.codeblock}
    Player lineup position
    ```
    

??? columnstyle "seq_ct    (smallint)"
    ```{.codeblock}
    Player is nth person of game to play in that lineup slot
    ```
    

??? columnstyle "home_fl    (boolean)"
    ```{.codeblock}
    Player is playing at home
    ```
    

??? columnstyle "opponent_id    (char(3))"
    ```{.codeblock}
    Team opponent ID
    ```
    

??? columnstyle "park_id    (char(5))"
    ```{.codeblock}
    Park ID
    ```
    

??? columnstyle "b_g    (smallint)"
    ```{.codeblock}
    Games played
    ```
    

??? columnstyle "b_pa    (smallint)"
    ```{.codeblock}
    Plate appearances
    ```
    

??? columnstyle "b_ab    (smallint)"
    ```{.codeblock}
    At bats
    ```
    

??? columnstyle "b_r    (smallint)"
    ```{.codeblock}
    Runs scored
    ```
    

??? columnstyle "b_h    (smallint)"
    ```{.codeblock}
    Hits
    ```
    

??? columnstyle "b_tb    (smallint)"
    ```{.codeblock}
    Total bases
    ```
    

??? columnstyle "b_2b    (smallint)"
    ```{.codeblock}
    Doubles
    ```
    

??? columnstyle "b_3b    (smallint)"
    ```{.codeblock}
    Triples
    ```
    

??? columnstyle "b_hr    (smallint)"
    ```{.codeblock}
    Home runs
    ```
    

??? columnstyle "b_hr4    (smallint)"
    ```{.codeblock}
    Grand slams
    ```
    

??? columnstyle "b_rbi    (smallint)"
    ```{.codeblock}
    Runs batted in
    ```
    

??? columnstyle "b_gw    (smallint)"
    ```{.codeblock}
    Game winning RBI
    ```
    

??? columnstyle "b_bb    (smallint)"
    ```{.codeblock}
    Walks
    ```
    

??? columnstyle "b_ibb    (smallint)"
    ```{.codeblock}
    Intentional walks
    ```
    

??? columnstyle "b_so    (smallint)"
    ```{.codeblock}
    Strikeouts
    ```
    

??? columnstyle "b_gdp    (smallint)"
    ```{.codeblock}
    Grounded into double plays
    ```
    

??? columnstyle "b_hp    (smallint)"
    ```{.codeblock}
    Hit by pitches
    ```
    

??? columnstyle "b_sh    (smallint)"
    ```{.codeblock}
    Sacrifice hits
    ```
    

??? columnstyle "b_sf    (smallint)"
    ```{.codeblock}
    Sacrifice files
    ```
    

??? columnstyle "b_sb    (smallint)"
    ```{.codeblock}
    Stolen bases
    ```
    

??? columnstyle "b_cs    (smallint)"
    ```{.codeblock}
    Caught stealing
    ```
    

??? columnstyle "b_xi    (smallint)"
    ```{.codeblock}
    Reached on interference
    ```
    

??? columnstyle "b_g_dh    (smallint)"
    ```{.codeblock}
    Games as DH
    ```
    

??? columnstyle "b_g_ph    (smallint)"
    ```{.codeblock}
    Games as pinch hitter
    ```
    

??? columnstyle "b_g_pr    (smallint)"
    ```{.codeblock}
    Games as pinch runner
    ```
    

??? columnstyle "p_g    (smallint)"
    ```{.codeblock}
    Games pitched
    ```
    

??? columnstyle "p_gs    (smallint)"
    ```{.codeblock}
    Games as starting pitcher
    ```
    

??? columnstyle "p_cg    (smallint)"
    ```{.codeblock}
    Complete games
    ```
    

??? columnstyle "p_sho    (smallint)"
    ```{.codeblock}
    Shutouts
    ```
    

??? columnstyle "p_gf    (smallint)"
    ```{.codeblock}
    Games finished
    ```
    

??? columnstyle "p_w    (smallint)"
    ```{.codeblock}
    Wins
    ```
    

??? columnstyle "p_l    (smallint)"
    ```{.codeblock}
    Losses
    ```
    

??? columnstyle "p_sv    (smallint)"
    ```{.codeblock}
    Saves
    ```
    

??? columnstyle "p_out    (smallint)"
    ```{.codeblock}
    Outs recorded
    ```
    

??? columnstyle "p_tbf    (smallint)"
    ```{.codeblock}
    Total batters faced
    ```
    

??? columnstyle "p_ab    (smallint)"
    ```{.codeblock}
    At bats against
    ```
    

??? columnstyle "p_r    (smallint)"
    ```{.codeblock}
    Runs allowed
    ```
    

??? columnstyle "p_er    (smallint)"
    ```{.codeblock}
    Earned runs allowed
    ```
    

??? columnstyle "p_h    (smallint)"
    ```{.codeblock}
    Hits allowed
    ```
    

??? columnstyle "p_tb    (smallint)"
    ```{.codeblock}
    Total bases allowed
    ```
    

??? columnstyle "p_2b    (smallint)"
    ```{.codeblock}
    Doubles allowed
    ```
    

??? columnstyle "p_3b    (smallint)"
    ```{.codeblock}
    Triples allowed
    ```
    

??? columnstyle "p_hr    (smallint)"
    ```{.codeblock}
    Home runs allowed
    ```
    

??? columnstyle "p_hr4    (smallint)"
    ```{.codeblock}
    Grand slams allowed
    ```
    

??? columnstyle "p_bb    (smallint)"
    ```{.codeblock}
    Walks allowed
    ```
    

??? columnstyle "p_ibb    (smallint)"
    ```{.codeblock}
    Intentional walks allowed
    ```
    

??? columnstyle "p_so    (smallint)"
    ```{.codeblock}
    Strikeouts against
    ```
    

??? columnstyle "p_gdp    (smallint)"
    ```{.codeblock}
    Grounded into double plays against
    ```
    

??? columnstyle "p_hp    (smallint)"
    ```{.codeblock}
    Hit by pitches allowed
    ```
    

??? columnstyle "p_sh    (smallint)"
    ```{.codeblock}
    Sacrifice hits allowed
    ```
    

??? columnstyle "p_sf    (smallint)"
    ```{.codeblock}
    Sacrifice flies allowed
    ```
    

??? columnstyle "p_xi    (smallint)"
    ```{.codeblock}
    Reached on interference allowed
    ```
    

??? columnstyle "p_wp    (smallint)"
    ```{.codeblock}
    Wild pitches allowed
    ```
    

??? columnstyle "p_bk    (smallint)"
    ```{.codeblock}
    Balks allowed
    ```
    

??? columnstyle "p_ir    (smallint)"
    ```{.codeblock}
    Inherited runners
    ```
    

??? columnstyle "p_irs    (smallint)"
    ```{.codeblock}
    Inherited runners scored
    ```
    

??? columnstyle "p_go    (smallint)"
    ```{.codeblock}
    Groundouts recorded
    ```
    

??? columnstyle "p_ao    (smallint)"
    ```{.codeblock}
    Fly ball outs recorded
    ```
    

??? columnstyle "p_pitch    (smallint)"
    ```{.codeblock}
    Pitches thrown
    ```
    

??? columnstyle "p_strike    (smallint)"
    ```{.codeblock}
    Strikes thrown
    ```
    

??? columnstyle "f_p_g    (smallint)"
    ```{.codeblock}
    Appearances at pitcher
    ```
    

??? columnstyle "f_p_gs    (smallint)"
    ```{.codeblock}
    Starts at pitcher
    ```
    

??? columnstyle "f_p_out    (smallint)"
    ```{.codeblock}
    Outs played as pitcher
    ```
    

??? columnstyle "f_p_tc    (smallint)"
    ```{.codeblock}
    Total chances as pitcher
    ```
    

??? columnstyle "f_p_po    (smallint)"
    ```{.codeblock}
    Putouts as pitcher
    ```
    

??? columnstyle "f_p_a    (smallint)"
    ```{.codeblock}
    Assists as pitcher
    ```
    

??? columnstyle "f_p_e    (smallint)"
    ```{.codeblock}
    Errors as pitcher
    ```
    

??? columnstyle "f_p_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as pitcher
    ```
    

??? columnstyle "f_p_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as pitcher
    ```
    

??? columnstyle "f_c_g    (smallint)"
    ```{.codeblock}
    Appearances at catcher
    ```
    

??? columnstyle "f_c_gs    (smallint)"
    ```{.codeblock}
    Starts at catcher
    ```
    

??? columnstyle "f_c_out    (smallint)"
    ```{.codeblock}
    Outs played as catcher
    ```
    

??? columnstyle "f_c_tc    (smallint)"
    ```{.codeblock}
    Total chances as catcher
    ```
    

??? columnstyle "f_c_po    (smallint)"
    ```{.codeblock}
    Putouts as catcher
    ```
    

??? columnstyle "f_c_a    (smallint)"
    ```{.codeblock}
    Assists as catcher
    ```
    

??? columnstyle "f_c_e    (smallint)"
    ```{.codeblock}
    Errors as catcher
    ```
    

??? columnstyle "f_c_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as catcher
    ```
    

??? columnstyle "f_c_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as catcher
    ```
    

??? columnstyle "f_c_pb    (smallint)"
    ```{.codeblock}
    Passed balls
    ```
    

??? columnstyle "f_c_xi    (smallint)"
    ```{.codeblock}
    Catcher's interference
    ```
    

??? columnstyle "f_1b_g    (smallint)"
    ```{.codeblock}
    Appearances at first baseman
    ```
    

??? columnstyle "f_1b_gs    (smallint)"
    ```{.codeblock}
    Starts at first baseman
    ```
    

??? columnstyle "f_1b_out    (smallint)"
    ```{.codeblock}
    Outs played as first baseman
    ```
    

??? columnstyle "f_1b_tc    (smallint)"
    ```{.codeblock}
    Total chances as first baseman
    ```
    

??? columnstyle "f_1b_po    (smallint)"
    ```{.codeblock}
    Putouts as first baseman
    ```
    

??? columnstyle "f_1b_a    (smallint)"
    ```{.codeblock}
    Assists as first baseman
    ```
    

??? columnstyle "f_1b_e    (smallint)"
    ```{.codeblock}
    Errors as first baseman
    ```
    

??? columnstyle "f_1b_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as first baseman
    ```
    

??? columnstyle "f_1b_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as first baseman
    ```
    

??? columnstyle "f_2b_g    (smallint)"
    ```{.codeblock}
    Appearances at second baseman
    ```
    

??? columnstyle "f_2b_gs    (smallint)"
    ```{.codeblock}
    Starts at second baseman
    ```
    

??? columnstyle "f_2b_out    (smallint)"
    ```{.codeblock}
    Outs played as second baseman
    ```
    

??? columnstyle "f_2b_tc    (smallint)"
    ```{.codeblock}
    Total chances as second baseman
    ```
    

??? columnstyle "f_2b_po    (smallint)"
    ```{.codeblock}
    Putouts as second baseman
    ```
    

??? columnstyle "f_2b_a    (smallint)"
    ```{.codeblock}
    Assists as second baseman
    ```
    

??? columnstyle "f_2b_e    (smallint)"
    ```{.codeblock}
    Errors as second baseman
    ```
    

??? columnstyle "f_2b_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as second baseman
    ```
    

??? columnstyle "f_2b_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as second baseman
    ```
    

??? columnstyle "f_3b_g    (smallint)"
    ```{.codeblock}
    Appearances at third baseman
    ```
    

??? columnstyle "f_3b_gs    (smallint)"
    ```{.codeblock}
    Starts at third baseman
    ```
    

??? columnstyle "f_3b_out    (smallint)"
    ```{.codeblock}
    Outs played as third baseman
    ```
    

??? columnstyle "f_3b_tc    (smallint)"
    ```{.codeblock}
    Total chances as third baseman
    ```
    

??? columnstyle "f_3b_po    (smallint)"
    ```{.codeblock}
    Putouts as third baseman
    ```
    

??? columnstyle "f_3b_a    (smallint)"
    ```{.codeblock}
    Assists as third baseman
    ```
    

??? columnstyle "f_3b_e    (smallint)"
    ```{.codeblock}
    Errors as third baseman
    ```
    

??? columnstyle "f_3b_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as third baseman
    ```
    

??? columnstyle "f_3b_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as third baseman
    ```
    

??? columnstyle "f_ss_g    (smallint)"
    ```{.codeblock}
    Appearances at shortstop
    ```
    

??? columnstyle "f_ss_gs    (smallint)"
    ```{.codeblock}
    Starts at shortstop
    ```
    

??? columnstyle "f_ss_out    (smallint)"
    ```{.codeblock}
    Outs played as shortstop
    ```
    

??? columnstyle "f_ss_tc    (smallint)"
    ```{.codeblock}
    Total chances as shortstop
    ```
    

??? columnstyle "f_ss_po    (smallint)"
    ```{.codeblock}
    Putouts as shortstop
    ```
    

??? columnstyle "f_ss_a    (smallint)"
    ```{.codeblock}
    Assists as shortstop
    ```
    

??? columnstyle "f_ss_e    (smallint)"
    ```{.codeblock}
    Errors as shortstop
    ```
    

??? columnstyle "f_ss_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as shortstop
    ```
    

??? columnstyle "f_ss_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as shortstop
    ```
    

??? columnstyle "f_lf_g    (smallint)"
    ```{.codeblock}
    Appearances at left fielder
    ```
    

??? columnstyle "f_lf_gs    (smallint)"
    ```{.codeblock}
    Starts at left fielder
    ```
    

??? columnstyle "f_lf_out    (smallint)"
    ```{.codeblock}
    Outs played as left fielder
    ```
    

??? columnstyle "f_lf_tc    (smallint)"
    ```{.codeblock}
    Total chances as left fielder
    ```
    

??? columnstyle "f_lf_po    (smallint)"
    ```{.codeblock}
    Putouts as left fielder
    ```
    

??? columnstyle "f_lf_a    (smallint)"
    ```{.codeblock}
    Assists as left fielder
    ```
    

??? columnstyle "f_lf_e    (smallint)"
    ```{.codeblock}
    Errors as left fielder
    ```
    

??? columnstyle "f_lf_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as left fielder
    ```
    

??? columnstyle "f_lf_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as left fielder
    ```
    

??? columnstyle "f_cf_g    (smallint)"
    ```{.codeblock}
    Appearances at center fielder
    ```
    

??? columnstyle "f_cf_gs    (smallint)"
    ```{.codeblock}
    Starts at center fielder
    ```
    

??? columnstyle "f_cf_out    (smallint)"
    ```{.codeblock}
    Outs played as center fielder
    ```
    

??? columnstyle "f_cf_tc    (smallint)"
    ```{.codeblock}
    Total chances as center fielder
    ```
    

??? columnstyle "f_cf_po    (smallint)"
    ```{.codeblock}
    Putouts as center fielder
    ```
    

??? columnstyle "f_cf_a    (smallint)"
    ```{.codeblock}
    Assists as center fielder
    ```
    

??? columnstyle "f_cf_e    (smallint)"
    ```{.codeblock}
    Errors as center fielder
    ```
    

??? columnstyle "f_cf_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as center fielder
    ```
    

??? columnstyle "f_cf_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as center fielder
    ```
    

??? columnstyle "f_rf_g    (smallint)"
    ```{.codeblock}
    Appearances at right fielder
    ```
    

??? columnstyle "f_rf_gs    (smallint)"
    ```{.codeblock}
    Starts at right fielder
    ```
    

??? columnstyle "f_rf_out    (smallint)"
    ```{.codeblock}
    Outs played as right fielder
    ```
    

??? columnstyle "f_rf_tc    (smallint)"
    ```{.codeblock}
    Total chances as right fielder
    ```
    

??? columnstyle "f_rf_po    (smallint)"
    ```{.codeblock}
    Putouts as right fielder
    ```
    

??? columnstyle "f_rf_a    (smallint)"
    ```{.codeblock}
    Assists as right fielder
    ```
    

??? columnstyle "f_rf_e    (smallint)"
    ```{.codeblock}
    Errors as right fielder
    ```
    

??? columnstyle "f_rf_dp    (smallint)"
    ```{.codeblock}
    Double plays turned as right fielder
    ```
    

??? columnstyle "f_rf_tp    (smallint)"
    ```{.codeblock}
    Triple pays turned as right fielder
    ```
    



### deduced_game

??? keycolumnstyle "game_id    (char(12))"
    ```{.codeblock}
    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    



### event

??? keycolumnstyle "game_id    (char(12))"
    ```{.codeblock}
    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? keycolumnstyle "event_id    (integer)"
    ```{.codeblock}
    Event number of game
    ```
    

??? columnstyle "away_team_id    (char(3))"
    ```{.codeblock}
    Visiting Team
    ```
    

??? columnstyle "inn_ct    (smallint)"
    ```{.codeblock}
    Inning
    ```
    

??? columnstyle "bat_home_id    (boolean)"
    ```{.codeblock}
    Home team is batting
    ```
    

??? columnstyle "outs_ct    (smallint)"
    ```{.codeblock}
    Outs (0-2)
    ```
    

??? columnstyle "balls_ct    (smallint)"
    ```{.codeblock}
    Balls (0-3)
    ```
    

??? columnstyle "strikes_ct    (smallint)"
    ```{.codeblock}
    Strikes (0-2
    ```
    

??? columnstyle "pitch_seq_tx    (varchar(30))"
    ```{.codeblock}
    Pitch sequence
    ```
    

??? columnstyle "away_score_ct    (smallint)"
    ```{.codeblock}
    Away score
    ```
    

??? columnstyle "home_score_ct    (smallint)"
    ```{.codeblock}
    Home score
    ```
    

??? columnstyle "bat_id    (char(8))"
    ```{.codeblock}
    Batter ID
    ```
    

??? columnstyle "bat_hand_cd    (char(1))"
    ```{.codeblock}
    Batter handedness
    ```
    

??? columnstyle "resp_bat_id    (char(8))"
    ```{.codeblock}
    ID of batter charged with event
    ```
    

??? columnstyle "resp_bat_hand_cd    (char(1))"
    ```{.codeblock}
    Handedness of batter charged with event
    ```
    

??? columnstyle "pit_id    (char(8))"
    ```{.codeblock}
    Pitcher ID
    ```
    

??? columnstyle "pit_hand_cd    (char(1))"
    ```{.codeblock}
    Pitcher handedness
    ```
    

??? columnstyle "resp_pit_id    (char(8))"
    ```{.codeblock}
    ID of pitcher charged with event
    ```
    

??? columnstyle "resp_pit_hand_cd    (char(1))"
    ```{.codeblock}
    Handedness of pitcher charged with event
    ```
    

??? columnstyle "pos2_fld_id    (char(8))"
    ```{.codeblock}
    Catcher ID
    ```
    

??? columnstyle "pos3_fld_id    (char(8))"
    ```{.codeblock}
    First baseman ID
    ```
    

??? columnstyle "pos4_fld_id    (char(8))"
    ```{.codeblock}
    Second baseman ID
    ```
    

??? columnstyle "pos5_fld_id    (char(8))"
    ```{.codeblock}
    Third baseman ID
    ```
    

??? columnstyle "pos6_fld_id    (char(8))"
    ```{.codeblock}
    Shortstop ID
    ```
    

??? columnstyle "pos7_fld_id    (char(8))"
    ```{.codeblock}
    Left fielder ID
    ```
    

??? columnstyle "pos8_fld_id    (char(8))"
    ```{.codeblock}
    Center fielder ID
    ```
    

??? columnstyle "pos9_fld_id    (char(8))"
    ```{.codeblock}
    Right fielder ID
    ```
    

??? columnstyle "base1_run_id    (char(8))"
    ```{.codeblock}
    ID of runner on first
    ```
    

??? columnstyle "base2_run_id    (char(8))"
    ```{.codeblock}
    ID of runner on second
    ```
    

??? columnstyle "base3_run_id    (char(8))"
    ```{.codeblock}
    ID of runner on third
    ```
    

??? columnstyle "event_tx    (varchar(128))"
    ```{.codeblock}
    Event text (in scoring shorthand
    ```
    

??? columnstyle "leadoff_fl    (boolean)"
    ```{.codeblock}
    Batter is leading off the inning
    ```
    

??? columnstyle "ph_fl    (boolean)"
    ```{.codeblock}
    Batter is pinch-hitting
    ```
    

??? columnstyle "bat_fld_cd    (smallint)"
    ```{.codeblock}
    Defensive position of batter (10 for DH, 11 for PH, 12 for PR
    ```
    

??? columnstyle "bat_lineup_id    (smallint)"
    ```{.codeblock}
    Lineup position (1-9)
    ```
    

??? columnstyle "event_cd    (smallint)"
    ```{.codeblock}
    Event code (join table `code_event` for descriptions
    ```
    

??? columnstyle "bat_event_fl    (boolean)"
    ```{.codeblock}
    Event is related to the batter
    ```
    

??? columnstyle "ab_fl    (boolean)"
    ```{.codeblock}
    Event is an at-bat
    ```
    

??? columnstyle "h_fl    (smallint)"
    ```{.codeblock}
    Event is a hit
    ```
    

??? columnstyle "sh_fl    (boolean)"
    ```{.codeblock}
    Event is a sacrifice hit
    ```
    

??? columnstyle "sf_fl    (boolean)"
    ```{.codeblock}
    Event is a sacrifice fly
    ```
    

??? columnstyle "event_outs_ct    (smallint)"
    ```{.codeblock}
    Outs recorded on event (0-3)
    ```
    

??? columnstyle "dp_fl    (boolean)"
    ```{.codeblock}
    Event is a double play
    ```
    

??? columnstyle "tp_fl    (boolean)"
    ```{.codeblock}
    Event is a triple play
    ```
    

??? columnstyle "rbi_ct    (smallint)"
    ```{.codeblock}
    Runs batted in on event
    ```
    

??? columnstyle "wp_fl    (boolean)"
    ```{.codeblock}
    Event is a wild pitch
    ```
    

??? columnstyle "pb_fl    (boolean)"
    ```{.codeblock}
    Event is a passed ball
    ```
    

??? columnstyle "fld_cd    (smallint)"
    ```{.codeblock}
    Position id of event fielder
    ```
    

??? columnstyle "battedball_cd    (char(1))"
    ```{.codeblock}
    Batted ball code (P - pop-up, G - ground ball, F - fly ball, L - line drive
    ```
    

??? columnstyle "bunt_fl    (boolean)"
    ```{.codeblock}
    Event is a bunt
    ```
    

??? columnstyle "foul_fl    (boolean)"
    ```{.codeblock}
    Event is a foul ball
    ```
    

??? columnstyle "battedball_loc_tx    (varchar(5))"
    ```{.codeblock}
    Hit location code (see https://www.retrosheet.org/location.htm)
    ```
    

??? columnstyle "err_ct    (smallint)"
    ```{.codeblock}
    Number of errors recorded during event
    ```
    

??? columnstyle "err1_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder committing first error during event
    ```
    

??? columnstyle "err1_cd    (char(1))"
    ```{.codeblock}
    First error type (T - throwing, F - fielding)
    ```
    

??? columnstyle "err2_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder committing second error during event
    ```
    

??? columnstyle "err2_cd    (char(1))"
    ```{.codeblock}
    Second error type (T - throwing, F - fielding)
    ```
    

??? columnstyle "err3_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder committing third error during event
    ```
    

??? columnstyle "err3_cd    (char(1))"
    ```{.codeblock}
    Third error type (T - throwing, F - fielding)
    ```
    

??? columnstyle "bat_dest_id    (smallint)"
    ```{.codeblock}
    Destination of batter after event (0 - putout, 1-3 - bases, 4 - scored asearned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "run1_dest_id    (smallint)"
    ```{.codeblock}
    Destination of runner on first after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "run2_dest_id    (smallint)"
    ```{.codeblock}
    Destination of runner on second after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "run3_dest_id    (smallint)"
    ```{.codeblock}
    Destination of runner on third after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "bat_play_tx    (varchar(15))"
    ```{.codeblock}
    Fielding play on batter
    ```
    

??? columnstyle "run1_play_tx    (varchar(15))"
    ```{.codeblock}
    Fielding play on runner on first
    ```
    

??? columnstyle "run2_play_tx    (varchar(15))"
    ```{.codeblock}
    Fielding play on runner on second
    ```
    

??? columnstyle "run3_play_tx    (varchar(15))"
    ```{.codeblock}
    Fielding play on runner on third
    ```
    

??? columnstyle "run1_sb_fl    (boolean)"
    ```{.codeblock}
    Runner on first steals base
    ```
    

??? columnstyle "run2_sb_fl    (boolean)"
    ```{.codeblock}
    Runner on second steals base
    ```
    

??? columnstyle "run3_sb_fl    (boolean)"
    ```{.codeblock}
    Runner on third steals base
    ```
    

??? columnstyle "run1_cs_fl    (boolean)"
    ```{.codeblock}
    Runner on first caught stealing
    ```
    

??? columnstyle "run2_cs_fl    (boolean)"
    ```{.codeblock}
    Runner on second caught stealing
    ```
    

??? columnstyle "run3_cs_fl    (boolean)"
    ```{.codeblock}
    Runner on third caught stealing
    ```
    

??? columnstyle "run1_pk_fl    (boolean)"
    ```{.codeblock}
    Runner on first picked off
    ```
    

??? columnstyle "run2_pk_fl    (boolean)"
    ```{.codeblock}
    Runner on second picked off
    ```
    

??? columnstyle "run3_pk_fl    (boolean)"
    ```{.codeblock}
    Runner on third picked off
    ```
    

??? columnstyle "run1_resp_pit_id    (char(8))"
    ```{.codeblock}
    ID of pitcher charged with runner on first
    ```
    

??? columnstyle "run2_resp_pit_id    (char(8))"
    ```{.codeblock}
    ID of pitcher charged with runner on second
    ```
    

??? columnstyle "run3_resp_pit_id    (char(8))"
    ```{.codeblock}
    ID of pitcher charged with runner on third
    ```
    

??? columnstyle "game_new_fl    (boolean)"
    ```{.codeblock}
    Start of game flag
    ```
    

??? columnstyle "game_end_fl    (boolean)"
    ```{.codeblock}
    End of game flag
    ```
    

??? columnstyle "pr_run1_fl    (boolean)"
    ```{.codeblock}
    Pinch-runner on first
    ```
    

??? columnstyle "pr_run2_fl    (boolean)"
    ```{.codeblock}
    Pinch-runner on second
    ```
    

??? columnstyle "pr_run3_fl    (boolean)"
    ```{.codeblock}
    Runner on third
    ```
    

??? columnstyle "removed_for_pr_run1_id    (char(8))"
    ```{.codeblock}
    ID of former runner on first removed for pinch-runner
    ```
    

??? columnstyle "removed_for_pr_run2_id    (char(8))"
    ```{.codeblock}
    ID of former runner on second removed for pinch-runner
    ```
    

??? columnstyle "removed_for_pr_run3_id    (char(8))"
    ```{.codeblock}
    ID of former runner on third removed for pinch-runner
    ```
    

??? columnstyle "removed_for_ph_bat_id    (char(8))"
    ```{.codeblock}
    ID of former batter removed for pinch-hitter
    ```
    

??? columnstyle "removed_for_ph_bat_fld_cd    (integer)"
    ```{.codeblock}
    Position code of batter removed for pinch-hitter
    ```
    

??? columnstyle "po1_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with first putout
    ```
    

??? columnstyle "po2_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with second putout
    ```
    

??? columnstyle "po3_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with third putout
    ```
    

??? columnstyle "ass1_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with first assist
    ```
    

??? columnstyle "ass2_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with second assist
    ```
    

??? columnstyle "ass3_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with third assist
    ```
    

??? columnstyle "ass4_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with fourth assist
    ```
    

??? columnstyle "ass5_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with fifth assist
    ```
    

??? columnstyle "home_team_id    (char(3))"
    ```{.codeblock}
    Home team ID
    ```
    

??? columnstyle "bat_team_id    (char(3))"
    ```{.codeblock}
    Batting team ID
    ```
    

??? columnstyle "fld_team_id    (char(3))"
    ```{.codeblock}
    Fielding team ID
    ```
    

??? columnstyle "bat_last_id    (smallint)"
    ```{.codeblock}
    Half inning (differs from batting team if home team bats first)
    ```
    

??? columnstyle "inn_new_fl    (boolean)"
    ```{.codeblock}
    Start of half-inning flag
    ```
    

??? columnstyle "inn_end_fl    (boolean)"
    ```{.codeblock}
    End of half-inning flag
    ```
    

??? columnstyle "start_bat_score_ct    (smallint)"
    ```{.codeblock}
    Runs scored by batting team (prior to this event)
    ```
    

??? columnstyle "start_fld_score_ct    (smallint)"
    ```{.codeblock}
    Runs scored by fielding team
    ```
    

??? columnstyle "inn_runs_ct    (smallint)"
    ```{.codeblock}
    Runs scored in this half-inning (prior to this event)
    ```
    

??? columnstyle "game_pa_ct    (smallint)"
    ```{.codeblock}
    Batting team PA total (prior to this event)
    ```
    

??? columnstyle "inn_pa_ct    (smallint)"
    ```{.codeblock}
    Half-inning PA total (prior to this event)
    ```
    

??? columnstyle "pa_new_fl    (boolean)"
    ```{.codeblock}
    Event is the start of a plate appearance
    ```
    

??? columnstyle "pa_trunc_fl    (boolean)"
    ```{.codeblock}
    Event is a truncated plate appearance
    ```
    

??? columnstyle "start_bases_cd    (smallint)"
    ```{.codeblock}
    Base state at start of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
    ```
    

??? columnstyle "end_bases_cd    (smallint)"
    ```{.codeblock}
    Base state end of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
    ```
    

??? columnstyle "bat_start_fl    (boolean)"
    ```{.codeblock}
    Batter started game
    ```
    

??? columnstyle "resp_bat_start_fl    (boolean)"
    ```{.codeblock}
    Result-charged batter is a starter
    ```
    

??? columnstyle "bat_on_deck_id    (char(8))"
    ```{.codeblock}
    ID of batter on deck
    ```
    

??? columnstyle "bat_in_hold_id    (char(8))"
    ```{.codeblock}
    Id of batter in the hole
    ```
    

??? columnstyle "pit_start_fl    (boolean)"
    ```{.codeblock}
    Pitcher started game
    ```
    

??? columnstyle "resp_pit_start_fl    (boolean)"
    ```{.codeblock}
    Result-charged pitcher started game
    ```
    

??? columnstyle "run1_fld_cd    (smallint)"
    ```{.codeblock}
    Defensive position code of runner on first
    ```
    

??? columnstyle "run1_lineup_cd    (smallint)"
    ```{.codeblock}
    Lineup position of runner on first
    ```
    

??? columnstyle "run1_origin_event_id    (smallint)"
    ```{.codeblock}
    Event number on which runner on first reached base
    ```
    

??? columnstyle "run2_fld_cd    (smallint)"
    ```{.codeblock}
    Defensive position code of runner on second
    ```
    

??? columnstyle "run2_lineup_cd    (smallint)"
    ```{.codeblock}
    Lineup position of runner on second
    ```
    

??? columnstyle "run2_origin_event_id    (smallint)"
    ```{.codeblock}
    Event number on which runner on second reached base
    ```
    

??? columnstyle "run3_fld_cd    (smallint)"
    ```{.codeblock}
    Defensive position code of runner on third
    ```
    

??? columnstyle "run3_lineup_cd    (smallint)"
    ```{.codeblock}
    Lineup position of runner on third
    ```
    

??? columnstyle "run3_origin_event_id    (smallint)"
    ```{.codeblock}
    Event number on which runner on third reached base
    ```
    

??? columnstyle "run1_resp_cat_id    (char(8))"
    ```{.codeblock}
    ID of responsible catcher for runner on first
    ```
    

??? columnstyle "run2_resp_cat_id    (char(8))"
    ```{.codeblock}
    ID of responsible catcher for runner on second
    ```
    

??? columnstyle "run3_resp_cat_id    (char(8))"
    ```{.codeblock}
    ID of responsible catcher for runner on third
    ```
    

??? columnstyle "pa_ball_ct    (smallint)"
    ```{.codeblock}
    Number of balls in plate appearance
    ```
    

??? columnstyle "pa_called_ball_ct    (smallint)"
    ```{.codeblock}
    Number of called balls in plate appearance
    ```
    

??? columnstyle "pa_intent_ball_ct    (smallint)"
    ```{.codeblock}
    Number of intentional balls in plate appearance
    ```
    

??? columnstyle "pa_pitchout_ball_ct    (smallint)"
    ```{.codeblock}
    Number of pitchouts in plate appearance
    ```
    

??? columnstyle "pa_hitbatter_ball_ct    (smallint)"
    ```{.codeblock}
    Number of pitches hitting batter in plate appearance
    ```
    

??? columnstyle "pa_other_ball_ct    (smallint)"
    ```{.codeblock}
    Number of other balls in plate appearance
    ```
    

??? columnstyle "pa_strike_ct    (smallint)"
    ```{.codeblock}
    Number of strikes in plate appearance
    ```
    

??? columnstyle "pa_called_strike_ct    (smallint)"
    ```{.codeblock}
    Number of called strikes in plate appearance
    ```
    

??? columnstyle "pa_swingmiss_strike_ct    (smallint)"
    ```{.codeblock}
    Number of swing-and-miss strikes in plate appearance
    ```
    

??? columnstyle "pa_foul_strike_ct    (smallint)"
    ```{.codeblock}
    Number of foul balls in plate appearance
    ```
    

??? columnstyle "pa_inplay_strike_ct    (smallint)"
    ```{.codeblock}
    Number of balls in play in plate appearance
    ```
    

??? columnstyle "pa_other_strike_ct    (smallint)"
    ```{.codeblock}
    Number of other strikes in plate appearance
    ```
    

??? columnstyle "event_runs_ct    (smallint)"
    ```{.codeblock}
    Number of runs on play
    ```
    

??? columnstyle "fld_id    (char(8))"
    ```{.codeblock}
    ID of player fielding batted ball
    ```
    

??? columnstyle "base2_force_fl    (boolean)"
    ```{.codeblock}
    Event has force play at second
    ```
    

??? columnstyle "base3_force_fl    (boolean)"
    ```{.codeblock}
    Event has force play at third
    ```
    

??? columnstyle "base4_force_fl    (boolean)"
    ```{.codeblock}
    Event has force play at home
    ```
    

??? columnstyle "bat_safe_err_fl    (boolean)"
    ```{.codeblock}
    Event has batter safe on an error
    ```
    

??? columnstyle "bat_fate_id    (smallint)"
    ```{.codeblock}
    Ultimate fate of batter (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "run1_fate_id    (smallint)"
    ```{.codeblock}
    Ultimate fate of runner on first (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "run2_fate_id    (smallint)"
    ```{.codeblock}
    Ultimate fate of runner on second (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "run3_fate_id    (smallint)"
    ```{.codeblock}
    Ultimate fate of runner on third (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "fate_runs_ct    (smallint)"
    ```{.codeblock}
    Additional runs scored in half inning after this event
    ```
    

??? columnstyle "ass6_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with sixth assist
    ```
    

??? columnstyle "ass7_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with seventh assist
    ```
    

??? columnstyle "ass8_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with eighth assist
    ```
    

??? columnstyle "ass9_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with ninth assist
    ```
    

??? columnstyle "ass10_fld_cd    (smallint)"
    ```{.codeblock}
    Position code of fielder with tenth assist
    ```
    

??? columnstyle "unknown_out_exc_fl    (boolean)"
    ```{.codeblock}
    Unknown fielding credit flag
    ```
    

??? columnstyle "uncertain_play_exc_fl    (boolean)"
    ```{.codeblock}
    Uncertain play flag
    ```
    



### game

??? keycolumnstyle "game_id    (char(12))"
    ```{.codeblock}
    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "game_dt    (date)"
    ```{.codeblock}
    Game date
    ```
    

??? columnstyle "game_ct    (smallint)"
    ```{.codeblock}
    Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
    ```
    

??? columnstyle "game_dy    (varchar(9))"
    ```{.codeblock}
    Day of week
    ```
    

??? columnstyle "start_game_tm    (smallint)"
    ```{.codeblock}
    Game start time (12HMM coded as integer, eg 1015 for 10:15 PM)
    ```
    

??? columnstyle "dh_fl    (varchar(1))"
    ```{.codeblock}
    DH used
    ```
    

??? columnstyle "daynight_park_cd    (varchar(1))"
    ```{.codeblock}
    D - day game, N - night game
    ```
    

??? columnstyle "away_team_id    (char(3))"
    ```{.codeblock}
    Away team ID
    ```
    

??? columnstyle "home_team_id    (char(3))"
    ```{.codeblock}
    Home team ID
    ```
    

??? columnstyle "park_id    (varchar(5))"
    ```{.codeblock}
    Park ID
    ```
    

??? columnstyle "away_start_pit_id    (char(8))"
    ```{.codeblock}
    Away team starting pitcher ID
    ```
    

??? columnstyle "home_start_pit_id    (char(8))"
    ```{.codeblock}
    Home team starting pitcher ID
    ```
    

??? columnstyle "base4_ump_id    (varchar(32))"
    ```{.codeblock}
    Home plate umpire ID
    ```
    

??? columnstyle "base1_ump_id    (varchar(32))"
    ```{.codeblock}
    First base umpire ID
    ```
    

??? columnstyle "base2_ump_id    (varchar(32))"
    ```{.codeblock}
    Second base umpire ID
    ```
    

??? columnstyle "base3_ump_id    (varchar(32))"
    ```{.codeblock}
    Third base umpire ID
    ```
    

??? columnstyle "lf_ump_id    (char(8))"
    ```{.codeblock}
    Left field umpire ID
    ```
    

??? columnstyle "rf_ump_id    (char(8))"
    ```{.codeblock}
    Right field umpire ID
    ```
    

??? columnstyle "attend_park_ct    (integer)"
    ```{.codeblock}
    Attendance
    ```
    

??? columnstyle "scorer_record_id    (varchar(50))"
    ```{.codeblock}
    Scorekeeper
    ```
    

??? columnstyle "translator_record_id    (varchar(50))"
    ```{.codeblock}
    Translator
    ```
    

??? columnstyle "inputter_record_id    (varchar(50))"
    ```{.codeblock}
    Inputter
    ```
    

??? columnstyle "input_record_ts    (varchar(20))"
    ```{.codeblock}
    Date and time of record input
    ```
    

??? columnstyle "edit_record_ts    (varchar(20))"
    ```{.codeblock}
    Date and time of Most recent record edit
    ```
    

??? columnstyle "method_record_cd    (varchar(1))"
    ```{.codeblock}
    How the game was scored (join `code_method_record` for details
    ```
    

??? columnstyle "pitches_record_cd    (varchar(1))"
    ```{.codeblock}
    Highest detail of pitches recorded (join `code_pitches_record` for details). Note that many games with pitch detail do not have that info for all events, so pitch totals may not be accurate.
    ```
    

??? columnstyle "temp_park_ct    (smallint)"
    ```{.codeblock}
    Park temperature in degrees F (0 if unknown)
    ```
    

??? columnstyle "wind_direction_park_cd    (smallint)"
    ```{.codeblock}
    Wind direction park code (join `code_wind_direction_park` for details)
    ```
    

??? columnstyle "wind_speed_park_ct    (smallint)"
    ```{.codeblock}
    Wind speed in miles per hour (-1 if unknown)
    ```
    

??? columnstyle "field_park_cd    (smallint)"
    ```{.codeblock}
    Park field condition code (join `code_field_park` for details)
    ```
    

??? columnstyle "precip_park_cd    (smallint)"
    ```{.codeblock}
    Park precipitation code (join `code_precip_park` for details
    ```
    

??? columnstyle "sky_park_cd    (smallint)"
    ```{.codeblock}
    Park sky condition code (join `code_sky_park` for details
    ```
    

??? columnstyle "minutes_game_ct    (smallint)"
    ```{.codeblock}
    Length of game in minutes
    ```
    

??? columnstyle "inn_ct    (smallint)"
    ```{.codeblock}
    Length of game in innings
    ```
    

??? columnstyle "away_score_ct    (smallint)"
    ```{.codeblock}
    Away team final score
    ```
    

??? columnstyle "home_score_ct    (smallint)"
    ```{.codeblock}
    Home team final score
    ```
    

??? columnstyle "away_hits_ct    (smallint)"
    ```{.codeblock}
    Away team hits
    ```
    

??? columnstyle "home_hits_ct    (smallint)"
    ```{.codeblock}
    Home team hits
    ```
    

??? columnstyle "away_err_ct    (smallint)"
    ```{.codeblock}
    Away team errors
    ```
    

??? columnstyle "home_err_ct    (smallint)"
    ```{.codeblock}
    Home team errors
    ```
    

??? columnstyle "away_lob_ct    (smallint)"
    ```{.codeblock}
    Away team left on base
    ```
    

??? columnstyle "home_lob_ct    (smallint)"
    ```{.codeblock}
    Home team left on base
    ```
    

??? columnstyle "win_pit_id    (char(8))"
    ```{.codeblock}
    ID of winning pitcher
    ```
    

??? columnstyle "lose_pit_id    (char(8))"
    ```{.codeblock}
    ID of losing pitcher
    ```
    

??? columnstyle "save_pit_id    (char(8))"
    ```{.codeblock}
    ID of saving pitcher
    ```
    

??? columnstyle "gwrbi_bat_id    (char(8))"
    ```{.codeblock}
    ID of batter wit game-winning RBI
    ```
    

??? columnstyle "away_lineup1_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 1
    ```
    

??? columnstyle "away_lineup1_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 1
    ```
    

??? columnstyle "away_lineup2_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 2
    ```
    

??? columnstyle "away_lineup2_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 2
    ```
    

??? columnstyle "away_lineup3_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 3
    ```
    

??? columnstyle "away_lineup3_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 3
    ```
    

??? columnstyle "away_lineup4_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 4
    ```
    

??? columnstyle "away_lineup4_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 4
    ```
    

??? columnstyle "away_lineup5_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 5
    ```
    

??? columnstyle "away_lineup5_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 5
    ```
    

??? columnstyle "away_lineup6_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 6
    ```
    

??? columnstyle "away_lineup6_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 6
    ```
    

??? columnstyle "away_lineup7_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 7
    ```
    

??? columnstyle "away_lineup7_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 7
    ```
    

??? columnstyle "away_lineup8_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 8
    ```
    

??? columnstyle "away_lineup8_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 8
    ```
    

??? columnstyle "away_lineup9_bat_id    (char(8))"
    ```{.codeblock}
    ID of away team starting batter in lineup position 9
    ```
    

??? columnstyle "away_lineup9_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of away team starting batter in lineup position 9
    ```
    

??? columnstyle "home_lineup1_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 1
    ```
    

??? columnstyle "home_lineup1_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 1
    ```
    

??? columnstyle "home_lineup2_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 2
    ```
    

??? columnstyle "home_lineup2_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 2
    ```
    

??? columnstyle "home_lineup3_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 3
    ```
    

??? columnstyle "home_lineup3_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 3
    ```
    

??? columnstyle "home_lineup4_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 4
    ```
    

??? columnstyle "home_lineup4_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 4
    ```
    

??? columnstyle "home_lineup5_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 5
    ```
    

??? columnstyle "home_lineup5_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 5
    ```
    

??? columnstyle "home_lineup6_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 6
    ```
    

??? columnstyle "home_lineup6_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 6
    ```
    

??? columnstyle "home_lineup7_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 7
    ```
    

??? columnstyle "home_lineup7_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 7
    ```
    

??? columnstyle "home_lineup8_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 8
    ```
    

??? columnstyle "home_lineup8_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 8
    ```
    

??? columnstyle "home_lineup9_bat_id    (char(8))"
    ```{.codeblock}
    ID of home team starting batter in lineup position 9
    ```
    

??? columnstyle "home_lineup9_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position code of home team starting batter in lineup position 9
    ```
    

??? columnstyle "away_finish_pit_id    (char(8))"
    ```{.codeblock}
    Away team finishing pitcher
    ```
    

??? columnstyle "home_finish_pit_id    (char(8))"
    ```{.codeblock}
    Home team finishing pitcher
    ```
    

??? columnstyle "away_team_league_id    (char(1))"
    ```{.codeblock}
    Away team league (1 char ID)
    ```
    

??? columnstyle "home_team_league_id    (char(1))"
    ```{.codeblock}
    Home team league (1 char ID)
    ```
    

??? columnstyle "away_team_game_ct    (smallint)"
    ```{.codeblock}
    Away team game number
    ```
    

??? columnstyle "home_team_game_ct    (smallint)"
    ```{.codeblock}
    Home team game number
    ```
    

??? columnstyle "outs_ct    (smallint)"
    ```{.codeblock}
    Length of game in outs
    ```
    

??? columnstyle "completion_tx    (varchar(26))"
    ```{.codeblock}
    Information on completion of game
    ```
    

??? columnstyle "forfeit_tx    (varchar(26))"
    ```{.codeblock}
    Information on forfeit of game
    ```
    

??? columnstyle "protest_tx    (varchar(26))"
    ```{.codeblock}
    Information on protest of game
    ```
    

??? columnstyle "away_line_tx    (varchar(26))"
    ```{.codeblock}
    Away team linescore
    ```
    

??? columnstyle "home_line_tx    (varchar(26))"
    ```{.codeblock}
    Home team linescore
    ```
    

??? columnstyle "away_ab_ct    (smallint)"
    ```{.codeblock}
    Away team at bats
    ```
    

??? columnstyle "away_2b_ct    (smallint)"
    ```{.codeblock}
    Away team doubles
    ```
    

??? columnstyle "away_3b_ct    (smallint)"
    ```{.codeblock}
    Away team triples
    ```
    

??? columnstyle "away_hr_ct    (smallint)"
    ```{.codeblock}
    Away team home runs
    ```
    

??? columnstyle "away_bi_ct    (smallint)"
    ```{.codeblock}
    Away team runs batted in
    ```
    

??? columnstyle "away_sh_ct    (smallint)"
    ```{.codeblock}
    Away team sacrifice hits
    ```
    

??? columnstyle "away_sf_ct    (smallint)"
    ```{.codeblock}
    Away team sacrifice flies
    ```
    

??? columnstyle "away_hp_ct    (smallint)"
    ```{.codeblock}
    Away team hit by pitches
    ```
    

??? columnstyle "away_bb_ct    (smallint)"
    ```{.codeblock}
    Away team walks
    ```
    

??? columnstyle "away_ibb_ct    (smallint)"
    ```{.codeblock}
    Away team intentional walks
    ```
    

??? columnstyle "away_so_ct    (smallint)"
    ```{.codeblock}
    Away team strikeouts
    ```
    

??? columnstyle "away_sb_ct    (smallint)"
    ```{.codeblock}
    Away team stolen bases
    ```
    

??? columnstyle "away_cs_ct    (smallint)"
    ```{.codeblock}
    Away team caught stealing
    ```
    

??? columnstyle "away_gdp_ct    (smallint)"
    ```{.codeblock}
    Away team grounded into double plays
    ```
    

??? columnstyle "away_xi_ct    (smallint)"
    ```{.codeblock}
    Away team reached on interference
    ```
    

??? columnstyle "away_pitcher_ct    (smallint)"
    ```{.codeblock}
    Away team number of pitchers used
    ```
    

??? columnstyle "away_er_ct    (smallint)"
    ```{.codeblock}
    Away team individual earned runs
    ```
    

??? columnstyle "away_ter_ct    (smallint)"
    ```{.codeblock}
    Away team team earned runs
    ```
    

??? columnstyle "away_wp_ct    (smallint)"
    ```{.codeblock}
    Away team wild pitches
    ```
    

??? columnstyle "away_bk_ct    (smallint)"
    ```{.codeblock}
    Away team balks
    ```
    

??? columnstyle "away_po_ct    (smallint)"
    ```{.codeblock}
    Away team putouts
    ```
    

??? columnstyle "away_a_ct    (smallint)"
    ```{.codeblock}
    Away team assists
    ```
    

??? columnstyle "away_pb_ct    (smallint)"
    ```{.codeblock}
    Away team passed balls
    ```
    

??? columnstyle "away_dp_ct    (smallint)"
    ```{.codeblock}
    Away team double plays turned
    ```
    

??? columnstyle "away_tp_ct    (smallint)"
    ```{.codeblock}
    Away team triple plays turned
    ```
    

??? columnstyle "home_ab_ct    (smallint)"
    ```{.codeblock}
    Home team at bats
    ```
    

??? columnstyle "home_2b_ct    (smallint)"
    ```{.codeblock}
    Home team doubles
    ```
    

??? columnstyle "home_3b_ct    (smallint)"
    ```{.codeblock}
    Home team triples
    ```
    

??? columnstyle "home_hr_ct    (smallint)"
    ```{.codeblock}
    Home team home runs
    ```
    

??? columnstyle "home_bi_ct    (smallint)"
    ```{.codeblock}
    Home team runs batted in
    ```
    

??? columnstyle "home_sh_ct    (smallint)"
    ```{.codeblock}
    Home team sacrifice hits
    ```
    

??? columnstyle "home_sf_ct    (smallint)"
    ```{.codeblock}
    Home team sacrifice flies
    ```
    

??? columnstyle "home_hp_ct    (smallint)"
    ```{.codeblock}
    Home team hit by pitches
    ```
    

??? columnstyle "home_bb_ct    (smallint)"
    ```{.codeblock}
    Home team walks
    ```
    

??? columnstyle "home_ibb_ct    (smallint)"
    ```{.codeblock}
    Home team intentional walks
    ```
    

??? columnstyle "home_so_ct    (smallint)"
    ```{.codeblock}
    Home team strikeouts
    ```
    

??? columnstyle "home_sb_ct    (smallint)"
    ```{.codeblock}
    Home team stolen bases
    ```
    

??? columnstyle "home_cs_ct    (smallint)"
    ```{.codeblock}
    Home team caught stealing
    ```
    

??? columnstyle "home_gdp_ct    (smallint)"
    ```{.codeblock}
    Home team grounded into double plays
    ```
    

??? columnstyle "home_xi_ct    (smallint)"
    ```{.codeblock}
    Home team reached on interference
    ```
    

??? columnstyle "home_pitcher_ct    (smallint)"
    ```{.codeblock}
    Home team number of pitchers used
    ```
    

??? columnstyle "home_er_ct    (smallint)"
    ```{.codeblock}
    Home team individual earned runs
    ```
    

??? columnstyle "home_ter_ct    (smallint)"
    ```{.codeblock}
    Home team team earned runs
    ```
    

??? columnstyle "home_wp_ct    (smallint)"
    ```{.codeblock}
    Home team wild pitches
    ```
    

??? columnstyle "home_bk_ct    (smallint)"
    ```{.codeblock}
    Home team balks
    ```
    

??? columnstyle "home_po_ct    (smallint)"
    ```{.codeblock}
    Home team putouts
    ```
    

??? columnstyle "home_a_ct    (smallint)"
    ```{.codeblock}
    Home team assists
    ```
    

??? columnstyle "home_pb_ct    (smallint)"
    ```{.codeblock}
    Home team passed balls
    ```
    

??? columnstyle "home_dp_ct    (smallint)"
    ```{.codeblock}
    Home team double plays turned
    ```
    

??? columnstyle "home_tp_ct    (smallint)"
    ```{.codeblock}
    Home team triple plays turned
    ```
    

??? columnstyle "ump_home_name_tx    (varchar(26))"
    ```{.codeblock}
    Home plate umpire name
    ```
    

??? columnstyle "ump_1b_name_tx    (varchar(26))"
    ```{.codeblock}
    First base umpire name
    ```
    

??? columnstyle "ump_2b_name_tx    (varchar(26))"
    ```{.codeblock}
    Second base umpire name
    ```
    

??? columnstyle "ump_3b_name_tx    (varchar(26))"
    ```{.codeblock}
    Third base umpire name
    ```
    

??? columnstyle "ump_lf_name_tx    (varchar(26))"
    ```{.codeblock}
    Left field umpire name
    ```
    

??? columnstyle "ump_rf_name_tx    (varchar(26))"
    ```{.codeblock}
    Right field umpire name
    ```
    

??? columnstyle "away_manager_id    (char(8))"
    ```{.codeblock}
    Away manager ID
    ```
    

??? columnstyle "away_manager_name_tx    (varchar(26))"
    ```{.codeblock}
    Away manager name
    ```
    

??? columnstyle "home_manager_id    (char(8))"
    ```{.codeblock}
    Home manager ID
    ```
    

??? columnstyle "home_manager_name_tx    (varchar(26))"
    ```{.codeblock}
    Home manager name
    ```
    

??? columnstyle "win_pit_name_tx    (varchar(26))"
    ```{.codeblock}
    Wining pitcher name
    ```
    

??? columnstyle "lose_pit_name_tx    (varchar(26))"
    ```{.codeblock}
    Losing pitcher name
    ```
    

??? columnstyle "save_pit_name_tx    (varchar(26))"
    ```{.codeblock}
    Saving pitcher name
    ```
    

??? columnstyle "goahead_rbi_id    (char(8))"
    ```{.codeblock}
    ID of batter with goahead RBI
    ```
    

??? columnstyle "goahead_rbi_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of batter with goahead RBI
    ```
    

??? columnstyle "away_lineup1_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 1
    ```
    

??? columnstyle "away_lineup2_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 2
    ```
    

??? columnstyle "away_lineup3_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 3
    ```
    

??? columnstyle "away_lineup4_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 4
    ```
    

??? columnstyle "away_lineup5_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 5
    ```
    

??? columnstyle "away_lineup6_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 6
    ```
    

??? columnstyle "away_lineup7_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 7
    ```
    

??? columnstyle "away_lineup8_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of away team batter in lineup position 8
    ```
    

??? columnstyle "away_lineup9_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 9
    ```
    

??? columnstyle "home_lineup1_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 1
    ```
    

??? columnstyle "home_lineup2_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 2
    ```
    

??? columnstyle "home_lineup3_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 3
    ```
    

??? columnstyle "home_lineup4_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 4
    ```
    

??? columnstyle "home_lineup5_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 5
    ```
    

??? columnstyle "home_lineup6_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 6
    ```
    

??? columnstyle "home_lineup7_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 7
    ```
    

??? columnstyle "home_lineup8_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 8
    ```
    

??? columnstyle "home_lineup9_bat_name_tx    (varchar(26))"
    ```{.codeblock}
    Name of home team batter in lineup position 9
    ```
    

??? columnstyle "add_info_tx    (varchar(26))"
    ```{.codeblock}
    Additional information
    ```
    

??? columnstyle "acq_info_tx    (varchar(26))"
    ```{.codeblock}
    Acquisition information
    ```
    



### gamelog

??? keycolumnstyle "date    (date)"
    ```{.codeblock}
    Game date
    ```
    

??? keycolumnstyle "double_header    (char(1))"
    ```{.codeblock}
    Number of game:
    "0" -- a single game
    "1" -- the first game of a double (or triple) header
           including separate admission doubleheaders
    "2" -- the second game of a double (or triple) header
           including separate admission doubleheaders
    "3" -- the third game of a triple-header
    "A" -- the first game of a double-header involving 3 teams
    "B" -- the second game of a double-header involving 3 teams
    
    ```
    

??? keycolumnstyle "visiting_team    (char(3))"
    ```{.codeblock}
    Visiting team ID
    ```
    

??? keycolumnstyle "home_team    (char(3))"
    ```{.codeblock}
    Home team ID
    ```
    

??? columnstyle "day_of_week    (char(3))"
    ```{.codeblock}
    Day of week (3 char abbreviation)
    ```
    

??? columnstyle "visiting_team_league    (char(2))"
    ```{.codeblock}
    Away team league ID
    ```
    

??? columnstyle "visiting_team_game_number    (smallint)"
    ```{.codeblock}
    Away team game number
    ```
    

??? columnstyle "home_team_league    (char(2))"
    ```{.codeblock}
    Home team league ID
    ```
    

??? columnstyle "home_team_game_number    (smallint)"
    ```{.codeblock}
    Home team game number
    ```
    

??? columnstyle "visitor_runs_scored    (smallint)"
    ```{.codeblock}
    Away team runs scored
    ```
    

??? columnstyle "home_runs_score    (smallint)"
    ```{.codeblock}
    Home team runs scored
    ```
    

??? columnstyle "length_in_outs    (smallint)"
    ```{.codeblock}
    Game length in outs
    ```
    

??? columnstyle "day_night    (char(1))"
    ```{.codeblock}
    D - day game, N - night game
    ```
    

??? columnstyle "completion_info    (varchar(23))"
    ```{.codeblock}
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
    
    ```
    

??? columnstyle "forfeit_info    (varchar(3))"
    ```{.codeblock}
    V - forfeited to away team, H - forfeited to home team, T - ruled a no-decision
    ```
    

??? columnstyle "protest_info    (varchar(3))"
    ```{.codeblock}
    P - protested by unidentified team, V - disallowed protest by away team, H - disallowed protest by home team, X - upheld protest by away team, Y - upheld protest by home team
    ```
    

??? columnstyle "park_id    (char(5))"
    ```{.codeblock}
    Park ID
    ```
    

??? columnstyle "attendance    (integer)"
    ```{.codeblock}
    Attendance
    ```
    

??? columnstyle "duration    (smallint)"
    ```{.codeblock}
    Time of game in minutes
    ```
    

??? columnstyle "vistor_line_score    (varchar(26))"
    ```{.codeblock}
    Away team line score, e.g. 010000(10)0x
    ```
    

??? columnstyle "home_line_score    (varchar(26))"
    ```{.codeblock}
    Home team line score, e.g. 010000(10)0x
    ```
    

??? columnstyle "visitor_ab    (smallint)"
    ```{.codeblock}
    Away team at bats
    ```
    

??? columnstyle "visitor_h    (smallint)"
    ```{.codeblock}
    Away team hits
    ```
    

??? columnstyle "visitor_d    (smallint)"
    ```{.codeblock}
    Away team doubles
    ```
    

??? columnstyle "visitor_t    (smallint)"
    ```{.codeblock}
    Away team triples
    ```
    

??? columnstyle "visitor_hr    (smallint)"
    ```{.codeblock}
    Away team home runs
    ```
    

??? columnstyle "visitor_rbi    (smallint)"
    ```{.codeblock}
    Away team runs batted in
    ```
    

??? columnstyle "visitor_sh    (smallint)"
    ```{.codeblock}
    Away team sacrifice hits (may include sac flies before 1954)
    ```
    

??? columnstyle "visitor_sf    (smallint)"
    ```{.codeblock}
    Away team sacrifice flies (since 1954)
    ```
    

??? columnstyle "visitor_hbp    (smallint)"
    ```{.codeblock}
    Away team hit by pitches
    ```
    

??? columnstyle "visitor_bb    (smallint)"
    ```{.codeblock}
    Away team walks
    ```
    

??? columnstyle "visitor_ibb    (smallint)"
    ```{.codeblock}
    Away team intentional walks
    ```
    

??? columnstyle "visitor_k    (smallint)"
    ```{.codeblock}
    Away team strikeouts
    ```
    

??? columnstyle "visitor_sb    (smallint)"
    ```{.codeblock}
    Away team stolen bases
    ```
    

??? columnstyle "visitor_cs    (smallint)"
    ```{.codeblock}
    Away team caught stealing
    ```
    

??? columnstyle "visitor_gdp    (smallint)"
    ```{.codeblock}
    Away team grounded into double plays
    ```
    

??? columnstyle "visitor_ci    (smallint)"
    ```{.codeblock}
    Away team reached on interference
    ```
    

??? columnstyle "visitor_lob    (smallint)"
    ```{.codeblock}
    Away team left on base
    ```
    

??? columnstyle "visitor_pitchers    (smallint)"
    ```{.codeblock}
    Away team pitchers used
    ```
    

??? columnstyle "visitor_er    (smallint)"
    ```{.codeblock}
    Away team individual earned runs allowed
    ```
    

??? columnstyle "visitor_ter    (smallint)"
    ```{.codeblock}
    Away team team earned runs allowed
    ```
    

??? columnstyle "visitor_wp    (smallint)"
    ```{.codeblock}
    Away team wild pitches allowed
    ```
    

??? columnstyle "visitor_balks    (smallint)"
    ```{.codeblock}
    Away team balks allowed
    ```
    

??? columnstyle "visitor_po    (smallint)"
    ```{.codeblock}
    Away team putouts
    ```
    

??? columnstyle "visitor_a    (smallint)"
    ```{.codeblock}
    Away team assists
    ```
    

??? columnstyle "visitor_e    (smallint)"
    ```{.codeblock}
    Away team errors
    ```
    

??? columnstyle "visitor_passed    (smallint)"
    ```{.codeblock}
    Away team passed balls
    ```
    

??? columnstyle "visitor_db    (smallint)"
    ```{.codeblock}
    Away team double plays turned
    ```
    

??? columnstyle "visitor_tp    (smallint)"
    ```{.codeblock}
    Away team triple plays turned
    ```
    

??? columnstyle "home_ab    (smallint)"
    ```{.codeblock}
    Home team at bats
    ```
    

??? columnstyle "home_h    (smallint)"
    ```{.codeblock}
    Home team hits
    ```
    

??? columnstyle "home_d    (smallint)"
    ```{.codeblock}
    Home team doubles
    ```
    

??? columnstyle "home_t    (smallint)"
    ```{.codeblock}
    Home team triples
    ```
    

??? columnstyle "home_hr    (smallint)"
    ```{.codeblock}
    Home team home runs
    ```
    

??? columnstyle "home_rbi    (smallint)"
    ```{.codeblock}
    Home team runs batted in
    ```
    

??? columnstyle "home_sh    (smallint)"
    ```{.codeblock}
    Home team sacrifice hits (may include sac flies before 1954)
    ```
    

??? columnstyle "home_sf    (smallint)"
    ```{.codeblock}
    Home team sacrifice flies (since 1954)
    ```
    

??? columnstyle "home_hbp    (smallint)"
    ```{.codeblock}
    Home team hit by pitches
    ```
    

??? columnstyle "home_bb    (smallint)"
    ```{.codeblock}
    Home team walks
    ```
    

??? columnstyle "home_ibb    (smallint)"
    ```{.codeblock}
    Home team intentional walks
    ```
    

??? columnstyle "home_k    (smallint)"
    ```{.codeblock}
    Home team strikeouts
    ```
    

??? columnstyle "home_sb    (smallint)"
    ```{.codeblock}
    Home team stolen bases
    ```
    

??? columnstyle "home_cs    (smallint)"
    ```{.codeblock}
    Home team caught stealing
    ```
    

??? columnstyle "home_gdp    (smallint)"
    ```{.codeblock}
    Home team grounded into double plays
    ```
    

??? columnstyle "home_ci    (smallint)"
    ```{.codeblock}
    Home team reached on interference
    ```
    

??? columnstyle "home_lob    (smallint)"
    ```{.codeblock}
    Home team left on base
    ```
    

??? columnstyle "home_pitchers    (smallint)"
    ```{.codeblock}
    Home team pitchers used
    ```
    

??? columnstyle "home_er    (smallint)"
    ```{.codeblock}
    Home team individual earned runs allowed
    ```
    

??? columnstyle "home_ter    (smallint)"
    ```{.codeblock}
    Home team team earned runs allowed
    ```
    

??? columnstyle "home_wp    (smallint)"
    ```{.codeblock}
    Home team wild pitches allowed
    ```
    

??? columnstyle "home_balks    (smallint)"
    ```{.codeblock}
    Home team balks allowed
    ```
    

??? columnstyle "home_po    (smallint)"
    ```{.codeblock}
    Home team putouts
    ```
    

??? columnstyle "home_a    (smallint)"
    ```{.codeblock}
    Home team assists
    ```
    

??? columnstyle "home_e    (smallint)"
    ```{.codeblock}
    Home team errors
    ```
    

??? columnstyle "home_passed    (smallint)"
    ```{.codeblock}
    Home team passed balls
    ```
    

??? columnstyle "home_db    (smallint)"
    ```{.codeblock}
    Home team double plays turned
    ```
    

??? columnstyle "home_tp    (smallint)"
    ```{.codeblock}
    Home team triple plays turned
    ```
    

??? columnstyle "umpire_h_id    (char(8))"
    ```{.codeblock}
    Home plate umpire ID
    ```
    

??? columnstyle "umpire_h_name    (varchar(32))"
    ```{.codeblock}
    Home plate umpire name
    ```
    

??? columnstyle "umpire_1b_id    (char(8))"
    ```{.codeblock}
    First base umpire ID
    ```
    

??? columnstyle "umpire_1b_name    (varchar(32))"
    ```{.codeblock}
    First base umpire name
    ```
    

??? columnstyle "umpire_2b_id    (char(8))"
    ```{.codeblock}
    Second base umpire ID
    ```
    

??? columnstyle "umpire_2b_name    (varchar(32))"
    ```{.codeblock}
    Second base umpire name
    ```
    

??? columnstyle "umpire_3b_id    (char(8))"
    ```{.codeblock}
    Third base umpire ID
    ```
    

??? columnstyle "umpire_3b_name    (varchar(32))"
    ```{.codeblock}
    Third base umpire name
    ```
    

??? columnstyle "umpire_lf_id    (char(8))"
    ```{.codeblock}
    Left field umpire ID
    ```
    

??? columnstyle "umpire_lf_name    (varchar(32))"
    ```{.codeblock}
    Left field umpire name
    ```
    

??? columnstyle "umpire_rf_id    (char(8))"
    ```{.codeblock}
    Right field umpire ID
    ```
    

??? columnstyle "umpire_rf_name    (varchar(32))"
    ```{.codeblock}
    Right field umpire name
    ```
    

??? columnstyle "visitor_manager_id    (char(8))"
    ```{.codeblock}
    Away team manager ID
    ```
    

??? columnstyle "visitor_manager_name    (varchar(32))"
    ```{.codeblock}
    Away team manager name
    ```
    

??? columnstyle "home_manager_id    (char(8))"
    ```{.codeblock}
    Home team manager ID
    ```
    

??? columnstyle "home_manager_name    (varchar(32))"
    ```{.codeblock}
    Home team manager name
    ```
    

??? columnstyle "winning_pitcher_id    (char(8))"
    ```{.codeblock}
    Winning pitcher ID
    ```
    

??? columnstyle "winning_pitcher_name    (varchar(32))"
    ```{.codeblock}
    Winning pitcher name
    ```
    

??? columnstyle "losing_pitcher_id    (char(8))"
    ```{.codeblock}
    Losing pitcher ID
    ```
    

??? columnstyle "losing_pitcher_name    (varchar(32))"
    ```{.codeblock}
    Losing pitcher name
    ```
    

??? columnstyle "saving_pitcher_id    (char(8))"
    ```{.codeblock}
    Saving pitcher ID
    ```
    

??? columnstyle "saving_pitcher_name    (varchar(32))"
    ```{.codeblock}
    Saving pitcher name
    ```
    

??? columnstyle "game_winning_rbi_id    (char(8))"
    ```{.codeblock}
    Game-winning RBI ID
    ```
    

??? columnstyle "game_winning_rbi_name    (varchar(32))"
    ```{.codeblock}
    Game-winning RBI name
    ```
    

??? columnstyle "visitor_starting_pitcher_id    (char(8))"
    ```{.codeblock}
    Away team starting pitcher ID
    ```
    

??? columnstyle "visitor_starting_pitcher_name    (varchar(32))"
    ```{.codeblock}
    Away team starting pitcher name
    ```
    

??? columnstyle "home_starting_pitcher_id    (char(8))"
    ```{.codeblock}
    Home team starting pitcher ID
    ```
    

??? columnstyle "home_starting_pitcher_name    (varchar(32))"
    ```{.codeblock}
    Home team starting pitcher name
    ```
    

??? columnstyle "visitor_batting_1_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 1 starting player ID
    ```
    

??? columnstyle "visitor_batting_1_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 1 starting player name
    ```
    

??? columnstyle "visitor_batting_1_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 1 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_2_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 2 starting player ID
    ```
    

??? columnstyle "visitor_batting_2_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 2 starting player name
    ```
    

??? columnstyle "visitor_batting_2_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 2 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_3_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 3 starting player ID
    ```
    

??? columnstyle "visitor_batting_3_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 3 starting player name
    ```
    

??? columnstyle "visitor_batting_3_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 3 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_4_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 4 starting player ID
    ```
    

??? columnstyle "visitor_batting_4_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 4 starting player name
    ```
    

??? columnstyle "visitor_batting_4_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 4 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_5_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 5 starting player ID
    ```
    

??? columnstyle "visitor_batting_5_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 5 starting player name
    ```
    

??? columnstyle "visitor_batting_5_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 5 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_6_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 6 starting player ID
    ```
    

??? columnstyle "visitor_batting_6_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 6 starting player name
    ```
    

??? columnstyle "visitor_batting_6_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 6 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_7_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 7 starting player ID
    ```
    

??? columnstyle "visitor_batting_7_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 7 starting player name
    ```
    

??? columnstyle "visitor_batting_7_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 7 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_8_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 8 starting player ID
    ```
    

??? columnstyle "visitor_batting_8_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 8 starting player name
    ```
    

??? columnstyle "visitor_batting_8_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 8 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_9_player_id    (char(8))"
    ```{.codeblock}
    Away team lineup slot 9 starting player ID
    ```
    

??? columnstyle "visitor_batting_9_name    (varchar(32))"
    ```{.codeblock}
    Away team lineup slot 9 starting player name
    ```
    

??? columnstyle "visitor_batting_9_position    (smallint)"
    ```{.codeblock}
    Away team lineup slot 9 starting player fielding position
    ```
    

??? columnstyle "home_batting_1_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 1 starting player ID
    ```
    

??? columnstyle "home_batting_1_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 1 starting player name
    ```
    

??? columnstyle "home_batting_1_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 1 starting player fielding position
    ```
    

??? columnstyle "home_batting_2_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 2 starting player ID
    ```
    

??? columnstyle "home_batting_2_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 2 starting player name
    ```
    

??? columnstyle "home_batting_2_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 2 starting player fielding position
    ```
    

??? columnstyle "home_batting_3_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 3 starting player ID
    ```
    

??? columnstyle "home_batting_3_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 3 starting player name
    ```
    

??? columnstyle "home_batting_3_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 3 starting player fielding position
    ```
    

??? columnstyle "home_batting_4_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 4 starting player ID
    ```
    

??? columnstyle "home_batting_4_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 4 starting player name
    ```
    

??? columnstyle "home_batting_4_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 4 starting player fielding position
    ```
    

??? columnstyle "home_batting_5_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 5 starting player ID
    ```
    

??? columnstyle "home_batting_5_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 5 starting player name
    ```
    

??? columnstyle "home_batting_5_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 5 starting player fielding position
    ```
    

??? columnstyle "home_batting_6_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 6 starting player ID
    ```
    

??? columnstyle "home_batting_6_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 6 starting player name
    ```
    

??? columnstyle "home_batting_6_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 6 starting player fielding position
    ```
    

??? columnstyle "home_batting_7_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 7 starting player ID
    ```
    

??? columnstyle "home_batting_7_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 7 starting player name
    ```
    

??? columnstyle "home_batting_7_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 7 starting player fielding position
    ```
    

??? columnstyle "home_batting_8_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 8 starting player ID
    ```
    

??? columnstyle "home_batting_8_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 8 starting player name
    ```
    

??? columnstyle "home_batting_8_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 8 starting player fielding position
    ```
    

??? columnstyle "home_batting_9_player_id    (char(8))"
    ```{.codeblock}
    Home team lineup slot 9 starting player ID
    ```
    

??? columnstyle "home_batting_9_name    (varchar(32))"
    ```{.codeblock}
    Home team lineup slot 9 starting player name
    ```
    

??? columnstyle "home_batting_9_position    (smallint)"
    ```{.codeblock}
    Home team lineup slot 9 starting player fielding position
    ```
    

??? columnstyle "additional_info    (varchar(128))"
    ```{.codeblock}
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
    
    ```
    

??? columnstyle "acquisition_info    (char(1))"
    ```{.codeblock}
    Y - complete game information, N - no game information, D - game derived from box score and game story, P - portions of game information
    ```
    



### park

??? keycolumnstyle "park_id    (char(5))"
    ```{.codeblock}
    Park ID
    ```
    

??? columnstyle "name    (varchar(41))"
    ```{.codeblock}
    Park name
    ```
    

??? columnstyle "aka    (varchar(55))"
    ```{.codeblock}
    Common park alias
    ```
    

??? columnstyle "city    (varchar(17))"
    ```{.codeblock}
    City
    ```
    

??? columnstyle "state    (varchar(9))"
    ```{.codeblock}
    State
    ```
    

??? columnstyle "start_date    (varchar(10))"
    ```{.codeblock}
    First game
    ```
    

??? columnstyle "end_date    (varchar(10))"
    ```{.codeblock}
    Last game
    ```
    

??? columnstyle "league    (char(2))"
    ```{.codeblock}
    League ID
    ```
    

??? columnstyle "notes    (varchar(54))"
    ```{.codeblock}
    Misc. notes
    ```
    



### roster

??? keycolumnstyle "year    (integer)"
    ```{.codeblock}
    Year of roster
    ```
    

??? keycolumnstyle "player_id    (char(8))"
    ```{.codeblock}
    Player ID
    ```
    

??? keycolumnstyle "team_id    (char(3))"
    ```{.codeblock}
    Team ID
    ```
    

??? keycolumnstyle "position    (varchar(2))"
    ```{.codeblock}
    Primary fielding position
    ```
    

??? columnstyle "last_name    (varchar(32))"
    ```{.codeblock}
    Player last name
    ```
    

??? columnstyle "first_name    (varchar(32))"
    ```{.codeblock}
    Player first name
    ```
    

??? columnstyle "bats    (char(1))"
    ```{.codeblock}
    Bat handedness
    ```
    

??? columnstyle "throws    (char(1))"
    ```{.codeblock}
    Throw handedness
    ```
    



### schedule

??? keycolumnstyle "date    (date)"
    ```{.codeblock}
    Scheduled game date
    ```
    

??? keycolumnstyle "home_team    (char(3))"
    ```{.codeblock}
    Home team ID
    ```
    

??? keycolumnstyle "home_team_game_number    (integer)"
    ```{.codeblock}
    Home team game number
    ```
    

??? columnstyle "double_header    (smallint)"
    ```{.codeblock}
    Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
    ```
    

??? columnstyle "day_of_week    (char(3))"
    ```{.codeblock}
    Day of week (3 letter abbreviation
    ```
    

??? columnstyle "visiting_team    (char(3))"
    ```{.codeblock}
    Away team ID
    ```
    

??? columnstyle "visiting_team_league    (char(2))"
    ```{.codeblock}
    Away team league ID
    ```
    

??? columnstyle "visiting_team_game_number    (smallint)"
    ```{.codeblock}
    Away team game number
    ```
    

??? columnstyle "home_team_league    (char(2))"
    ```{.codeblock}
    Home team league ID
    ```
    

??? columnstyle "day_night    (char(1))"
    ```{.codeblock}
    D - day, N - night
    ```
    

??? columnstyle "postponement_indicator    (varchar(120))"
    ```{.codeblock}
    This field will contain one or more phrases related to the game if it was
    not played as scheduled. If there is more than one phrase, they are separated
    by a semi-colon (";"). There are three possible outcomes for games not played
    on the originally scheduled date:
    -- The game was played on another date
    -- The game was played on the original date but at another site
    -- The game was not played
    
    ```
    

??? columnstyle "makeup_dates    (varchar(120))"
    ```{.codeblock}
    This field will contain a makeup date if the postponed game was played at
    another time or place. If an attempt was known to have been made on a date but
    postponed again, that date will be listed. In that case, there will be a second
    date for the date when the game was actually played, in this form: "20150428;
    20150528" For the note about a team folding, the team code is one of the
    standard Retrosheet team IDs. The same is true for the team played as note.
    Often, the two of these are combined in one field.
    
    ```
    



### sub

??? keycolumnstyle "dummy_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "game_id    (char(12))"
    ```{.codeblock}
    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "inn_ct    (smallint)"
    ```{.codeblock}
    Inning of substitution
    ```
    

??? columnstyle "bat_home_id    (smallint)"
    ```{.codeblock}
    Is home team batting (-1 for N/A)
    ```
    

??? columnstyle "sub_id    (char(8))"
    ```{.codeblock}
    Player ID of substitute
    ```
    

??? columnstyle "sub_home_id    (boolean)"
    ```{.codeblock}
    Is the home team making the substitution
    ```
    

??? columnstyle "sub_lineup_id    (smallint)"
    ```{.codeblock}
    Lineup position of substitution
    ```
    

??? columnstyle "sub_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position of substitution
    ```
    

??? columnstyle "removed_id    (char(8))"
    ```{.codeblock}
    ID of removed player
    ```
    

??? columnstyle "removed_fld_cd    (smallint)"
    ```{.codeblock}
    Fielding position of removed player
    ```
    

??? columnstyle "event_id    (smallint)"
    ```{.codeblock}
    Event number in which substitution occurred
    ```
    





## baseballdatabank
### allstar_full

??? keycolumnstyle "dummy_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "game_num    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "game_id    (varchar(12))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "starting_pos    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### appearances

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_all    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_batting    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_defense    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_p    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_c    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_1b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_2b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_3b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_ss    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_lf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_cf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_rf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_of    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_dh    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_ph    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_pr    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### awards_managers

??? keycolumnstyle "dummy_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "player_id    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "award_id    (varchar(75))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "tie    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "notes    (varchar(100))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### awards_players

??? keycolumnstyle "dummy_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "award_id    (varchar(255))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "tie    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "notes    (varchar(100))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### awards_share_managers

??? keycolumnstyle "award_id    (varchar(25))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "player_id    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "points_won    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "points_max    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "votes_first    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### awards_share_players

??? keycolumnstyle "award_id    (varchar(25))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "points_won    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "points_max    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "votes_first    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### batting

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "stint    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ab    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "r    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "h    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "_2b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "_3b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hr    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "rbi    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "so    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ibb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hbp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sh    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gidp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### batting_post

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "round    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ab    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "r    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "h    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "_2b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "_3b    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hr    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "rbi    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "so    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ibb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hbp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sh    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gidp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### college_playing

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "school_id    (varchar(15))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### fielding

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "stint    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "pos    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "inn_outs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "po    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "a    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "e    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "dp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "pb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "wp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "zr    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### fielding_of

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "stint    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_lf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_cf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_rf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### fielding_of_split

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "stint    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "pos    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "inn_outs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "po    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "a    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "e    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "dp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "pb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "wp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "zr    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### fielding_post

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "round    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "pos    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "inn_outs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "po    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "a    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "e    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "dp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "tp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "pb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### hall_of_fame

??? keycolumnstyle "player_id    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "voted_by    (varchar(64))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ballots    (varchar(64))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "needed    (varchar(64))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "votes    (varchar(64))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "inducted    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "category    (varchar(20))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "needed_note    (varchar(25))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### home_games

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "park_id    (varchar(5))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "first_game    (date)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "last_game    (date)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "games    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "openings    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "attendance    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### managers

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "inseason    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "player_id    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "w    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "l    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "rank    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "plyr_mgr    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### managers_half

??? keycolumnstyle "player_id    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "half    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "inseason    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "w    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "l    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "rank    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### parks

??? keycolumnstyle "park_id    (varchar(5))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "park_name    (varchar(40))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "park_alias    (varchar(55))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "city    (varchar(25))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "state    (varchar(16))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "country    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### people

??? keycolumnstyle "player_id    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "birth_year    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "birth_month    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "birth_day    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "birth_country    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "birth_state    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "birth_city    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "death_year    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "death_month    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "death_day    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "death_country    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "death_state    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "death_city    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "name_first    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "name_last    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "name_given    (varchar(255))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "weight    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "height    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bats    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "throws    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "debut    (date)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "final_game    (date)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "retro_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bbref_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### pitching

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "stint    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "w    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "l    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cg    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sho    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sv    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ip_outs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "h    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "er    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hr    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "so    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ba_opp    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "era    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ibb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "wp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hbp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bk    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bfp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "r    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sh    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gidp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### pitching_post

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "round    (varchar(10))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "w    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "l    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cg    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sho    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sv    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ip_outs    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "h    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "er    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hr    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "so    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ba_opp    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "era    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ibb    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "wp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hbp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bk    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bfp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "r    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sh    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sf    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "gidp    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### salaries

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "player_id    (varchar(9))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "salary    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### schools

??? keycolumnstyle "school_id    (varchar(15))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "name_full    (varchar(255))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "city    (varchar(55))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "state    (varchar(55))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "country    (varchar(55))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### series_post

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "round    (varchar(5))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id_winner    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id_winner    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id_loser    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_id_loser    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "wins    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "losses    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ties    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    



### teams

??? keycolumnstyle "year_id    (smallint)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "franch_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "div_id    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "rank    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g_home    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "w    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "l    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "div_win    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "wc_win    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "lg_win    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ws_win    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "r    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ab    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "h    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "_2b    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "_3b    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hr    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bb    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "so    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sb    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cs    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hbp    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sf    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ra    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "er    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "era    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "cg    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sho    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "sv    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ip_outs    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "h_a    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "hr_a    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bb_a    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "so_a    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "e    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "dp    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "fp    (float)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "name    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "park    (varchar(255))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "attendance    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "bpf    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "ppf    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id_br    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id_lahman45    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "team_id_retro    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### teams_franchises

??? keycolumnstyle "franch_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "franch_name    (varchar(50))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "active    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "na_assoc    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    



### teams_half

??? keycolumnstyle "year_id    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id    (varchar(2))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "team_id    (varchar(3))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? keycolumnstyle "half    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "div_id    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "div_win    (varchar(1))"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "rank    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "g    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "w    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    

??? columnstyle "l    (integer)"
    ```{.codeblock}
    No documentation provided.
    ```
    




