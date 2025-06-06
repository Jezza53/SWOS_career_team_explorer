d_posfaceval = {
    # HEX values displayed below
    #
    #       G 	RB 	LB 	D 	RW 	LW 	M 	A
    #dface  00 	20 	40 	60 	80 	A0 	C0 	E0
    #lface  08 	28 	48 	68 	88 	A8 	C8 	E8
    #bface	10 	30 	50 	70 	90 	B0 	D0 	F0

    #Goalkepers
    0:("G","n", "img/d_face.png"),
    8:("G","l", "img/l_face.png"),
    16:("G","b", "img/b_face.png"),

    #Rightbacks
    32:("RB","n", "img/d_face.png"),
    40:("RB","l", "img/l_face.png"),
    48:("RB","b", "img/b_face.png"),

    #Leftbacks
    64:("LB","n", "img/d_face.png"),
    72:("LB","l", "img/l_face.png"),
    80:("LB","b", "img/b_face.png"),

    #Defenders
    96:("D","n", "img/d_face.png"),
    104:("D","l", "img/l_face.png"),
    112:("D","b", "img/b_face.png"),

    #Rightwings
    128:("RW","n", "img/d_face.png"),
    136:("RW","l", "img/l_face.png"),
    144:("RW","b", "img/b_face.png"),

    #Leftwings
    160:("LW","n", "img/d_face.png"),
    168:("LW","l", "img/l_face.png"),
    176:("LW","b", "img/b_face.png"),

    #Midfielders
    192:("M","n", "img/d_face.png"),
    200:("M","l", "img/l_face.png"),
    208:("M","b", "img/b_face.png"),

    #Attackers
    224:("A","n", "img/d_face.png"),
    232:("A","l", "img/l_face.png"),
    240:("A","b", "img/b_face.png")
}

