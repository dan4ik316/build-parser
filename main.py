import json
import plotly.graph_objects as go

def parse_json(file_name):
    f = open(file_name)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    substepsTitles = []
    substepsDurations = []
    for i in data['subSteps']:
        substepsTitles.append(i['title'])
        substepsDurations.append(i['duration'])

    print(substepsDurations)
    return substepsTitles, substepsDurations

    f.close()


def parse_specific_title(file_name, title):
    f = open(file_name)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    substepsTitles = []
    substepsDurations = []
    for i in data['subSteps']:
        if i['title'] == title:
            for j in i['subSteps']:
                substepsTitles.append(j['title'])
                substepsDurations.append(j['duration'])

    print(substepsDurations)
    return substepsTitles, substepsDurations

def parse_json_pd(file_name, arch_name):

    titles, durations = parse_json(file_name)

    dict_of_fig = dict({
        "data": [{"type": "bar",
                  "x": titles,
                  "y": durations}],
        "layout": {"title": {"text": "Главные фазы борки проекта с использованием архитектуры " + arch_name + ":"}}
    })

    fig = go.Figure(dict_of_fig)

    fig.show()

    for t in titles:
        # for t in titles:
        tt, td = parse_specific_title(file_name, t)
        dict_of_fig_t = dict({
            "data": [{"type": "bar",
                      "x": tt,
                      "y": td}],
            "layout": {"title": {"text": "Этап " + t + ":"}}
        })
        fig_t = go.Figure(dict_of_fig_t)

        fig_t.show()






if __name__ == '__main__':
    parse_json_pd('buildMVVM.json', 'MVVM')
    parse_json_pd('buildVIPER.json', 'VIPER')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
