from sqlalchemy import MetaData, Boolean, CHAR, Column, Date, Integer, SmallInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData(schema="retrosheet"))
metadata: MetaData = Base.metadata


class Sub(Base):
    """
    A complement to `event` that provides convenient information about substitutions.
    """
    __tablename__ = 'sub'

    game_id = Column(CHAR(12), doc="Game ID (home team ID + YYYYMMDD + doubleheader flag")
    inn_ct = Column(SmallInteger, doc="Inning of substitution")
    # TODO: Handle -1 so this can be a boolean
    bat_home_id = Column(SmallInteger, doc="Is home team batting (-1 for N/A)")
    sub_id = Column(CHAR(8), doc="Player ID of substitute")
    sub_home_id = Column(Boolean, doc="Is the home team making the substitution")
    sub_lineup_id = Column(SmallInteger, doc="Lineup position of substitution")
    sub_fld_cd = Column(SmallInteger, doc="Fielding position of substitution")
    removed_id = Column(CHAR(8), doc="ID of removed player")
    removed_fld_cd = Column(SmallInteger, doc="Fielding position of removed player")
    event_id = Column(SmallInteger, doc="Event number in which substitution occurred")
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class Comment(Base):
    """
    A complement to `event` that sources detailed text comments from play-by-play files. When present,
    these comments can be helpful in figuring out what happened on unusual plays.
    """
    __tablename__ = 'comment'

    game_id = Column(CHAR(12), doc="Game ID (home team ID + YYYYMMDD + doubleheader flag")
    event_id = Column(SmallInteger, doc="Commented event number")
    comment = Column(String(1638), doc="Comment text")
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class Park(Base):
    """
    Basic information about ballparks.
    """
    __tablename__ = 'park'

    park_id = Column(CHAR(5), primary_key=True, doc="Park ID")
    name = Column(String(41), doc="Park name")
    aka = Column(String(55), doc="Common park alias")
    city = Column(String(17), doc="City")
    state = Column(String(9), doc="State")
    # TODO: Handle this MySQL edge case so these can be dates again
    start_date = Column(String(10), doc="First game")
    end_date = Column(String(10), doc="Last game")
    league = Column(CHAR(2), doc="League ID")
    notes = Column(String(54), doc="Misc. notes")


class Roster(Base):
    """
    Contains one row for each unique combination of player, team, and year. For more detailed/convenient player
    biographical data, use the `people` table from the Baseball Databank schema, joining on `retro_id`.
    """
    __tablename__ = 'roster'
    # We inserted the year in preprocessing
    year = Column(Integer, primary_key=True, doc="Year of roster")
    player_id = Column(CHAR(8), primary_key=True, doc="Player ID")
    last_name = Column(String(32), doc="Player last name")
    first_name = Column(String(32), doc="Player first name")
    bats = Column(CHAR(1), doc="Bat handedness")
    throws = Column(CHAR(1), doc="Throw handedness")
    team_id = Column(CHAR(3), primary_key=True, doc="Team ID")
    position = Column(String(2), doc="Primary fielding position")


class Schedule(Base):
    """
    Contains the original regular season schedules for all seasons dating back to 1877.
    """
    __tablename__ = 'schedule'

    date = Column(Date, primary_key=True, doc="Scheduled game date")
    double_header = Column(SmallInteger, doc="Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, "
                                             "2 - second game of doubleheader")
    day_of_week = Column(CHAR(3), doc="Day of week (3 letter abbreviation")
    visiting_team = Column(CHAR(3), doc="Away team ID")
    visiting_team_league = Column(CHAR(2), doc="Away team league ID")
    visiting_team_game_number = Column(SmallInteger, doc="Away team game number")
    home_team = Column(CHAR(3), primary_key=True, doc="Home team ID")
    home_team_league = Column(CHAR(2), doc="Home team league ID")
    home_team_game_number = Column(Integer, primary_key=True, doc="Home team game number")
    day_night = Column(CHAR(1), doc="D - day, N - night")
    postponement_indicator = Column(String(120), doc="""
        This field will contain one or more phrases related to the game if it was
        not played as scheduled. If there is more than one phrase, they are separated
        by a semi-colon (";"). There are three possible outcomes for games not played
        on the originally scheduled date:
        -- The game was played on another date
        -- The game was played on the original date but at another site
        -- The game was not played
        """)
    makeup_dates = Column(String(120), doc="""
        This field will contain a makeup date if the postponed game was played at
        another time or place. If an attempt was known to have been made on a date but
        postponed again, that date will be listed. In that case, there will be a second
        date for the date when the game was actually played, in this form: "20150428;
        20150528" For the note about a team folding, the team code is one of the
        standard Retrosheet team IDs. The same is true for the team played as note.
        Often, the two of these are combined in one field.
        """)


class CodeEvent(Base):
    """
    Descriptions for codes in `event.event_cd`
    """
    __tablename__ = 'code_event'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class CodeFieldPark(Base):
    """
    Descriptions for codes in `game.field_park_cd`
    """
    __tablename__ = 'code_field_park'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class CodeMethodRecord(Base):
    """
    Descriptions for codes in `game.method_record_cd`
    """
    __tablename__ = 'code_method_record'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class CodePitchesRecord(Base):
    """
    Descriptions for codes in `game.pitches_record_cd`
    """
    __tablename__ = 'code_pitches_record'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class CodePrecipPark(Base):
    """
    Descriptions for codes in `game.precip_park_cd`
    """
    __tablename__ = 'code_precip_park'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class CodeSkyPark(Base):
    """
    Descriptions for codes in `game.sky_park_cd`
    """
    __tablename__ = 'code_sky_park'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class CodeWindDirectionPark(Base):
    """
    Descriptions for codes in `game.wind_direction_park_cd`
    """
    __tablename__ = 'code_wind_direction_park'

    code = Column(SmallInteger, primary_key=True, autoincrement=False)
    description = Column(String(30))