d_HEX_nation = {
    # HEX VALUE;DECIMAL VALUE;DATA FILE NUMBER
    '0x00':(0,'000'),'0x01':(1,'001'),'0x02':(2,'002'),'0x03':(3,'003'),'0x04':(4,'004'),'0x05':(5,'005'),'0x06':(6,'006'),'0x07':(7,'007'),'0x08':(8,'008'),'0x09':(9,'010'),
    '0x0a':(10,'011'),'0x0b':(11,'012'),'0x0c':(12,'013'),'0x0d':(13,'014'),'0x0e':(14,'015'),'0x0f':(15,'016'),'0x10':(16,'017'),'0x11':(17,'019'),'0x12':(18,'020'),'0x13':(19,'021'),
    '0x14':(20,'022'),'0x15':(21,'023'),'0x16':(22,'024'),'0x17':(23,'025'),'0x18':(24,'026'),'0x19':(25,'027'),'0x1a':(26,'028'),'0x1b':(27,'029'),'0x1c':(28,'030'),'0x1d':(29,'031'),
    '0x1e':(30,'032'),'0x1f':(31,'033'),'0x20':(32,'034'),'0x21':(33,'036'),'0x22':(34,'038'),'0x23':(35,'039'),'0x24':(36,'040'),'0x25':(37,'041'),'0x26':(38,'076'),'0x27':(39,'078'),
    '0x28':(40,'042'),'0x29':(41,'?'),'0x2a':(42,'?'),'0x2b':(43,'?'),'0x2c':(44,'?'),'0x2d':(45,'037'),'0x2e':(46,'018'),'0x2f':(47,'?'),'0x30':(48,'?'),'0x31':(49,'?'),
    '0x32':(50,'?'),'0x33':(51,'047'),'0x34':(52,'051'),'0x35':(53,'?'),'0x36':(54,'?'),'0x37':(55,'?'),'0x38':(56,'060'),'0x39':(57,'?'),'0x3a':(58,'073'),'0x3b':(59,'?'),
    '0x3c':(60,'?'),'0x3d':(61,'?'),'0x3e':(62,'?'),'0x3f':(63,'?'),'0x40':(64,'?'),'0x41':(65,'?'),'0x42':(66,'?'),'0x43':(67,'?'),'0x44':(68,'043'),'0x45':(69,'045'),
    '0x46':(70,'046'),'0x47':(71,'048'),'0x48':(72,'049'),'0x49':(73,'050'),'0x4a':(74,'064'),'0x4b':(75,'066'),'0x4c':(76,'071'),'0x4d':(77,'077'),'0x4e':(78,'?'),'0x4f':(79,'065'),
    '0x50':(80,'042'),'0x51':(81,'069'),'0x52':(82,'?'),'0x53':(83,'?'),'0x54':(84,'?'),'0x55':(85,'?'),'0x56':(86,'?'),'0x57':(87,'?'),'0x58':(88,'079'),'0x59':(89,'?'),
    '0x5a':(90,'?'),'0x5b':(91,'?'),'0x5c':(92,'?'),'0x5d':(93,'?'),'0x5e':(94,'?'),'0x5f':(95,'?'),'0x60':(96,'?'),'0x61':(97,'?'),'0x62':(98,'?'),'0x63':(99,'?'),
    '0x64':(100,'?'),'0x65':(101,'?'),'0x66':(102,'?'),'0x67':(103,'?'),'0x68':(104,'?'),'0x69':(105,'?'),'0x6a':(106,'070'),'0x6b':(107,'?'),'0x6c':(108,'?'),'0x6d':(109,'?'),
    '0x6e':(110,'?'),'0x6f':(111,'?'),'0x70':(112,'?'),'0x71':(113,'?'),'0x72':(114,'?'),'0x73':(115,'?'),'0x74':(116,'?'),'0x75':(117,'?'),'0x76':(118,'055'),'0x77':(119,'067'),
    '0x78':(120,'075'),'0x79':(121,'?'),'0x7a':(122,'?'),'0x7b':(123,'?'),'0x7c':(124,'?'),'0x7d':(125,'?'),'0x7e':(126,'?'),'0x7f':(127,'057'),'0x80':(128,'?'),'0x81':(129,'?'),
    '0x82':(130,'059'),'0x83':(131,'?'),'0x84':(132,'?'),'0x85':(133,'?'),'0x86':(134,'?'),'0x87':(135,'?'),'0x88':(136,'?'),'0x89':(137,'?'),'0x8a':(138,'?'),'0x8b':(139,'?'),
    '0x8c':(140,'?'),'0x8d':(141,'?'),'0x8e':(142,'?'),'0x8f':(143,'?'),'0x90':(144,'?'),'0x91':(145,'?'),'0x92':(146,'?'),'0x93':(147,'?'),'0x94':(148,'044'),'0x95':(149,'062'),
    '0x96':(150,'?'),'0x97':(151,'?'),'0x98':(152,'072')
}

d_HEX_callplayer = {
    # HEX VALUE; HEX ADDRESS
    '00': 0xDBCC,    '01': 0xDBF2,    '02': 0xDC18,    '03': 0xDC3E,    '04': 0xDC64,    '05': 0xDC8A,    '06': 0xDCB0,    '07': 0xDCD6,    '08': 0xDCFC,
    '09': 0xDD22,    '0a': 0xDD48,    '0b': 0xDD6E,    '0c': 0xDD94,    '0d': 0xDDBA,    '0e': 0xDDE0,    '0f': 0xDE06,    '10': 0xDE2C,    '11': 0xDE52,
    '12': 0xDE78,    '13': 0xDE9E,    '14': 0xDEC4,    '15': 0xDEEA,    '16': 0xDF10,    '17': 0xDF36,    '18': 0xDF5C,    '19': 0xDF82,    '1a': 0xDFA8,
    '1b': 0xDFCE,    '1c': 0xDFF4,    '1d': 0xE01A,    'ff': 0x0000
}

