# Boxball Schemas
[TOC]
## retrosheet
### code_event

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### code_field_park

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### code_method_record

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### code_pitches_record

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### code_precip_park

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### code_sky_park

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### code_wind_direction_park

??? keycolumnstyle "code"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "description"
    ```{.codeblock}
    Type: varchar(30)

    No documentation provided.
    ```
    



### comment

??? keycolumnstyle "dummy_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "game_id"
    ```{.codeblock}
    Type: char(12)

    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "event_id"
    ```{.codeblock}
    Type: smallint

    Commented event number
    ```
    

??? columnstyle "comment"
    ```{.codeblock}
    Type: varchar(1638)

    Comment text
    ```
    

??? columnstyle "ejected_person_id"
    ```{.codeblock}
    Type: varchar(256)

    ID of ejected person
    ```
    

??? columnstyle "ejected_person_role_cd"
    ```{.codeblock}
    Type: varchar(256)

    No documentation provided.
    ```
    

??? columnstyle "eject_umpire_id"
    ```{.codeblock}
    Type: varchar(256)

    ID of umpire who ejected person
    ```
    

??? columnstyle "eject_reason"
    ```{.codeblock}
    Type: varchar(1639)

    No documentation provided.
    ```
    

??? columnstyle "umpchange_inning"
    ```{.codeblock}
    Type: varchar(256)

    No documentation provided.
    ```
    

??? columnstyle "umpchange_position"
    ```{.codeblock}
    Type: varchar(256)

    No documentation provided.
    ```
    

??? columnstyle "umpchange_person_id"
    ```{.codeblock}
    Type: varchar(256)

    ID of new umpire
    ```
    



### daily

??? keycolumnstyle "dummy_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "game_id"
    ```{.codeblock}
    Type: char(12)

    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "game_dt"
    ```{.codeblock}
    Type: date

    Game date
    ```
    

??? columnstyle "game_ct"
    ```{.codeblock}
    Type: smallint

    Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
    ```
    

??? columnstyle "appearance_dt"
    ```{.codeblock}
    Type: date

    Player appearance date. Can be different from game date if the game was suspended and the player entered the game at the later date
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: char(3)

    Team ID of player
    ```
    

??? columnstyle "player_id"
    ```{.codeblock}
    Type: char(8)

    Player ID
    ```
    

??? columnstyle "slot_ct"
    ```{.codeblock}
    Type: smallint

    Player lineup position
    ```
    

??? columnstyle "seq_ct"
    ```{.codeblock}
    Type: smallint

    Player is nth person of game to play in that lineup slot
    ```
    

??? columnstyle "home_fl"
    ```{.codeblock}
    Type: boolean

    Player is playing at home
    ```
    

??? columnstyle "opponent_id"
    ```{.codeblock}
    Type: char(3)

    Team opponent ID
    ```
    

??? columnstyle "park_id"
    ```{.codeblock}
    Type: char(5)

    Park ID
    ```
    

??? columnstyle "b_g"
    ```{.codeblock}
    Type: smallint

    Games played
    ```
    

??? columnstyle "b_pa"
    ```{.codeblock}
    Type: smallint

    Plate appearances
    ```
    

??? columnstyle "b_ab"
    ```{.codeblock}
    Type: smallint

    At bats
    ```
    

??? columnstyle "b_r"
    ```{.codeblock}
    Type: smallint

    Runs scored
    ```
    

??? columnstyle "b_h"
    ```{.codeblock}
    Type: smallint

    Hits
    ```
    

??? columnstyle "b_tb"
    ```{.codeblock}
    Type: smallint

    Total bases
    ```
    

??? columnstyle "b_2b"
    ```{.codeblock}
    Type: smallint

    Doubles
    ```
    

??? columnstyle "b_3b"
    ```{.codeblock}
    Type: smallint

    Triples
    ```
    

??? columnstyle "b_hr"
    ```{.codeblock}
    Type: smallint

    Home runs
    ```
    

??? columnstyle "b_hr4"
    ```{.codeblock}
    Type: smallint

    Grand slams
    ```
    

??? columnstyle "b_rbi"
    ```{.codeblock}
    Type: smallint

    Runs batted in
    ```
    

??? columnstyle "b_gw"
    ```{.codeblock}
    Type: smallint

    Game winning RBI
    ```
    

??? columnstyle "b_bb"
    ```{.codeblock}
    Type: smallint

    Walks
    ```
    

??? columnstyle "b_ibb"
    ```{.codeblock}
    Type: smallint

    Intentional walks
    ```
    

??? columnstyle "b_so"
    ```{.codeblock}
    Type: smallint

    Strikeouts
    ```
    

??? columnstyle "b_gdp"
    ```{.codeblock}
    Type: smallint

    Grounded into double plays
    ```
    

??? columnstyle "b_hp"
    ```{.codeblock}
    Type: smallint

    Hit by pitches
    ```
    

??? columnstyle "b_sh"
    ```{.codeblock}
    Type: smallint

    Sacrifice hits
    ```
    

??? columnstyle "b_sf"
    ```{.codeblock}
    Type: smallint

    Sacrifice files
    ```
    

??? columnstyle "b_sb"
    ```{.codeblock}
    Type: smallint

    Stolen bases
    ```
    

??? columnstyle "b_cs"
    ```{.codeblock}
    Type: smallint

    Caught stealing
    ```
    

??? columnstyle "b_xi"
    ```{.codeblock}
    Type: smallint

    Reached on interference
    ```
    

??? columnstyle "b_g_dh"
    ```{.codeblock}
    Type: smallint

    Games as DH
    ```
    

??? columnstyle "b_g_ph"
    ```{.codeblock}
    Type: smallint

    Games as pinch hitter
    ```
    

??? columnstyle "b_g_pr"
    ```{.codeblock}
    Type: smallint

    Games as pinch runner
    ```
    

??? columnstyle "p_g"
    ```{.codeblock}
    Type: smallint

    Games pitched
    ```
    

??? columnstyle "p_gs"
    ```{.codeblock}
    Type: smallint

    Games as starting pitcher
    ```
    

??? columnstyle "p_cg"
    ```{.codeblock}
    Type: smallint

    Complete games
    ```
    

??? columnstyle "p_sho"
    ```{.codeblock}
    Type: smallint

    Shutouts
    ```
    

??? columnstyle "p_gf"
    ```{.codeblock}
    Type: smallint

    Games finished
    ```
    

??? columnstyle "p_w"
    ```{.codeblock}
    Type: smallint

    Wins
    ```
    

??? columnstyle "p_l"
    ```{.codeblock}
    Type: smallint

    Losses
    ```
    

??? columnstyle "p_sv"
    ```{.codeblock}
    Type: smallint

    Saves
    ```
    

??? columnstyle "p_out"
    ```{.codeblock}
    Type: smallint

    Outs recorded
    ```
    

??? columnstyle "p_tbf"
    ```{.codeblock}
    Type: smallint

    Total batters faced
    ```
    

??? columnstyle "p_ab"
    ```{.codeblock}
    Type: smallint

    At bats against
    ```
    

??? columnstyle "p_r"
    ```{.codeblock}
    Type: smallint

    Runs allowed
    ```
    

??? columnstyle "p_er"
    ```{.codeblock}
    Type: smallint

    Earned runs allowed
    ```
    

??? columnstyle "p_h"
    ```{.codeblock}
    Type: smallint

    Hits allowed
    ```
    

??? columnstyle "p_tb"
    ```{.codeblock}
    Type: smallint

    Total bases allowed
    ```
    

??? columnstyle "p_2b"
    ```{.codeblock}
    Type: smallint

    Doubles allowed
    ```
    

??? columnstyle "p_3b"
    ```{.codeblock}
    Type: smallint

    Triples allowed
    ```
    

??? columnstyle "p_hr"
    ```{.codeblock}
    Type: smallint

    Home runs allowed
    ```
    

??? columnstyle "p_hr4"
    ```{.codeblock}
    Type: smallint

    Grand slams allowed
    ```
    

??? columnstyle "p_bb"
    ```{.codeblock}
    Type: smallint

    Walks allowed
    ```
    

??? columnstyle "p_ibb"
    ```{.codeblock}
    Type: smallint

    Intentional walks allowed
    ```
    

??? columnstyle "p_so"
    ```{.codeblock}
    Type: smallint

    Strikeouts against
    ```
    

??? columnstyle "p_gdp"
    ```{.codeblock}
    Type: smallint

    Grounded into double plays against
    ```
    

??? columnstyle "p_hp"
    ```{.codeblock}
    Type: smallint

    Hit by pitches allowed
    ```
    

??? columnstyle "p_sh"
    ```{.codeblock}
    Type: smallint

    Sacrifice hits allowed
    ```
    

??? columnstyle "p_sf"
    ```{.codeblock}
    Type: smallint

    Sacrifice flies allowed
    ```
    

??? columnstyle "p_xi"
    ```{.codeblock}
    Type: smallint

    Reached on interference allowed
    ```
    

??? columnstyle "p_wp"
    ```{.codeblock}
    Type: smallint

    Wild pitches allowed
    ```
    

??? columnstyle "p_bk"
    ```{.codeblock}
    Type: smallint

    Balks allowed
    ```
    

??? columnstyle "p_ir"
    ```{.codeblock}
    Type: smallint

    Inherited runners
    ```
    

??? columnstyle "p_irs"
    ```{.codeblock}
    Type: smallint

    Inherited runners scored
    ```
    

??? columnstyle "p_go"
    ```{.codeblock}
    Type: smallint

    Groundouts recorded
    ```
    

??? columnstyle "p_ao"
    ```{.codeblock}
    Type: smallint

    Fly ball outs recorded
    ```
    

??? columnstyle "p_pitch"
    ```{.codeblock}
    Type: smallint

    Pitches thrown
    ```
    

??? columnstyle "p_strike"
    ```{.codeblock}
    Type: smallint

    Strikes thrown
    ```
    

??? columnstyle "f_p_g"
    ```{.codeblock}
    Type: smallint

    Appearances at pitcher
    ```
    

??? columnstyle "f_p_gs"
    ```{.codeblock}
    Type: smallint

    Starts at pitcher
    ```
    

??? columnstyle "f_p_out"
    ```{.codeblock}
    Type: smallint

    Outs played as pitcher
    ```
    

??? columnstyle "f_p_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as pitcher
    ```
    

??? columnstyle "f_p_po"
    ```{.codeblock}
    Type: smallint

    Putouts as pitcher
    ```
    

??? columnstyle "f_p_a"
    ```{.codeblock}
    Type: smallint

    Assists as pitcher
    ```
    

??? columnstyle "f_p_e"
    ```{.codeblock}
    Type: smallint

    Errors as pitcher
    ```
    

??? columnstyle "f_p_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as pitcher
    ```
    

??? columnstyle "f_p_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as pitcher
    ```
    

??? columnstyle "f_c_g"
    ```{.codeblock}
    Type: smallint

    Appearances at catcher
    ```
    

??? columnstyle "f_c_gs"
    ```{.codeblock}
    Type: smallint

    Starts at catcher
    ```
    

??? columnstyle "f_c_out"
    ```{.codeblock}
    Type: smallint

    Outs played as catcher
    ```
    

??? columnstyle "f_c_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as catcher
    ```
    

