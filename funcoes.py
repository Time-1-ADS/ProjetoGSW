from flask import render_template


def projet(nome):
    if nome == 'albuquerque':
        return render_template('albuquerque.html')
    elif nome == 'batista':
        return render_template('batista.html')
    elif nome == 'carvalho':
        return render_template('carvalho.html')
    elif nome == 'costacomercio':
        return render_template('costacomercio.html')
    elif nome == 'costaltda':
        return render_template('costaltda.html')
    elif nome == 'melo':
        return render_template('melo.html')
    elif nome == 'pereira':
        return render_template('pereira.html')
    elif nome == 'santos':
        return render_template('santos.html')
    elif nome == 'souza':
        return render_template('souza.html')
    elif nome == 'xavier':
        return render_template('xavier.html')