d_AGEdit_nation = {
    # DECIMAL VALUE; NATION
    0:'ALB',	1:'AUT',	2:'BEL',	3:'BUL',	4:'CRO',	5:'CYP',	6:'TCH',	7:'DEN',	8:'ENG',	9:'EST',	10:'FAR',	11:'FIN',
    12:'FRA',	13:'GER',	14:'GRE',	15:'HUN',	16:'ICE',	17:'ISR',	18:'ITA',	19:'LAT',	20:'LIT',	21:'LUX',	22:'MLT',	23:'HOL',
    24:'NIR',	25:'NOR',	26:'POL',	27:'POR',	28:'ROM',	29:'RUS',	30:'SMA',	31:'SCO',	32:'SLO',	33:'SWE',	34:'TUR',	35:'UKR',
    36:'WAL',	37:'SRB',	38:'BLS',	39:'SVK',	40:'ESP',	41:'ARM',	42:'BOS',	43:'AZB',	44:'GEO',	45:'SUI',	46:'IRL',	47:'MAC',
    48:'TKM',	49:'LIE',	50:'MOL',	51:'CRC',	52:'SAL',	53:'GUA',	54:'HON',	55:'BHM',	56:'MEX',	57:'PAN',	58:'USA',	59:'BAH',
    60:'NIC',	61:'BER',	62:'JAM',	63:'TRI',	64:'CAN',	65:'BAR',	66:'ELS',	67:'SVC',	68:'ARG',	69:'BOL',	70:'BRA',	71:'CHL',
    72:'COL',	73:'ECU',	74:'PAR',	75:'SUR',	76:'URU',	77:'VEN',	78:'GUY',	79:'PER',	80:'ALG',	81:'SAF',	82:'BOT',	83:'BFS',
    84:'BUR',	85:'LES',	86:'ZAI',	87:'ZAM',	88:'GHA',	89:'SEN',	90:'CIV',	91:'TUN',	92:'MLI',	93:'MDG',	94:'CMR',	95:'CHD',
    96:'UGA',	97:'LIB',	98:'MOZ',	99:'KEN',	100:'SUD',	101:'SWA',	102:'ANG',	103:'TOG',	104:'ZIM',	105:'EGY',	106:'TAN',	107:'NIG',
    108:'ETH',	109:'GAB',	110:'SIE',	111:'BEN',	112:'CON',	113:'GUI',	114:'SRL',	115:'MAR',	116:'GAM',	117:'MLW',	118:'JAP',	119:'TAI',
    120:'IND',	121:'BAN',	122:'BRU',	123:'IRA',	124:'JOR',	125:'SRI',	126:'SYR',	127:'KOR',	128:'IRN',	129:'VIE',	130:'MLY',	131:'SAU',
    132:'YEM',	133:'KUW',	134:'LAO',	135:'NKR',	136:'OMA',	137:'PAK',	138:'PHI',	139:'CHN',	140:'SGP',	141:'MAU',	142:'MYA',	143:'PAP',
    144:'TAD',	145:'UZB',	146:'QAT',	147:'UAE',	148:'AUS',	149:'NZL',	150:'FIJ',	151:'SOL',	152:'CUS'
}

d_AGEDIT_POSITION = {
    "G":0,    "RB":1,    "LB":2,    "D":3,    "LW":4,    "RW":5,    "M":6,    "A":7
}

d_AGEDIT_SKIN = {
    "n":1,    "l":2,    "b":3
}

d_HEX_skills = {
    '0x0':0,'0x1':1,'0x2':2,'0x3':3,'0x4':4,'0x5':5,'0x6':6,'0x7':7,
    '0x8':8,'0x9':9,'0xa':10,'0xb':11,'0xc':12,'0xd':13,'0xe':14,'0xf':15
}

d_HEX_squadno = {
    '01': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6, '07': 7,
    '08': 8, '09': 9, '0a': 10, '0b': 11, '0c': 12, '0d': 13, '0e': 14, '0f': 15, '10': 16
}

d_stars = {
    '00': 'img/s01.png',    '01': 'img/s01.png',    '02': 'img/s01.png',    '03': 'img/s01.png',
    '04': 'img/s02.png',    '05': 'img/s02.png',    '06': 'img/s02.png',    '07': 'img/s03.png',
    '08': 'img/s03.png',    '09': 'img/s03.png',    '0a': 'img/s03.png',    '0b': 'img/s03.png',
    '0c': 'img/s04.png',    '0d': 'img/s04.png',    '0e': 'img/s04.png',    '0f': 'img/s04.png',
    '10': 'img/s05.png',    '11': 'img/s05.png',    '12': 'img/s05.png',    '13': 'img/s05.png',
    '14': 'img/s05.png',    '15': 'img/s06.png',    '16': 'img/s06.png',    '17': 'img/s06.png',
    '18': 'img/s06.png',    '19': 'img/s06.png',    '1a': 'img/s06.png',    '1b': 'img/s06.png',
    '1c': 'img/s06.png',    '1d': 'img/s07.png',    '1e': 'img/s07.png',    '1f': 'img/s07.png',
    '20': 'img/s07.png',    '21': 'img/s07.png',    '22': 'img/s08.png',    '23': 'img/s08.png',
    '24': 'img/s08.png',    '25': 'img/s08.png',    '26': 'img/s08.png',    '27': 'img/s08.png',
    '28': 'img/s09.png',    '29': 'img/s09.png',    '2a': 'img/s09.png',    '2b': 'img/s09.png',
    '2c': 'img/s09.png',    '2d': 'img/s09.png',    '2e': 'img/s09.png',    '2f': 'img/s10.png',
    '30': 'img/s10.png',    '31': 'img/s10.png'
}

