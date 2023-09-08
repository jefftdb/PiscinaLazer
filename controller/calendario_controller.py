from flask import render_template
from app import app
import calendar
import locale
from datetime import datetime



class CustomHTMLCal(calendar.HTMLCalendar):
    #cssclasses = [style + "" for style in calendar.HTMLCalendar.cssclasses]
    #cssclass_month_head = "text-center month-head"
    #cssclass_month = "text-center month table"
    #cssclass_year = "text-italic lead"

    
    cssclass_month = "table month"
                                   
    def formatday(self, day, weekday):
                        
        hoje = datetime.now().date()
        reserva1 = datetime(2023,7,3)
        reserva2 = datetime(2023,8,27) 
        reserva3 = datetime(2023,7,20) 
        reserva4 = datetime(2023,7,26)         
        dias_reservados = [reserva1,reserva2,reserva3,reserva4]

        for i in dias_reservados:
            if day == i.day and day >= hoje.day and i.month == hoje.month :
                 return '<td class="%s reservada">%d</td>' % (self.cssclasses[weekday], day)
        
        # Adicione a classe "hoje" ao dia de hoje
        if hoje.day == day and hoje.month == hoje_DataTime.month:
            return '<td class="%s hoje">%d</td>' % (self.cssclasses[weekday], day)
        
                                           
        else:
            #Os dias que não existem nesse mês.
            if day == 0:
                return '<td class="%s noday"></td>' % (self.cssclasses[weekday])
            elif day > hoje.day:
                #Os dias livres para reserva.
                return '<td class="%s"><a href="https://wa.me/send/?phone=5521994280064&text=oi gostaria de reservar o dia'"%d"'&type=phone_number&app_absent=0">%d</a></td>' % (self.cssclasses[weekday], day,day)
            else:
                return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

      

            
                        
        


# Seleciona localização, língua
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Coloca primeira letra em maiúsculo

calendar.month_name = [m.capitalize() for m in calendar.month_name]
calendar.month_abbr = [m.capitalize() for m in calendar.month_abbr]
calendar.day_abbr = [d.capitalize() for d in calendar.day_abbr]

hoje_DataTime = datetime.now()

@app.route('/calendario/<mes>')
def calendario(mes): 
    if mes == '<mes>':
        mes = hoje_DataTime.month
        # Cria o arquivo calendario.html em utf_8
        cal = open('view/templates/calendario.html', 'w', encoding='UTF-8')
        c = CustomHTMLCal(calendar.SUNDAY)
        
        cal.write(c.formatmonth(hoje_DataTime.year,mes))

        cal.close()
        return render_template('calendario.html', mes = mes)
    else:
        
        # Cria o arquivo calendario.html em utf_8
        cal = open('view/templates/calendario.html', 'w', encoding='UTF-8')
        c = CustomHTMLCal(calendar.SUNDAY)
        mes = int(mes)
        mes+=1

        cal.write(c.formatmonth(hoje_DataTime.year,mes))

        cal.close()
        return render_template('calendario.html', mes = mes)
        
    

    