class DeducedGame(Base):
    """
    One-column table that contains a list of all game IDs for which the PBP account was
    deduced from newspaper accounts of the game. The table can be used to filter out those games
    from the event file if desired, or to create a flag variable when performing analysis.
    """
    __tablename__ = 'deduced_game'

    game_id = Column(CHAR(12), primary_key=True, doc="Game ID (home team ID + YYYYMMDD + doubleheader flag")


class Game(Base):
    """
    Contains one row for every unique game in the `event` table, and provides useful summary and metadata information
    about those games.

    Note that this table will suffer from the same data quality/completeness issues as `event`. This table only
    includes games for which play-by-play accounts exist, which means that some games from 1921-1936 and all games
    prior to 1921 will be missing from this table. The `gamelog` table provides one row for each game in major league
    history, making it a better choice for complete historical analyses.
    """
    __tablename__ = 'game'

    game_id = Column(CHAR(12), primary_key=True, doc="Game ID (home team ID + YYYYMMDD + doubleheader flag")
    game_dt = Column(Date, doc="Game date")
    game_ct = Column(SmallInteger, doc="Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, "
                                       "2 - second game of doubleheader")
    game_dy = Column(String(9), doc="Day of week")
    start_game_tm = Column(SmallInteger, doc="Game start time (12HMM coded as integer, eg 1015 for 10:15 PM)")
    dh_fl = Column(String(1), doc="DH used")
    daynight_park_cd = Column(String(1), doc="D - day game, N - night game")
    away_team_id = Column(CHAR(3), doc="Away team ID")
    home_team_id = Column(CHAR(3), doc="Home team ID")
    park_id = Column(String(5), doc="Park ID")
    away_start_pit_id = Column(CHAR(8), doc="Away team starting pitcher ID")
    home_start_pit_id = Column(CHAR(8), doc="Home team starting pitcher ID")
    # 9 rather than 8 to protect against "(unknown)"
    base4_ump_id = Column(String(9), doc="Home plate umpire ID")
    base1_ump_id = Column(String(9), doc="First base umpire ID")
    base2_ump_id = Column(String(9), doc="Second base umpire ID")
    base3_ump_id = Column(String(9), doc="Third base umpire ID")
    lf_ump_id = Column(CHAR(8), doc="Left field umpire ID")
    rf_ump_id = Column(CHAR(8), doc="Right field umpire ID")
    attend_park_ct = Column(Integer, doc="Attendance")
    scorer_record_id = Column(String(50), doc="Scorekeeper")
    translator_record_id = Column(String(50), doc="Translator")
    inputter_record_id = Column(String(50), doc="Inputter")
    # TODO: Figure out how to parse in parquet
    input_record_ts = Column(String(20), doc="Date and time of record input")
    edit_record_ts = Column(String(20), doc="Date and time of Most recent record edit")
    method_record_cd = Column(String(1), doc="How the game was scored (join `code_method_record` for details")
    pitches_record_cd = Column(String(1), doc="Highest detail of pitches recorded "
                                              "(join `code_pitches_record` for details). Note that many games with "
                                              "pitch detail do not have that info for all events, so pitch totals "
                                              "may not be accurate.")
    temp_park_ct = Column(SmallInteger, doc="Park temperature in degrees F (0 if unknown)")
    wind_direction_park_cd = Column(SmallInteger, doc="Wind direction park code (join `code_wind_direction_park` "
                                                      "for details)")
    wind_speed_park_ct = Column(SmallInteger, doc="Wind speed in miles per hour (-1 if unknown)")
    field_park_cd = Column(SmallInteger, doc="Park field condition code (join `code_field_park` for details)")
    precip_park_cd = Column(SmallInteger, doc="Park precipitation code (join `code_precip_park` for details")
    sky_park_cd = Column(SmallInteger, doc="Park sky condition code (join `code_sky_park` for details")
    minutes_game_ct = Column(SmallInteger, doc="Length of game in minutes")
    inn_ct = Column(SmallInteger, doc="Length of game in innings")
    away_score_ct = Column(SmallInteger, doc="Away team final score")
    home_score_ct = Column(SmallInteger, doc="Home team final score")
    away_hits_ct = Column(SmallInteger, doc="Away team hits")
    home_hits_ct = Column(SmallInteger, doc="Home team hits")
    away_err_ct = Column(SmallInteger, doc="Away team errors")
    home_err_ct = Column(SmallInteger, doc="Home team errors")
    away_lob_ct = Column(SmallInteger, doc="Away team left on base")
    home_lob_ct = Column(SmallInteger, doc="Home team left on base")
    win_pit_id = Column(CHAR(8), doc="ID of winning pitcher")
    lose_pit_id = Column(CHAR(8), doc="ID of losing pitcher")
    save_pit_id = Column(CHAR(8), doc="ID of saving pitcher")
    gwrbi_bat_id = Column(CHAR(8), doc="ID of batter wit game-winning RBI")
    away_lineup1_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 1")
    away_lineup1_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 1")
    away_lineup2_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 2")
    away_lineup2_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 2")
    away_lineup3_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 3")
    away_lineup3_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 3")
    away_lineup4_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 4")
    away_lineup4_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 4")
    away_lineup5_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 5")
    away_lineup5_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 5")
    away_lineup6_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 6")
    away_lineup6_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 6")
    away_lineup7_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 7")
    away_lineup7_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 7")
    away_lineup8_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 8")
    away_lineup8_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 8")
    away_lineup9_bat_id = Column(CHAR(8), doc="ID of away team starting batter in lineup position 9")
    away_lineup9_fld_cd = Column(SmallInteger, doc="Fielding position code of away team starting batter "
                                                   "in lineup position 9")
    home_lineup1_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 1")
    home_lineup1_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 1")
    home_lineup2_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 2")
    home_lineup2_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 2")
    home_lineup3_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 3")
    home_lineup3_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 3")
    home_lineup4_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 4")
    home_lineup4_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 4")
    home_lineup5_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 5")
    home_lineup5_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 5")
    home_lineup6_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 6")
    home_lineup6_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 6")
    home_lineup7_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 7")
    home_lineup7_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 7")
    home_lineup8_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 8")
    home_lineup8_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 8")
    home_lineup9_bat_id = Column(CHAR(8), doc="ID of home team starting batter in lineup position 9")
    home_lineup9_fld_cd = Column(SmallInteger, doc="Fielding position code of home team starting batter "
                                                   "in lineup position 9"
                                                   "")
    away_finish_pit_id = Column(CHAR(8), doc="Away team finishing pitcher")
    home_finish_pit_id = Column(CHAR(8), doc="Home team finishing pitcher")
    away_team_league_id = Column(CHAR(1), doc="Away team league (1 char ID)")
    home_team_league_id = Column(CHAR(1), doc="Home team league (1 char ID)")
    away_team_game_ct = Column(SmallInteger, doc="Away team game number")
    home_team_game_ct = Column(SmallInteger, doc="Home team game number")
    outs_ct = Column(SmallInteger, doc="Length of game in outs")
    completion_tx = Column(String(26), doc="Information on completion of game")
    forfeit_tx = Column(String(26), doc="Information on forfeit of game")
    protest_tx = Column(String(26), doc="Information on protest of game")
    away_line_tx = Column(String(26), doc="Away team linescore")
    home_line_tx = Column(String(26), doc="Home team linescore")
    away_ab_ct = Column(SmallInteger, doc="Away team at bats")
    away_2b_ct = Column(SmallInteger, doc="Away team doubles")
    away_3b_ct = Column(SmallInteger, doc="Away team triples")
    away_hr_ct = Column(SmallInteger, doc="Away team home runs")
    away_bi_ct = Column(SmallInteger, doc="Away team runs batted in")
    away_sh_ct = Column(SmallInteger, doc="Away team sacrifice hits")
    away_sf_ct = Column(SmallInteger, doc="Away team sacrifice flies")
    away_hp_ct = Column(SmallInteger, doc="Away team hit by pitches")
    away_bb_ct = Column(SmallInteger, doc="Away team walks")
    away_ibb_ct = Column(SmallInteger, doc="Away team intentional walks")
    away_so_ct = Column(SmallInteger, doc="Away team strikeouts")
    away_sb_ct = Column(SmallInteger, doc="Away team stolen bases")
    away_cs_ct = Column(SmallInteger, doc="Away team caught stealing")
    away_gdp_ct = Column(SmallInteger, doc="Away team grounded into double plays")
    away_xi_ct = Column(SmallInteger, doc="Away team reached on interference")
    away_pitcher_ct = Column(SmallInteger, doc="Away team number of pitchers used")
    away_er_ct = Column(SmallInteger, doc="Away team individual earned runs")
    away_ter_ct = Column(SmallInteger, doc="Away team team earned runs")
    away_wp_ct = Column(SmallInteger, doc="Away team wild pitches")
    away_bk_ct = Column(SmallInteger, doc="Away team balks")
    away_po_ct = Column(SmallInteger, doc="Away team putouts")
    away_a_ct = Column(SmallInteger, doc="Away team assists")
    away_pb_ct = Column(SmallInteger, doc="Away team passed balls")
    away_dp_ct = Column(SmallInteger, doc="Away team double plays turned")
    away_tp_ct = Column(SmallInteger, doc="Away team triple plays turned")
    home_ab_ct = Column(SmallInteger, doc="Home team at bats")
    home_2b_ct = Column(SmallInteger, doc="Home team doubles")
    home_3b_ct = Column(SmallInteger, doc="Home team triples")
    home_hr_ct = Column(SmallInteger, doc="Home team home runs")
    home_bi_ct = Column(SmallInteger, doc="Home team runs batted in")
    home_sh_ct = Column(SmallInteger, doc="Home team sacrifice hits")
    home_sf_ct = Column(SmallInteger, doc="Home team sacrifice flies")
    home_hp_ct = Column(SmallInteger, doc="Home team hit by pitches")
    home_bb_ct = Column(SmallInteger, doc="Home team walks")
    home_ibb_ct = Column(SmallInteger, doc="Home team intentional walks")
    home_so_ct = Column(SmallInteger, doc="Home team strikeouts")
    home_sb_ct = Column(SmallInteger, doc="Home team stolen bases")
    home_cs_ct = Column(SmallInteger, doc="Home team caught stealing")
    home_gdp_ct = Column(SmallInteger, doc="Home team grounded into double plays")
    home_xi_ct = Column(SmallInteger, doc="Home team reached on interference")
    home_pitcher_ct = Column(SmallInteger, doc="Home team number of pitchers used")
    home_er_ct = Column(SmallInteger, doc="Home team individual earned runs")
    home_ter_ct = Column(SmallInteger, doc="Home team team earned runs")
    home_wp_ct = Column(SmallInteger, doc="Home team wild pitches")
    home_bk_ct = Column(SmallInteger, doc="Home team balks")
    home_po_ct = Column(SmallInteger, doc="Home team putouts")
    home_a_ct = Column(SmallInteger, doc="Home team assists")
    home_pb_ct = Column(SmallInteger, doc="Home team passed balls")
    home_dp_ct = Column(SmallInteger, doc="Home team double plays turned")
    home_tp_ct = Column(SmallInteger, doc="Home team triple plays turned")
    ump_home_name_tx = Column(String(26), doc="Home plate umpire name")
    ump_1b_name_tx = Column(String(26), doc="First base umpire name")
    ump_2b_name_tx = Column(String(26), doc="Second base umpire name")
    ump_3b_name_tx = Column(String(26), doc="Third base umpire name")
    ump_lf_name_tx = Column(String(26), doc="Left field umpire name")
    ump_rf_name_tx = Column(String(26), doc="Right field umpire name")
    away_manager_id = Column(CHAR(8), doc="Away manager ID")
    away_manager_name_tx = Column(String(26), doc="Away manager name")
    home_manager_id = Column(CHAR(8), doc="Home manager ID")
    home_manager_name_tx = Column(String(26), doc="Home manager name")
    win_pit_name_tx = Column(String(26), doc="Wining pitcher name")
    lose_pit_name_tx = Column(String(26), doc="Losing pitcher name")
    save_pit_name_tx = Column(String(26), doc="Saving pitcher name")
    goahead_rbi_id = Column(CHAR(8), doc="ID of batter with goahead RBI")
    goahead_rbi_name_tx = Column(String(26), doc="Name of batter with goahead RBI")
    away_lineup1_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 1")
    away_lineup2_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 2")
    away_lineup3_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 3")
    away_lineup4_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 4")
    away_lineup5_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 5")
    away_lineup6_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 6")
    away_lineup7_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 7")
    away_lineup8_bat_name_tx = Column(String(26), doc="Name of away team batter in lineup position 8")
    away_lineup9_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 9")
    home_lineup1_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 1")
    home_lineup2_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 2")
    home_lineup3_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 3")
    home_lineup4_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 4")
    home_lineup5_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 5")
    home_lineup6_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 6")
    home_lineup7_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 7")
    home_lineup8_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 8")
    home_lineup9_bat_name_tx = Column(String(26), doc="Name of home team batter in lineup position 9")
    add_info_tx = Column(String(26), doc="Additional information")
    acq_info_tx = Column(String(26), doc="Acquisition information")


