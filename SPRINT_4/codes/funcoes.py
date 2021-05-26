from flask import render_template


def projet(nome):
    if nome == 'albuquerque':
        return render_template('albdash.html')
    elif nome == 'batista':
        return render_template('batdash.html')
    elif nome == 'carvalho':
        return render_template('cardash.html')
    elif nome == 'costacomercio':
        return render_template('coscdash.html')
    elif nome == 'costaltda':
        return render_template('cosldash.html')
    elif nome == 'melo':
        return render_template('meldash.html')
    elif nome == 'pereira':
        return render_template('perdash.html')
    elif nome == 'santos':
        return render_template('sandash.html')
    elif nome == 'souza':
        return render_template('soudash.html')
    elif nome == 'xavier':
        return render_template('xavdash.html')