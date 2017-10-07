#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import BasePlugin
import logging

logger = logging.getLogger(__name__)


class TroutPlugin(BasePlugin):
    '''TroutPlugin offers one command to slap users with trouts.

    Examples:
        user | ~trout otheruser
        ---> | qbot slaps otheruser around a bit with a large trout

    Available commands:
        ~trout <string>
            slap <string> with trout. <string> can be a user or any other
            single word
    '''

    def __init__(self, **kwargs):
        logger.info('Creating trout plugin instance')
        self.regex_mappings = {
            r'~trout\s(\w+).*': self.trout,
        }

    def trout(self, match):
        victim = match.group(1)
        logger.debug(f'Slapping {victim} with trout')
        return f'ACTION slaps {victim} around a bit with a large trout'
