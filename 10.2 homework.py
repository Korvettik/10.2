from flask import Flask
import json

app = Flask(__name__)


def load_json():
    """Функция загружает список словарей с кандидатами из json файла"""
    with open('candidates.json', 'r', encoding='utf-8') as json_file:
        cand_list = json.load(json_file)
    return cand_list


candidat_list = load_json()


@app.route('/', methods=['GET', 'POST'])  # главная страница, выводящая список json
def page_general():
    printing_list = list()
    for candidat in candidat_list:
        cand_name = candidat['name']
        cand_pos = candidat['position']
        cand_skills = candidat['skills']

        printing_list.append(f'Имя кандидата - {cand_name}')
        printing_list.append(f'Позиция кандидата {cand_pos}')
        printing_list.append(f'{cand_skills}')
        printing_list.append(' ')

    return '<pre>'+ '\n'.join(printing_list)+'<pre>'


@app.route('/candidate/<int:x>/', methods=['GET', 'POST'])  # страница, выводящая конкретного кандидата по его id
def page_candidate_x(x):
    printing_list = list()
    for candidat in candidat_list:
        if candidat['id'] == x:
            cand_pic = candidat['picture']
            cand_name = candidat['name']
            cand_pos = candidat['position']
            cand_skills = candidat['skills']

            printing_list.append(f'Имя кандидата - {cand_name}')
            printing_list.append(f'Позиция кандидата {cand_pos}')
            printing_list.append(f'{cand_skills}')
            printing_list.append(' ')

    return '<img src=cand_pic>'+ '<pre>'+ '\n'.join(printing_list[1:])+'<pre>'


@app.route('/skill/<skill>/', methods=['GET', 'POST'])  # страница, выводящая список кандидатов, у которых содержится конкретный навык
def page_candidate_skill(skill):
    printing_list = list()
    for candidat in candidat_list:
        if skill in candidat['skills'].lower().split(', '):  # не учитываем регистр
            cand_name = candidat['name']
            cand_pos = candidat['position']
            cand_skills = candidat['skills']

            printing_list.append(f'Имя кандидата - {cand_name}')
            printing_list.append(f'Позиция кандидата {cand_pos}')
            printing_list.append(f'{cand_skills}')
            printing_list.append(' ')

    return '<pre>'+ '\n'.join(printing_list)+'<pre>'


if __name__ == '__main__':
    app.run(debug=True)
