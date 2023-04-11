import pickle
import pandas as pd
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann


# Carregando o modelo salvo
model = pickle.load(open('C:\\Users\\raquel\\Documents\\Comunidade DS\\repos\\05-DS-emProducao\\rossmann_store_sales\\model\\model_rossmann.pkl', 'rb'))



# Inicializando a API
app = Flask(__name__)

# Definindo a rota e o método POST para a função de predição
@app.route('/rossmann/predict', methods=['POST'])

def rossmann_predict():
    # Obtendo os dados em formato JSON
    test_json = request.get_json()

    # Verificando se há dados presentes
    if test_json:
        # Se houver apenas um exemplo
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        # Se houverem múltiplos exemplos
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instanciando a classe Rossmann
        pipeline = Rossmann()

        # Realizando a limpeza dos dados
        df1 = pipeline.data_cleaning(test_raw)

        # Realizando a engenharia de features
        df2 = pipeline.feature_engineering(df1)

        # Preparando os dados
        df3 = pipeline.data_preparation(df2)

        # Realizando a predição
        df_response = pipeline.get_prediction(model=model, original_data=test_raw, test_data=df3)
        # Retornando os resultados em formato JSON
        return df_response

    else:
        # Caso não hajam dados presentes, retornando um JSON vazio com código 200
        return Response('{}', status=200, mimetype='application/json')

# Iniciando a aplicação
if __name__ == '__main__':
    app.run('0.0.0.0')
