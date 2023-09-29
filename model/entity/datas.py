from datetime import datetime
from datetime import date


class Datas():
    def __init__(self) -> None:
        self.mes = datetime.now().date().month
        self.ano = datetime.now().date().year
        self.mes_contador_calendario = datetime.now().date().month
        self.ano_contador_calendario = datetime.now().date().year
        self.dia = datetime.now().date().day
       

    def get_Datas_Reservadas(self):
        data1 = date(2023,10,11)
        data2 = date(2023,9,23)
        data3 = date(2023,9,10)
        data4 = date(2023,10,29)

        datas_reservadas = data1,data2,data3,data4
        return datas_reservadas