# coding: utf-8
from sqlalchemy import MetaData, Boolean, CHAR, Column, Date, Integer, SmallInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData(schema="retrosheet"))
metadata: MetaData = Base.metadata


class Event(Base):
    __tablename__ = 'event'

    game_id = Column(CHAR(12), primary_key=True, doc="Game ID (home team ID + YYYYMMDD + doubleheader flag")
    away_team_id = Column(CHAR(3), doc="Visiting Team")
    inn_ct = Column(SmallInteger, doc="Inning")
    bat_home_id = Column(Boolean, doc="Home team is batting")
    outs_ct = Column(SmallInteger, doc="Outs (0-2)")
    balls_ct = Column(SmallInteger, doc="Balls (0-3)")
    strikes_ct = Column(SmallInteger, doc="Strikes (0-2")
    pitch_seq_tx = Column(String(30), doc="Pitch sequence")
    away_score_ct = Column(SmallInteger, doc="Away score")
    home_score_ct = Column(SmallInteger, doc="Home score")
    bat_id = Column(CHAR(8), doc="Batter ID")
    bat_hand_cd = Column(CHAR(1), doc="Batter handedness")
    resp_bat_id = Column(CHAR(8), doc="ID of batter charged with event")
    resp_bat_hand_cd = Column(CHAR(1), doc="Handedness of batter charged with event")
    pit_id = Column(CHAR(8), doc="Pitcher ID")
    pit_hand_cd = Column(CHAR(1), doc="Pitcher handedness")
    resp_pit_id = Column(CHAR(8), doc="ID of pitcher charged with event")
    resp_pit_hand_cd = Column(CHAR(1), doc="Handedness of pitcher charged with event")
    pos2_fld_id = Column(CHAR(8), doc="Catcher ID")
    pos3_fld_id = Column(CHAR(8), doc="First baseman ID")
    pos4_fld_id = Column(CHAR(8), doc="Second baseman ID")
    pos5_fld_id = Column(CHAR(8), doc="Third baseman ID")
    pos6_fld_id = Column(CHAR(8), doc="Shortstop ID")
    pos7_fld_id = Column(CHAR(8), doc="Left fielder ID")
    pos8_fld_id = Column(CHAR(8), doc="Center fielder ID")
    pos9_fld_id = Column(CHAR(8), doc="Right fielder ID")
    base1_run_id = Column(CHAR(8), doc="ID of runner on first")
    base2_run_id = Column(CHAR(8), doc="ID of runner on second")
    base3_run_id = Column(CHAR(8), doc="ID of runner on third")
    event_tx = Column(String(58), doc="Event text (in scoring shorthand")
    leadoff_fl = Column(Boolean, doc="Batter is leading off the inning")
    ph_fl = Column(Boolean, doc="Batter is pinch-hitting")
    bat_fld_cd = Column(SmallInteger, doc="Defensive position of batter (10 for DH, 11 for PH, 12 for PR")
    bat_lineup_id = Column(SmallInteger, doc="Lineup position (1-9)")
    event_cd = Column(SmallInteger, doc="Event code (join table `code_event` for descriptions")
    bat_event_fl = Column(Boolean, doc="Event is related to the batter")
    ab_fl = Column(Boolean, doc="Event is an at-bat")
    h_fl = Column(SmallInteger, doc="Event is a hit")
    sh_fl = Column(Boolean, doc="Event is a sacrifice hit")
    sf_fl = Column(Boolean, doc="Event is a sacrifice fly")
    event_outs_ct = Column(SmallInteger, doc="Outs recorded on event (0-3)")
    dp_fl = Column(Boolean, doc="Event is a double play")
    tp_fl = Column(Boolean, doc="Event is a triple play")
    rbi_ct = Column(SmallInteger, doc="Runs batted in on event")
    wp_fl = Column(Boolean, doc="Event is a wild pitch")
    pb_fl = Column(Boolean, doc="Event is a passed ball")
    fld_cd = Column(SmallInteger, doc="Position id of event fielder")
    battedball_cd = Column(CHAR(1), doc="Batted ball code (P - pop-up, G - ground ball, F - fly ball, L - line drive")
    bunt_fl = Column(Boolean, doc="Event is a bunt")
    foul_fl = Column(Boolean, doc="Event is a foul ball")
    battedball_loc_tx = Column(String(5), "Hit location code (see https://www.retrosheet.org/location.htm)")
    err_ct = Column(SmallInteger, doc="Number of errors recorded during event")
    err1_fld_cd = Column(SmallInteger, doc="Position code of fielder committing first error during event")
    err1_cd = Column(CHAR(1), doc="First error type (T - throwing, F - fielding)")
    err2_fld_cd = Column(SmallInteger, doc="Position code of fielder committing second error during event")
    err2_cd = Column(CHAR(1), doc="Second error type (T - throwing, F - fielding)")
    err3_fld_cd = Column(SmallInteger, doc="Position code of fielder committing third error during event")
    err3_cd = Column(CHAR(1), doc="Third error type (T - throwing, F - fielding)")
    bat_dest_id = Column(SmallInteger, doc="Destination of batter after event (0 - putout, 1-3 - bases, 4 - scored as"
                                           "earned run, 5 - scored as unearned, 6 - scored as unearned to team "
                                           "earned to pitcher)")
    run1_dest_id = Column(SmallInteger, doc="Destination of runner on first after event (0 - putout, 1-3 - bases, "
                                            "4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned "
                                            "to team earned to pitcher)")
    run2_dest_id = Column(SmallInteger, doc="Destination of runner on second after event (0 - putout, 1-3 - bases, "
                                            "4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned "
                                            "to team earned to pitcher)")
    run3_dest_id = Column(SmallInteger, doc="Destination of runner on third after event (0 - putout, 1-3 - bases, "
                                            "4 - scored as earned run, 5 - scored as unearned, 6 - scored as unearned "
                                            "to team earned to pitcher)")
    bat_play_tx = Column(String(15), doc="Fielding play on batter")
    run1_play_tx = Column(String(15), doc="Fielding play on runner on first")
    run2_play_tx = Column(String(15), doc="Fielding play on runner on second")
    run3_play_tx = Column(String(15), doc="Fielding play on runner on third")
    run1_sb_fl = Column(Boolean, doc="Runner on first steals base")
    run2_sb_fl = Column(Boolean, doc="Runner on second steals base")
    run3_sb_fl = Column(Boolean, doc="Runner on third steals base")
    run1_cs_fl = Column(Boolean, doc="Runner on first caught stealing")
    run2_cs_fl = Column(Boolean, doc="Runner on second caught stealing")
    run3_cs_fl = Column(Boolean, doc="Runner on third caught stealing")
    run1_pk_fl = Column(Boolean, doc="Runner on first picked off")
    run2_pk_fl = Column(Boolean, doc="Runner on second picked off")
    run3_pk_fl = Column(Boolean, doc="Runner on third picked off")
    run1_resp_pit_id = Column(CHAR(8), doc="ID of pitcher charged with runner on first")
    run2_resp_pit_id = Column(CHAR(8), doc="ID of pitcher charged with runner on second")
    run3_resp_pit_id = Column(CHAR(8), doc="ID of pitcher charged with runner on third")
    game_new_fl = Column(Boolean, doc="Start of game flag")
    game_end_fl = Column(Boolean, doc="End of game flag")
    pr_run1_fl = Column(Boolean, doc="Pinch-runner on first")
    pr_run2_fl = Column(Boolean, doc="Pinch-runner on second")
    pr_run3_fl = Column(Boolean, doc="Runner on third")
    removed_for_pr_run1_id = Column(CHAR(8), doc="ID of former runner on first removed for pinch-runner")
    removed_for_pr_run2_id = Column(CHAR(8), doc="ID of former runner on second removed for pinch-runner")
    removed_for_pr_run3_id = Column(CHAR(8), doc="ID of former runner on third removed for pinch-runner")
    removed_for_ph_bat_id = Column(CHAR(8), doc="ID of former batter removed for pinch-hitter")
    removed_for_ph_bat_fld_cd = Column(Integer, doc="Position code of batter removed for pinch-hitter")
    po1_fld_cd = Column(SmallInteger, doc="Position code of fielder with first putout")
    po2_fld_cd = Column(SmallInteger, doc="Position code of fielder with second putout")
    po3_fld_cd = Column(SmallInteger, doc="Position code of fielder with third putout")
    ass1_fld_cd = Column(SmallInteger, doc="Position code of fielder with first assist")
    ass2_fld_cd = Column(SmallInteger, doc="Position code of fielder with second assist")
    ass3_fld_cd = Column(SmallInteger, doc="Position code of fielder with third assist")
    ass4_fld_cd = Column(SmallInteger, doc="Position code of fielder with fourth assist")
    ass5_fld_cd = Column(SmallInteger, doc="Position code of fielder with fifth assist")
    event_id = Column(Integer, primary_key=True, doc="Event number of game")
    home_team_id = Column(CHAR(3), doc="Home team ID")
    bat_team_id = Column(CHAR(3), doc="Batting team ID")
    fld_team_id = Column(CHAR(3), doc="Fielding team ID")
    bat_last_id = Column(SmallInteger, doc="Half inning (differs from batting team if home team bats first)")
    inn_new_fl = Column(Boolean, doc="Start of half-inning flag")
    inn_end_fl = Column(Boolean, doc="End of half-inning flag")
    start_bat_score_ct = Column(SmallInteger, doc="Runs scored by batting team (prior to this event)")
    start_fld_score_ct = Column(SmallInteger, doc="Runs scored by fielding team")
    inn_runs_ct = Column(SmallInteger, doc="Runs scored in this half-inning (prior to this event)")
    game_pa_ct = Column(SmallInteger, doc="Batting team PA total (prior to this event)")
    inn_pa_ct = Column(SmallInteger, doc="Half-inning PA total (prior to this event)")
    pa_new_fl = Column(Boolean, doc="Event is the start of a plate appearance")
    pa_trunc_fl = Column(Boolean, doc="Event is a truncated plate appearance")
    start_bases_cd = Column(SmallInteger, doc="Base state at start of event (0-7, binary value is flags for "
                                              "runners on third, second, and first left-to-right)")
    end_bases_cd = Column(SmallInteger, doc="Base state end of event (0-7, binary value is flags for "
                                            "runners on third, second, and first left-to-right)")
    bat_start_fl = Column(Boolean, doc="Batter started game")
    resp_bat_start_fl = Column(Boolean, doc="Result-charged batter is a starter")
    bat_on_deck_id = Column(CHAR(8), doc="ID of batter on deck")
    bat_in_hold_id = Column(CHAR(8), doc="Id of batter in the hole")
    pit_start_fl = Column(Boolean, doc="Pitcher started game")
    resp_pit_start_fl = Column(Boolean, doc="Result-charged pitcher started game")
    run1_fld_cd = Column(SmallInteger, doc="Defensive position code of runner on first")
    run1_lineup_cd = Column(SmallInteger, doc="Lineup position of runner on first")
    run1_origin_event_id = Column(SmallInteger, doc="Event number on which runner on first reached base")
    run2_fld_cd = Column(SmallInteger, doc="Defensive position code of runner on second")
    run2_lineup_cd = Column(SmallInteger, doc="Lineup position of runner on second")
    run2_origin_event_id = Column(SmallInteger, doc="Event number on which runner on second reached base")
    run3_fld_cd = Column(SmallInteger, doc="Defensive position code of runner on third")
    run3_lineup_cd = Column(SmallInteger, doc="Lineup position of runner on third")
    run3_origin_event_id = Column(SmallInteger, doc="Event number on which runner on third reached base")
    run1_resp_cat_id = Column(CHAR(8), doc="ID of responsible catcher for runner on first")
    run2_resp_cat_id = Column(CHAR(8), doc="ID of responsible catcher for runner on second")
    run3_resp_cat_id = Column(CHAR(8), doc="ID of responsible catcher for runner on third")
    pa_ball_ct = Column(SmallInteger, doc="Number of balls in plate appearance")
    pa_called_ball_ct = Column(SmallInteger, doc="Number of called balls in plate appearance")
    pa_intent_ball_ct = Column(SmallInteger, doc="Number of intentional balls in plate appearance")
    pa_pitchout_ball_ct = Column(SmallInteger, doc="Number of pitchouts in plate appearance")
    pa_hitbatter_ball_ct = Column(SmallInteger, doc="Number of pitches hitting batter in plate appearance")
    pa_other_ball_ct = Column(SmallInteger, doc="Number of other balls in plate appearance")
    pa_strike_ct = Column(SmallInteger, doc="Number of strikes in plate appearance")
    pa_called_strike_ct = Column(SmallInteger, doc="Number of called strikes in plate appearance")
    pa_swingmiss_strike_ct = Column(SmallInteger, doc="Number of swing-and-miss strikes in plate appearance")
    pa_foul_strike_ct = Column(SmallInteger, doc="Number of foul balls in plate appearance")
    pa_inplay_strike_ct = Column(SmallInteger, doc="Number of balls in play in plate appearance")
    pa_other_strike_ct = Column(SmallInteger, doc="Number of other strikes in plate appearance")
    event_runs_ct = Column(SmallInteger, doc="Number of runs on play")
    fld_id = Column(CHAR(8), doc="ID of player fielding batted ball")
    base2_force_fl = Column(Boolean, doc="Event has force play at second")
    base3_force_fl = Column(Boolean, doc="Event has force play at third")
    base4_force_fl = Column(Boolean, doc="Event has force play at home")
    bat_safe_err_fl = Column(Boolean, doc="Event has batter safe on an error")
    bat_fate_id = Column(SmallInteger, doc="Ultimate fate of batter (see `dest_id` cols for code meaning")
    run1_fate_id = Column(SmallInteger, doc="Ultimate fate of runner on first (see `dest_id` cols for code meaning")
    run2_fate_id = Column(SmallInteger, doc="Ultimate fate of runner on second (see `dest_id` cols for code meaning")
    run3_fate_id = Column(SmallInteger, doc="Ultimate fate of runner on third (see `dest_id` cols for code meaning")
    fate_runs_ct = Column(SmallInteger, doc="Additional runs scored in half inning after this event")
    ass6_fld_cd = Column(SmallInteger, doc="Position code of fielder with sixth assist")
    ass7_fld_cd = Column(SmallInteger, doc="Position code of fielder with seventh assist")
    ass8_fld_cd = Column(SmallInteger, doc="Position code of fielder with eighth assist")
    ass9_fld_cd = Column(SmallInteger, doc="Position code of fielder with ninth assist")
    ass10_fld_cd = Column(SmallInteger, doc="Position code of fielder with tenth assist")
    unknown_out_exc_fl = Column(Boolean, doc="Unknown fielding credit flag")
    uncertain_play_exc_fl = Column(Boolean, doc="Uncertain play flag")


