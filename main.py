from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # selected_member = request.form["memberselect"]
    member_list = ["Barnabás Tóth", "Kristóf Szabó", "Péter Ormai", "Helga Kalicz"]
    title = "Cödermeisters"
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        filelist = [item.split(',') for item in data_list]
    return render_template('index.html', member_list=member_list, title=title, filelist=filelist)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
