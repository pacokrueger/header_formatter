import json
import pyperclip

class Headers_charles:

    def __init__(self, headers_charles: str):

        self.formatted = {}

        self.headers_raw = headers_charles

    def format_headers(self):

        headers_parsed = self.headers_raw.replace(':method', 'method').replace(':path', 'path').replace(':scheme', 'scheme').replace(':authority', 'authority')

        split = headers_parsed.split('\n')

        for element in split:
            splits = element.split('	')
            if splits[0] == 'cookie':
                pass
            elif splits[0] == 'path':
                self.formatted.update(
                    {splits[0]: '!='}
                )
            else:
                self.formatted.update(
                    {splits[0]: splits[1]}
                )

        print(f'Headers formatted: {self.formatted}')
        print('Copied to clipboard.')

        return pyperclip.copy(json.dumps(self.formatted, sort_keys=True, indent=4))

class Headers_chrome:

    def __init__(self, headers_chrome: str):

        self.headers_raw = headers_chrome

        self.formatted = {}

    def format_headers(self):

        headers_parsed = self.headers_raw.replace(':method', 'method').replace(':path', 'path').replace(':scheme','scheme').replace(':authority', 'authority')

        new_line_split = headers_parsed.split('\n')

        for element in new_line_split:
            splits = element.split(': ')
            if splits[0] == 'cookie':
                pass
            elif splits[0] == 'path':
                self.formatted.update(
                    {splits[0]: '!='}
                )
            else:
                self.formatted.update(
                    {splits[0]: splits[1]}
                )

        print(f'Headers formatted: {self.formatted}')
        print('Copied to clipboard.')

        pyperclip.copy(json.dumps(self.formatted, sort_keys=True, indent=4))