class Game(Base):
    __tablename__ = 'game'

    game_id = Column(CHAR(12), primary_key=True)
    game_dt = Column(Date)
    game_ct = Column(SmallInteger)
    game_dy = Column(String(9))
    start_game_tm = Column(SmallInteger)
    dh_fl = Column(String(1))
    daynight_park_cd = Column(String(1))
    away_team_id = Column(CHAR(3))
    home_team_id = Column(CHAR(3))
    park_id = Column(String(5))
    away_start_pit_id = Column(CHAR(8))
    home_start_pit_id = Column(CHAR(8))
    # 9 rather than 8 to protect against "(unknown)"
    base4_ump_id = Column(String(9))
    base1_ump_id = Column(String(9))
    base2_ump_id = Column(String(9))
    base3_ump_id = Column(String(9))
    lf_ump_id = Column(CHAR(8))
    rf_ump_id = Column(CHAR(8))
    attend_park_ct = Column(Integer)
    scorer_record_id = Column(String(50))
    translator_record_id = Column(String(50))
    inputter_record_id = Column(String(50))
    input_record_ts = Column(String(20))
    edit_record_ts = Column(String(20))
    method_record_cd = Column(String(18))
    pitches_record_cd = Column(String(1))
    temp_park_ct = Column(SmallInteger)
    wind_direction_park_cd = Column(SmallInteger)
    wind_speed_park_ct = Column(SmallInteger)
    field_park_cd = Column(SmallInteger)
    precip_park_cd = Column(SmallInteger)
    sky_park_cd = Column(SmallInteger)
    minutes_game_ct = Column(SmallInteger)
    inn_ct = Column(SmallInteger)
    away_score_ct = Column(SmallInteger)
    home_score_ct = Column(SmallInteger)
    away_hits_ct = Column(SmallInteger)
    home_hits_ct = Column(SmallInteger)
    away_err_ct = Column(SmallInteger)
    home_err_ct = Column(SmallInteger)
    away_lob_ct = Column(SmallInteger)
    home_lob_ct = Column(SmallInteger)
    win_pit_id = Column(CHAR(8))
    lose_pit_id = Column(CHAR(8))
    save_pit_id = Column(CHAR(8))
    gwrbi_bat_id = Column(CHAR(8))
    away_lineup1_bat_id = Column(CHAR(8))
    away_lineup1_fld_cd = Column(SmallInteger)
    away_lineup2_bat_id = Column(CHAR(8))
    away_lineup2_fld_cd = Column(SmallInteger)
    away_lineup3_bat_id = Column(CHAR(8))
    away_lineup3_fld_cd = Column(SmallInteger)
    away_lineup4_bat_id = Column(CHAR(8))
    away_lineup4_fld_cd = Column(SmallInteger)
    away_lineup5_bat_id = Column(CHAR(8))
    away_lineup5_fld_cd = Column(SmallInteger)
    away_lineup6_bat_id = Column(CHAR(8))
    away_lineup6_fld_cd = Column(SmallInteger)
    away_lineup7_bat_id = Column(CHAR(8))
    away_lineup7_fld_cd = Column(SmallInteger)
    away_lineup8_bat_id = Column(CHAR(8))
    away_lineup8_fld_cd = Column(SmallInteger)
    away_lineup9_bat_id = Column(CHAR(8))
    away_lineup9_fld_cd = Column(SmallInteger)
    home_lineup1_bat_id = Column(CHAR(8))
    home_lineup1_fld_cd = Column(SmallInteger)
    home_lineup2_bat_id = Column(CHAR(8))
    home_lineup2_fld_cd = Column(SmallInteger)
    home_lineup3_bat_id = Column(CHAR(8))
    home_lineup3_fld_cd = Column(SmallInteger)
    home_lineup4_bat_id = Column(CHAR(8))
    home_lineup4_fld_cd = Column(SmallInteger)
    home_lineup5_bat_id = Column(CHAR(8))
    home_lineup5_fld_cd = Column(SmallInteger)
    home_lineup6_bat_id = Column(CHAR(8))
    home_lineup6_fld_cd = Column(SmallInteger)
    home_lineup7_bat_id = Column(CHAR(8))
    home_lineup7_fld_cd = Column(SmallInteger)
    home_lineup8_bat_id = Column(CHAR(8))
    home_lineup8_fld_cd = Column(SmallInteger)
    home_lineup9_bat_id = Column(CHAR(8))
    home_lineup9_fld_cd = Column(SmallInteger)
    away_finish_pit_id = Column(CHAR(8))
    home_finish_pit_id = Column(CHAR(8))
    away_team_league_id = Column(CHAR(1))
    home_team_league_id = Column(CHAR(1))
    away_team_game_ct = Column(SmallInteger)
    home_team_game_ct = Column(SmallInteger)
    outs_ct = Column(SmallInteger)
    completion_tx = Column(String(26))
    forfeit_tx = Column(String(26))
    protest_tx = Column(String(26))
    away_line_tx = Column(String(26))
    home_line_tx = Column(String(26))
    away_ab_ct = Column(SmallInteger)
    away_2b_ct = Column(SmallInteger)
    away_3b_ct = Column(SmallInteger)
    away_hr_ct = Column(SmallInteger)
    away_bi_ct = Column(SmallInteger)
    away_sh_ct = Column(SmallInteger)
    away_sf_ct = Column(SmallInteger)
    away_hp_ct = Column(SmallInteger)
    away_bb_ct = Column(SmallInteger)
    away_ibb_ct = Column(SmallInteger)
    away_so_ct = Column(SmallInteger)
    away_sb_ct = Column(SmallInteger)
    away_cs_ct = Column(SmallInteger)
    away_gdp_ct = Column(SmallInteger)
    away_xi_ct = Column(SmallInteger)
    away_pitcher_ct = Column(SmallInteger)
    away_er_ct = Column(SmallInteger)
    away_ter_ct = Column(SmallInteger)
    away_wp_ct = Column(SmallInteger)
    away_bk_ct = Column(SmallInteger)
    away_po_ct = Column(SmallInteger)
    away_a_ct = Column(SmallInteger)
    away_pb_ct = Column(SmallInteger)
    away_dp_ct = Column(SmallInteger)
    away_tp_ct = Column(SmallInteger)
    home_ab_ct = Column(SmallInteger)
    home_2b_ct = Column(SmallInteger)
    home_3b_ct = Column(SmallInteger)
    home_hr_ct = Column(SmallInteger)
    home_bi_ct = Column(SmallInteger)
    home_sh_ct = Column(SmallInteger)
    home_sf_ct = Column(SmallInteger)
    home_hp_ct = Column(SmallInteger)
    home_bb_ct = Column(SmallInteger)
    home_ibb_ct = Column(SmallInteger)
    home_so_ct = Column(SmallInteger)
    home_sb_ct = Column(SmallInteger)
    home_cs_ct = Column(SmallInteger)
    home_gdp_ct = Column(SmallInteger)
    home_xi_ct = Column(SmallInteger)
    home_pitcher_ct = Column(SmallInteger)
    home_er_ct = Column(SmallInteger)
    home_ter_ct = Column(SmallInteger)
    home_wp_ct = Column(SmallInteger)
    home_bk_ct = Column(SmallInteger)
    home_po_ct = Column(SmallInteger)
    home_a_ct = Column(SmallInteger)
    home_pb_ct = Column(SmallInteger)
    home_dp_ct = Column(SmallInteger)
    home_tp_ct = Column(SmallInteger)
    ump_home_name_tx = Column(String(26))
    ump_1b_name_tx = Column(String(26))
    ump_2b_name_tx = Column(String(26))
    ump_3b_name_tx = Column(String(26))
    ump_lf_name_tx = Column(String(26))
    ump_rf_name_tx = Column(String(26))
    away_manager_id = Column(CHAR(8))
    away_manager_name_tx = Column(String(26))
    home_manager_id = Column(CHAR(8))
    home_manager_name_tx = Column(String(26))
    win_pit_name_tx = Column(String(26))
    lose_pit_name_tx = Column(String(26))
    save_pit_name_tx = Column(String(26))
    goahead_rbi_id = Column(CHAR(8))
    goahead_rbi_name_tx = Column(String(26))
    away_lineup1_bat_name_tx = Column(String(26))
    away_lineup2_bat_name_tx = Column(String(26))
    away_lineup3_bat_name_tx = Column(String(26))
    away_lineup4_bat_name_tx = Column(String(26))
    away_lineup5_bat_name_tx = Column(String(26))
    away_lineup6_bat_name_tx = Column(String(26))
    away_lineup7_bat_name_tx = Column(String(26))
    away_lineup8_bat_name_tx = Column(String(26))
    away_lineup9_bat_name_tx = Column(String(26))
    home_lineup1_bat_name_tx = Column(String(26))
    home_lineup2_bat_name_tx = Column(String(26))
    home_lineup3_bat_name_tx = Column(String(26))
    home_lineup4_bat_name_tx = Column(String(26))
    home_lineup5_bat_name_tx = Column(String(26))
    home_lineup6_bat_name_tx = Column(String(26))
    home_lineup7_bat_name_tx = Column(String(26))
    home_lineup8_bat_name_tx = Column(String(26))
    home_lineup9_bat_name_tx = Column(String(26))
    add_info_tx = Column(String(26))
    acq_info_tx = Column(String(26))


