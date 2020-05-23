from sqlalchemy import MetaData, Column, Date, Float, Integer, String, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData(schema="baseballdatabank"))
metadata = Base.metadata


class AllstarFull(Base):
    __tablename__ = 'allstar_full'

    player_id = Column(String(9), nullable=False)
    # Should be non-nullable, see https://github.com/chadwickbureau/baseballdatabank/issues/105
    year_id = Column(SmallInteger)
    game_num = Column(SmallInteger)
    game_id = Column(String(12))
    team_id = Column(String(3))
    lg_id = Column(String(2))
    gp = Column(SmallInteger)
    starting_pos = Column(SmallInteger)
    # Note -- Billy Herman's 1934 record prevents us from using the true PK, player-year-gamenum
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class Appearance(Base):
    __tablename__ = 'appearances'

    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    lg_id = Column(String(2))
    player_id = Column(String(9), primary_key=True, nullable=False)
    g_all = Column(SmallInteger)
    gs = Column(SmallInteger)
    g_batting = Column(SmallInteger)
    g_defense = Column(SmallInteger)
    g_p = Column(SmallInteger)
    g_c = Column(SmallInteger)
    g_1b = Column(SmallInteger)
    g_2b = Column(SmallInteger)
    g_3b = Column(SmallInteger)
    g_ss = Column(SmallInteger)
    g_lf = Column(SmallInteger)
    g_cf = Column(SmallInteger)
    g_rf = Column(SmallInteger)
    g_of = Column(SmallInteger)
    g_dh = Column(SmallInteger)
    g_ph = Column(SmallInteger)
    g_pr = Column(SmallInteger)


class AwardsManager(Base):
    __tablename__ = 'awards_managers'

    player_id = Column(String(10), nullable=False)
    award_id = Column(String(75), nullable=False)
    year_id = Column(SmallInteger, nullable=False)
    lg_id = Column(String(2))
    tie = Column(String(1))
    notes = Column(String(100))
    # PK should be player/award/year/lg, see https://github.com/chadwickbureau/baseballdatabank/issues/105
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class AwardsPlayer(Base):
    __tablename__ = 'awards_players'

    player_id = Column(String(9))
    award_id = Column(String(255))
    year_id = Column(SmallInteger)
    lg_id = Column(String(2))
    tie = Column(String(1))
    notes = Column(String(100))
    dummy_id = Column(Integer, autoincrement=True, primary_key=True)


class AwardsShareManager(Base):
    __tablename__ = 'awards_share_managers'

    award_id = Column(String(25), primary_key=True, nullable=False)
    year_id = Column(Integer, primary_key=True, nullable=False)
    lg_id = Column(String(2))
    player_id = Column(String(10), primary_key=True, nullable=False)
    points_won = Column(Integer)
    points_max = Column(Integer)
    votes_first = Column(Integer)