class Gamelog(Base):
    """
    Contains one row for every game in major league history. While a bare minimum of result information exists
    for all rows, the data becomes significantly more sparse for years prior to box score event files (< 1906).
    """
    __tablename__ = "gamelog"
    # No explicit column names are provided by Retrosheet.
    # Alternative source used for header names: https://github.com/maxtoki/baseball_R
    # Did some exploratory analysis to find data types

    date = Column(Date, primary_key=True, doc="Game date")
    double_header = Column(CHAR(1), primary_key=True, doc="""
        Number of game:
         "0" -- a single game
         "1" -- the first game of a double (or triple) header
                including separate admission doubleheaders
         "2" -- the second game of a double (or triple) header
                including separate admission doubleheaders
         "3" -- the third game of a triple-header
         "A" -- the first game of a double-header involving 3 teams
         "B" -- the second game of a double-header involving 3 teams
         """)
    day_of_week = Column(CHAR(3), doc="Day of week (3 char abbreviation)")
    visiting_team = Column(CHAR(3), primary_key=True, doc="Visiting team ID")
    visiting_team_league = Column(CHAR(2), doc="Away team league ID")
    visiting_team_game_number = Column(SmallInteger, doc="Away team game number")
    home_team = Column(CHAR(3), primary_key=True, doc="Home team ID")
    home_team_league = Column(CHAR(2), doc="Home team league ID")
    home_team_game_number = Column(SmallInteger, doc="Home team game number")
    visitor_runs_scored = Column(SmallInteger, doc="Away team runs scored")
    home_runs_score = Column(SmallInteger, doc="Home team runs scored")
    length_in_outs = Column(SmallInteger, doc="Game length in outs")
    day_night = Column(CHAR(1), doc="D - day game, N - night game")
    completion_info = Column(String(23), doc="""
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
        """)
    forfeit_info = Column(String(3), doc="V - forfeited to away team, H - forfeited to home team, "
                                         "T - ruled a no-decision")
    protest_info = Column(String(3), doc="P - protested by unidentified team, V - disallowed protest by away team, "
                                         "H - disallowed protest by home team, X - upheld protest by away team, "
                                         "Y - upheld protest by home team")
    park_id = Column(CHAR(5), doc="Park ID")
    attendance = Column(Integer, doc="Attendance")
    duration = Column(SmallInteger, doc="Time of game in minutes")
    vistor_line_score = Column(String(26), doc="Away team line score, e.g. 010000(10)0x")
    home_line_score = Column(String(26), doc="Home team line score, e.g. 010000(10)0x")
    visitor_ab = Column(SmallInteger, doc="Away team at bats")
    visitor_h = Column(SmallInteger, doc="Away team hits")
    visitor_d = Column(SmallInteger, doc="Away team doubles")
    visitor_t = Column(SmallInteger, doc="Away team triples")
    visitor_hr = Column(SmallInteger, doc="Away team home runs")
    visitor_rbi = Column(SmallInteger, doc="Away team runs batted in")
    visitor_sh = Column(SmallInteger, doc="Away team sacrifice hits (may include sac flies before 1954)")
    visitor_sf = Column(SmallInteger, doc="Away team sacrifice flies (since 1954)")
    visitor_hbp = Column(SmallInteger, doc="Away team hit by pitches")
    visitor_bb = Column(SmallInteger, doc="Away team walks")
    visitor_ibb = Column(SmallInteger, doc="Away team intentional walks")
    visitor_k = Column(SmallInteger, doc="Away team strikeouts")
    visitor_sb = Column(SmallInteger, doc="Away team stolen bases")
    visitor_cs = Column(SmallInteger, doc="Away team caught stealing")
    visitor_gdp = Column(SmallInteger, doc="Away team grounded into double plays")
    visitor_ci = Column(SmallInteger, doc="Away team reached on interference")
    visitor_lob = Column(SmallInteger, doc="Away team left on base")
    visitor_pitchers = Column(SmallInteger, doc="Away team pitchers used")
    visitor_er = Column(SmallInteger, doc="Away team individual earned runs allowed")
    visitor_ter = Column(SmallInteger, doc="Away team team earned runs allowed")
    visitor_wp = Column(SmallInteger, doc="Away team wild pitches allowed")
    visitor_balks = Column(SmallInteger, doc="Away team balks allowed")
    visitor_po = Column(SmallInteger, doc="Away team putouts")
    visitor_a = Column(SmallInteger, doc="Away team assists")
    visitor_e = Column(SmallInteger, doc="Away team errors")
    visitor_passed = Column(SmallInteger, doc="Away team passed balls")
    visitor_db = Column(SmallInteger, doc="Away team double plays turned")
    visitor_tp = Column(SmallInteger, doc="Away team triple plays turned")
    home_ab = Column(SmallInteger, doc="Home team at bats")
    home_h = Column(SmallInteger, doc="Home team hits")
    home_d = Column(SmallInteger, doc="Home team doubles")
    home_t = Column(SmallInteger, doc="Home team triples")
    home_hr = Column(SmallInteger, doc="Home team home runs")
    home_rbi = Column(SmallInteger, doc="Home team runs batted in")
    home_sh = Column(SmallInteger, doc="Home team sacrifice hits (may include sac flies before 1954)")
    home_sf = Column(SmallInteger, doc="Home team sacrifice flies (since 1954)")
    home_hbp = Column(SmallInteger, doc="Home team hit by pitches")
    home_bb = Column(SmallInteger, doc="Home team walks")
    home_ibb = Column(SmallInteger, doc="Home team intentional walks")
    home_k = Column(SmallInteger, doc="Home team strikeouts")
    home_sb = Column(SmallInteger, doc="Home team stolen bases")
    home_cs = Column(SmallInteger, doc="Home team caught stealing")
    home_gdp = Column(SmallInteger, doc="Home team grounded into double plays")
    home_ci = Column(SmallInteger, doc="Home team reached on interference")
    home_lob = Column(SmallInteger, doc="Home team left on base")
    home_pitchers = Column(SmallInteger, doc="Home team pitchers used")
    home_er = Column(SmallInteger, doc="Home team individual earned runs allowed")
    home_ter = Column(SmallInteger, doc="Home team team earned runs allowed")
    home_wp = Column(SmallInteger, doc="Home team wild pitches allowed")
    home_balks = Column(SmallInteger, doc="Home team balks allowed")
    home_po = Column(SmallInteger, doc="Home team putouts")
    home_a = Column(SmallInteger, doc="Home team assists")
    home_e = Column(SmallInteger, doc="Home team errors")
    home_passed = Column(SmallInteger, doc="Home team passed balls")
    home_db = Column(SmallInteger, doc="Home team double plays turned")
    home_tp = Column(SmallInteger, doc="Home team triple plays turned")
    umpire_h_id = Column(CHAR(8), doc="Home plate umpire ID")
    umpire_h_name = Column(String(32), doc="Home plate umpire name")
    umpire_1b_id = Column(CHAR(8), doc="First base umpire ID")
    umpire_1b_name = Column(String(32), doc="First base umpire name")
    umpire_2b_id = Column(CHAR(8), doc="Second base umpire ID")
    umpire_2b_name = Column(String(32), doc="Second base umpire name")
    umpire_3b_id = Column(CHAR(8), doc="Third base umpire ID")
    umpire_3b_name = Column(String(32), doc="Third base umpire name")
    umpire_lf_id = Column(CHAR(8), doc="Left field umpire ID")
    umpire_lf_name = Column(String(32), doc="Left field umpire name")
    umpire_rf_id = Column(CHAR(8), doc="Right field umpire ID")
    umpire_rf_name = Column(String(32), doc="Right field umpire name")
    visitor_manager_id = Column(CHAR(8), doc="Away team manager ID")
    visitor_manager_name = Column(String(32), doc="Away team manager name")
    home_manager_id = Column(CHAR(8), doc="Home team manager ID")
    home_manager_name = Column(String(32), doc="Home team manager name")
    winning_pitcher_id = Column(CHAR(8), doc="Winning pitcher ID")
    winning_pitcher_name = Column(String(32), doc="Winning pitcher name")
    losing_pitcher_id = Column(CHAR(8), doc="Losing pitcher ID")
    losing_pitcher_name = Column(String(32), doc="Losing pitcher name")
    saving_pitcher_id = Column(CHAR(8), doc="Saving pitcher ID")
    saving_pitcher_name = Column(String(32), doc="Saving pitcher name")
    game_winning_rbi_id = Column(CHAR(8), doc="Game-winning RBI ID")
    game_winning_rbi_name = Column(String(32), doc="Game-winning RBI name")
    visitor_starting_pitcher_id = Column(CHAR(8), doc="Away team starting pitcher ID")
    visitor_starting_pitcher_name = Column(String(32), doc="Away team starting pitcher name")
    home_starting_pitcher_id = Column(CHAR(8), doc="Home team starting pitcher ID")
    home_starting_pitcher_name = Column(String(32), doc="Home team starting pitcher name")
    visitor_batting_1_player_id = Column(CHAR(8), doc="Away team lineup slot 1 starting player ID")
    visitor_batting_1_name = Column(String(32), doc="Away team lineup slot 1 starting player name")
    visitor_batting_1_position = Column(SmallInteger, doc="Away team lineup slot 1 starting player fielding position")
    visitor_batting_2_player_id = Column(CHAR(8), doc="Away team lineup slot 2 starting player ID")
    visitor_batting_2_name = Column(String(32), doc="Away team lineup slot 2 starting player name")
    visitor_batting_2_position = Column(SmallInteger, doc="Away team lineup slot 2 starting player fielding position")
    visitor_batting_3_player_id = Column(CHAR(8), doc="Away team lineup slot 3 starting player ID")
    visitor_batting_3_name = Column(String(32), doc="Away team lineup slot 3 starting player name")
    visitor_batting_3_position = Column(SmallInteger, doc="Away team lineup slot 3 starting player fielding position")
    visitor_batting_4_player_id = Column(CHAR(8), doc="Away team lineup slot 4 starting player ID")
    visitor_batting_4_name = Column(String(32), doc="Away team lineup slot 4 starting player name")
    visitor_batting_4_position = Column(SmallInteger, doc="Away team lineup slot 4 starting player fielding position")
    visitor_batting_5_player_id = Column(CHAR(8), doc="Away team lineup slot 5 starting player ID")
    visitor_batting_5_name = Column(String(32), doc="Away team lineup slot 5 starting player name")
    visitor_batting_5_position = Column(SmallInteger, doc="Away team lineup slot 5 starting player fielding position")
    visitor_batting_6_player_id = Column(CHAR(8), doc="Away team lineup slot 6 starting player ID")
    visitor_batting_6_name = Column(String(32), doc="Away team lineup slot 6 starting player name")
    visitor_batting_6_position = Column(SmallInteger, doc="Away team lineup slot 6 starting player fielding position")
    visitor_batting_7_player_id = Column(CHAR(8), doc="Away team lineup slot 7 starting player ID")
    visitor_batting_7_name = Column(String(32), doc="Away team lineup slot 7 starting player name")
    visitor_batting_7_position = Column(SmallInteger, doc="Away team lineup slot 7 starting player fielding position")
    visitor_batting_8_player_id = Column(CHAR(8), doc="Away team lineup slot 8 starting player ID")
    visitor_batting_8_name = Column(String(32), doc="Away team lineup slot 8 starting player name")
    visitor_batting_8_position = Column(SmallInteger, doc="Away team lineup slot 8 starting player fielding position")
    visitor_batting_9_player_id = Column(CHAR(8), doc="Away team lineup slot 9 starting player ID")
    visitor_batting_9_name = Column(String(32), doc="Away team lineup slot 9 starting player name")
    visitor_batting_9_position = Column(SmallInteger, doc="Away team lineup slot 9 starting player fielding position")
    home_batting_1_player_id = Column(CHAR(8), doc="Home team lineup slot 1 starting player ID")
    home_batting_1_name = Column(String(32), doc="Home team lineup slot 1 starting player name")
    home_batting_1_position = Column(SmallInteger, doc="Home team lineup slot 1 starting player fielding position")
    home_batting_2_player_id = Column(CHAR(8), doc="Home team lineup slot 2 starting player ID")
    home_batting_2_name = Column(String(32), doc="Home team lineup slot 2 starting player name")
    home_batting_2_position = Column(SmallInteger, doc="Home team lineup slot 2 starting player fielding position")
    home_batting_3_player_id = Column(CHAR(8), doc="Home team lineup slot 3 starting player ID")
    home_batting_3_name = Column(String(32), doc="Home team lineup slot 3 starting player name")
    home_batting_3_position = Column(SmallInteger, doc="Home team lineup slot 3 starting player fielding position")
    home_batting_4_player_id = Column(CHAR(8), doc="Home team lineup slot 4 starting player ID")
    home_batting_4_name = Column(String(32), doc="Home team lineup slot 4 starting player name")
    home_batting_4_position = Column(SmallInteger, doc="Home team lineup slot 4 starting player fielding position")
    home_batting_5_player_id = Column(CHAR(8), doc="Home team lineup slot 5 starting player ID")
    home_batting_5_name = Column(String(32), doc="Home team lineup slot 5 starting player name")
    home_batting_5_position = Column(SmallInteger, doc="Home team lineup slot 5 starting player fielding position")
    home_batting_6_player_id = Column(CHAR(8), doc="Home team lineup slot 6 starting player ID")
    home_batting_6_name = Column(String(32), doc="Home team lineup slot 6 starting player name")
    home_batting_6_position = Column(SmallInteger, doc="Home team lineup slot 6 starting player fielding position")
    home_batting_7_player_id = Column(CHAR(8), doc="Home team lineup slot 7 starting player ID")
    home_batting_7_name = Column(String(32), doc="Home team lineup slot 7 starting player name")
    home_batting_7_position = Column(SmallInteger, doc="Home team lineup slot 7 starting player fielding position")
    home_batting_8_player_id = Column(CHAR(8), doc="Home team lineup slot 8 starting player ID")
    home_batting_8_name = Column(String(32), doc="Home team lineup slot 8 starting player name")
    home_batting_8_position = Column(SmallInteger, doc="Home team lineup slot 8 starting player fielding position")
    home_batting_9_player_id = Column(CHAR(8), doc="Home team lineup slot 9 starting player ID")
    home_batting_9_name = Column(String(32), doc="Home team lineup slot 9 starting player name")
    home_batting_9_position = Column(SmallInteger, doc="Home team lineup slot 9 starting player fielding position")
    additional_info = Column(String(128), doc="""
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
        """)
    acquisition_info = Column(CHAR(1), doc="Y - complete game information, N - no game information, "
                                           "D - game derived from box score and game story, "
                                           "P - portions of game information")