d_stars_values = {
    '00': 0.5, '01': 0.5, '02': 0.5, '03': 0.5,
    '04': 1.0, '05': 1.0, '06': 1.0, '07': 1.5,
    '08': 1.5, '09': 1.5, '0a': 1.5, '0b': 1.5,
    '0c': 2.0, '0d': 2.0, '0e': 2.0, '0f': 2.0,
    '10': 2.5, '11': 2.5, '12': 2.5, '13': 2.5,
    '14': 2.5, '15': 3.0, '16': 3.0, '17': 3.0,
    '18': 3.0, '19': 3.0, '1a': 3.0, '1b': 3.0,
    '1c': 3.0, '1d': 3.5, '1e': 3.5, '1f': 3.5,
    '20': 3.5, '21': 3.5, '22': 4.0, '23': 4.0,
    '24': 4.0, '25': 4.0, '26': 4.0, '27': 4.0,
    '28': 4.5, '29': 4.5, '2a': 4.5, '2b': 4.5,
    '2c': 4.5, '2d': 4.5, '2e': 4.5, '2f': 5.0,
    '30': 5.0, '31': 5.0
}

# Dictionary mapping hex codes to monetary values
d_values = {
    '00': '25K', '01': '25K', '02': '30K', '03': '40K',
    '04': '50K', '05': '65K', '06': '75K', '07': '85K',
    '08': '100K', '09': '110K', '0a': '130K', '0b': '150K',
    '0c': '160K', '0d': '180K', '0e': '200K', '0f': '250K',
    '10': '300K', '11': '350K', '12': '450K', '13': '500K',
    '14': '550K', '15': '600K', '16': '650K', '17': '700K',
    '18': '750K', '19': '800K', '1a': '850K', '1b': '950K',
    '1c': '1M', '1d': '1.1M', '1e': '1.3M', '1f': '1.5M',
    '20': '1.6M', '21': '1.8M', '22': '1.9M', '23': '2M',
    '24': '2.25M', '25': '2.75M', '26': '3M', '27': '3.5M',
    '28': '4.5M', '29': '5M', '2a': '6M', '2b': '7M',
    '2c': '8M', '2d': '9M', '2e': '10M', '2f': '12M',
    '30': '15M', '31': '15M+'
}

d_skillcolor = {
    0: '#770022',    1: '#770022',    2: '#ff0000',    3: '#ff0000',    4: '#ff7711',    5: '#ff7711',
    6: '#ffff00',    7: '#ffffff',    8: '#770022',    9: '#770022',    10: '#ff0000',    11: '#ff0000',
    12: '#ff7711',    13: '#ff7711',    14: '#ffff00',    15: '#ffffff'
}

