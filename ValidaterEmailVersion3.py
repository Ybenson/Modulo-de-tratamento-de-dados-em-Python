from validate_email import validate_email
import threading
import time


start = time.time()
def run(mails):

    df_valid_domain = []
    df_invalid_domain = []

    class Ping(threading.Thread):

        def __init__(self, mail):
            threading.Thread.__init__(self)
            self.mail = mail

        def run(self):
            response = validate_email(self.mail)
            if response == True:
                df_valid_domain.append(self.mail)

    def validaremail(self):

        i = 0
        l = 0
        maximum = 13500
        number_batch = 1
        batch_size = 50

        lista_domain = []

        for mail in mails:
            lista_domain.append(mail)

        while (i <= maximum):

            lista_requests = []

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
                            and not lista_requests[20].isAlive()
                            and not lista_requests[21].isAlive()
                            and not lista_requests[22].isAlive()
                            and not lista_requests[23].isAlive()
                            and not lista_requests[24].isAlive()
                            and not lista_requests[25].isAlive()
                            and not lista_requests[26].isAlive()
                            and not lista_requests[27].isAlive()
                            and not lista_requests[28].isAlive()
                            and not lista_requests[29].isAlive()
                            and not lista_requests[30].isAlive()
                            and not lista_requests[31].isAlive()
                            and not lista_requests[32].isAlive()
                            and not lista_requests[33].isAlive()
                            and not lista_requests[34].isAlive()
                            and not lista_requests[35].isAlive()
                            and not lista_requests[36].isAlive()
                            and not lista_requests[37].isAlive()
                            and not lista_requests[38].isAlive()
                            and not lista_requests[39].isAlive()
                            and not lista_requests[40].isAlive()
                            and not lista_requests[41].isAlive()
                            and not lista_requests[42].isAlive()
                            and not lista_requests[43].isAlive()
                            and not lista_requests[44].isAlive()
                            and not lista_requests[45].isAlive()
                            and not lista_requests[46].isAlive()
                            and not lista_requests[47].isAlive()
                            and not lista_requests[48].isAlive()
                            and not lista_requests[49].isAlive()
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
file_read = 'Modulo_DataLoad/LISTA_EMAILS_1000.TXT'
ref_arquivo = open(path + file_read, 'r')
mails = ref_arquivo.read().splitlines()

print(run(mails))
end = time.time()
print(end-start)