class AwardsSharePlayer(Base):
    __tablename__ = 'awards_share_players'

    award_id = Column(String(25), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    lg_id = Column(String(2))
    player_id = Column(String(9), primary_key=True, nullable=False)
    points_won = Column(Float(53))
    points_max = Column(Integer)
    votes_first = Column(Float(53))


class Batting(Base):
    __tablename__ = 'batting'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    stint = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    g = Column(SmallInteger)
    ab = Column(SmallInteger)
    r = Column(SmallInteger)
    h = Column(SmallInteger)
    _2b = Column(SmallInteger)
    _3b = Column(SmallInteger)
    hr = Column(SmallInteger)
    rbi = Column(SmallInteger)
    sb = Column(SmallInteger)
    cs = Column(SmallInteger)
    bb = Column(SmallInteger)
    so = Column(SmallInteger)
    ibb = Column(SmallInteger)
    hbp = Column(SmallInteger)
    sh = Column(SmallInteger)
    sf = Column(SmallInteger)
    gidp = Column(SmallInteger)


class BattingPost(Base):
    __tablename__ = 'batting_post'

    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    round = Column(String(10), primary_key=True, nullable=False)
    player_id = Column(String(9), primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    g = Column(SmallInteger)
    ab = Column(SmallInteger)
    r = Column(SmallInteger)
    h = Column(SmallInteger)
    _2b = Column(SmallInteger)
    _3b = Column(SmallInteger)
    hr = Column(SmallInteger)
    rbi = Column(SmallInteger)
    sb = Column(SmallInteger)
    cs = Column(SmallInteger)
    bb = Column(SmallInteger)
    so = Column(SmallInteger)
    ibb = Column(SmallInteger)
    hbp = Column(SmallInteger)
    sh = Column(SmallInteger)
    sf = Column(SmallInteger)
    gidp = Column(SmallInteger)


class CollegePlaying(Base):
    __tablename__ = 'college_playing'

    player_id = Column(String(9), primary_key=True)
    school_id = Column(String(15), primary_key=True)
    year_id = Column(SmallInteger, primary_key=True)


class Fielding(Base):
    __tablename__ = 'fielding'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    stint = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    pos = Column(String(2), primary_key=True, nullable=False)
    g = Column(SmallInteger)
    gs = Column(SmallInteger)
    inn_outs = Column(SmallInteger)
    po = Column(SmallInteger)
    a = Column(SmallInteger)
    e = Column(SmallInteger)
    dp = Column(SmallInteger)
    pb = Column(SmallInteger)
    wp = Column(SmallInteger)
    sb = Column(SmallInteger)
    cs = Column(SmallInteger)
    zr = Column(Float(53))


class FieldingOF(Base):
    __tablename__ = 'fielding_of'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    stint = Column(SmallInteger, primary_key=True, nullable=False)
    g_lf = Column(SmallInteger)
    g_cf = Column(SmallInteger)
    g_rf = Column(SmallInteger)


class FieldingOFSplit(Base):
    """
    Disaggregates outfield statistics from `Fielding` into LF, CF, and RF
    """
    __tablename__ = 'fielding_of_split'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    stint = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    pos = Column(String(2), primary_key=True, nullable=False)
    g = Column(SmallInteger)
    gs = Column(SmallInteger)
    inn_outs = Column(SmallInteger)
    po = Column(SmallInteger)
    a = Column(SmallInteger)
    e = Column(SmallInteger)
    dp = Column(SmallInteger)
    pb = Column(SmallInteger)
    wp = Column(SmallInteger)
    sb = Column(SmallInteger)
    cs = Column(SmallInteger)
    zr = Column(Float(53))


class FieldingPost(Base):
    __tablename__ = 'fielding_post'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    round = Column(String(10), primary_key=True, nullable=False)
    pos = Column(String(2), primary_key=True, nullable=False)
    g = Column(SmallInteger)
    gs = Column(SmallInteger)
    inn_outs = Column(SmallInteger)
    po = Column(SmallInteger)
    a = Column(SmallInteger)
    e = Column(SmallInteger)
    dp = Column(SmallInteger)
    tp = Column(SmallInteger)
    pb = Column(SmallInteger)
    sb = Column(SmallInteger)
    cs = Column(SmallInteger)


class HallOfFame(Base):
    __tablename__ = 'hall_of_fame'

    player_id = Column(String(10), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    voted_by = Column(String(64), primary_key=True, nullable=False)
    ballots = Column(SmallInteger)
    needed = Column(SmallInteger)
    votes = Column(SmallInteger)
    inducted = Column(String(1))
    category = Column(String(20))
    needed_note = Column(String(25))


class HomeGames(Base):
    __tablename__ = "home_games"

    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    lg_id = Column(String(2), primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    park_id = Column(String(5), primary_key=True, nullable=False)
    first_game = Column(Date)
    last_game = Column(Date)
    games = Column(SmallInteger)
    openings = Column(SmallInteger)
    attendance = Column(Integer)


class Manager(Base):
    __tablename__ = 'managers'

    player_id = Column(String(10))
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    lg_id = Column(String(2))
    inseason = Column(SmallInteger, primary_key=True, nullable=False)
    g = Column(SmallInteger)
    w = Column(SmallInteger)
    l = Column(SmallInteger)
    rank = Column(SmallInteger)
    plyr_mgr = Column(String(1))


class ManagersHalf(Base):
    __tablename__ = 'managers_half'

    player_id = Column(String(10), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    lg_id = Column(String(2))
    inseason = Column(SmallInteger)
    half = Column(SmallInteger, primary_key=True, nullable=False)
    g = Column(SmallInteger)
    w = Column(SmallInteger)
    l = Column(SmallInteger)
    rank = Column(SmallInteger)


class Parks(Base):
    __tablename__ = "parks"

    park_id = Column(String(5), primary_key=True, nullable=False)
    park_name = Column(String(40))
    park_alias = Column(String(55))
    city = Column(String(25))
    state = Column(String(16))
    country = Column(String(2))


class People(Base):
    __tablename__ = 'people'

    player_id = Column(String(10), primary_key=True)
    birth_year = Column(SmallInteger)
    birth_month = Column(SmallInteger)
    birth_day = Column(SmallInteger)
    birth_country = Column(String(50))
    birth_state = Column(String(50))
    birth_city = Column(String(50))
    death_year = Column(SmallInteger)
    death_month = Column(SmallInteger)
    death_day = Column(SmallInteger)
    death_country = Column(String(50))
    death_state = Column(String(50))
    death_city = Column(String(50))
    name_first = Column(String(50))
    name_last = Column(String(50))
    name_given = Column(String(255))
    weight = Column(SmallInteger)
    height = Column(Float(53))
    bats = Column(String(1))
    throws = Column(String(1))
    debut = Column(Date)
    final_game = Column(Date)
    retro_id = Column(String(9))
    bbref_id = Column(String(9))


class Pitching(Base):
    __tablename__ = 'pitching'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    stint = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    w = Column(SmallInteger)
    l = Column(SmallInteger)
    g = Column(SmallInteger)
    gs = Column(SmallInteger)
    cg = Column(SmallInteger)
    sho = Column(SmallInteger)
    sv = Column(SmallInteger)
    ip_outs = Column(SmallInteger)
    h = Column(SmallInteger)
    er = Column(SmallInteger)
    hr = Column(SmallInteger)
    bb = Column(SmallInteger)
    so = Column(SmallInteger)
    ba_opp = Column(Float(53))
    era = Column(Float(53))
    ibb = Column(SmallInteger)
    wp = Column(SmallInteger)
    hbp = Column(SmallInteger)
    bk = Column(SmallInteger)
    bfp = Column(SmallInteger)
    gf = Column(SmallInteger)
    r = Column(SmallInteger)
    sh = Column(SmallInteger)
    sf = Column(SmallInteger)
    gidp = Column(SmallInteger)


class PitchingPost(Base):
    __tablename__ = 'pitching_post'

    player_id = Column(String(9), primary_key=True, nullable=False)
    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    round = Column(String(10), primary_key=True, nullable=False)
    team_id = Column(String(3))
    lg_id = Column(String(2))
    w = Column(SmallInteger)
    l = Column(SmallInteger)
    g = Column(SmallInteger)
    gs = Column(SmallInteger)
    cg = Column(SmallInteger)
    sho = Column(SmallInteger)
    sv = Column(SmallInteger)
    ip_outs = Column(SmallInteger)
    h = Column(SmallInteger)
    er = Column(SmallInteger)
    hr = Column(SmallInteger)
    bb = Column(SmallInteger)
    so = Column(SmallInteger)
    ba_opp = Column(Float(53))
    era = Column(Float(53))
    ibb = Column(SmallInteger)
    wp = Column(SmallInteger)
    hbp = Column(SmallInteger)
    bk = Column(SmallInteger)
    bfp = Column(SmallInteger)
    gf = Column(SmallInteger)
    r = Column(SmallInteger)
    sh = Column(SmallInteger)
    sf = Column(SmallInteger)
    gidp = Column(SmallInteger)


class Salary(Base):
    __tablename__ = 'salaries'

    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    lg_id = Column(String(2), primary_key=True, nullable=False)
    player_id = Column(String(9), primary_key=True, nullable=False)
    salary = Column(Float(53))


class School(Base):
    __tablename__ = 'schools'

    school_id = Column(String(15), primary_key=True)
    name_full = Column(String(255))
    city = Column(String(55))
    state = Column(String(55))
    country = Column(String(55))


class SeriesPost(Base):
    __tablename__ = 'series_post'

    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    round = Column(String(5), primary_key=True, nullable=False)
    team_id_winner = Column(String(3))
    lg_id_winner = Column(String(2))
    team_id_loser = Column(String(3))
    lg_id_loser = Column(String(2))
    wins = Column(SmallInteger)
    losses = Column(SmallInteger)
    ties = Column(SmallInteger)


class Team(Base):
    __tablename__ = 'teams'

    year_id = Column(SmallInteger, primary_key=True, nullable=False)
    lg_id = Column(String(2), primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    franch_id = Column(String(3))
    div_id = Column(String(1))
    rank = Column(Integer)
    g = Column(Integer)
    g_home = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    div_win = Column(String(1))
    wc_win = Column(String(1))
    lg_win = Column(String(1))
    ws_win = Column(String(1))
    r = Column(Integer)
    ab = Column(Integer)
    h = Column(Integer)
    _2b = Column(Integer)
    _3b = Column(Integer)
    hr = Column(Integer)
    bb = Column(Integer)
    so = Column(Integer)
    sb = Column(Integer)
    cs = Column(Integer)
    hbp = Column(Integer)
    sf = Column(Integer)
    ra = Column(Integer)
    er = Column(Integer)
    era = Column(Float(53))
    cg = Column(Integer)
    sho = Column(Integer)
    sv = Column(Integer)
    ip_outs = Column(Integer)
    h_a = Column(Integer)
    hr_a = Column(Integer)
    bb_a = Column(Integer)
    so_a = Column(Integer)
    e = Column(Integer)
    dp = Column(Integer)
    fp = Column(Float(53))
    name = Column(String(50))
    park = Column(String(255))
    attendance = Column(Integer)
    bpf = Column(Integer)
    ppf = Column(Integer)
    team_id_br = Column(String(3))
    team_id_lahman45 = Column(String(3))
    team_id_retro = Column(String(3))


class TeamsFranchise(Base):
    __tablename__ = 'teams_franchises'

    franch_id = Column(String(3), primary_key=True)
    franch_name = Column(String(50))
    active = Column(String(2))
    na_assoc = Column(String(3))


class TeamsHalf(Base):
    """Table for years in MLB history that the season was divided into halves (e.g. 1981)"""

    __tablename__ = 'teams_half'

    year_id = Column(Integer, primary_key=True, nullable=False)
    lg_id = Column(String(2), primary_key=True, nullable=False)
    team_id = Column(String(3), primary_key=True, nullable=False)
    half = Column(String(1), primary_key=True, nullable=False)
    div_id = Column(String(1))
    div_win = Column(String(1))
    rank = Column(Integer)
    g = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
