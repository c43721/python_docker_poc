from json import load, dumps, JSONDecodeError

class SettingsService:
    def __init__(self):
        self.settings = self.get_settings()

    def get_settings(self):
        """
            Returns the settings.json file as a dict
            Will return an empty dict if the file is not found, or if the json was invalid
        """

        if self.settings is not None:
            return self.settings

        try:
            with open('settings.json', 'r') as f:
                settings = load(f)

                self.settings = settings

                return settings 
        except FileNotFoundError:
            return dict()
        except JSONDecodeError:
            return dict()

    def write_settings(self, new_settings: dict):
        """
            Writes the new settings to the settings.json file   
        """

        self.settings = new_settings

        # TODO: Resiliance with JSON structure (probably ensure that all callers enforce strict JSON structure) 
        with open('settings.json', 'w') as f:
            f.write(dumps(new_settings))