??? columnstyle "f_c_po"
    ```{.codeblock}
    Type: smallint

    Putouts as catcher
    ```
    

??? columnstyle "f_c_a"
    ```{.codeblock}
    Type: smallint

    Assists as catcher
    ```
    

??? columnstyle "f_c_e"
    ```{.codeblock}
    Type: smallint

    Errors as catcher
    ```
    

??? columnstyle "f_c_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as catcher
    ```
    

??? columnstyle "f_c_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as catcher
    ```
    

??? columnstyle "f_c_pb"
    ```{.codeblock}
    Type: smallint

    Passed balls
    ```
    

??? columnstyle "f_c_xi"
    ```{.codeblock}
    Type: smallint

    Catcher's interference
    ```
    

??? columnstyle "f_1b_g"
    ```{.codeblock}
    Type: smallint

    Appearances at first baseman
    ```
    

??? columnstyle "f_1b_gs"
    ```{.codeblock}
    Type: smallint

    Starts at first baseman
    ```
    

??? columnstyle "f_1b_out"
    ```{.codeblock}
    Type: smallint

    Outs played as first baseman
    ```
    

??? columnstyle "f_1b_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as first baseman
    ```
    

??? columnstyle "f_1b_po"
    ```{.codeblock}
    Type: smallint

    Putouts as first baseman
    ```
    

??? columnstyle "f_1b_a"
    ```{.codeblock}
    Type: smallint

    Assists as first baseman
    ```
    

??? columnstyle "f_1b_e"
    ```{.codeblock}
    Type: smallint

    Errors as first baseman
    ```
    

??? columnstyle "f_1b_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as first baseman
    ```
    

??? columnstyle "f_1b_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as first baseman
    ```
    

??? columnstyle "f_2b_g"
    ```{.codeblock}
    Type: smallint

    Appearances at second baseman
    ```
    

??? columnstyle "f_2b_gs"
    ```{.codeblock}
    Type: smallint

    Starts at second baseman
    ```
    

??? columnstyle "f_2b_out"
    ```{.codeblock}
    Type: smallint

    Outs played as second baseman
    ```
    

??? columnstyle "f_2b_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as second baseman
    ```
    

??? columnstyle "f_2b_po"
    ```{.codeblock}
    Type: smallint

    Putouts as second baseman
    ```
    

??? columnstyle "f_2b_a"
    ```{.codeblock}
    Type: smallint

    Assists as second baseman
    ```
    

??? columnstyle "f_2b_e"
    ```{.codeblock}
    Type: smallint

    Errors as second baseman
    ```
    

??? columnstyle "f_2b_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as second baseman
    ```
    

??? columnstyle "f_2b_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as second baseman
    ```
    

??? columnstyle "f_3b_g"
    ```{.codeblock}
    Type: smallint

    Appearances at third baseman
    ```
    

??? columnstyle "f_3b_gs"
    ```{.codeblock}
    Type: smallint

    Starts at third baseman
    ```
    

??? columnstyle "f_3b_out"
    ```{.codeblock}
    Type: smallint

    Outs played as third baseman
    ```
    

??? columnstyle "f_3b_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as third baseman
    ```
    

??? columnstyle "f_3b_po"
    ```{.codeblock}
    Type: smallint

    Putouts as third baseman
    ```
    

??? columnstyle "f_3b_a"
    ```{.codeblock}
    Type: smallint

    Assists as third baseman
    ```
    

??? columnstyle "f_3b_e"
    ```{.codeblock}
    Type: smallint

    Errors as third baseman
    ```
    

??? columnstyle "f_3b_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as third baseman
    ```
    

??? columnstyle "f_3b_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as third baseman
    ```
    

??? columnstyle "f_ss_g"
    ```{.codeblock}
    Type: smallint

    Appearances at shortstop
    ```
    

??? columnstyle "f_ss_gs"
    ```{.codeblock}
    Type: smallint

    Starts at shortstop
    ```
    

??? columnstyle "f_ss_out"
    ```{.codeblock}
    Type: smallint

    Outs played as shortstop
    ```
    

??? columnstyle "f_ss_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as shortstop
    ```
    

??? columnstyle "f_ss_po"
    ```{.codeblock}
    Type: smallint

    Putouts as shortstop
    ```
    

??? columnstyle "f_ss_a"
    ```{.codeblock}
    Type: smallint

    Assists as shortstop
    ```
    

??? columnstyle "f_ss_e"
    ```{.codeblock}
    Type: smallint

    Errors as shortstop
    ```
    

??? columnstyle "f_ss_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as shortstop
    ```
    

??? columnstyle "f_ss_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as shortstop
    ```
    

??? columnstyle "f_lf_g"
    ```{.codeblock}
    Type: smallint

    Appearances at left fielder
    ```
    

??? columnstyle "f_lf_gs"
    ```{.codeblock}
    Type: smallint

    Starts at left fielder
    ```
    

??? columnstyle "f_lf_out"
    ```{.codeblock}
    Type: smallint

    Outs played as left fielder
    ```
    

??? columnstyle "f_lf_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as left fielder
    ```
    

??? columnstyle "f_lf_po"
    ```{.codeblock}
    Type: smallint

    Putouts as left fielder
    ```
    

??? columnstyle "f_lf_a"
    ```{.codeblock}
    Type: smallint

    Assists as left fielder
    ```
    

??? columnstyle "f_lf_e"
    ```{.codeblock}
    Type: smallint

    Errors as left fielder
    ```
    

??? columnstyle "f_lf_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as left fielder
    ```
    

??? columnstyle "f_lf_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as left fielder
    ```
    

??? columnstyle "f_cf_g"
    ```{.codeblock}
    Type: smallint

    Appearances at center fielder
    ```
    

??? columnstyle "f_cf_gs"
    ```{.codeblock}
    Type: smallint

    Starts at center fielder
    ```
    

??? columnstyle "f_cf_out"
    ```{.codeblock}
    Type: smallint

    Outs played as center fielder
    ```
    

??? columnstyle "f_cf_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as center fielder
    ```
    

??? columnstyle "f_cf_po"
    ```{.codeblock}
    Type: smallint

    Putouts as center fielder
    ```
    

??? columnstyle "f_cf_a"
    ```{.codeblock}
    Type: smallint

    Assists as center fielder
    ```
    

??? columnstyle "f_cf_e"
    ```{.codeblock}
    Type: smallint

    Errors as center fielder
    ```
    

??? columnstyle "f_cf_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as center fielder
    ```
    

??? columnstyle "f_cf_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as center fielder
    ```
    

??? columnstyle "f_rf_g"
    ```{.codeblock}
    Type: smallint

    Appearances at right fielder
    ```
    

??? columnstyle "f_rf_gs"
    ```{.codeblock}
    Type: smallint

    Starts at right fielder
    ```
    

??? columnstyle "f_rf_out"
    ```{.codeblock}
    Type: smallint

    Outs played as right fielder
    ```
    

??? columnstyle "f_rf_tc"
    ```{.codeblock}
    Type: smallint

    Total chances as right fielder
    ```
    

??? columnstyle "f_rf_po"
    ```{.codeblock}
    Type: smallint

    Putouts as right fielder
    ```
    

??? columnstyle "f_rf_a"
    ```{.codeblock}
    Type: smallint

    Assists as right fielder
    ```
    

??? columnstyle "f_rf_e"
    ```{.codeblock}
    Type: smallint

    Errors as right fielder
    ```
    

??? columnstyle "f_rf_dp"
    ```{.codeblock}
    Type: smallint

    Double plays turned as right fielder
    ```
    

??? columnstyle "f_rf_tp"
    ```{.codeblock}
    Type: smallint

    Triple pays turned as right fielder
    ```
    



### deduced_game

??? keycolumnstyle "game_id"
    ```{.codeblock}
    Type: char(12)

    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    



### event

??? keycolumnstyle "game_id"
    ```{.codeblock}
    Type: char(12)

    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? keycolumnstyle "event_id"
    ```{.codeblock}
    Type: integer

    Event number of game
    ```
    

??? columnstyle "away_team_id"
    ```{.codeblock}
    Type: char(3)

    Visiting Team
    ```
    

??? columnstyle "inn_ct"
    ```{.codeblock}
    Type: smallint

    Inning
    ```
    

??? columnstyle "bat_home_id"
    ```{.codeblock}
    Type: boolean

    Home team is batting
    ```
    

??? columnstyle "outs_ct"
    ```{.codeblock}
    Type: smallint

    Outs (0-2)
    ```
    

??? columnstyle "balls_ct"
    ```{.codeblock}
    Type: smallint

    Balls (0-3)
    ```
    

??? columnstyle "strikes_ct"
    ```{.codeblock}
    Type: smallint

    Strikes (0-2
    ```
    

??? columnstyle "pitch_seq_tx"
    ```{.codeblock}
    Type: varchar(30)

    Pitch sequence
    ```
    

??? columnstyle "away_score_ct"
    ```{.codeblock}
    Type: smallint

    Away score
    ```
    

??? columnstyle "home_score_ct"
    ```{.codeblock}
    Type: smallint

    Home score
    ```
    

??? columnstyle "bat_id"
    ```{.codeblock}
    Type: char(8)

    Batter ID
    ```
    

??? columnstyle "bat_hand_cd"
    ```{.codeblock}
    Type: char(1)

    Batter handedness
    ```
    

??? columnstyle "resp_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of batter charged with event
    ```
    

??? columnstyle "resp_bat_hand_cd"
    ```{.codeblock}
    Type: char(1)

    Handedness of batter charged with event
    ```
    

??? columnstyle "pit_id"
    ```{.codeblock}
    Type: char(8)

    Pitcher ID
    ```
    

??? columnstyle "pit_hand_cd"
    ```{.codeblock}
    Type: char(1)

    Pitcher handedness
    ```
    

??? columnstyle "resp_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of pitcher charged with event
    ```
    

??? columnstyle "resp_pit_hand_cd"
    ```{.codeblock}
    Type: char(1)

    Handedness of pitcher charged with event
    ```
    

??? columnstyle "pos2_fld_id"
    ```{.codeblock}
    Type: char(8)

    Catcher ID
    ```
    

??? columnstyle "pos3_fld_id"
    ```{.codeblock}
    Type: char(8)

    First baseman ID
    ```
    

??? columnstyle "pos4_fld_id"
    ```{.codeblock}
    Type: char(8)

    Second baseman ID
    ```
    

??? columnstyle "pos5_fld_id"
    ```{.codeblock}
    Type: char(8)

    Third baseman ID
    ```
    

??? columnstyle "pos6_fld_id"
    ```{.codeblock}
    Type: char(8)

    Shortstop ID
    ```
    

??? columnstyle "pos7_fld_id"
    ```{.codeblock}
    Type: char(8)

    Left fielder ID
    ```
    

??? columnstyle "pos8_fld_id"
    ```{.codeblock}
    Type: char(8)

    Center fielder ID
    ```
    

??? columnstyle "pos9_fld_id"
    ```{.codeblock}
    Type: char(8)

    Right fielder ID
    ```
    

??? columnstyle "base1_run_id"
    ```{.codeblock}
    Type: char(8)

    ID of runner on first
    ```
    

??? columnstyle "base2_run_id"
    ```{.codeblock}
    Type: char(8)

    ID of runner on second
    ```
    

