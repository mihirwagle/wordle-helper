from enums import Result
from filter import filter_words
from flask import Flask, jsonify, request

words = [word.replace("\r", "").replace("\n", "").upper() for word in open("word-list.txt").readlines()]
app = Flask("WordleHelper")

def build_results(color):
    # Build results enum using colors
    results = []
    for char in color:
        match char:
            case "G": results.append(Result.Green)
            case "Y": results.append(Result.Yellow)
            case _: results.append(Result.Gray)
    return results

@app.route('/first', methods = ['POST'])
def first():
    try:
        data = request.get_json(force=True)
        word = data['word'].upper()
        color = data['color'].upper()
        results = build_results(color)
        word_list = filter_words(word, results, words)
        return jsonify({"words":word_list})
    except Exception as e:
        return 'Request has to be a post request with JSON body {"word": ..., "color": ..., "words": ...}', 400

@app.route('/subsequent', methods = ['POST'])
def subsequent():
    try:
        data = request.get_json(force=True)
        word = data['word'].upper()
        color = data['color'].upper()
        word_list = data['words']
        results = build_results(color)
        word_list = filter_words(word, results, word_list)
        return jsonify({"words":word_list})
    except Exception as e:
        return 'Request has to be a post request with JSON body {"word": ..., "color": ..., "words": ...}', 400

app.run("0.0.0.0")