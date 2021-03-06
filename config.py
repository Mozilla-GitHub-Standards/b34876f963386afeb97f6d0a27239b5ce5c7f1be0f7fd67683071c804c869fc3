# Environment loading borrowed from
# https://github.com/marchibbins/teela/blob/9d65abaff804f9a79483529ed194581feafdd745/teela/config.py

import os
from enum import Enum

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def env_var(key, default=None):
    """ Parse environment variable """

    val = os.getenv(key, default)

    if val == 'True':
        val = True
    elif val == 'False':
        val = False

    return val


class ReturnCodes(Enum):
    PERMANENT = 301
    TEMPORARY = 307


class Config(object):
    """
    Configure the application with environment variables
    """

    DEBUG = env_var('DEBUG', default=False)
    FORCE_SSL = env_var('FORCE_SSL', default=False)

    # Redirect Rules
    # The key is the host header to match
    # At [0]: the redirect target, without trailing slash
    # At [1]: the HTTP status code to return - use the ReturnCodes enum
    # At [2]: a Tuple, indicating if the path and query are to be preserved ( {path}, {query} )
    REDIRECT_RULES = {
        'mofo-redirector.herokuapp.com': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (True, True),
        ),
        'chat.mozillafoundation.org': (
            'https://mozfest.slack.com',
            ReturnCodes.PERMANENT,
            (False, False),
        ),
        'www.hivelearningnetwork.org': (
            'https://foundation.mozilla.org/get-involved',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'hivelearningnetwork.org': (
            'https://foundation.mozilla.org/get-involved',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'www.hivelearningnetworks.org': (
            'https://foundation.mozilla.org/get-involved',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'hivelearningnetworks.org': (
            'https://foundation.mozilla.org/get-involved',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'validator.openbadges.org': (
            'https://openbadgesvalidator.imsglobal.org',
            ReturnCodes.PERMANENT,
            (True, True)
        ),
        'indicators.internethealthreport.org': (
            'https://internethealthreport.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'www.typeoutloud.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'science.typeoutloud.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'www.responsiblecs.org': (
            'https://foundation.mozilla.org/initiatives/responsible-cs/',
            ReturnCodes.TEMPORARY,
            (False, True)
        ),
        'www.responsiblecschallenge.org': (
            'https://foundation.mozilla.org/initiatives/responsible-cs/',
            ReturnCodes.TEMPORARY,
            (False, True)
        ),
        'www.iheartopendata.org': (
            'https://foundation.mozilla.org/campaigns/i-heart-open-data/',
            ReturnCodes.TEMPORARY,
            (False, True)
        ),
        'fbsurvey.mozillafoundation.org': (
            'https://github.com/mozilla/shinysurvey/',
            ReturnCodes.TEMPORARY,
            (False, True)
        ),
        'app.mozillafestival.org': (
            'https://guidebook.com/guide/147793/',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'forum.learning.mozilla.org': (
            'https://discourse.mozilla.org/',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'discourse.mozilla-advocacy.org': (
            'https://discourse.mozilla.org/',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'forum.mozillascience.org': (
            'https://discourse.mozilla.org/',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'popcorn.webmaker.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'postcrimes.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'www.postcrimes.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'mozillapopcorn.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'www.mozillapopcorn.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'maker.mozillapopcorn.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'static.mozillapopcorn.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
        'tedglobal.mozillapopcorn.org': (
            'https://foundation.mozilla.org',
            ReturnCodes.TEMPORARY,
            (False, False)
        ),
    }
