from flask import render_template
from app import app
from model.custon_HTMLCal import CustomHTMLCal
from model.entity.datas import Datas
import calendar

   

agora = Datas()
@app.route('/calendario')
def calendario():
    
    # Cria o arquivo calendario.html em utf_8
    cal = open('view/templates/calendario.html', 'w', encoding='UTF-8')
    c = CustomHTMLCal(calendar.SUNDAY)
    
    cal.write(c.formatmonth(agora.ano,agora.mes))

    cal.close()
    return render_template('calendario.html')





        
    

    



