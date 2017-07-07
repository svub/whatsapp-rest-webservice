from subprocess import Popen, PIPE
from config import Config

class WhatsApp:

    """
    The WhatsApp AP Interface
    """

    # for the time being, only one account can be actived and run at the same time
    # no need for loading account's data from the DB for now
    #origin = '4917667020717'
    #password = 'NPpELYnv4y50CJDnhfKxcZZwb38='
    origin = Config.get('credentials', 'phone')
    password = Config.get('credentials', 'password')

    # send a message to WhatsApp via CLI
    # Example: yowsup-cli demos --login 4917667020717:NPpELYnv4y50CJDnhfKxcZZwb38= --env s40 --send 4917610407181 "Hello World d1"
    send_command = 'yowsup-cli demos --login {}:{} --env s40 --send {} "{}"'

    @classmethod
    def send(cls, target, body):
        rc, output = cls.run(cls.send_command, [cls.origin, cls.password, target, body]);
        return rc == 0

    @classmethod
    def run(cls, command, parameters):
        print('WhatsApp.run')
        print(command)
        print(parameters)
        formatted = command.format(*parameters)
        print('> run: ' + formatted)
        p = Popen(formatted, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        rc = p.returncode
        if rc > 0:
            print('Error occured running command '+formatted)
            print(rc)
            print(output)
            print(err)
        else:
            print('Successful executed command '+formatted)
            print(output)

        return [rc, output]