??? columnstyle "base3_run_id"
    ```{.codeblock}
    Type: char(8)

    ID of runner on third
    ```
    

??? columnstyle "event_tx"
    ```{.codeblock}
    Type: varchar(128)

    Event text (in scoring shorthand
    ```
    

??? columnstyle "leadoff_fl"
    ```{.codeblock}
    Type: boolean

    Batter is leading off the inning
    ```
    

??? columnstyle "ph_fl"
    ```{.codeblock}
    Type: boolean

    Batter is pinch-hitting
    ```
    

??? columnstyle "bat_fld_cd"
    ```{.codeblock}
    Type: smallint

    Defensive position of batter (10 for DH, 11 for PH, 12 for PR
    ```
    

??? columnstyle "bat_lineup_id"
    ```{.codeblock}
    Type: smallint

    Lineup position (1-9)
    ```
    

??? columnstyle "event_cd"
    ```{.codeblock}
    Type: smallint

    Event code (join table `code_event` for descriptions
    ```
    

??? columnstyle "bat_event_fl"
    ```{.codeblock}
    Type: boolean

    Event is related to the batter
    ```
    

??? columnstyle "ab_fl"
    ```{.codeblock}
    Type: boolean

    Event is an at-bat
    ```
    

??? columnstyle "h_fl"
    ```{.codeblock}
    Type: smallint

    Event is a hit
    ```
    

??? columnstyle "sh_fl"
    ```{.codeblock}
    Type: boolean

    Event is a sacrifice hit
    ```
    

??? columnstyle "sf_fl"
    ```{.codeblock}
    Type: boolean

    Event is a sacrifice fly
    ```
    

??? columnstyle "event_outs_ct"
    ```{.codeblock}
    Type: smallint

    Outs recorded on event (0-3)
    ```
    

??? columnstyle "dp_fl"
    ```{.codeblock}
    Type: boolean

    Event is a double play
    ```
    

??? columnstyle "tp_fl"
    ```{.codeblock}
    Type: boolean

    Event is a triple play
    ```
    

??? columnstyle "rbi_ct"
    ```{.codeblock}
    Type: smallint

    Runs batted in on event
    ```
    

??? columnstyle "wp_fl"
    ```{.codeblock}
    Type: boolean

    Event is a wild pitch
    ```
    

??? columnstyle "pb_fl"
    ```{.codeblock}
    Type: boolean

    Event is a passed ball
    ```
    

??? columnstyle "fld_cd"
    ```{.codeblock}
    Type: smallint

    Position id of event fielder
    ```
    

??? columnstyle "battedball_cd"
    ```{.codeblock}
    Type: char(1)

    Batted ball code (P - pop-up, G - ground ball, F - fly ball, L - line drive
    ```
    

??? columnstyle "bunt_fl"
    ```{.codeblock}
    Type: boolean

    Event is a bunt
    ```
    

??? columnstyle "foul_fl"
    ```{.codeblock}
    Type: boolean

    Event is a foul ball
    ```
    

??? columnstyle "battedball_loc_tx"
    ```{.codeblock}
    Type: varchar(5)

    Hit location code (see https://www.retrosheet.org/location.htm)
    ```
    

??? columnstyle "err_ct"
    ```{.codeblock}
    Type: smallint

    Number of errors recorded during event
    ```
    

??? columnstyle "err1_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder committing first error during event
    ```
    

??? columnstyle "err1_cd"
    ```{.codeblock}
    Type: char(1)

    First error type (T - throwing, F - fielding)
    ```
    

??? columnstyle "err2_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder committing second error during event
    ```
    

??? columnstyle "err2_cd"
    ```{.codeblock}
    Type: char(1)

    Second error type (T - throwing, F - fielding)
    ```
    

