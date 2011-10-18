

"""\
This file contains expanded versions of data values and other utilities for
working with data.

"""


import re


# For informant fields
INFTYPE = {
        'I': 'Folk',
        'II': 'Common',
        'III': 'Cultivated',
        }
SEX = {
        'F': 'Female',
        'M': 'Male',
        }
EDUCATION = {
        '0': 'Illiterate',
        '1': 'Some grade school',
        '2': 'Grade school',
        '3': 'Some high school',
        '4': 'High school',
        '5': 'Some college',
        '6': 'College',
        }
OCCUPATION = {
        'P': 'Professional and technical',
        'F': 'Farmers',
        'M': 'Managers, officials, proprietors',
        'R': 'Clerical and sales',
        'C': 'Craftsmen and foremen',
        'O': 'Operatives',
        'H': 'Private household workers',
        'S': 'Service workers',
        'W': 'Farm laborers',
        'K': 'Keeping house',
        'L': 'Non-farm laborers',
        'U': 'Seeking work',
        'G': 'Students',
        }
RACE = {
        'W': 'Caucasian',
        'B': 'African-American',
        }

COMMUNITY_TYPE = {
        'R': 'Rural',
        'U': 'Urban',
        }

TARGET_TYPE = {
        'p': 'Phonetic',
        'g': 'Grammatical',
        'l': 'Lexical',
        }

# Response fields
GRAMFLAG = {
        'N': 'Noun',
        'V': 'Verb',
        'M': 'Pronoun',
        'C': 'Copula',
        'A': 'Adjective',
        'B': 'Adverb',
        'J': 'Conjunction',
        'P': 'Preposition',
        'X': 'Verb Auxiliary',
        'D': 'Determiner',
        'R': 'Relative pronoun',
        'T': 'Existential (there/it)',
        'S': 'Clause',
        'E': 'Verb phrase',
        'Q': 'Prepsitional phrase',
        'O': 'Noun phrase',
        'K': 'Modifier phrase',
        }



# For phonetics.

SUBSCRIPT = u'\u0317\u0323\u0325\u032c\u032f\u032a\u033a\u0331\u032b\u0329' \
            u'\u032e\u031e\u031d\u031f\u032d\u0318\u0319\u031c\u203f\u0327'
SUPERSCRIPT = u"\u030b\u0319\u0318\u0311\u030a\u0302\u0361'\u0307\u030c" \
              u"\u0300\u0306\u0304\u0308\u0301\u0303"
STRESS = u'^\u02b9\u02cb\u02c8\u02d8\u02cc\u02d5\u02d4\u02b2\u02c4\xb7' \
         u'\u02c2\u02c5\u02c3~'
REMOVENDA = SUBSCRIPT + SUPERSCRIPT + STRESS
re_remove = re.compile(u'[' + re.escape(REMOVENDA) + ']', re.UNICODE)


def simplify(unistring, regex=re_remove):
    """\
    This simplifies the phonetics by removing diacriticals and other characters.

    """

    return regex.sub('', unistring)


FIELD_WORKERS = {
        'L' : 'Guy Lowman',
        'M' : 'Raven McDavid',
        'P' : 'Lee Pederson',
        'S' : 'Student',
        'Rr': 'Grace Reuter',
        'U' : 'Gerald Udell',
        'Rt': 'Barbara Rutledge',
        'O' : "Raymond O'Cain",
        'B' : 'Bernard Bloch',
        'T' : 'Lorenzo Turner',
        }

WORK_SHEETS = {
        'S': 'South Atlantic',
        'M': 'Middle Atlantic',
        'P': 'Preliminary South Atlantic',
        'C': 'Combined',
        'E': 'New England',
        }

FIELD_DESCRIPTIONS = {
        # INFORMANTS
        'Informants.infid': 'Informant ID Number',
        'Informants.informid': 'Informant ID',
        'Informants.oldnumber': 'Old Informant ID',
        'Informants.auxiliary': 'Auxiliary Informant',
        'Informants.yearinterviewed': 'Year Interviewed',
        'Informants.inftype': 'Type of Informant',
        'Informants.generation': 'Generation',
        'Informants.cultivation': 'Cultivated',
        'Informants.sex': 'Sex',
        'Informants.age': 'Age',
        'Informants.education': 'Education',
        'Informants.occupation': 'Occupation',
        'Informants.race': 'Race',
        'Informants.latitude': 'Latitude',
        'Informants.longitude': 'Longitude',
        # COMMUNITIES
        'Communities.comid': 'Community ID',
        'Communities.code': 'Community code',
        'Communities.type': 'Type of Community',
        'Communities.name': 'Community Name',
        'Communities.state': 'State',
        'Communities.x': 'X Location on Map (in Pixels)',
        'Communities.y': 'Y Location on Map (in Pixels)',
        # FIELDWORKERS
        'FieldWorkers.fwid': 'Field Worker ID',
        'FieldWorkers.code': 'Field Worker Code',
        'FieldWorkers.name': 'Field Worker',
        # WORKSHEETS
        'WorkSheets.wsid': 'Work Sheet ID',
        'WorkSheets.code': 'Work Sheet Code',
        'WorkSheets.name': 'Work Sheet',
        # TARGETS
        'Targets.targetid': 'Target ID',
        'Targets.target': 'Target Item',
        'Targets.type': 'Type of data',
        'Targets.page': 'Page',
        'Targets.subpage': 'Subpage',
        'Targets.item': 'Item Number',
        'Targets.subitem': 'Subitem Number',
        'Targets.notes': 'Notes',
        # RESPONSE
        'Responses.item': 'Item',
        'Responses.gramflag': 'Grammatical Category',
        'Responses.doubtflag': 'Doubtful Response',
        'Responses.commenttext': 'Long Comments',
        'Responses.commentcodes': 'Comment Codes',
        'Responses.phonetic': 'Phonetic Transcription',
        'Responses.simplephone': 'Simplified Phonetic Transcription',
        'Responses.responseid': 'Response ID',
        }

FIELD_LENGTHS = {
        # INFORMANTS
        'Informants.infid': 5,
        'Informants.informid': 6,
        'Informants.oldnumber': 6,
        'Informants.auxiliary': 3,
        'Informants.yearinterviewed': 4,
        'Informants.inftype': 4,
        'Informants.generation': 3,
        'Informants.cultivation': 4,
        'Informants.sex': 3,
        'Informants.age': 3,
        'Informants.education': 2,
        'Informants.occupation': 3,
        'Informants.race': 4,
        'Informants.latitude': 16,
        'Informants.longitude': 16,
        # COMMUNITIES
        'Communities.comid': 5,
        'Communities.code': 6,
        'Communities.type': 4,
        'Communities.name': 10,
        'Communities.state': 2,
        'Communities.x': 4,
        'Communities.y': 4,
        # FIELDWORKERS
        'FieldWorkers.fwcode': 2,
        'FieldWorkers.name': 10,
        # WORKSHEETS
        'WorkSheets.wscode': 2,
        'WorkSheets.name': 10,
        # TARGETS
        'Targets.target': 10,
        'Targets.type': 1,
        'Targets.page': 4,
        'Targets.subpage': 4,
        'Targets.item': 4,
        'Targets.subitem': 4,
        'Targets.notes': 20,
        # RESPONSES
        'Responses.item': 20,
        'Responses.gramflag': 4,
        'Responses.doubtflag': 1,
        'Responses.commenttext': 20,
        'Responses.commentcodes': 20,
        'Responses.phonetic': 20,
        'Responses.simplephone': 20,
        'Responses.responseid': 6,
        }


