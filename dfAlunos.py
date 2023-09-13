import pandas as pd
from flask import Flask, jsonify


dados_alunos = {
    'Nome': ['João Alberto', 'Ana Maria', 'Pedro Paulo', 'Ana Carolina', 'Luiza Silva'],
    'Idade': [15, 16, 15, 17, 16],
    'Série': ['9º ano', '5º ano', '9º ano', '8º ano', '7º ano'],
    'Nota_Matematica_1': [8.5, 7.2, 9.0, 6.5, 8.8],
    'Nota_Matematica_2': [7.5, 8.0, 6.0, 7.2, 7.9],
    'Nota_Portugues_1': [7.8, 8.0, 7.5, 8.2, 7.0],
    'Nota_Portugues_2': [8.2, 7.5, 8.0, 7.8, 8.3],
    'Nota_Historia_1': [7.0, 6.5, 7.8, 6.2, 7.5],
    'Nota_Historia_2': [6.8, 7.2, 6.5, 7.0, 7.4],
    'Nota_Quimica_1': [8.0, 7.5, 8.5, 7.2, 7.8],
    'Nota_Quimica_2': [7.2, 8.0, 7.6, 8.3, 8.1],
    'Nota_Fisica_1': [7.5, 8.2, 7.0, 7.8, 8.4],
    'Nota_Fisica_2': [7.0, 7.8, 7.2, 7.5, 8.0],
    'Nota_Geografia_1': [6.8, 7.0, 6.5, 7.2, 7.1],
    'Nota_Geografia_2': [7.2, 6.8, 7.0, 6.5, 7.3]
}


df_alunos = pd.DataFrame(dados_alunos)
df_alunos['Media_Matematica'] = (df_alunos['Nota_Matematica_1'] + df_alunos['Nota_Matematica_2']) / 2
df_alunos['Media_Portugues'] = (df_alunos['Nota_Portugues_1'] + df_alunos['Nota_Portugues_2']) / 2
df_alunos['Media_Historia'] = (df_alunos['Nota_Historia_1'] + df_alunos['Nota_Historia_2']) / 2
df_alunos['Media_Quimica'] = (df_alunos['Nota_Quimica_1'] + df_alunos['Nota_Quimica_2']) / 2
df_alunos['Media_Fisica'] = (df_alunos['Nota_Fisica_1'] + df_alunos['Nota_Fisica_2']) / 2
df_alunos['Media_Geografia'] = (df_alunos['Nota_Geografia_1'] + df_alunos['Nota_Geografia_2']) / 2


df_alunos['Media_Geral'] = (df_alunos['Media_Matematica'] + df_alunos['Media_Portugues'] +
                            df_alunos['Media_Historia'] + df_alunos['Media_Quimica'] +
                            df_alunos['Media_Fisica'] + df_alunos['Media_Geografia']) / 6


df_alunos['Status'] = df_alunos['Media_Geral'].apply(lambda x: 'Aprovado' if x >= 7 else 'Reprovado')


df_alunos.to_json('alunos_com_notas.json', orient='records', lines=True)


dados_alunos = df_alunos[['Nome', 'Série', 'Media_Geral', 'Status']]

app = Flask(__name__)

@app.route('/alunos', methods=['GET'])
def obter_alunos():
    dados_alunos = df_alunos[['Nome', 'Media_Geral', 'Status']]
   
    alunos_json = dados_alunos.to_dict(orient='records')
    return jsonify(alunos_json)

if __name__ == '__main__':
    app.run(debug=True)