class Daily(Base):
    """
    Contains one row per player per game. In addition to providing more convenient summaries of player data than the
    `event` table, the `daily` table also includes information from box score event files, giving it complete coverage
    for all games dating back to 1906 (as well as the 1871 and 1872 seasons).

    If you are going to use this table regularly, it is highly recommended that you choose a column-oriented storage
    option like postgres_cstore_fdw or Clickhouse, as the large row size and row count will create bottlenecks for
    traditional row-oriented stores.

    The same caveats around data quality from `event` apply here as well. Additionally, there appear to be some minor
    referential integrity issues in a couple rows: in at least one case, a player truly appeared in a single game more
    than once (in the 1934 All-Star Game), while a parsing error caused this to appear in at least one other case.
    """
    __tablename__ = "daily"

    game_id = Column(CHAR(12), doc="Game ID (home team ID + YYYYMMDD + doubleheader flag")
    game_dt = Column(Date, doc="Game date")
    game_ct = Column(SmallInteger, doc="Doubleheader flag (0 - only game of day, 1 - first game of doubleheader, "
                                       "2 - second game of doubleheader")
    appearance_dt = Column(Date, doc="Player appearance date. Can be different from game date if the game was "
                                     "suspended and the player entered the game at the later date")
    team_id = Column(CHAR(3), doc="Team ID of player")
    player_id = Column(CHAR(8), doc="Player ID")
    slot_ct = Column(SmallInteger, doc="Player lineup position")
    seq_ct = Column(SmallInteger, doc="Player is nth person of game to play in that lineup slot")
    home_fl = Column(Boolean, doc="Player is playing at home")
    opponent_id = Column(CHAR(3), doc="Team opponent ID")
    park_id = Column(CHAR(5), doc="Park ID")
    b_g = Column(SmallInteger, doc="Games played")
    b_pa = Column(SmallInteger, doc="Plate appearances")
    b_ab = Column(SmallInteger, doc="At bats")
    b_r = Column(SmallInteger, doc="Runs scored")
    b_h = Column(SmallInteger, doc="Hits")
    b_tb = Column(SmallInteger, doc="Total bases")
    b_2b = Column(SmallInteger, doc="Doubles")
    b_3b = Column(SmallInteger, doc="Triples")
    b_hr = Column(SmallInteger, doc="Home runs")
    b_hr4 = Column(SmallInteger, doc="Grand slams")
    b_rbi = Column(SmallInteger, doc="Runs batted in")
    b_gw = Column(SmallInteger, doc="Game winning RBI")
    b_bb = Column(SmallInteger, doc="Walks")
    b_ibb = Column(SmallInteger, doc="Intentional walks")
    b_so = Column(SmallInteger, doc="Strikeouts")
    b_gdp = Column(SmallInteger, doc="Grounded into double plays")
    b_hp = Column(SmallInteger, doc="Hit by pitches")
    b_sh = Column(SmallInteger, doc="Sacrifice hits")
    b_sf = Column(SmallInteger, doc="Sacrifice files")
    b_sb = Column(SmallInteger, doc="Stolen bases")
    b_cs = Column(SmallInteger, doc="Caught stealing")
    b_xi = Column(SmallInteger, doc="Reached on interference")
    b_g_dh = Column(SmallInteger, doc="Games as DH")
    b_g_ph = Column(SmallInteger, doc="Games as pinch hitter")
    b_g_pr = Column(SmallInteger, doc="Games as pinch runner")
    p_g = Column(SmallInteger, doc="Games pitched")
    p_gs = Column(SmallInteger, doc="Games as starting pitcher")
    p_cg = Column(SmallInteger, doc="Complete games")
    p_sho = Column(SmallInteger, doc="Shutouts")
    p_gf = Column(SmallInteger, doc="Games finished")
    p_w = Column(SmallInteger, doc="Wins")
    p_l = Column(SmallInteger, doc="Losses")
    p_sv = Column(SmallInteger, doc="Saves")
    p_out = Column(SmallInteger, doc="Outs recorded")
    p_tbf = Column(SmallInteger, doc="Total batters faced")
    p_ab = Column(SmallInteger, doc="At bats against")
    p_r = Column(SmallInteger, doc="Runs allowed")
    p_er = Column(SmallInteger, doc="Earned runs allowed")
    p_h = Column(SmallInteger, doc="Hits allowed")
    p_tb = Column(SmallInteger, doc="Total bases allowed")
    p_2b = Column(SmallInteger, doc="Doubles allowed")
    p_3b = Column(SmallInteger, doc="Triples allowed")
    p_hr = Column(SmallInteger, doc="Home runs allowed")
    p_hr4 = Column(SmallInteger, doc="Grand slams allowed")
    p_bb = Column(SmallInteger, doc="Walks allowed")
    p_ibb = Column(SmallInteger, doc="Intentional walks allowed")
    p_so = Column(SmallInteger, doc="Strikeouts against")
    p_gdp = Column(SmallInteger, doc="Grounded into double plays against")
    p_hp = Column(SmallInteger, doc="Hit by pitches allowed")
    p_sh = Column(SmallInteger, doc="Sacrifice hits allowed")
    p_sf = Column(SmallInteger, doc="Sacrifice flies allowed")
    p_xi = Column(SmallInteger, doc="Reached on interference allowed")
    p_wp = Column(SmallInteger, doc="Wild pitches allowed")
    p_bk = Column(SmallInteger, doc="Balks allowed")
    p_ir = Column(SmallInteger, doc="Inherited runners")
    p_irs = Column(SmallInteger, doc="Inherited runners scored")
    p_go = Column(SmallInteger, doc="Groundouts recorded")
    p_ao = Column(SmallInteger, doc="Fly ball outs recorded")
    p_pitch = Column(SmallInteger, doc="Pitches thrown")
    p_strike = Column(SmallInteger, doc="Strikes thrown")
    f_p_g = Column(SmallInteger, doc="Appearances at pitcher")
    f_p_gs = Column(SmallInteger, doc="Starts at pitcher")
    f_p_out = Column(SmallInteger, doc="Outs played as pitcher")
    f_p_tc = Column(SmallInteger, doc="Total chances as pitcher")
    f_p_po = Column(SmallInteger, doc="Putouts as pitcher")
    f_p_a = Column(SmallInteger, doc="Assists as pitcher")
    f_p_e = Column(SmallInteger, doc="Errors as pitcher")
    f_p_dp = Column(SmallInteger, doc="Double plays turned as pitcher")
    f_p_tp = Column(SmallInteger, doc="Triple pays turned as pitcher")
    f_c_g = Column(SmallInteger, doc="Appearances at catcher")
    f_c_gs = Column(SmallInteger, doc="Starts at catcher")
    f_c_out = Column(SmallInteger, doc="Outs played as catcher")
    f_c_tc = Column(SmallInteger, doc="Total chances as catcher")
    f_c_po = Column(SmallInteger, doc="Putouts as catcher")
    f_c_a = Column(SmallInteger, doc="Assists as catcher")
    f_c_e = Column(SmallInteger, doc="Errors as catcher")
    f_c_dp = Column(SmallInteger, doc="Double plays turned as catcher")
    f_c_tp = Column(SmallInteger, doc="Triple pays turned as catcher")
    f_c_pb = Column(SmallInteger, doc="Passed balls")
    f_c_xi = Column(SmallInteger, doc="Catcher's interference")
    f_1b_g = Column(SmallInteger, doc="Appearances at first baseman")
    f_1b_gs = Column(SmallInteger, doc="Starts at first baseman")
    f_1b_out = Column(SmallInteger, doc="Outs played as first baseman")
    f_1b_tc = Column(SmallInteger, doc="Total chances as first baseman")
    f_1b_po = Column(SmallInteger, doc="Putouts as first baseman")
    f_1b_a = Column(SmallInteger, doc="Assists as first baseman")
    f_1b_e = Column(SmallInteger, doc="Errors as first baseman")
    f_1b_dp = Column(SmallInteger, doc="Double plays turned as first baseman")
    f_1b_tp = Column(SmallInteger, doc="Triple pays turned as first baseman")
    f_2b_g = Column(SmallInteger, doc="Appearances at second baseman")
    f_2b_gs = Column(SmallInteger, doc="Starts at second baseman")
    f_2b_out = Column(SmallInteger, doc="Outs played as second baseman")
    f_2b_tc = Column(SmallInteger, doc="Total chances as second baseman")
    f_2b_po = Column(SmallInteger, doc="Putouts as second baseman")
    f_2b_a = Column(SmallInteger, doc="Assists as second baseman")
    f_2b_e = Column(SmallInteger, doc="Errors as second baseman")
    f_2b_dp = Column(SmallInteger, doc="Double plays turned as second baseman")
    f_2b_tp = Column(SmallInteger, doc="Triple pays turned as second baseman")
    f_3b_g = Column(SmallInteger, doc="Appearances at third baseman")
    f_3b_gs = Column(SmallInteger, doc="Starts at third baseman")
    f_3b_out = Column(SmallInteger, doc="Outs played as third baseman")
    f_3b_tc = Column(SmallInteger, doc="Total chances as third baseman")
    f_3b_po = Column(SmallInteger, doc="Putouts as third baseman")
    f_3b_a = Column(SmallInteger, doc="Assists as third baseman")
    f_3b_e = Column(SmallInteger, doc="Errors as third baseman")
    f_3b_dp = Column(SmallInteger, doc="Double plays turned as third baseman")
    f_3b_tp = Column(SmallInteger, doc="Triple pays turned as third baseman")
    f_ss_g = Column(SmallInteger, doc="Appearances at shortstop")
    f_ss_gs = Column(SmallInteger, doc="Starts at shortstop")
    f_ss_out = Column(SmallInteger, doc="Outs played as shortstop")
    f_ss_tc = Column(SmallInteger, doc="Total chances as shortstop")
    f_ss_po = Column(SmallInteger, doc="Putouts as shortstop")
    f_ss_a = Column(SmallInteger, doc="Assists as shortstop")
    f_ss_e = Column(SmallInteger, doc="Errors as shortstop")
    f_ss_dp = Column(SmallInteger, doc="Double plays turned as shortstop")
    f_ss_tp = Column(SmallInteger, doc="Triple pays turned as shortstop")
    f_lf_g = Column(SmallInteger, doc="Appearances at left fielder")
    f_lf_gs = Column(SmallInteger, doc="Starts at left fielder")
    f_lf_out = Column(SmallInteger, doc="Outs played as left fielder")
    f_lf_tc = Column(SmallInteger, doc="Total chances as left fielder")
    f_lf_po = Column(SmallInteger, doc="Putouts as left fielder")
    f_lf_a = Column(SmallInteger, doc="Assists as left fielder")
    f_lf_e = Column(SmallInteger, doc="Errors as left fielder")
    f_lf_dp = Column(SmallInteger, doc="Double plays turned as left fielder")
    f_lf_tp = Column(SmallInteger, doc="Triple pays turned as left fielder")
    f_cf_g = Column(SmallInteger, doc="Appearances at center fielder")
    f_cf_gs = Column(SmallInteger, doc="Starts at center fielder")
    f_cf_out = Column(SmallInteger, doc="Outs played as center fielder")
    f_cf_tc = Column(SmallInteger, doc="Total chances as center fielder")
    f_cf_po = Column(SmallInteger, doc="Putouts as center fielder")
    f_cf_a = Column(SmallInteger, doc="Assists as center fielder")
    f_cf_e = Column(SmallInteger, doc="Errors as center fielder")
    f_cf_dp = Column(SmallInteger, doc="Double plays turned as center fielder")
    f_cf_tp = Column(SmallInteger, doc="Triple pays turned as center fielder")
    f_rf_g = Column(SmallInteger, doc="Appearances at right fielder")
    f_rf_gs = Column(SmallInteger, doc="Starts at right fielder")
    f_rf_out = Column(SmallInteger, doc="Outs played as right fielder")
    f_rf_tc = Column(SmallInteger, doc="Total chances as right fielder")
    f_rf_po = Column(SmallInteger, doc="Putouts as right fielder")
    f_rf_a = Column(SmallInteger, doc="Assists as right fielder")
    f_rf_e = Column(SmallInteger, doc="Errors as right fielder")
    f_rf_dp = Column(SmallInteger, doc="Double plays turned as right fielder")
    f_rf_tp = Column(SmallInteger, doc="Triple pays turned as right fielder")
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class Event(Base):
    """
    The event table is the most granular data available, containing one row for every play of every game
    for which Retrosheet has data. This includes all postseason games in history, all All-Star games in history,
    all regular season games dating back to 1937, and a majority of regular season games dating back to 1921.

    Each row in the table does not necessarily constitute a new or complete plate appearance, as events like
    stolen bases and balks have their own rows.

    If you are going to use this table regularly, it is highly recommended that you choose a column-oriented storage
    option like postgres_cstore_fdw or Clickhouse, as the large row size and row count will create bottlenecks for
    traditional row-oriented stores.

    While all games present in the table have the bare minimum of information about every play in the game,
    there are significant differences in data quality from game to game. These differences in data quality often
    complicate historical analyses.
    -- A significant number of games from 1937-1973 do not have complete play-by-play accounts available. For these
        missing games, Retrosheet has derived play-by-play data using a combination of box scores and game stories.
        These derived games are likely to have less granular data around fielding plays.
    -- The overwhelming majority of games prior to 1988 do not have pitch-by-pitch data available (the most notable
        exceptions to this are the 1950s Dodgers home games). From 1988-1999, nearly all games have pitch sequences,
        but a significant number of games are missing pitch sequences from at least one plate appearance, making
        pitch count analysis a bit more difficult. Games from 2000 on have complete pitch data.
    -- A similar situation exists for hit location data, although location data is more frequently populated for
        older games than pitch data is.
    """
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
    battedball_loc_tx = Column(String(5), doc="Hit location code (see https://www.retrosheet.org/location.htm)")
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
