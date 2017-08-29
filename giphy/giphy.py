from errbot import BotPlugin, botcmd

import requests
import random


class Giphy(BotPlugin):

    def get_configuration_template(self):
        """ configuration entries """
        config = {
            'api_key': '',
        }
        return config

    def _check_config(self, option):

        # if no config, return nothing
        if self.config is None:
            return None
        else:
            # now, let's validate the key
            if option in self.config:
                return self.config[option]
            else:
                return None

    def _get_api_key(self):
        return self._check_config('api_key') or 'dc6zaTOxFJmzC'

    @botcmd
    def giphy(self, msg, args):
        """ Return a gif based on search
            Example:
            !giphy funny cats
            !giphy dance
        """

        api_key = self._get_api_key()
        gif_size = 'original'
        max_image_size = 8000000

        params = {
            'q': args,
            'limit': 20,
            'api_key': api_key,
        }

        r = requests.get('http://api.giphy.com/v1/gifs/search', params=params)
        self.log.debug('url sent: {}'.format(r.url))

        results = r.json()
        results_count = len(results['data'])
        self.log.debug('results found: {}'.format(results_count))

        if results_count != 0:
            response = None
            while response is None:
                image_number = random.randrange(0, results_count)
                image_size = int(results['data'][image_number]['images'][gif_size]['size'])
                # Restricting to max size limit
                if image_size < max_image_size:
                    response = results['data'][image_number]['images'][gif_size]['url']
        else:
            response = 'No results found.'

        return response

    @botcmd
    def giphy_ids(self, msg, args):
        """ Return a gif based on ids
            Example:
            !giphy ids 7rzbxdu0ZEXLy
            !giphy ids feqkVgjJpYtjy,7rzbxdu0ZEXLy
        """

        api_key = self._get_api_key()
        gif_size = 'original'
        response = ''

        params = {
            'api_key': api_key,
            'ids': args,
        }

        r = requests.get('http://api.giphy.com/v1/gifs', params=params)
        self.log.debug('url sent: {}'.format(r.url))

        results = r.json()
        results_count = len(results['data'])

        if results_count != 0:
            for image in range(0, results_count):
                response += '{} '.format(results['data'][image]['images'][gif_size]['url'])
        else:
            response = 'No results found.'

        return response