d_teamfile = { # teamfile number: (country name, region, career playable)
    'TEAM.000': ('Albania', 'Europe', True),
    'TEAM.001': ('Austria', 'Europe', True),
    'TEAM.002': ('Belgium', 'Europe', True),
    'TEAM.003': ('Bulgaria', 'Europe', True),
    'TEAM.004': ('Croatia', 'Europe', True),
    'TEAM.005': ('Cyprus', 'Europe', True),
    'TEAM.006': ('Czechia', 'Europe', True),
    'TEAM.007': ('Denmark', 'Europe', True),
    'TEAM.008': ('England', 'Europe', True),
    'TEAM.010': ('Estonia', 'Europe', True),
    'TEAM.011': ('Faroe Islands', 'Europe', True),
    'TEAM.012': ('Finland', 'Europe', True),
    'TEAM.013': ('France', 'Europe', True),
    'TEAM.014': ('Germany', 'Europe', True),
    'TEAM.015': ('Greece', 'Europe', True),
    'TEAM.016': ('Hungary', 'Europe', True),
    'TEAM.017': ('Iceland', 'Europe', True),
    'TEAM.018': ('Rep. Of Ireland', 'Europe', True),
    'TEAM.019': ('Israel', 'Europe', True),
    'TEAM.020': ('Italy', 'Europe', True),
    'TEAM.021': ('Latvia', 'Europe', True),
    'TEAM.022': ('Lithuania', 'Europe', True),
    'TEAM.023': ('Luxembourg', 'Europe', True),
    'TEAM.024': ('Malta', 'Europe', True),
    'TEAM.025': ('Holland', 'Europe', True),
    'TEAM.026': ('Northern Ireland', 'Europe', True),
    'TEAM.027': ('Norway', 'Europe', True),
    'TEAM.028': ('Poland', 'Europe', True),
    'TEAM.029': ('Portugal', 'Europe', True),
    'TEAM.030': ('Romania', 'Europe', True),
    'TEAM.031': ('Russia', 'Europe', True),
    'TEAM.032': ('San Marino', 'Europe', True),
    'TEAM.033': ('Scotland', 'Europe', True),
    'TEAM.034': ('Slovenia', 'Europe', True),
    'TEAM.035': ('Spain', 'Europe', True),
    'TEAM.036': ('Sweden', 'Europe', True),
    'TEAM.037': ('Switzerland', 'Europe', True),
    'TEAM.038': ('Turkiye', 'Europe', True),
    'TEAM.039': ('Ukraine', 'Europe', True),
    'TEAM.040': ('Wales', 'Europe', True),
    'TEAM.041': ('Yugoslavia', 'Europe', True),
    'TEAM.042': ('Algeria', 'Africa', True),
    'TEAM.043': ('Argentina', 'South America', True),
    'TEAM.044': ('Australia', 'Oceania', True),
    'TEAM.045': ('Bolivia', 'South America', True),
    'TEAM.046': ('Brazil', 'South America', True),
    'TEAM.047': ('Costa Rica', 'None', True),
    'TEAM.048': ('Chile', 'South America', True),
    'TEAM.049': ('Colombia', 'South America', True),
    'TEAM.050': ('Ecuador', 'South America', True),
    'TEAM.051': ('El Salvador', 'North America', True),
    'TEAM.055': ('Japan', 'Asia', True),
    'TEAM.057': ('KOR', 'None', False),
    'TEAM.059': ('MAL', 'None', False),
    'TEAM.060': ('Mexico', 'North America', True),
    'TEAM.062': ('New Zealand', 'Oceania', True),
    'TEAM.064': ('Paraguay', 'South America', True),
    'TEAM.065': ('Peru', 'South America', True),
    'TEAM.066': ('Surinam', 'South America', True),
    'TEAM.067': ('Taiwan', 'Asia', True),
    'TEAM.068': ('Other National Teams', 'None', False),
    'TEAM.069': ('Rep. South Africa', 'Africa', True),
    'TEAM.070': ('TAN', 'None', False),
    'TEAM.071': ('Uruguay', 'South America', True),
    'TEAM.072': ('Original Custom Teams', 'None', False),
    'TEAM.073': ('USA', 'North America', True),
    'TEAM.074': ('FIFA World Cup', 'None', False),
    'TEAM.075': ('India', 'Asia', True),
    'TEAM.076': ('Belarus', 'Europe', True),
    'TEAM.077': ('Venezuela', 'South America', True),
    'TEAM.078': ('Slovakia', 'Europe', True),
    'TEAM.079': ('Ghana', 'Africa', True),
    'TEAM.080': ('UEFA', 'Europe', True),
    'TEAM.081': ('CAF', 'Africa', True),
    'TEAM.082': ('CONMEBOL', 'North America', True),
    'TEAM.083': ('CONCACAF', 'South America', True),
    'TEAM.084': ('AFC', 'Asia', True),
    'TEAM.085': ('OFC', 'Oceania', True)
    }