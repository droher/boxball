from sqlalchemy import Column, DateTime, Float, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AllstarFull(Base):
    __tablename__ = 'AllstarFull'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    gameNum = Column(Integer, primary_key=True, nullable=False)
    gameID = Column(String(12))
    teamID = Column(String(3))
    lgID = Column(String(2))
    GP = Column(Integer)
    startingPos = Column(Integer)


class Appearance(Base):
    __tablename__ = 'Appearances'

    yearID = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3), primary_key=True, nullable=False)
    lgID = Column(String(2))
    playerID = Column(String(9), primary_key=True, nullable=False)
    G_all = Column(Integer)
    GS = Column(Integer)
    G_batting = Column(Integer)
    G_defense = Column(Integer)
    G_p = Column(Integer)
    G_c = Column(Integer)
    G_1b = Column(Integer)
    G_2b = Column(Integer)
    G_3b = Column(Integer)
    G_ss = Column(Integer)
    G_lf = Column(Integer)
    G_cf = Column(Integer)
    G_rf = Column(Integer)
    G_of = Column(Integer)
    G_dh = Column(Integer)
    G_ph = Column(Integer)
    G_pr = Column(Integer)


class AwardsManager(Base):
    __tablename__ = 'AwardsManagers'

    playerID = Column(String(10), primary_key=True, nullable=False)
    awardID = Column(String(75), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    tie = Column(String(1))
    notes = Column(String(100))


class AwardsPlayer(Base):
    __tablename__ = 'AwardsPlayers'

    playerID = Column(String(9), primary_key=True, nullable=False)
    awardID = Column(String(255), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    tie = Column(String(1))
    notes = Column(String(100))


class AwardsShareManager(Base):
    __tablename__ = 'AwardsShareManagers'

    awardID = Column(String(25), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    playerID = Column(String(10), primary_key=True, nullable=False)
    pointsWon = Column(Integer)
    pointsMax = Column(Integer)
    votesFirst = Column(Integer)


class AwardsSharePlayer(Base):
    __tablename__ = 'AwardsSharePlayers'

    awardID = Column(String(25), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    playerID = Column(String(9), primary_key=True, nullable=False)
    pointsWon = Column(Float(53))
    pointsMax = Column(Integer)
    votesFirst = Column(Float(53))


class Batting(Base):
    __tablename__ = 'Batting'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    stint = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    G = Column(Integer)
    G_batting = Column(Integer)
    AB = Column(Integer)
    R = Column(Integer)
    H = Column(Integer)
    _2B = Column('2B', Integer)
    _3B = Column('3B', Integer)
    HR = Column(Integer)
    RBI = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    IBB = Column(Integer)
    HBP = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class BattingPost(Base):
    __tablename__ = 'BattingPost'

    yearID = Column(Integer, primary_key=True, nullable=False)
    round = Column(String(10), primary_key=True, nullable=False)
    playerID = Column(String(9), primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    G = Column(Integer)
    AB = Column(Integer)
    R = Column(Integer)
    H = Column(Integer)
    _2B = Column('2B', Integer)
    _3B = Column('3B', Integer)
    HR = Column(Integer)
    RBI = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    IBB = Column(Integer)
    HBP = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class CollegePlaying(Base):
    __tablename__ = 'CollegePlaying'

    Column('playerID', String(9), primary_key=True),
    Column('schoolID', String(15), primary_key=True),
    Column('yearID', Integer, primary_key=True)


class Fielding(Base):
    __tablename__ = 'Fielding'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    stint = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    POS = Column(String(2), primary_key=True, nullable=False)
    G = Column(Integer)
    GS = Column(Integer)
    InnOuts = Column(Integer)
    PO = Column(Integer)
    A = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    PB = Column(Integer)
    WP = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    ZR = Column(Float(53))


class FieldingOF(Base):
    __tablename__ = 'FieldingOF'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    stint = Column(Integer, primary_key=True, nullable=False)
    Glf = Column(Integer)
    Gcf = Column(Integer)
    Grf = Column(Integer)


class FieldingOFSplit(Base):
    __tablename__ = 'FieldingOFSplit'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    stint = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    POS = Column(String(2), primary_key=True, nullable=False)
    G = Column(Integer)
    GS = Column(Integer)
    InnOuts = Column(Integer)
    PO = Column(Integer)
    A = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    PB = Column(Integer)
    WP = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    ZR = Column(Float(53))


class FieldingPost(Base):
    __tablename__ = 'FieldingPost'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    round = Column(String(10), primary_key=True, nullable=False)
    POS = Column(String(2), primary_key=True, nullable=False)
    G = Column(Integer)
    GS = Column(Integer)
    InnOuts = Column(Integer)
    PO = Column(Integer)
    A = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    TP = Column(Integer)
    PB = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)


class HallOfFame(Base):
    __tablename__ = 'HallOfFame'

    playerID = Column(String(10), primary_key=True, nullable=False)
    yearid = Column(Integer, primary_key=True, nullable=False)
    votedBy = Column(String(64), primary_key=True, nullable=False)
    ballots = Column(Integer)
    needed = Column(Integer)
    votes = Column(Integer)
    inducted = Column(String(1))
    category = Column(String(20))
    needed_note = Column(String(25))


class Manager(Base):
    __tablename__ = 'Managers'

    playerID = Column(String(10))
    yearID = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3), primary_key=True, nullable=False)
    lgID = Column(String(2))
    inseason = Column(Integer, primary_key=True, nullable=False)
    G = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
    rank = Column(Integer)
    plyrMgr = Column(String(1))


class ManagersHalf(Base):
    __tablename__ = 'ManagersHalf'

    playerID = Column(String(10), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3), primary_key=True, nullable=False)
    lgID = Column(String(2))
    inseason = Column(Integer)
    half = Column(Integer, primary_key=True, nullable=False)
    G = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
    rank = Column(Integer)


class People(Base):
    __tablename__ = 'People'

    playerID = Column(String(10), primary_key=True)
    birthYear = Column(Integer)
    birthMonth = Column(Integer)
    birthDay = Column(Integer)
    birthCountry = Column(String(50))
    birthState = Column(String(2))
    birthCity = Column(String(50))
    deathYear = Column(Integer)
    deathMonth = Column(Integer)
    deathDay = Column(Integer)
    deathCountry = Column(String(50))
    deathState = Column(String(2))
    deathCity = Column(String(50))
    nameFirst = Column(String(50))
    nameLast = Column(String(50))
    nameGiven = Column(String(255))
    weight = Column(Integer)
    height = Column(Float(53))
    bats = Column(String(1))
    throws = Column(String(1))
    debut = Column(DateTime)
    finalGame = Column(DateTime)
    retroID = Column(String(9))
    bbrefID = Column(String(9))


class Pitching(Base):
    __tablename__ = 'Pitching'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    stint = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    W = Column(Integer)
    L = Column(Integer)
    G = Column(Integer)
    GS = Column(Integer)
    CG = Column(Integer)
    SHO = Column(Integer)
    SV = Column(Integer)
    IPouts = Column(Integer)
    H = Column(Integer)
    ER = Column(Integer)
    HR = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    BAOpp = Column(Float(53))
    ERA = Column(Float(53))
    IBB = Column(Integer)
    WP = Column(Integer)
    HBP = Column(Integer)
    BK = Column(Integer)
    BFP = Column(Integer)
    GF = Column(Integer)
    R = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class PitchingPost(Base):
    __tablename__ = 'PitchingPost'

    playerID = Column(String(9), primary_key=True, nullable=False)
    yearID = Column(Integer, primary_key=True, nullable=False)
    round = Column(String(10), primary_key=True, nullable=False)
    teamID = Column(String(3))
    lgID = Column(String(2))
    W = Column(Integer)
    L = Column(Integer)
    G = Column(Integer)
    GS = Column(Integer)
    CG = Column(Integer)
    SHO = Column(Integer)
    SV = Column(Integer)
    IPouts = Column(Integer)
    H = Column(Integer)
    ER = Column(Integer)
    HR = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    BAOpp = Column(Float(53))
    ERA = Column(Float(53))
    IBB = Column(Integer)
    WP = Column(Integer)
    HBP = Column(Integer)
    BK = Column(Integer)
    BFP = Column(Integer)
    GF = Column(Integer)
    R = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class Salary(Base):
    __tablename__ = 'Salaries'

    yearID = Column(Integer, primary_key=True, nullable=False)
    teamID = Column(String(3), primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    playerID = Column(String(9), primary_key=True, nullable=False)
    salary = Column(Float(53))


class School(Base):
    __tablename__ = 'Schools'

    schoolID = Column(String(15), primary_key=True)
    name_full = Column(String(255))
    city = Column(String(55))
    state = Column(String(55))
    country = Column(String(55))


class SeriesPost(Base):
    __tablename__ = 'SeriesPost'

    yearID = Column(Integer, primary_key=True, nullable=False)
    round = Column(String(5), primary_key=True, nullable=False)
    teamIDwinner = Column(String(3))
    lgIDwinner = Column(String(2))
    teamIDloser = Column(String(3))
    lgIDloser = Column(String(2))
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)


class Team(Base):
    __tablename__ = 'Teams'

    yearID = Column(Integer, primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    teamID = Column(String(3), primary_key=True, nullable=False)
    franchID = Column(String(3))
    divID = Column(String(1))
    Rank = Column(Integer)
    G = Column(Integer)
    Ghome = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
    DivWin = Column(String(1))
    WCWin = Column(String(1))
    LgWin = Column(String(1))
    WSWin = Column(String(1))
    R = Column(Integer)
    AB = Column(Integer)
    H = Column(Integer)
    _2B = Column('2B', Integer)
    _3B = Column('3B', Integer)
    HR = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    HBP = Column(Integer)
    SF = Column(Integer)
    RA = Column(Integer)
    ER = Column(Integer)
    ERA = Column(Float(53))
    CG = Column(Integer)
    SHO = Column(Integer)
    SV = Column(Integer)
    IPouts = Column(Integer)
    HA = Column(Integer)
    HRA = Column(Integer)
    BBA = Column(Integer)
    SOA = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    FP = Column(Float(53))
    name = Column(String(50))
    park = Column(String(255))
    attendance = Column(Integer)
    BPF = Column(Integer)
    PPF = Column(Integer)
    teamIDBR = Column(String(3))
    teamIDlahman45 = Column(String(3))
    teamIDretro = Column(String(3))


class TeamsFranchise(Base):
    __tablename__ = 'TeamsFranchises'

    franchID = Column(String(3), primary_key=True)
    franchName = Column(String(50))
    active = Column(String(2))
    NAassoc = Column(String(3))


class TeamsHalf(Base):
    __tablename__ = 'TeamsHalf'

    yearID = Column(Integer, primary_key=True, nullable=False)
    lgID = Column(String(2), primary_key=True, nullable=False)
    teamID = Column(String(3), primary_key=True, nullable=False)
    Half = Column(String(1), primary_key=True, nullable=False)
    divID = Column(String(1))
    DivWin = Column(String(1))
    Rank = Column(Integer)
    G = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
