import threading
import os
import time


start = time.time()
def run(mails):

    df_valid_domain = []

    class Ping(threading.Thread):

        def __init__(self, domain):
            threading.Thread.__init__(self)
            self.domain = domain

        def run(self):
            # to windows
            response = os.system("ping -n 1 -c1 -w1 " + self.domain)
            # to Linux
            #response = os.system("ping -c 1 " + self.domain)

            if response == 0:
                df_valid_domain.append(self.domain)

    def validaremail(self):

        i = 0
        l = 0
        maximum = 1020
        number_batch = 1
        batch_size = 20

        lista_domain = []

        for mail in mails:
            #mail = mail.rstrip('\n')
            if "@" in mail:
                domain = mail.split("@")[1]

                lista_domain.append(domain)

        while (i <= maximum):

            lista_requests = []

            lista_domain = list(set(lista_domain))

            items = lista_domain[l+1:l+batch_size]

            for item in items:
                lista_requests.append(Ping(item))

            # Envia o lote
            for item in lista_requests:
                item.start()

            # Verifica se todas as requisições terminaram
            try:
                while (True):
                    if ( not lista_requests[0].isAlive()
                            and not lista_requests[1].isAlive()
                            and not lista_requests[2].isAlive()
                            and not lista_requests[3].isAlive()
                            and not lista_requests[4].isAlive()
                            and not lista_requests[5].isAlive()
                            and not lista_requests[6].isAlive()
                            and not lista_requests[7].isAlive()
                            and not lista_requests[8].isAlive()
                            and not lista_requests[9].isAlive()
                            and not lista_requests[10].isAlive()
                            and not lista_requests[11].isAlive()
                            and not lista_requests[12].isAlive()
                            and not lista_requests[13].isAlive()
                            and not lista_requests[14].isAlive()
                            and not lista_requests[15].isAlive()
                            and not lista_requests[16].isAlive()
                            and not lista_requests[17].isAlive()
                            and not lista_requests[18].isAlive()
                            and not lista_requests[19].isAlive()


                    ):
                        break
                    else:
                        continue
            except IndexError as ex:
                print(ex)

            i += batch_size
            number_batch += 1

            print('Lote {} '.format(number_batch))
            print('batch_size: {}'.format(i))

    validaremail(mails)
    return df_valid_domain


path = 'C:/Users/ybenson.augustave/Desktop/'
file_read = 'Modulo_DataLoad/LISTA_EMAILS_10000.TXT'
ref_arquivo = open(path + file_read, 'r')
mails = ref_arquivo.read().splitlines()

print(run(mails))
end = time.time()
print(end-start)
