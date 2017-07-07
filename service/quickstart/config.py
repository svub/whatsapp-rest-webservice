import ConfigParser
import os


class Config:
    defaults = {}
    # load example.conf for defaults and overwrite if a real config has been created.
    configfiles = ['whatsapp.example.conf', 'service/whatsapp.example.conf', 'whatsapp.conf', 'service/whatsapp.conf']
    config=None

    @classmethod
    def get(self, section, value):
        if not self.config:
            # load configuration file once
            self.config = ConfigParser.RawConfigParser(self.defaults);
            self.config.read(self.configfiles)

            print('Loading WhatsApp configuration.')
            print('phone number='+self.config.get('credentials', 'phone'))
            print('password='+self.config.get('credentials', 'password'))

        return self.config.get(section, value)
