from threading import Thread
import os

def run(mails):
    df_valid_domain = []

    class Ping(Thread):

        def __init__(self, mails):
            Thread.__init__(self)
            self.mails = mails

        def run(self):
            domain = self.mails.split("@")[1]

            response = os.system("ping -c 1 " + domain)

            if response == 1 or response == True:
                df_valid_domain.append(domain)
                return set(df_valid_domain)

    def validaremail(self):
        i = 0
        maximum = 10
        number_batch = 1
        batch_size = 5

        while (i <= maximum):

            lista_requests = []

            # Popula a lista

            items = mails[i + 1:i + batch_size]

            for item in items:
                lista_requests.append(Ping(item))

            # Envia o lote
            for item in lista_requests:
                item.start()

            # Verifica se todas as requisições terminaram
            try:
                while (True):
                    if (not lista_requests[0].isAlive()
                            and not lista_requests[1].isAlive()
                            and not lista_requests[2].isAlive()
                            and not lista_requests[3].isAlive()):
                        break
                    else:
                        continue
            except IndexError as ex:
                print(ex)

            i += batch_size
            number_batch += 1

    validaremail(mails)

    return df_valid_domain


mails = ['marib@gmail', 'joao@gmail.com', 'abc@targetdata.com.br', 'ybenson@yahoo.fr', 'ybenson509@yahoo.com',
         'ybenson509@hotmail.com','marib@gmail.com', 'joao@gmail.com', 'abc@targetdata.com.br', 'ybenson@yahoo.fr', 'ybenson509@yahoo.com',
         'ybenson509@hotmail.com']

print(run(mails))


