import calendar
from model.entity.datas import Datas
import locale


# Seleciona localização, língua
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Coloca primeira letra em maiúsculo
calendar.month_name = [m.capitalize() for m in calendar.month_name]
calendar.month_abbr = [m.capitalize() for m in calendar.month_abbr]
calendar.day_abbr = [d.capitalize() for d in calendar.day_abbr]

class CustomHTMLCal(calendar.HTMLCalendar):   
    
   
    #cssclasses = [style + "" for style in calendar.HTMLCalendar.cssclasses]
    #cssclass_month_head = "text-center month-head"
    #cssclass_month = "text-center month table"
    #cssclass_year = "text-italic lead"


    cssclass_month_head = "header_title"
    cssclasses = [style + " day-number" for style in calendar.HTMLCalendar.cssclasses]

    def formatmonth(self, year, month):
        self.data = Datas()
        
        self.year, self.month,self.datas_reservadas = year, month,self.data.get_Datas_Reservadas()
        
        v = []
        a = v.append
        a('<div border="0" cellpadding="0" cellspacing="0" class="calendar month">' )
        a(self.formatmonthname(year, month, 1))
        a(self.formatweekheader())
        for week in self.monthdays2calendar(year, month):
            a(self.formatweek(week))
        a('</div>')
        return ''.join(v)
    
    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name, formatted for the calendar heading.
        """
        if withyear:
            return '<div colspan="7" class="header month"><h1 class="header_title">%s</h1><p class="header_subtitle"> %i </p></div>' % (calendar.month_name[themonth],theyear)
        return '<div colspan="7" class="header month"><h1 class="header_title">%s</h1></div>' % (calendar.month_name[themonth])
    

    def formatweekheader(self):
        """
        Return a header for a week.
        """
        header = '<div class="days-of-week">'
        for weekday,day in enumerate(self.iterweekdays()):
            # Adicione a classe "day-name" a cada elemento do cabeçalho da semana
            header += '<div class="day-name %s">%s</div>' % (self.cssclasses_weekday_head[day], calendar.day_abbr[day] )
        header += '</div>'
        return header
    
    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        
        # Personalize a saída da semana conforme necessário
        s = '<div class="week days">' + s + '</div>'
        
        return s

    
                                       
    def formatday(self, day, weekday):                                
        
        for data_reservada in self.datas_reservadas:
            if day == data_reservada.day and self.month == data_reservada.month and self.year == data_reservada.year:
                return '<div class="%s day-reserved">%d</div>' % (self.cssclasses[weekday], day)
                
        # Adicione a classe "hoje" ao dia de hoje
        if day == self.data.dia and self.month == self.data.mes and self.year == self.data.ano:
            return '<div class="%s day-today">%d</div>' % (self.cssclasses[weekday], day)
        
                                           
        else:
            #Os dias que não existem nesse mês.
            if day == 0:
                return '<div class="%s noday day-number_disabled"></div>' % (self.cssclasses[weekday])
            elif day > self.data.dia:
                #Os dias livres para reserva.
                return '<div class="%s"><a href="https://wa.me/send/?phone=5521994280064&text=oi gostaria de reservar o dia'"%d"'&type=phone_number&app_absent=0">%d</a></div>' % (self.cssclasses[weekday], day,day)
            else:
                return '<div class="%s">%d</div>' % (self.cssclasses[weekday], day)

   
        