class Daily(Base):
    __tablename__ = "daily"

    game_id = Column(CHAR(12))
    game_dt = Column(Date)
    game_ct = Column(SmallInteger)
    appearance_dt = Column(Date)
    team_id = Column(CHAR(3))
    player_id = Column(CHAR(8))
    slot_ct = Column(SmallInteger)
    seq_ct = Column(SmallInteger)
    home_fl = Column(Boolean)
    opponent_id = Column(CHAR(3))
    park_id = Column(CHAR(5))
    b_g = Column(SmallInteger)
    b_pa = Column(SmallInteger)
    b_ab = Column(SmallInteger)
    b_r = Column(SmallInteger)
    b_h = Column(SmallInteger)
    b_tb = Column(SmallInteger)
    b_2b = Column(SmallInteger)
    b_3b = Column(SmallInteger)
    b_hr = Column(SmallInteger)
    b_hr4 = Column(SmallInteger)
    b_rbi = Column(SmallInteger)
    b_gw = Column(SmallInteger)
    b_bb = Column(SmallInteger)
    b_ibb = Column(SmallInteger)
    b_so = Column(SmallInteger)
    b_gdp = Column(SmallInteger)
    b_hp = Column(SmallInteger)
    b_sh = Column(SmallInteger)
    b_sf = Column(SmallInteger)
    b_sb = Column(SmallInteger)
    b_cs = Column(SmallInteger)
    b_xi = Column(SmallInteger)
    b_g_dh = Column(SmallInteger)
    b_g_ph = Column(SmallInteger)
    b_g_pr = Column(SmallInteger)
    p_g = Column(SmallInteger)
    p_gs = Column(SmallInteger)
    p_cg = Column(SmallInteger)
    p_sho = Column(SmallInteger)
    p_gf = Column(SmallInteger)
    p_w = Column(SmallInteger)
    p_l = Column(SmallInteger)
    p_sv = Column(SmallInteger)
    p_out = Column(SmallInteger)
    p_tbf = Column(SmallInteger)
    p_ab = Column(SmallInteger)
    p_r = Column(SmallInteger)
    p_er = Column(SmallInteger)
    p_h = Column(SmallInteger)
    p_tb = Column(SmallInteger)
    p_2b = Column(SmallInteger)
    p_3b = Column(SmallInteger)
    p_hr = Column(SmallInteger)
    p_hr4 = Column(SmallInteger)
    p_bb = Column(SmallInteger)
    p_ibb = Column(SmallInteger)
    p_so = Column(SmallInteger)
    p_gdp = Column(SmallInteger)
    p_hp = Column(SmallInteger)
    p_sh = Column(SmallInteger)
    p_sf = Column(SmallInteger)
    p_xi = Column(SmallInteger)
    p_wp = Column(SmallInteger)
    p_bk = Column(SmallInteger)
    p_ir = Column(SmallInteger)
    p_irs = Column(SmallInteger)
    p_go = Column(SmallInteger)
    p_ao = Column(SmallInteger)
    p_pitch = Column(SmallInteger)
    p_strike = Column(SmallInteger)
    f_p_g = Column(SmallInteger)
    f_p_gs = Column(SmallInteger)
    f_p_out = Column(SmallInteger)
    f_p_tc = Column(SmallInteger)
    f_p_po = Column(SmallInteger)
    f_p_a = Column(SmallInteger)
    f_p_e = Column(SmallInteger)
    f_p_dp = Column(SmallInteger)
    f_p_tp = Column(SmallInteger)
    f_c_g = Column(SmallInteger)
    f_c_gs = Column(SmallInteger)
    f_c_out = Column(SmallInteger)
    f_c_tc = Column(SmallInteger)
    f_c_po = Column(SmallInteger)
    f_c_a = Column(SmallInteger)
    f_c_e = Column(SmallInteger)
    f_c_dp = Column(SmallInteger)
    f_c_tp = Column(SmallInteger)
    f_c_pb = Column(SmallInteger)
    f_c_xi = Column(SmallInteger)
    f_1b_g = Column(SmallInteger)
    f_1b_gs = Column(SmallInteger)
    f_1b_out = Column(SmallInteger)
    f_1b_tc = Column(SmallInteger)
    f_1b_po = Column(SmallInteger)
    f_1b_a = Column(SmallInteger)
    f_1b_e = Column(SmallInteger)
    f_1b_dp = Column(SmallInteger)
    f_1b_tp = Column(SmallInteger)
    f_2b_g = Column(SmallInteger)
    f_2b_gs = Column(SmallInteger)
    f_2b_out = Column(SmallInteger)
    f_2b_tc = Column(SmallInteger)
    f_2b_po = Column(SmallInteger)
    f_2b_a = Column(SmallInteger)
    f_2b_e = Column(SmallInteger)
    f_2b_dp = Column(SmallInteger)
    f_2b_tp = Column(SmallInteger)
    f_3b_g = Column(SmallInteger)
    f_3b_gs = Column(SmallInteger)
    f_3b_out = Column(SmallInteger)
    f_3b_tc = Column(SmallInteger)
    f_3b_po = Column(SmallInteger)
    f_3b_a = Column(SmallInteger)
    f_3b_e = Column(SmallInteger)
    f_3b_dp = Column(SmallInteger)
    f_3b_tp = Column(SmallInteger)
    f_ss_g = Column(SmallInteger)
    f_ss_gs = Column(SmallInteger)
    f_ss_out = Column(SmallInteger)
    f_ss_tc = Column(SmallInteger)
    f_ss_po = Column(SmallInteger)
    f_ss_a = Column(SmallInteger)
    f_ss_e = Column(SmallInteger)
    f_ss_dp = Column(SmallInteger)
    f_ss_tp = Column(SmallInteger)
    f_lf_g = Column(SmallInteger)
    f_lf_gs = Column(SmallInteger)
    f_lf_out = Column(SmallInteger)
    f_lf_tc = Column(SmallInteger)
    f_lf_po = Column(SmallInteger)
    f_lf_a = Column(SmallInteger)
    f_lf_e = Column(SmallInteger)
    f_lf_dp = Column(SmallInteger)
    f_lf_tp = Column(SmallInteger)
    f_cf_g = Column(SmallInteger)
    f_cf_gs = Column(SmallInteger)
    f_cf_out = Column(SmallInteger)
    f_cf_tc = Column(SmallInteger)
    f_cf_po = Column(SmallInteger)
    f_cf_a = Column(SmallInteger)
    f_cf_e = Column(SmallInteger)
    f_cf_dp = Column(SmallInteger)
    f_cf_tp = Column(SmallInteger)
    f_rf_g = Column(SmallInteger)
    f_rf_gs = Column(SmallInteger)
    f_rf_out = Column(SmallInteger)
    f_rf_tc = Column(SmallInteger)
    f_rf_po = Column(SmallInteger)
    f_rf_a = Column(SmallInteger)
    f_rf_e = Column(SmallInteger)
    f_rf_dp = Column(SmallInteger)
    f_rf_tp = Column(SmallInteger)
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class Sub(Base):
    __tablename__ = 'sub'

    game_id = Column(CHAR(12))
    inn_ct = Column(SmallInteger)
    bat_home_id = Column(SmallInteger)
    sub_id = Column(CHAR(8))
    sub_home_id = Column(SmallInteger)
    sub_lineup_id = Column(SmallInteger)
    sub_fld_cd = Column(SmallInteger)
    removed_id = Column(CHAR(8))
    removed_fld_cd = Column(SmallInteger)
    event_id = Column(SmallInteger)
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class Comment(Base):
    __tablename__ = 'comment'

    game_id = Column(CHAR(12))
    event_id = Column(SmallInteger)
    comment = Column(String(1638))
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)



