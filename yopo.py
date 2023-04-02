from flask import Flask, render_template
app = Flask(__name__)


import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

song_list = convert_to_dict('yopo.csv')

pairs_list = []
for song in song_list:
    pairs_list.append( (song['id'], song['song_name']) )


@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

@app.route('/song/<num>')
def song(num):
    s = song_list[int(num)-1]
    return render_template('yopo.html', s=s)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=4999, debug=True)