??? columnstyle "err3_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder committing third error during event
    ```
    

??? columnstyle "err3_cd"
    ```{.codeblock}
    Type: char(1)

    Third error type (T - throwing, F - fielding)
    ```
    

??? columnstyle "bat_dest_id"
    ```{.codeblock}
    Type: smallint

    Destination of batter after event (0 - putout, 1-3 - bases, 4 - scored asearned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "run1_dest_id"
    ```{.codeblock}
    Type: smallint

    Destination of runner on first after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "run2_dest_id"
    ```{.codeblock}
    Type: smallint

    Destination of runner on second after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "run3_dest_id"
    ```{.codeblock}
    Type: smallint

    Destination of runner on third after event (0 - putout, 1-3 - bases, 4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned to team earned to pitcher)
    ```
    

??? columnstyle "bat_play_tx"
    ```{.codeblock}
    Type: varchar(15)

    Fielding play on batter
    ```
    

??? columnstyle "run1_play_tx"
    ```{.codeblock}
    Type: varchar(15)

    Fielding play on runner on first
    ```
    

??? columnstyle "run2_play_tx"
    ```{.codeblock}
    Type: varchar(15)

    Fielding play on runner on second
    ```
    

??? columnstyle "run3_play_tx"
    ```{.codeblock}
    Type: varchar(15)

    Fielding play on runner on third
    ```
    

??? columnstyle "run1_sb_fl"
    ```{.codeblock}
    Type: boolean

    Runner on first steals base
    ```
    

??? columnstyle "run2_sb_fl"
    ```{.codeblock}
    Type: boolean

    Runner on second steals base
    ```
    

??? columnstyle "run3_sb_fl"
    ```{.codeblock}
    Type: boolean

    Runner on third steals base
    ```
    

??? columnstyle "run1_cs_fl"
    ```{.codeblock}
    Type: boolean

    Runner on first caught stealing
    ```
    

??? columnstyle "run2_cs_fl"
    ```{.codeblock}
    Type: boolean

    Runner on second caught stealing
    ```
    

??? columnstyle "run3_cs_fl"
    ```{.codeblock}
    Type: boolean

    Runner on third caught stealing
    ```
    

??? columnstyle "run1_pk_fl"
    ```{.codeblock}
    Type: boolean

    Runner on first picked off
    ```
    

??? columnstyle "run2_pk_fl"
    ```{.codeblock}
    Type: boolean

    Runner on second picked off
    ```
    

??? columnstyle "run3_pk_fl"
    ```{.codeblock}
    Type: boolean

    Runner on third picked off
    ```
    

??? columnstyle "run1_resp_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of pitcher charged with runner on first
    ```
    

??? columnstyle "run2_resp_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of pitcher charged with runner on second
    ```
    

??? columnstyle "run3_resp_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of pitcher charged with runner on third
    ```
    

??? columnstyle "game_new_fl"
    ```{.codeblock}
    Type: boolean

    Start of game flag
    ```
    

??? columnstyle "game_end_fl"
    ```{.codeblock}
    Type: boolean

    End of game flag
    ```
    

??? columnstyle "pr_run1_fl"
    ```{.codeblock}
    Type: boolean

    Pinch-runner on first
    ```
    

??? columnstyle "pr_run2_fl"
    ```{.codeblock}
    Type: boolean

    Pinch-runner on second
    ```
    

??? columnstyle "pr_run3_fl"
    ```{.codeblock}
    Type: boolean

    Runner on third
    ```
    

??? columnstyle "removed_for_pr_run1_id"
    ```{.codeblock}
    Type: char(8)

    ID of former runner on first removed for pinch-runner
    ```
    

??? columnstyle "removed_for_pr_run2_id"
    ```{.codeblock}
    Type: char(8)

    ID of former runner on second removed for pinch-runner
    ```
    

??? columnstyle "removed_for_pr_run3_id"
    ```{.codeblock}
    Type: char(8)

    ID of former runner on third removed for pinch-runner
    ```
    

??? columnstyle "removed_for_ph_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of former batter removed for pinch-hitter
    ```
    

??? columnstyle "removed_for_ph_bat_fld_cd"
    ```{.codeblock}
    Type: integer

    Position code of batter removed for pinch-hitter
    ```
    

??? columnstyle "po1_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with first putout
    ```
    

??? columnstyle "po2_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with second putout
    ```
    

??? columnstyle "po3_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with third putout
    ```
    

??? columnstyle "ass1_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with first assist
    ```
    

??? columnstyle "ass2_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with second assist
    ```
    

??? columnstyle "ass3_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with third assist
    ```
    

??? columnstyle "ass4_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with fourth assist
    ```
    

??? columnstyle "ass5_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with fifth assist
    ```
    

??? columnstyle "home_team_id"
    ```{.codeblock}
    Type: char(3)

    Home team ID
    ```
    

??? columnstyle "bat_team_id"
    ```{.codeblock}
    Type: char(3)

    Batting team ID
    ```
    

??? columnstyle "fld_team_id"
    ```{.codeblock}
    Type: char(3)

    Fielding team ID
    ```
    

??? columnstyle "bat_last_id"
    ```{.codeblock}
    Type: smallint

    Half inning (differs from batting team if home team bats first)
    ```
    

??? columnstyle "inn_new_fl"
    ```{.codeblock}
    Type: boolean

    Start of half-inning flag
    ```
    

??? columnstyle "inn_end_fl"
    ```{.codeblock}
    Type: boolean

    End of half-inning flag
    ```
    

??? columnstyle "start_bat_score_ct"
    ```{.codeblock}
    Type: smallint

    Runs scored by batting team (prior to this event)
    ```
    

??? columnstyle "start_fld_score_ct"
    ```{.codeblock}
    Type: smallint

    Runs scored by fielding team
    ```
    

??? columnstyle "inn_runs_ct"
    ```{.codeblock}
    Type: smallint

    Runs scored in this half-inning (prior to this event)
    ```
    

??? columnstyle "game_pa_ct"
    ```{.codeblock}
    Type: smallint

    Batting team PA total (prior to this event)
    ```
    

??? columnstyle "inn_pa_ct"
    ```{.codeblock}
    Type: smallint

    Half-inning PA total (prior to this event)
    ```
    

??? columnstyle "pa_new_fl"
    ```{.codeblock}
    Type: boolean

    Event is the start of a plate appearance
    ```
    

??? columnstyle "pa_trunc_fl"
    ```{.codeblock}
    Type: boolean

    Event is a truncated plate appearance
    ```
    

??? columnstyle "start_bases_cd"
    ```{.codeblock}
    Type: smallint

    Base state at start of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
    ```
    

??? columnstyle "end_bases_cd"
    ```{.codeblock}
    Type: smallint

    Base state end of event (0-7, binary value is flags for runners on third, second, and first left-to-right)
    ```
    

??? columnstyle "bat_start_fl"
    ```{.codeblock}
    Type: boolean

    Batter started game
    ```
    

??? columnstyle "resp_bat_start_fl"
    ```{.codeblock}
    Type: boolean

    Result-charged batter is a starter
    ```
    

??? columnstyle "bat_on_deck_id"
    ```{.codeblock}
    Type: char(8)

    ID of batter on deck
    ```
    

??? columnstyle "bat_in_hold_id"
    ```{.codeblock}
    Type: char(8)

    Id of batter in the hole
    ```
    

??? columnstyle "pit_start_fl"
    ```{.codeblock}
    Type: boolean

    Pitcher started game
    ```
    

??? columnstyle "resp_pit_start_fl"
    ```{.codeblock}
    Type: boolean

    Result-charged pitcher started game
    ```
    

??? columnstyle "run1_fld_cd"
    ```{.codeblock}
    Type: smallint

    Defensive position code of runner on first
    ```
    

??? columnstyle "run1_lineup_cd"
    ```{.codeblock}
    Type: smallint

    Lineup position of runner on first
    ```
    

??? columnstyle "run1_origin_event_id"
    ```{.codeblock}
    Type: smallint

    Event number on which runner on first reached base
    ```
    

??? columnstyle "run2_fld_cd"
    ```{.codeblock}
    Type: smallint

    Defensive position code of runner on second
    ```
    

??? columnstyle "run2_lineup_cd"
    ```{.codeblock}
    Type: smallint

    Lineup position of runner on second
    ```
    

??? columnstyle "run2_origin_event_id"
    ```{.codeblock}
    Type: smallint

    Event number on which runner on second reached base
    ```
    

??? columnstyle "run3_fld_cd"
    ```{.codeblock}
    Type: smallint

    Defensive position code of runner on third
    ```
    

??? columnstyle "run3_lineup_cd"
    ```{.codeblock}
    Type: smallint

    Lineup position of runner on third
    ```
    

??? columnstyle "run3_origin_event_id"
    ```{.codeblock}
    Type: smallint

    Event number on which runner on third reached base
    ```
    

??? columnstyle "run1_resp_cat_id"
    ```{.codeblock}
    Type: char(8)

    ID of responsible catcher for runner on first
    ```
    

??? columnstyle "run2_resp_cat_id"
    ```{.codeblock}
    Type: char(8)

    ID of responsible catcher for runner on second
    ```
    

??? columnstyle "run3_resp_cat_id"
    ```{.codeblock}
    Type: char(8)

    ID of responsible catcher for runner on third
    ```
    

??? columnstyle "pa_ball_ct"
    ```{.codeblock}
    Type: smallint

    Number of balls in plate appearance
    ```
    

??? columnstyle "pa_called_ball_ct"
    ```{.codeblock}
    Type: smallint

    Number of called balls in plate appearance
    ```
    

??? columnstyle "pa_intent_ball_ct"
    ```{.codeblock}
    Type: smallint

    Number of intentional balls in plate appearance
    ```
    

??? columnstyle "pa_pitchout_ball_ct"
    ```{.codeblock}
    Type: smallint

    Number of pitchouts in plate appearance
    ```
    

??? columnstyle "pa_hitbatter_ball_ct"
    ```{.codeblock}
    Type: smallint

    Number of pitches hitting batter in plate appearance
    ```
    

??? columnstyle "pa_other_ball_ct"
    ```{.codeblock}
    Type: smallint

    Number of other balls in plate appearance
    ```
    

??? columnstyle "pa_strike_ct"
    ```{.codeblock}
    Type: smallint

    Number of strikes in plate appearance
    ```
    

??? columnstyle "pa_called_strike_ct"
    ```{.codeblock}
    Type: smallint

    Number of called strikes in plate appearance
    ```
    

??? columnstyle "pa_swingmiss_strike_ct"
    ```{.codeblock}
    Type: smallint

    Number of swing-and-miss strikes in plate appearance
    ```
    

??? columnstyle "pa_foul_strike_ct"
    ```{.codeblock}
    Type: smallint

    Number of foul balls in plate appearance
    ```
    

??? columnstyle "pa_inplay_strike_ct"
    ```{.codeblock}
    Type: smallint

    Number of balls in play in plate appearance
    ```
    

??? columnstyle "pa_other_strike_ct"
    ```{.codeblock}
    Type: smallint

    Number of other strikes in plate appearance
    ```
    

??? columnstyle "event_runs_ct"
    ```{.codeblock}
    Type: smallint

    Number of runs on play
    ```
    

??? columnstyle "fld_id"
    ```{.codeblock}
    Type: char(8)

    ID of player fielding batted ball
    ```
    

??? columnstyle "base2_force_fl"
    ```{.codeblock}
    Type: boolean

    Event has force play at second
    ```
    

??? columnstyle "base3_force_fl"
    ```{.codeblock}
    Type: boolean

    Event has force play at third
    ```
    

??? columnstyle "base4_force_fl"
    ```{.codeblock}
    Type: boolean

    Event has force play at home
    ```
    

??? columnstyle "bat_safe_err_fl"
    ```{.codeblock}
    Type: boolean

    Event has batter safe on an error
    ```
    

??? columnstyle "bat_fate_id"
    ```{.codeblock}
    Type: smallint

    Ultimate fate of batter (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "run1_fate_id"
    ```{.codeblock}
    Type: smallint

    Ultimate fate of runner on first (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "run2_fate_id"
    ```{.codeblock}
    Type: smallint

    Ultimate fate of runner on second (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "run3_fate_id"
    ```{.codeblock}
    Type: smallint

    Ultimate fate of runner on third (see `dest_id` cols for code meaning
    ```
    

??? columnstyle "fate_runs_ct"
    ```{.codeblock}
    Type: smallint

    Additional runs scored in half inning after this event
    ```
    

??? columnstyle "ass6_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with sixth assist
    ```
    

??? columnstyle "ass7_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with seventh assist
    ```
    

??? columnstyle "ass8_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with eighth assist
    ```
    

??? columnstyle "ass9_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with ninth assist
    ```
    

??? columnstyle "ass10_fld_cd"
    ```{.codeblock}
    Type: smallint

    Position code of fielder with tenth assist
    ```
    

??? columnstyle "unknown_out_exc_fl"
    ```{.codeblock}
    Type: boolean

    Unknown fielding credit flag
    ```
    

??? columnstyle "uncertain_play_exc_fl"
    ```{.codeblock}
    Type: boolean

    Uncertain play flag
    ```
    



### game

??? keycolumnstyle "game_id"
    ```{.codeblock}
    Type: char(12)

    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "game_dt"
    ```{.codeblock}
    Type: date

    Game date
    ```
    

??? columnstyle "game_ct"
    ```{.codeblock}
    Type: smallint

    Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
    ```
    

??? columnstyle "game_dy"
    ```{.codeblock}
    Type: varchar(9)

    Day of week
    ```
    

??? columnstyle "start_game_tm"
    ```{.codeblock}
    Type: smallint

    Game start time (12HMM coded as integer, eg 1015 for 10:15 PM)
    ```
    

??? columnstyle "dh_fl"
    ```{.codeblock}
    Type: varchar(1)

    DH used
    ```
    

??? columnstyle "daynight_park_cd"
    ```{.codeblock}
    Type: varchar(1)

    D - day game, N - night game
    ```
    

??? columnstyle "away_team_id"
    ```{.codeblock}
    Type: char(3)

    Away team ID
    ```
    

??? columnstyle "home_team_id"
    ```{.codeblock}
    Type: char(3)

    Home team ID
    ```
    

??? columnstyle "park_id"
    ```{.codeblock}
    Type: varchar(5)

    Park ID
    ```
    

??? columnstyle "away_start_pit_id"
    ```{.codeblock}
    Type: char(8)

    Away team starting pitcher ID
    ```
    

??? columnstyle "home_start_pit_id"
    ```{.codeblock}
    Type: char(8)

    Home team starting pitcher ID
    ```
    

??? columnstyle "base4_ump_id"
    ```{.codeblock}
    Type: varchar(32)

    Home plate umpire ID
    ```
    

??? columnstyle "base1_ump_id"
    ```{.codeblock}
    Type: varchar(32)

    First base umpire ID
    ```
    

??? columnstyle "base2_ump_id"
    ```{.codeblock}
    Type: varchar(32)

    Second base umpire ID
    ```
    

??? columnstyle "base3_ump_id"
    ```{.codeblock}
    Type: varchar(32)

    Third base umpire ID
    ```
    

??? columnstyle "lf_ump_id"
    ```{.codeblock}
    Type: char(8)

    Left field umpire ID
    ```
    

??? columnstyle "rf_ump_id"
    ```{.codeblock}
    Type: char(8)

    Right field umpire ID
    ```
    

??? columnstyle "attend_park_ct"
    ```{.codeblock}
    Type: integer

    Attendance
    ```
    

??? columnstyle "scorer_record_id"
    ```{.codeblock}
    Type: varchar(50)

    Scorekeeper
    ```
    

??? columnstyle "translator_record_id"
    ```{.codeblock}
    Type: varchar(50)

    Translator
    ```
    

??? columnstyle "inputter_record_id"
    ```{.codeblock}
    Type: varchar(50)

    Inputter
    ```
    

??? columnstyle "input_record_ts"
    ```{.codeblock}
    Type: varchar(20)

    Date and time of record input
    ```
    

??? columnstyle "edit_record_ts"
    ```{.codeblock}
    Type: varchar(20)

    Date and time of Most recent record edit
    ```
    

??? columnstyle "method_record_cd"
    ```{.codeblock}
    Type: varchar(1)

    How the game was scored (join `code_method_record` for details
    ```
    

??? columnstyle "pitches_record_cd"
    ```{.codeblock}
    Type: varchar(1)

    Highest detail of pitches recorded (join `code_pitches_record` for details). Note that many games with pitch detail do not have that info for all events, so pitch totals may not be accurate.
    ```
    

??? columnstyle "temp_park_ct"
    ```{.codeblock}
    Type: smallint

    Park temperature in degrees F (0 if unknown)
    ```
    

??? columnstyle "wind_direction_park_cd"
    ```{.codeblock}
    Type: smallint

    Wind direction park code (join `code_wind_direction_park` for details)
    ```
    

??? columnstyle "wind_speed_park_ct"
    ```{.codeblock}
    Type: smallint

    Wind speed in miles per hour (-1 if unknown)
    ```
    

??? columnstyle "field_park_cd"
    ```{.codeblock}
    Type: smallint

    Park field condition code (join `code_field_park` for details)
    ```
    

??? columnstyle "precip_park_cd"
    ```{.codeblock}
    Type: smallint

    Park precipitation code (join `code_precip_park` for details
    ```
    

??? columnstyle "sky_park_cd"
    ```{.codeblock}
    Type: smallint

    Park sky condition code (join `code_sky_park` for details
    ```
    

??? columnstyle "minutes_game_ct"
    ```{.codeblock}
    Type: smallint

    Length of game in minutes
    ```
    

??? columnstyle "inn_ct"
    ```{.codeblock}
    Type: smallint

    Length of game in innings
    ```
    

??? columnstyle "away_score_ct"
    ```{.codeblock}
    Type: smallint

    Away team final score
    ```
    

??? columnstyle "home_score_ct"
    ```{.codeblock}
    Type: smallint

    Home team final score
    ```
    

??? columnstyle "away_hits_ct"
    ```{.codeblock}
    Type: smallint

    Away team hits
    ```
    

??? columnstyle "home_hits_ct"
    ```{.codeblock}
    Type: smallint

    Home team hits
    ```
    

??? columnstyle "away_err_ct"
    ```{.codeblock}
    Type: smallint

    Away team errors
    ```
    

??? columnstyle "home_err_ct"
    ```{.codeblock}
    Type: smallint

    Home team errors
    ```
    

??? columnstyle "away_lob_ct"
    ```{.codeblock}
    Type: smallint

    Away team left on base
    ```
    

??? columnstyle "home_lob_ct"
    ```{.codeblock}
    Type: smallint

    Home team left on base
    ```
    

??? columnstyle "win_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of winning pitcher
    ```
    

??? columnstyle "lose_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of losing pitcher
    ```
    

??? columnstyle "save_pit_id"
    ```{.codeblock}
    Type: char(8)

    ID of saving pitcher
    ```
    

??? columnstyle "gwrbi_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of batter wit game-winning RBI
    ```
    

??? columnstyle "away_lineup1_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 1
    ```
    

??? columnstyle "away_lineup1_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 1
    ```
    

??? columnstyle "away_lineup2_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 2
    ```
    

??? columnstyle "away_lineup2_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 2
    ```
    

??? columnstyle "away_lineup3_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 3
    ```
    

??? columnstyle "away_lineup3_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 3
    ```
    

??? columnstyle "away_lineup4_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 4
    ```
    

??? columnstyle "away_lineup4_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 4
    ```
    

??? columnstyle "away_lineup5_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 5
    ```
    

??? columnstyle "away_lineup5_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 5
    ```
    

??? columnstyle "away_lineup6_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 6
    ```
    

??? columnstyle "away_lineup6_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 6
    ```
    

??? columnstyle "away_lineup7_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 7
    ```
    

??? columnstyle "away_lineup7_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 7
    ```
    

??? columnstyle "away_lineup8_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 8
    ```
    

??? columnstyle "away_lineup8_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 8
    ```
    

??? columnstyle "away_lineup9_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of away team starting batter in lineup position 9
    ```
    

??? columnstyle "away_lineup9_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of away team starting batter in lineup position 9
    ```
    

??? columnstyle "home_lineup1_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 1
    ```
    

??? columnstyle "home_lineup1_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 1
    ```
    

??? columnstyle "home_lineup2_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 2
    ```
    

??? columnstyle "home_lineup2_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 2
    ```
    

??? columnstyle "home_lineup3_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 3
    ```
    

??? columnstyle "home_lineup3_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 3
    ```
    

??? columnstyle "home_lineup4_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 4
    ```
    

??? columnstyle "home_lineup4_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 4
    ```
    

??? columnstyle "home_lineup5_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 5
    ```
    

??? columnstyle "home_lineup5_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 5
    ```
    

??? columnstyle "home_lineup6_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 6
    ```
    

??? columnstyle "home_lineup6_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 6
    ```
    

??? columnstyle "home_lineup7_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 7
    ```
    

??? columnstyle "home_lineup7_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 7
    ```
    

??? columnstyle "home_lineup8_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 8
    ```
    

??? columnstyle "home_lineup8_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 8
    ```
    

??? columnstyle "home_lineup9_bat_id"
    ```{.codeblock}
    Type: char(8)

    ID of home team starting batter in lineup position 9
    ```
    

??? columnstyle "home_lineup9_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position code of home team starting batter in lineup position 9
    ```
    

??? columnstyle "away_finish_pit_id"
    ```{.codeblock}
    Type: char(8)

    Away team finishing pitcher
    ```
    

??? columnstyle "home_finish_pit_id"
    ```{.codeblock}
    Type: char(8)

    Home team finishing pitcher
    ```
    

??? columnstyle "away_team_league_id"
    ```{.codeblock}
    Type: char(1)

    Away team league (1 char ID)
    ```
    

??? columnstyle "home_team_league_id"
    ```{.codeblock}
    Type: char(1)

    Home team league (1 char ID)
    ```
    

??? columnstyle "away_team_game_ct"
    ```{.codeblock}
    Type: smallint

    Away team game number
    ```
    

??? columnstyle "home_team_game_ct"
    ```{.codeblock}
    Type: smallint

    Home team game number
    ```
    

??? columnstyle "outs_ct"
    ```{.codeblock}
    Type: smallint

    Length of game in outs
    ```
    

??? columnstyle "completion_tx"
    ```{.codeblock}
    Type: varchar(26)

    Information on completion of game
    ```
    

??? columnstyle "forfeit_tx"
    ```{.codeblock}
    Type: varchar(26)

    Information on forfeit of game
    ```
    

??? columnstyle "protest_tx"
    ```{.codeblock}
    Type: varchar(26)

    Information on protest of game
    ```
    

??? columnstyle "away_line_tx"
    ```{.codeblock}
    Type: varchar(26)

    Away team linescore
    ```
    

??? columnstyle "home_line_tx"
    ```{.codeblock}
    Type: varchar(26)

    Home team linescore
    ```
    

??? columnstyle "away_ab_ct"
    ```{.codeblock}
    Type: smallint

    Away team at bats
    ```
    

??? columnstyle "away_2b_ct"
    ```{.codeblock}
    Type: smallint

    Away team doubles
    ```
    

??? columnstyle "away_3b_ct"
    ```{.codeblock}
    Type: smallint

    Away team triples
    ```
    

??? columnstyle "away_hr_ct"
    ```{.codeblock}
    Type: smallint

    Away team home runs
    ```
    

??? columnstyle "away_bi_ct"
    ```{.codeblock}
    Type: smallint

    Away team runs batted in
    ```
    

??? columnstyle "away_sh_ct"
    ```{.codeblock}
    Type: smallint

    Away team sacrifice hits
    ```
    

??? columnstyle "away_sf_ct"
    ```{.codeblock}
    Type: smallint

    Away team sacrifice flies
    ```
    

??? columnstyle "away_hp_ct"
    ```{.codeblock}
    Type: smallint

    Away team hit by pitches
    ```
    

??? columnstyle "away_bb_ct"
    ```{.codeblock}
    Type: smallint

    Away team walks
    ```
    

??? columnstyle "away_ibb_ct"
    ```{.codeblock}
    Type: smallint

    Away team intentional walks
    ```
    

??? columnstyle "away_so_ct"
    ```{.codeblock}
    Type: smallint

    Away team strikeouts
    ```
    

??? columnstyle "away_sb_ct"
    ```{.codeblock}
    Type: smallint

    Away team stolen bases
    ```
    

??? columnstyle "away_cs_ct"
    ```{.codeblock}
    Type: smallint

    Away team caught stealing
    ```
    

??? columnstyle "away_gdp_ct"
    ```{.codeblock}
    Type: smallint

    Away team grounded into double plays
    ```
    

??? columnstyle "away_xi_ct"
    ```{.codeblock}
    Type: smallint

    Away team reached on interference
    ```
    

??? columnstyle "away_pitcher_ct"
    ```{.codeblock}
    Type: smallint

    Away team number of pitchers used
    ```
    

??? columnstyle "away_er_ct"
    ```{.codeblock}
    Type: smallint

    Away team individual earned runs
    ```
    

??? columnstyle "away_ter_ct"
    ```{.codeblock}
    Type: smallint

    Away team team earned runs
    ```
    

??? columnstyle "away_wp_ct"
    ```{.codeblock}
    Type: smallint

    Away team wild pitches
    ```
    

??? columnstyle "away_bk_ct"
    ```{.codeblock}
    Type: smallint

    Away team balks
    ```
    

??? columnstyle "away_po_ct"
    ```{.codeblock}
    Type: smallint

    Away team putouts
    ```
    

??? columnstyle "away_a_ct"
    ```{.codeblock}
    Type: smallint

    Away team assists
    ```
    

??? columnstyle "away_pb_ct"
    ```{.codeblock}
    Type: smallint

    Away team passed balls
    ```
    

??? columnstyle "away_dp_ct"
    ```{.codeblock}
    Type: smallint

    Away team double plays turned
    ```
    

??? columnstyle "away_tp_ct"
    ```{.codeblock}
    Type: smallint

    Away team triple plays turned
    ```
    

??? columnstyle "home_ab_ct"
    ```{.codeblock}
    Type: smallint

    Home team at bats
    ```
    

??? columnstyle "home_2b_ct"
    ```{.codeblock}
    Type: smallint

    Home team doubles
    ```
    

??? columnstyle "home_3b_ct"
    ```{.codeblock}
    Type: smallint

    Home team triples
    ```
    

??? columnstyle "home_hr_ct"
    ```{.codeblock}
    Type: smallint

    Home team home runs
    ```
    

??? columnstyle "home_bi_ct"
    ```{.codeblock}
    Type: smallint

    Home team runs batted in
    ```
    

??? columnstyle "home_sh_ct"
    ```{.codeblock}
    Type: smallint

    Home team sacrifice hits
    ```
    

??? columnstyle "home_sf_ct"
    ```{.codeblock}
    Type: smallint

    Home team sacrifice flies
    ```
    

??? columnstyle "home_hp_ct"
    ```{.codeblock}
    Type: smallint

    Home team hit by pitches
    ```
    

??? columnstyle "home_bb_ct"
    ```{.codeblock}
    Type: smallint

    Home team walks
    ```
    

??? columnstyle "home_ibb_ct"
    ```{.codeblock}
    Type: smallint

    Home team intentional walks
    ```
    

??? columnstyle "home_so_ct"
    ```{.codeblock}
    Type: smallint

    Home team strikeouts
    ```
    

??? columnstyle "home_sb_ct"
    ```{.codeblock}
    Type: smallint

    Home team stolen bases
    ```
    

??? columnstyle "home_cs_ct"
    ```{.codeblock}
    Type: smallint

    Home team caught stealing
    ```
    

??? columnstyle "home_gdp_ct"
    ```{.codeblock}
    Type: smallint

    Home team grounded into double plays
    ```
    

??? columnstyle "home_xi_ct"
    ```{.codeblock}
    Type: smallint

    Home team reached on interference
    ```
    

??? columnstyle "home_pitcher_ct"
    ```{.codeblock}
    Type: smallint

    Home team number of pitchers used
    ```
    

??? columnstyle "home_er_ct"
    ```{.codeblock}
    Type: smallint

    Home team individual earned runs
    ```
    

??? columnstyle "home_ter_ct"
    ```{.codeblock}
    Type: smallint

    Home team team earned runs
    ```
    

??? columnstyle "home_wp_ct"
    ```{.codeblock}
    Type: smallint

    Home team wild pitches
    ```
    

??? columnstyle "home_bk_ct"
    ```{.codeblock}
    Type: smallint

    Home team balks
    ```
    

??? columnstyle "home_po_ct"
    ```{.codeblock}
    Type: smallint

    Home team putouts
    ```
    

??? columnstyle "home_a_ct"
    ```{.codeblock}
    Type: smallint

    Home team assists
    ```
    

??? columnstyle "home_pb_ct"
    ```{.codeblock}
    Type: smallint

    Home team passed balls
    ```
    

??? columnstyle "home_dp_ct"
    ```{.codeblock}
    Type: smallint

    Home team double plays turned
    ```
    

??? columnstyle "home_tp_ct"
    ```{.codeblock}
    Type: smallint

    Home team triple plays turned
    ```
    

??? columnstyle "ump_home_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Home plate umpire name
    ```
    

??? columnstyle "ump_1b_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    First base umpire name
    ```
    

??? columnstyle "ump_2b_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Second base umpire name
    ```
    

??? columnstyle "ump_3b_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Third base umpire name
    ```
    

??? columnstyle "ump_lf_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Left field umpire name
    ```
    

??? columnstyle "ump_rf_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Right field umpire name
    ```
    

??? columnstyle "away_manager_id"
    ```{.codeblock}
    Type: char(8)

    Away manager ID
    ```
    

??? columnstyle "away_manager_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Away manager name
    ```
    

??? columnstyle "home_manager_id"
    ```{.codeblock}
    Type: char(8)

    Home manager ID
    ```
    

??? columnstyle "home_manager_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Home manager name
    ```
    

??? columnstyle "win_pit_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Wining pitcher name
    ```
    

??? columnstyle "lose_pit_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Losing pitcher name
    ```
    

??? columnstyle "save_pit_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Saving pitcher name
    ```
    

??? columnstyle "goahead_rbi_id"
    ```{.codeblock}
    Type: char(8)

    ID of batter with goahead RBI
    ```
    

??? columnstyle "goahead_rbi_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of batter with goahead RBI
    ```
    

??? columnstyle "away_lineup1_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 1
    ```
    

??? columnstyle "away_lineup2_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 2
    ```
    

??? columnstyle "away_lineup3_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 3
    ```
    

??? columnstyle "away_lineup4_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 4
    ```
    

??? columnstyle "away_lineup5_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 5
    ```
    

??? columnstyle "away_lineup6_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 6
    ```
    

??? columnstyle "away_lineup7_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 7
    ```
    

??? columnstyle "away_lineup8_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of away team batter in lineup position 8
    ```
    

??? columnstyle "away_lineup9_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 9
    ```
    

??? columnstyle "home_lineup1_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 1
    ```
    

??? columnstyle "home_lineup2_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 2
    ```
    

??? columnstyle "home_lineup3_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 3
    ```
    

??? columnstyle "home_lineup4_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 4
    ```
    

??? columnstyle "home_lineup5_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 5
    ```
    

??? columnstyle "home_lineup6_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 6
    ```
    

??? columnstyle "home_lineup7_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 7
    ```
    

??? columnstyle "home_lineup8_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 8
    ```
    

??? columnstyle "home_lineup9_bat_name_tx"
    ```{.codeblock}
    Type: varchar(26)

    Name of home team batter in lineup position 9
    ```
    

??? columnstyle "add_info_tx"
    ```{.codeblock}
    Type: varchar(26)

    Additional information
    ```
    

??? columnstyle "acq_info_tx"
    ```{.codeblock}
    Type: varchar(26)

    Acquisition information
    ```
    



### gamelog

??? keycolumnstyle "date"
    ```{.codeblock}
    Type: date

    Game date
    ```
    

??? keycolumnstyle "double_header"
    ```{.codeblock}
    Type: char(1)

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
    

??? keycolumnstyle "visiting_team"
    ```{.codeblock}
    Type: char(3)

    Visiting team ID
    ```
    

??? keycolumnstyle "home_team"
    ```{.codeblock}
    Type: char(3)

    Home team ID
    ```
    

??? columnstyle "day_of_week"
    ```{.codeblock}
    Type: char(3)

    Day of week (3 char abbreviation)
    ```
    

??? columnstyle "visiting_team_league"
    ```{.codeblock}
    Type: char(2)

    Away team league ID
    ```
    

??? columnstyle "visiting_team_game_number"
    ```{.codeblock}
    Type: smallint

    Away team game number
    ```
    

??? columnstyle "home_team_league"
    ```{.codeblock}
    Type: char(2)

    Home team league ID
    ```
    

??? columnstyle "home_team_game_number"
    ```{.codeblock}
    Type: smallint

    Home team game number
    ```
    

??? columnstyle "visitor_runs_scored"
    ```{.codeblock}
    Type: smallint

    Away team runs scored
    ```
    

??? columnstyle "home_runs_score"
    ```{.codeblock}
    Type: smallint

    Home team runs scored
    ```
    

??? columnstyle "length_in_outs"
    ```{.codeblock}
    Type: smallint

    Game length in outs
    ```
    

??? columnstyle "day_night"
    ```{.codeblock}
    Type: char(1)

    D - day game, N - night game
    ```
    

??? columnstyle "completion_info"
    ```{.codeblock}
    Type: varchar(23)

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
    

??? columnstyle "forfeit_info"
    ```{.codeblock}
    Type: varchar(3)

    V - forfeited to away team, H - forfeited to home team, T - ruled a no-decision
    ```
    

??? columnstyle "protest_info"
    ```{.codeblock}
    Type: varchar(3)

    P - protested by unidentified team, V - disallowed protest by away team, H - disallowed protest by home team, X - upheld protest by away team, Y - upheld protest by home team
    ```
    

??? columnstyle "park_id"
    ```{.codeblock}
    Type: char(5)

    Park ID
    ```
    

??? columnstyle "attendance"
    ```{.codeblock}
    Type: integer

    Attendance
    ```
    

??? columnstyle "duration"
    ```{.codeblock}
    Type: smallint

    Time of game in minutes
    ```
    

??? columnstyle "vistor_line_score"
    ```{.codeblock}
    Type: varchar(26)

    Away team line score, e.g. 010000(10)0x
    ```
    

??? columnstyle "home_line_score"
    ```{.codeblock}
    Type: varchar(26)

    Home team line score, e.g. 010000(10)0x
    ```
    

??? columnstyle "visitor_ab"
    ```{.codeblock}
    Type: smallint

    Away team at bats
    ```
    

??? columnstyle "visitor_h"
    ```{.codeblock}
    Type: smallint

    Away team hits
    ```
    

??? columnstyle "visitor_d"
    ```{.codeblock}
    Type: smallint

    Away team doubles
    ```
    

??? columnstyle "visitor_t"
    ```{.codeblock}
    Type: smallint

    Away team triples
    ```
    

??? columnstyle "visitor_hr"
    ```{.codeblock}
    Type: smallint

    Away team home runs
    ```
    

??? columnstyle "visitor_rbi"
    ```{.codeblock}
    Type: smallint

    Away team runs batted in
    ```
    

??? columnstyle "visitor_sh"
    ```{.codeblock}
    Type: smallint

    Away team sacrifice hits (may include sac flies before 1954)
    ```
    

??? columnstyle "visitor_sf"
    ```{.codeblock}
    Type: smallint

    Away team sacrifice flies (since 1954)
    ```
    

??? columnstyle "visitor_hbp"
    ```{.codeblock}
    Type: smallint

    Away team hit by pitches
    ```
    

??? columnstyle "visitor_bb"
    ```{.codeblock}
    Type: smallint

    Away team walks
    ```
    

??? columnstyle "visitor_ibb"
    ```{.codeblock}
    Type: smallint

    Away team intentional walks
    ```
    

??? columnstyle "visitor_k"
    ```{.codeblock}
    Type: smallint

    Away team strikeouts
    ```
    

??? columnstyle "visitor_sb"
    ```{.codeblock}
    Type: smallint

    Away team stolen bases
    ```
    

??? columnstyle "visitor_cs"
    ```{.codeblock}
    Type: smallint

    Away team caught stealing
    ```
    

??? columnstyle "visitor_gdp"
    ```{.codeblock}
    Type: smallint

    Away team grounded into double plays
    ```
    

??? columnstyle "visitor_ci"
    ```{.codeblock}
    Type: smallint

    Away team reached on interference
    ```
    

??? columnstyle "visitor_lob"
    ```{.codeblock}
    Type: smallint

    Away team left on base
    ```
    

??? columnstyle "visitor_pitchers"
    ```{.codeblock}
    Type: smallint

    Away team pitchers used
    ```
    

??? columnstyle "visitor_er"
    ```{.codeblock}
    Type: smallint

    Away team individual earned runs allowed
    ```
    

??? columnstyle "visitor_ter"
    ```{.codeblock}
    Type: smallint

    Away team team earned runs allowed
    ```
    

??? columnstyle "visitor_wp"
    ```{.codeblock}
    Type: smallint

    Away team wild pitches allowed
    ```
    

??? columnstyle "visitor_balks"
    ```{.codeblock}
    Type: smallint

    Away team balks allowed
    ```
    

??? columnstyle "visitor_po"
    ```{.codeblock}
    Type: smallint

    Away team putouts
    ```
    

??? columnstyle "visitor_a"
    ```{.codeblock}
    Type: smallint

    Away team assists
    ```
    

??? columnstyle "visitor_e"
    ```{.codeblock}
    Type: smallint

    Away team errors
    ```
    

??? columnstyle "visitor_passed"
    ```{.codeblock}
    Type: smallint

    Away team passed balls
    ```
    

??? columnstyle "visitor_db"
    ```{.codeblock}
    Type: smallint

    Away team double plays turned
    ```
    

??? columnstyle "visitor_tp"
    ```{.codeblock}
    Type: smallint

    Away team triple plays turned
    ```
    

??? columnstyle "home_ab"
    ```{.codeblock}
    Type: smallint

    Home team at bats
    ```
    

??? columnstyle "home_h"
    ```{.codeblock}
    Type: smallint

    Home team hits
    ```
    

??? columnstyle "home_d"
    ```{.codeblock}
    Type: smallint

    Home team doubles
    ```
    

??? columnstyle "home_t"
    ```{.codeblock}
    Type: smallint

    Home team triples
    ```
    

??? columnstyle "home_hr"
    ```{.codeblock}
    Type: smallint

    Home team home runs
    ```
    

??? columnstyle "home_rbi"
    ```{.codeblock}
    Type: smallint

    Home team runs batted in
    ```
    

??? columnstyle "home_sh"
    ```{.codeblock}
    Type: smallint

    Home team sacrifice hits (may include sac flies before 1954)
    ```
    

??? columnstyle "home_sf"
    ```{.codeblock}
    Type: smallint

    Home team sacrifice flies (since 1954)
    ```
    

??? columnstyle "home_hbp"
    ```{.codeblock}
    Type: smallint

    Home team hit by pitches
    ```
    

??? columnstyle "home_bb"
    ```{.codeblock}
    Type: smallint

    Home team walks
    ```
    

??? columnstyle "home_ibb"
    ```{.codeblock}
    Type: smallint

    Home team intentional walks
    ```
    

??? columnstyle "home_k"
    ```{.codeblock}
    Type: smallint

    Home team strikeouts
    ```
    

??? columnstyle "home_sb"
    ```{.codeblock}
    Type: smallint

    Home team stolen bases
    ```
    

??? columnstyle "home_cs"
    ```{.codeblock}
    Type: smallint

    Home team caught stealing
    ```
    

??? columnstyle "home_gdp"
    ```{.codeblock}
    Type: smallint

    Home team grounded into double plays
    ```
    

??? columnstyle "home_ci"
    ```{.codeblock}
    Type: smallint

    Home team reached on interference
    ```
    

??? columnstyle "home_lob"
    ```{.codeblock}
    Type: smallint

    Home team left on base
    ```
    

??? columnstyle "home_pitchers"
    ```{.codeblock}
    Type: smallint

    Home team pitchers used
    ```
    

??? columnstyle "home_er"
    ```{.codeblock}
    Type: smallint

    Home team individual earned runs allowed
    ```
    

??? columnstyle "home_ter"
    ```{.codeblock}
    Type: smallint

    Home team team earned runs allowed
    ```
    

??? columnstyle "home_wp"
    ```{.codeblock}
    Type: smallint

    Home team wild pitches allowed
    ```
    

??? columnstyle "home_balks"
    ```{.codeblock}
    Type: smallint

    Home team balks allowed
    ```
    

??? columnstyle "home_po"
    ```{.codeblock}
    Type: smallint

    Home team putouts
    ```
    

??? columnstyle "home_a"
    ```{.codeblock}
    Type: smallint

    Home team assists
    ```
    

??? columnstyle "home_e"
    ```{.codeblock}
    Type: smallint

    Home team errors
    ```
    

??? columnstyle "home_passed"
    ```{.codeblock}
    Type: smallint

    Home team passed balls
    ```
    

??? columnstyle "home_db"
    ```{.codeblock}
    Type: smallint

    Home team double plays turned
    ```
    

??? columnstyle "home_tp"
    ```{.codeblock}
    Type: smallint

    Home team triple plays turned
    ```
    

??? columnstyle "umpire_h_id"
    ```{.codeblock}
    Type: char(8)

    Home plate umpire ID
    ```
    

??? columnstyle "umpire_h_name"
    ```{.codeblock}
    Type: varchar(32)

    Home plate umpire name
    ```
    

??? columnstyle "umpire_1b_id"
    ```{.codeblock}
    Type: char(8)

    First base umpire ID
    ```
    

??? columnstyle "umpire_1b_name"
    ```{.codeblock}
    Type: varchar(32)

    First base umpire name
    ```
    

??? columnstyle "umpire_2b_id"
    ```{.codeblock}
    Type: char(8)

    Second base umpire ID
    ```
    

??? columnstyle "umpire_2b_name"
    ```{.codeblock}
    Type: varchar(32)

    Second base umpire name
    ```
    

??? columnstyle "umpire_3b_id"
    ```{.codeblock}
    Type: char(8)

    Third base umpire ID
    ```
    

??? columnstyle "umpire_3b_name"
    ```{.codeblock}
    Type: varchar(32)

    Third base umpire name
    ```
    

??? columnstyle "umpire_lf_id"
    ```{.codeblock}
    Type: char(8)

    Left field umpire ID
    ```
    

??? columnstyle "umpire_lf_name"
    ```{.codeblock}
    Type: varchar(32)

    Left field umpire name
    ```
    

??? columnstyle "umpire_rf_id"
    ```{.codeblock}
    Type: char(8)

    Right field umpire ID
    ```
    

??? columnstyle "umpire_rf_name"
    ```{.codeblock}
    Type: varchar(32)

    Right field umpire name
    ```
    

??? columnstyle "visitor_manager_id"
    ```{.codeblock}
    Type: char(8)

    Away team manager ID
    ```
    

??? columnstyle "visitor_manager_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team manager name
    ```
    

??? columnstyle "home_manager_id"
    ```{.codeblock}
    Type: char(8)

    Home team manager ID
    ```
    

??? columnstyle "home_manager_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team manager name
    ```
    

??? columnstyle "winning_pitcher_id"
    ```{.codeblock}
    Type: char(8)

    Winning pitcher ID
    ```
    

??? columnstyle "winning_pitcher_name"
    ```{.codeblock}
    Type: varchar(32)

    Winning pitcher name
    ```
    

??? columnstyle "losing_pitcher_id"
    ```{.codeblock}
    Type: char(8)

    Losing pitcher ID
    ```
    

??? columnstyle "losing_pitcher_name"
    ```{.codeblock}
    Type: varchar(32)

    Losing pitcher name
    ```
    

??? columnstyle "saving_pitcher_id"
    ```{.codeblock}
    Type: char(8)

    Saving pitcher ID
    ```
    

??? columnstyle "saving_pitcher_name"
    ```{.codeblock}
    Type: varchar(32)

    Saving pitcher name
    ```
    

??? columnstyle "game_winning_rbi_id"
    ```{.codeblock}
    Type: char(8)

    Game-winning RBI ID
    ```
    

??? columnstyle "game_winning_rbi_name"
    ```{.codeblock}
    Type: varchar(32)

    Game-winning RBI name
    ```
    

??? columnstyle "visitor_starting_pitcher_id"
    ```{.codeblock}
    Type: char(8)

    Away team starting pitcher ID
    ```
    

??? columnstyle "visitor_starting_pitcher_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team starting pitcher name
    ```
    

??? columnstyle "home_starting_pitcher_id"
    ```{.codeblock}
    Type: char(8)

    Home team starting pitcher ID
    ```
    

??? columnstyle "home_starting_pitcher_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team starting pitcher name
    ```
    

??? columnstyle "visitor_batting_1_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 1 starting player ID
    ```
    

??? columnstyle "visitor_batting_1_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 1 starting player name
    ```
    

??? columnstyle "visitor_batting_1_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 1 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_2_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 2 starting player ID
    ```
    

??? columnstyle "visitor_batting_2_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 2 starting player name
    ```
    

??? columnstyle "visitor_batting_2_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 2 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_3_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 3 starting player ID
    ```
    

??? columnstyle "visitor_batting_3_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 3 starting player name
    ```
    

??? columnstyle "visitor_batting_3_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 3 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_4_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 4 starting player ID
    ```
    

??? columnstyle "visitor_batting_4_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 4 starting player name
    ```
    

??? columnstyle "visitor_batting_4_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 4 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_5_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 5 starting player ID
    ```
    

??? columnstyle "visitor_batting_5_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 5 starting player name
    ```
    

??? columnstyle "visitor_batting_5_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 5 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_6_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 6 starting player ID
    ```
    

??? columnstyle "visitor_batting_6_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 6 starting player name
    ```
    

??? columnstyle "visitor_batting_6_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 6 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_7_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 7 starting player ID
    ```
    

??? columnstyle "visitor_batting_7_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 7 starting player name
    ```
    

??? columnstyle "visitor_batting_7_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 7 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_8_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 8 starting player ID
    ```
    

??? columnstyle "visitor_batting_8_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 8 starting player name
    ```
    

??? columnstyle "visitor_batting_8_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 8 starting player fielding position
    ```
    

??? columnstyle "visitor_batting_9_player_id"
    ```{.codeblock}
    Type: char(8)

    Away team lineup slot 9 starting player ID
    ```
    

??? columnstyle "visitor_batting_9_name"
    ```{.codeblock}
    Type: varchar(32)

    Away team lineup slot 9 starting player name
    ```
    

??? columnstyle "visitor_batting_9_position"
    ```{.codeblock}
    Type: smallint

    Away team lineup slot 9 starting player fielding position
    ```
    

??? columnstyle "home_batting_1_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 1 starting player ID
    ```
    

??? columnstyle "home_batting_1_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 1 starting player name
    ```
    

??? columnstyle "home_batting_1_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 1 starting player fielding position
    ```
    

??? columnstyle "home_batting_2_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 2 starting player ID
    ```
    

??? columnstyle "home_batting_2_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 2 starting player name
    ```
    

??? columnstyle "home_batting_2_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 2 starting player fielding position
    ```
    

??? columnstyle "home_batting_3_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 3 starting player ID
    ```
    

??? columnstyle "home_batting_3_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 3 starting player name
    ```
    

??? columnstyle "home_batting_3_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 3 starting player fielding position
    ```
    

??? columnstyle "home_batting_4_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 4 starting player ID
    ```
    

??? columnstyle "home_batting_4_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 4 starting player name
    ```
    

??? columnstyle "home_batting_4_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 4 starting player fielding position
    ```
    

??? columnstyle "home_batting_5_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 5 starting player ID
    ```
    

??? columnstyle "home_batting_5_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 5 starting player name
    ```
    

??? columnstyle "home_batting_5_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 5 starting player fielding position
    ```
    

??? columnstyle "home_batting_6_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 6 starting player ID
    ```
    

??? columnstyle "home_batting_6_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 6 starting player name
    ```
    

??? columnstyle "home_batting_6_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 6 starting player fielding position
    ```
    

??? columnstyle "home_batting_7_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 7 starting player ID
    ```
    

??? columnstyle "home_batting_7_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 7 starting player name
    ```
    

??? columnstyle "home_batting_7_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 7 starting player fielding position
    ```
    

??? columnstyle "home_batting_8_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 8 starting player ID
    ```
    

??? columnstyle "home_batting_8_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 8 starting player name
    ```
    

??? columnstyle "home_batting_8_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 8 starting player fielding position
    ```
    

??? columnstyle "home_batting_9_player_id"
    ```{.codeblock}
    Type: char(8)

    Home team lineup slot 9 starting player ID
    ```
    

??? columnstyle "home_batting_9_name"
    ```{.codeblock}
    Type: varchar(32)

    Home team lineup slot 9 starting player name
    ```
    

??? columnstyle "home_batting_9_position"
    ```{.codeblock}
    Type: smallint

    Home team lineup slot 9 starting player fielding position
    ```
    

??? columnstyle "additional_info"
    ```{.codeblock}
    Type: varchar(128)

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
    

??? columnstyle "acquisition_info"
    ```{.codeblock}
    Type: char(1)

    Y - complete game information, N - no game information, D - game derived from box score and game story, P - portions of game information
    ```
    



### park

??? keycolumnstyle "park_id"
    ```{.codeblock}
    Type: char(5)

    Park ID
    ```
    

??? columnstyle "name"
    ```{.codeblock}
    Type: varchar(41)

    Park name
    ```
    

??? columnstyle "aka"
    ```{.codeblock}
    Type: varchar(55)

    Common park alias
    ```
    

??? columnstyle "city"
    ```{.codeblock}
    Type: varchar(17)

    City
    ```
    

??? columnstyle "state"
    ```{.codeblock}
    Type: varchar(9)

    State
    ```
    

??? columnstyle "start_date"
    ```{.codeblock}
    Type: varchar(10)

    First game
    ```
    

??? columnstyle "end_date"
    ```{.codeblock}
    Type: varchar(10)

    Last game
    ```
    

??? columnstyle "league"
    ```{.codeblock}
    Type: char(2)

    League ID
    ```
    

??? columnstyle "notes"
    ```{.codeblock}
    Type: varchar(54)

    Misc. notes
    ```
    



### roster

??? keycolumnstyle "year"
    ```{.codeblock}
    Type: integer

    Year of roster
    ```
    

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: char(8)

    Player ID
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: char(3)

    Team ID
    ```
    

??? keycolumnstyle "position"
    ```{.codeblock}
    Type: varchar(2)

    Primary fielding position
    ```
    

??? columnstyle "last_name"
    ```{.codeblock}
    Type: varchar(32)

    Player last name
    ```
    

??? columnstyle "first_name"
    ```{.codeblock}
    Type: varchar(32)

    Player first name
    ```
    

??? columnstyle "bats"
    ```{.codeblock}
    Type: char(1)

    Bat handedness
    ```
    

??? columnstyle "throws"
    ```{.codeblock}
    Type: char(1)

    Throw handedness
    ```
    



### schedule

??? keycolumnstyle "date"
    ```{.codeblock}
    Type: date

    Scheduled game date
    ```
    

??? keycolumnstyle "home_team"
    ```{.codeblock}
    Type: char(3)

    Home team ID
    ```
    

??? keycolumnstyle "home_team_game_number"
    ```{.codeblock}
    Type: integer

    Home team game number
    ```
    

??? columnstyle "double_header"
    ```{.codeblock}
    Type: smallint

    Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, 2 - second game of doubleheader
    ```
    

??? columnstyle "day_of_week"
    ```{.codeblock}
    Type: char(3)

    Day of week (3 letter abbreviation
    ```
    

??? columnstyle "visiting_team"
    ```{.codeblock}
    Type: char(3)

    Away team ID
    ```
    

??? columnstyle "visiting_team_league"
    ```{.codeblock}
    Type: char(2)

    Away team league ID
    ```
    

??? columnstyle "visiting_team_game_number"
    ```{.codeblock}
    Type: smallint

    Away team game number
    ```
    

??? columnstyle "home_team_league"
    ```{.codeblock}
    Type: char(2)

    Home team league ID
    ```
    

??? columnstyle "day_night"
    ```{.codeblock}
    Type: char(1)

    D - day, N - night
    ```
    

??? columnstyle "postponement_indicator"
    ```{.codeblock}
    Type: varchar(120)

    This field will contain one or more phrases related to the game if it was
    not played as scheduled. If there is more than one phrase, they are separated
    by a semi-colon (";"). There are three possible outcomes for games not played
    on the originally scheduled date:
    -- The game was played on another date
    -- The game was played on the original date but at another site
    -- The game was not played
    
    ```
    

??? columnstyle "makeup_dates"
    ```{.codeblock}
    Type: varchar(120)

    This field will contain a makeup date if the postponed game was played at
    another time or place. If an attempt was known to have been made on a date but
    postponed again, that date will be listed. In that case, there will be a second
    date for the date when the game was actually played, in this form: "20150428;
    20150528" For the note about a team folding, the team code is one of the
    standard Retrosheet team IDs. The same is true for the team played as note.
    Often, the two of these are combined in one field.
    
    ```
    



### sub

??? keycolumnstyle "dummy_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "game_id"
    ```{.codeblock}
    Type: char(12)

    Game ID (home team ID + YYYYMMDD + doubleheader flag
    ```
    

??? columnstyle "inn_ct"
    ```{.codeblock}
    Type: smallint

    Inning of substitution
    ```
    

??? columnstyle "bat_home_id"
    ```{.codeblock}
    Type: smallint

    Is home team batting (-1 for N/A)
    ```
    

??? columnstyle "sub_id"
    ```{.codeblock}
    Type: char(8)

    Player ID of substitute
    ```
    

??? columnstyle "sub_home_id"
    ```{.codeblock}
    Type: boolean

    Is the home team making the substitution
    ```
    

??? columnstyle "sub_lineup_id"
    ```{.codeblock}
    Type: smallint

    Lineup position of substitution
    ```
    

??? columnstyle "sub_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position of substitution
    ```
    

??? columnstyle "removed_id"
    ```{.codeblock}
    Type: char(8)

    ID of removed player
    ```
    

??? columnstyle "removed_fld_cd"
    ```{.codeblock}
    Type: smallint

    Fielding position of removed player
    ```
    

??? columnstyle "event_id"
    ```{.codeblock}
    Type: smallint

    Event number in which substitution occurred
    ```
    





## baseballdatabank
### allstar_full

??? keycolumnstyle "dummy_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "game_num"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "game_id"
    ```{.codeblock}
    Type: varchar(12)

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "gp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "starting_pos"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### appearances

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g_all"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_batting"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_defense"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_p"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_c"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_1b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_2b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_3b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_ss"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_lf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_cf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_rf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_of"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_dh"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_ph"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_pr"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### awards_managers

??? keycolumnstyle "dummy_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "player_id"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? columnstyle "award_id"
    ```{.codeblock}
    Type: varchar(75)

    No documentation provided.
    ```
    

??? columnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "tie"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "notes"
    ```{.codeblock}
    Type: varchar(100)

    No documentation provided.
    ```
    



### awards_players

??? keycolumnstyle "dummy_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "award_id"
    ```{.codeblock}
    Type: varchar(255)

    No documentation provided.
    ```
    

??? columnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "tie"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "notes"
    ```{.codeblock}
    Type: varchar(100)

    No documentation provided.
    ```
    



### awards_share_managers

??? keycolumnstyle "award_id"
    ```{.codeblock}
    Type: varchar(25)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "points_won"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "points_max"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "votes_first"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    



### awards_share_players

??? keycolumnstyle "award_id"
    ```{.codeblock}
    Type: varchar(25)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "points_won"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "points_max"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "votes_first"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    



### batting

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "stint"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ab"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "r"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "h"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "_2b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "_3b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hr"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "rbi"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "so"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ibb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hbp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sh"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gidp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### batting_post

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "round"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ab"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "r"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "h"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "_2b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "_3b"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hr"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "rbi"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "so"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ibb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hbp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sh"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gidp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### college_playing

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "school_id"
    ```{.codeblock}
    Type: varchar(15)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### fielding

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "stint"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "pos"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "inn_outs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "po"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "a"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "e"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "dp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "pb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "wp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "zr"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    



### fielding_of

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "stint"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_lf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_cf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g_rf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### fielding_of_split

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "stint"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "pos"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "inn_outs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "po"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "a"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "e"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "dp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "pb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "wp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "zr"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    



### fielding_post

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "round"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? keycolumnstyle "pos"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "inn_outs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "po"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "a"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "e"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "dp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "tp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "pb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### hall_of_fame

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "voted_by"
    ```{.codeblock}
    Type: varchar(64)

    No documentation provided.
    ```
    

??? columnstyle "ballots"
    ```{.codeblock}
    Type: varchar(64)

    No documentation provided.
    ```
    

??? columnstyle "needed"
    ```{.codeblock}
    Type: varchar(64)

    No documentation provided.
    ```
    

??? columnstyle "votes"
    ```{.codeblock}
    Type: varchar(64)

    No documentation provided.
    ```
    

??? columnstyle "inducted"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "category"
    ```{.codeblock}
    Type: varchar(20)

    No documentation provided.
    ```
    

??? columnstyle "needed_note"
    ```{.codeblock}
    Type: varchar(25)

    No documentation provided.
    ```
    



### home_games

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? keycolumnstyle "park_id"
    ```{.codeblock}
    Type: varchar(5)

    No documentation provided.
    ```
    

??? columnstyle "first_game"
    ```{.codeblock}
    Type: date

    No documentation provided.
    ```
    

??? columnstyle "last_game"
    ```{.codeblock}
    Type: date

    No documentation provided.
    ```
    

??? columnstyle "games"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "openings"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "attendance"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    



### managers

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? keycolumnstyle "inseason"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "player_id"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "w"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "l"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "rank"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "plyr_mgr"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    



### managers_half

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? keycolumnstyle "half"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "inseason"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "w"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "l"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "rank"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### parks

??? keycolumnstyle "park_id"
    ```{.codeblock}
    Type: varchar(5)

    No documentation provided.
    ```
    

??? columnstyle "park_name"
    ```{.codeblock}
    Type: varchar(40)

    No documentation provided.
    ```
    

??? columnstyle "park_alias"
    ```{.codeblock}
    Type: varchar(55)

    No documentation provided.
    ```
    

??? columnstyle "city"
    ```{.codeblock}
    Type: varchar(25)

    No documentation provided.
    ```
    

??? columnstyle "state"
    ```{.codeblock}
    Type: varchar(16)

    No documentation provided.
    ```
    

??? columnstyle "country"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    



### people

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? columnstyle "birth_year"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "birth_month"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "birth_day"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "birth_country"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "birth_state"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "birth_city"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "death_year"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "death_month"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "death_day"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "death_country"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "death_state"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "death_city"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "name_first"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "name_last"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "name_given"
    ```{.codeblock}
    Type: varchar(255)

    No documentation provided.
    ```
    

??? columnstyle "weight"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "height"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "bats"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "throws"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "debut"
    ```{.codeblock}
    Type: date

    No documentation provided.
    ```
    

??? columnstyle "final_game"
    ```{.codeblock}
    Type: date

    No documentation provided.
    ```
    

??? columnstyle "retro_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "bbref_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    



### pitching

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "stint"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "w"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "l"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cg"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sho"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sv"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ip_outs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "h"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "er"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hr"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "so"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ba_opp"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "era"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "ibb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "wp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hbp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bk"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bfp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "r"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sh"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gidp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### pitching_post

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "round"
    ```{.codeblock}
    Type: varchar(10)

    No documentation provided.
    ```
    

??? columnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "w"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "l"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "cg"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sho"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sv"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ip_outs"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "h"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "er"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hr"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "so"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ba_opp"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "era"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "ibb"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "wp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "hbp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bk"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "bfp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "r"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sh"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "sf"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "gidp"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### salaries

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? keycolumnstyle "player_id"
    ```{.codeblock}
    Type: varchar(9)

    No documentation provided.
    ```
    

??? columnstyle "salary"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    



### schools

??? keycolumnstyle "school_id"
    ```{.codeblock}
    Type: varchar(15)

    No documentation provided.
    ```
    

??? columnstyle "name_full"
    ```{.codeblock}
    Type: varchar(255)

    No documentation provided.
    ```
    

??? columnstyle "city"
    ```{.codeblock}
    Type: varchar(55)

    No documentation provided.
    ```
    

??? columnstyle "state"
    ```{.codeblock}
    Type: varchar(55)

    No documentation provided.
    ```
    

??? columnstyle "country"
    ```{.codeblock}
    Type: varchar(55)

    No documentation provided.
    ```
    



### series_post

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "round"
    ```{.codeblock}
    Type: varchar(5)

    No documentation provided.
    ```
    

??? columnstyle "team_id_winner"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id_winner"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "team_id_loser"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "lg_id_loser"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "wins"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "losses"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? columnstyle "ties"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    



### teams

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: smallint

    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "franch_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "div_id"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "rank"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "g_home"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "w"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "l"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "div_win"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "wc_win"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "lg_win"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "ws_win"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "r"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "ab"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "h"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "_2b"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "_3b"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "hr"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "bb"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "so"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "sb"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "cs"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "hbp"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "sf"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "ra"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "er"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "era"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "cg"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "sho"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "sv"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "ip_outs"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "h_a"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "hr_a"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "bb_a"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "so_a"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "e"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "dp"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "fp"
    ```{.codeblock}
    Type: float

    No documentation provided.
    ```
    

??? columnstyle "name"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "park"
    ```{.codeblock}
    Type: varchar(255)

    No documentation provided.
    ```
    

??? columnstyle "attendance"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "bpf"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "ppf"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "team_id_br"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "team_id_lahman45"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "team_id_retro"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    



### teams_franchises

??? keycolumnstyle "franch_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? columnstyle "franch_name"
    ```{.codeblock}
    Type: varchar(50)

    No documentation provided.
    ```
    

??? columnstyle "active"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? columnstyle "na_assoc"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    



### teams_half

??? keycolumnstyle "year_id"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? keycolumnstyle "lg_id"
    ```{.codeblock}
    Type: varchar(2)

    No documentation provided.
    ```
    

??? keycolumnstyle "team_id"
    ```{.codeblock}
    Type: varchar(3)

    No documentation provided.
    ```
    

??? keycolumnstyle "half"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "div_id"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "div_win"
    ```{.codeblock}
    Type: varchar(1)

    No documentation provided.
    ```
    

??? columnstyle "rank"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "g"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "w"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    

??? columnstyle "l"
    ```{.codeblock}
    Type: integer

    No documentation provided.
    ```
    