class Gamelog(Base):
    __tablename__ = "gamelog"
    # No explicit column names are provided by Retrosheet.
    # Alternative source used for header names: https://github.com/maxtoki/baseball_R
    # Did some exploratory analysis to find data types

    date = Column(Date, primary_key=True)
    double_header = Column(Integer, primary_key=True)
    day_of_week = Column(CHAR(3))
    visiting_team = Column(CHAR(3), primary_key=True)
    visiting_team_league = Column(CHAR(2))
    visiting_team_game_number = Column(SmallInteger)
    home_team = Column(CHAR(3), primary_key=True)
    home_team_league = Column(CHAR(2))
    home_team_game_number = Column(SmallInteger)
    visitor_runs_scored = Column(SmallInteger)
    home_runs_score = Column(SmallInteger)
    length_in_outs = Column(SmallInteger)
    day_night = Column(CHAR(1))
    completion_info = Column(String(23))
    forfeit_info = Column(String(3))
    protest_info = Column(String(3))
    park_id = Column(CHAR(5))
    attendance = Column(Integer)
    duration = Column(SmallInteger)
    vistor_line_score = Column(String(26))
    home_line_score = Column(String(26))
    visitor_ab = Column(SmallInteger)
    visitor_h = Column(SmallInteger)
    visitor_d = Column(SmallInteger)
    visitor_t = Column(SmallInteger)
    visitor_hr = Column(SmallInteger)
    visitor_rbi = Column(SmallInteger)
    visitor_sh = Column(SmallInteger)
    visitor_sf = Column(SmallInteger)
    visitor_hbp = Column(SmallInteger)
    visitor_bb = Column(SmallInteger)
    visitor_ibb = Column(SmallInteger)
    visitor_k = Column(SmallInteger)
    visitor_sb = Column(SmallInteger)
    visitor_cs = Column(SmallInteger)
    visitor_gdp = Column(SmallInteger)
    visitor_ci = Column(SmallInteger)
    visitor_lob = Column(SmallInteger)
    visitor_pitchers = Column(SmallInteger)
    visitor_er = Column(SmallInteger)
    visitor_ter = Column(SmallInteger)
    visitor_wp = Column(SmallInteger)
    visitor_balks = Column(SmallInteger)
    visitor_po = Column(SmallInteger)
    visitor_a = Column(SmallInteger)
    visitor_e = Column(SmallInteger)
    visitor_passed = Column(SmallInteger)
    visitor_db = Column(SmallInteger)
    visitor_tp = Column(SmallInteger)
    home_ab = Column(SmallInteger)
    home_h = Column(SmallInteger)
    home_d = Column(SmallInteger)
    home_t = Column(SmallInteger)
    home_hr = Column(SmallInteger)
    home_rbi = Column(SmallInteger)
    home_sh = Column(SmallInteger)
    home_sf = Column(SmallInteger)
    home_hbp = Column(SmallInteger)
    home_bb = Column(SmallInteger)
    home_ibb = Column(SmallInteger)
    home_k = Column(SmallInteger)
    home_sb = Column(SmallInteger)
    home_cs = Column(SmallInteger)
    home_gdp = Column(SmallInteger)
    home_ci = Column(SmallInteger)
    home_lob = Column(SmallInteger)
    home_pitchers = Column(SmallInteger)
    home_er = Column(SmallInteger)
    home_ter = Column(SmallInteger)
    home_wp = Column(SmallInteger)
    home_balks = Column(SmallInteger)
    home_po = Column(SmallInteger)
    home_a = Column(SmallInteger)
    home_e = Column(SmallInteger)
    home_passed = Column(SmallInteger)
    home_db = Column(SmallInteger)
    home_tp = Column(SmallInteger)
    umpire_h_id = Column(CHAR(8))
    umpire_h_name = Column(String(32))
    umpire_1b_id = Column(CHAR(8))
    umpire_1b_name = Column(String(32))
    umpire_2b_id = Column(CHAR(8))
    umpire_2b_name = Column(String(32))
    umpire_3b_id = Column(CHAR(8))
    umpire_3b_name = Column(String(32))
    umpire_lf_id = Column(CHAR(8))
    umpire_lf_name = Column(String(32))
    umpire_rf_id = Column(CHAR(8))
    umpire_rf_name = Column(String(32))
    visitor_manager_id = Column(CHAR(8))
    visitor_manager_name = Column(String(32))
    home_manager_id = Column(CHAR(8))
    home_manager_name = Column(String(32))
    winning_pitcher_id = Column(CHAR(8))
    winning_pitcher_name = Column(String(32))
    losing_pitcher_id = Column(CHAR(8))
    losing_pitcher_name = Column(String(32))
    saving_pitcher_id = Column(CHAR(8))
    saving_pitcher_name = Column(String(32))
    game_winning_rbi_id = Column(CHAR(8))
    game_winning_rbi_name = Column(String(32))
    visitor_starting_pitcher_id = Column(CHAR(8))
    visitor_starting_pitcher_name = Column(String(32))
    home_starting_pitcher_id = Column(CHAR(8))
    home_starting_pitcher_name = Column(String(32))
    visitor_batting_1_player_id = Column(CHAR(8))
    visitor_batting_1_name = Column(String(32))
    visitor_batting_1_position = Column(SmallInteger)
    visitor_batting_2_player_id = Column(CHAR(8))
    visitor_batting_2_name = Column(String(32))
    visitor_batting_2_position = Column(SmallInteger)
    visitor_batting_3_player_id = Column(CHAR(8))
    visitor_batting_3_name = Column(String(32))
    visitor_batting_3_position = Column(SmallInteger)
    visitor_batting_4_player_id = Column(CHAR(8))
    visitor_batting_4_name = Column(String(32))
    visitor_batting_4_position = Column(SmallInteger)
    visitor_batting_5_player_id = Column(CHAR(8))
    visitor_batting_5_name = Column(String(32))
    visitor_batting_5_position = Column(SmallInteger)
    visitor_batting_6_player_id = Column(CHAR(8))
    visitor_batting_6_name = Column(String(32))
    visitor_batting_6_position = Column(SmallInteger)
    visitor_batting_7_player_id = Column(CHAR(8))
    visitor_batting_7_name = Column(String(32))
    visitor_batting_7_position = Column(SmallInteger)
    visitor_batting_8_player_id = Column(CHAR(8))
    visitor_batting_8_name = Column(String(32))
    visitor_batting_8_position = Column(SmallInteger)
    visitor_batting_9_player_id = Column(CHAR(8))
    visitor_batting_9_name = Column(String(32))
    visitor_batting_9_position = Column(SmallInteger)
    home_batting_1_player_id = Column(CHAR(8))
    home_batting_1_name = Column(String(32))
    home_batting_1_position = Column(SmallInteger)
    home_batting_2_player_id = Column(CHAR(8))
    home_batting_2_name = Column(String(32))
    home_batting_2_position = Column(SmallInteger)
    home_batting_3_player_id = Column(CHAR(8))
    home_batting_3_name = Column(String(32))
    home_batting_3_position = Column(SmallInteger)
    home_batting_4_player_id = Column(CHAR(8))
    home_batting_4_name = Column(String(32))
    home_batting_4_position = Column(SmallInteger)
    home_batting_5_player_id = Column(CHAR(8))
    home_batting_5_name = Column(String(32))
    home_batting_5_position = Column(SmallInteger)
    home_batting_6_player_id = Column(CHAR(8))
    home_batting_6_name = Column(String(32))
    home_batting_6_position = Column(SmallInteger)
    home_batting_7_player_id = Column(CHAR(8))
    home_batting_7_name = Column(String(32))
    home_batting_7_position = Column(SmallInteger)
    home_batting_8_player_id = Column(CHAR(8))
    home_batting_8_name = Column(String(32))
    home_batting_8_position = Column(SmallInteger)
    home_batting_9_player_id = Column(CHAR(8))
    home_batting_9_name = Column(String(32))
    home_batting_9_position = Column(SmallInteger)
    additional_info = Column(String(128))
    acquisition_info = Column(CHAR(1))


class Park(Base):
    __tablename__ = 'park'

    park_id = Column(CHAR(5), primary_key=True)
    name = Column(String(41))
    aka = Column(String(40))
    city = Column(String(17))
    state = Column(String(9))
    start_date = Column(Date)
    end_date = Column(Date)
    league = Column(CHAR(2))
    notes = Column(String(54))


class Roster(Base):
    __tablename__ = 'roster'
    # We inserted the year in preprocessing
    year = Column(Integer, primary_key=True)
    player_id = Column(CHAR(8), primary_key=True)
    last_name = Column(String(32))
    first_name = Column(String(32))
    bats = Column(CHAR(1))
    throws = Column(CHAR(1))
    team_id = Column(CHAR(3), primary_key=True)
    position = Column(String(2))


class Schedule(Base):
    __tablename__ = 'schedule'

    date = Column(Date, primary_key=True)
    double_header = Column(SmallInteger)
    day_of_week = Column(CHAR(3))
    visiting_team = Column(CHAR(3))
    visiting_team_league = Column(CHAR(2))
    visiting_team_game_number = Column(SmallInteger)
    home_team = Column(CHAR(3), primary_key=True)
    home_team_league = Column(CHAR(2))
    home_team_game_number = Column(Integer, primary_key=True)
    day_night = Column(CHAR(1))
    postponement_indicator = Column(String(30))
    makeup_dates = Column(String(20))


class CodeEvent(Base):
    __tablename__ = 'code_event'

    code = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


class CodeFieldPark(Base):
    __tablename__ = 'code_field_park'

    code = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


class CodeMethodRecord(Base):
    __tablename__ = 'code_method_record'

    code = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


class CodePitchesRecord(Base):
    __tablename__ = 'code_pitches_record'

    code = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


class CodePrecipPark(Base):
    __tablename__ = 'code_precip_park'

    code = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


class CodeSkyPark(Base):
    __tablename__ = 'code_sky_park'

    event_cd = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


class CodeWindDirectionPark(Base):
    __tablename__ = 'code_wind_direction_park'

    event_cd = Column(SmallInteger, primary_key=True)
    description = Column(String(30))


