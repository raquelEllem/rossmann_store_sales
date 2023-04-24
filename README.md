  

# Rossmann Sales Prediction Project <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/rossmann.gif" alt="logo" style="width: 150px;">  


## 1. Problema de Negócio

Prever a demanda ou vendas de produtos em um período específico de tempo é um problema crucial enfrentado pela Rossmann, uma das maiores redes de farmácias na Europa. Uma previsão de vendas precisa poderia ajudar a reduzir estoques e desperdícios, além de garantir a disponibilidade dos produtos nas lojas. Em uma empresa grande como a Rossmann, qualquer variação na demanda poderia ter um impacto em todas as suas lojas, tornando a previsão de vendas ainda mais crítica.

Para enfrentar esse desafio, a Rossmann organizou uma competição na plataforma Kaggle em 2015 para prever as vendas diárias de cada uma de suas 3.000 lojas em vários países para até seis semanas no futuro. O conjunto de dados da competição incluía vendas de 1.115 lojas de 2013 até meados de 2015, juntamente com outros fatores como feriados, promoções e concorrência.

Neste projeto, o desafio é inspirado na realidade da Rossmann, uma das maiores redes de drogarias da Europa, onde como cientista de dados, você é responsável por criar uma solução para a previsão de vendas das lojas da Rossmann para as próximas seis semanas. Essa necessidade surgiu quando o CFO da empresa solicitou aos gerentes de loja que fornecessem uma previsão de vendas para o final do mês, visando estimar a quantia de dinheiro necessária para a expansão da empresa.

Após conversar com o CFO, você compreendeu a importância da previsão de vendas para o sucesso da expansão da empresa no prazo de seis semanas. Por isso, propôs uma solução inovadora que permitirá que qualquer gerente de loja acesse, a qualquer momento, uma previsão instantânea de vendas para suas respectivas lojas. Para atender a essa necessidade, serão utilizadas técnicas avançadas de análise de dados e aprendizado de máquina, a fim de extrair insights relevantes dos dados históricos de vendas, dados de promoção, informações demográficas da região, clima e outros fatores externos que possam afetar as vendas. Além disso, também será criada uma interface amigável para a solução, garantindo que os gerentes de loja possam utilizá-la facilmente em outras ocasiões.
| Problema | Objetivo                | Questão principal                                             |
| --------| ------------------- | ------------------------------------------------------------- |
| Qual é a quantidade de dinheiro que a empresa precisa tomar emprestado? | Expansão da empresa | Qual será a quantidade de vendas diárias em cada loja para as próximas seis semanas? |


## 2. Premissas assumidas para a análise

Para realizar a análise e construir o modelo de previsão de vendas, foram feitas algumas premissas com o objetivo de lidar com as limitações dos dados e garantir a consistência dos resultados:

-   Lojas que não possuem informações sobre a distância de seus concorrentes serão consideradas como não tendo concorrentes próximos. Portanto, uma distância muito alta será considerada como relevante.
-   Algumas lojas têm concorrentes próximos, mas não possuem informações sobre a concorrência desde determinado mês/ano. Nesse caso, consideraremos a data de instalação do novo concorrente como a data de início da competição.
-   A mesma consideração acima será aplicada para as colunas promo2_since_week/year.
-   Foram removidos do conjunto de dados os dias em que as vendas foram iguais a 0 ou as lojas estavam fechadas, uma vez que esses dados não são relevantes para a análise de previsão de vendas.
-   Os dados dos clientes foram removidos do conjunto de dados, pois eles não estão disponíveis no momento da previsão e não são relevantes para a análise de previsão de vendas.

## 3. Estratégia da solução

### 3.1 Produto Final
O produto final deste projeto consiste em um relatório em formato CSV contendo as previsões de vendas diárias de cada loja da empresa, bem como os valores do melhor e pior cenário, MAE (Erro Absoluto Médio) e MAPE (Erro Percentual Absoluto Médio). Além disso, foi desenvolvido um bot no Telegram que permite o acesso às informações de previsão de vendas por meio de uma API.


### 3.2 Ferramentas utilizadas
Para o desenvolvimento deste projeto, foram utilizadas as seguintes ferramentas:

- Python: uma linguagem de programação popular e poderosa usada para desenvolver aplicativos de ciência de dados e aprendizado de máquina.

- Visual Studio Code: um editor de código-fonte que fornece recursos avançados para desenvolvimento, como depuração, controle de versão e integração com várias extensões.

- Anaconda: uma plataforma de ciência de dados que contém várias bibliotecas e ferramentas importantes para análise de dados.

- Render: uma plataforma de hospedagem na nuvem que oferece suporte a várias linguagens e estruturas, incluindo Python e Flask.

- Telegram: um aplicativo de mensagens instantâneas que oferece uma API para criar bots e integrá-los a outras plataformas.

- Git: um sistema de controle de versão amplamente utilizado para gerenciar alterações em arquivos de código-fonte.

- API Flask: um micro-framework web usado para criar aplicativos da web em Python.

### 3.3 Desenvolvimento 
Este projeto adotou a metodologia CRISP-DM (Cross Industry Process - Data Mining), desenvolvida por um consórcio de mais de 200 organizações interessadas em mineração de dados. O processo é amplamente utilizado como padrão de processo analítico desde 1999 e é flexível para se adequar a muitos métodos analíticos, incluindo Data Science. Embora a versão original seja composta por seis fases, neste projeto, foi utilizada uma versão estendida com dez fases.

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/ciclo_crisp.jpg" alt="Ciclo do CRISP" width="600" height="300">
</p>



 - **Passo 01:** Descrição dos dados: Nesta fase, foi realizada uma análise minuciosa dos dados de vendas de cada loja, com o objetivo de identificar e corrigir possíveis erros e comportamentos incomuns. Para isso, foram adotadas diversas técnicas, incluindo a renomeação das colunas para o formato snakecase, a modificação dos tipos de dados de algumas colunas, e a verificação de dados faltantes (NaN), que foram tratados com técnicas de imputação, como a substituição por valores extremos. Além disso, foi criado um dicionário que associa o mês ao nome do mês, o que permitiu a tradução dos valores da coluna promo_interval para o formato de texto. Por fim, foram utilizadas estatísticas descritivas para entender a distribuição das vendas, tanto para atributos numéricos quanto categóricos, o que permitiu identificar possíveis padrões e tendências nos dados.
                                    
 - **Passo 02:** Feature engineering: Nesta fase, foram criadas hipóteses a partir da visão da loja, do produto e do tempo, que foram organizadas em um mapa mental. A lista final de hipóteses contém 12 itens que serviram como base para a criação de novos atributos. Foram realizadas transformações no DataFrame com o objetivo de criar novas colunas que representam informações relevantes a partir de outras colunas já existentes. Essas novas colunas foram utilizadas posteriormente para treinar os modelos de Machine Learning.
 
 - **Passo 03:** Filtragem de variáveis: Durante essa fase, algumas colunas e linhas de dados irrelevantes ou ausentes em algumas lojas foram removidas para o modelo. As lojas fechadas e aquelas sem vendas registradas foram excluídas. Adicionalmente, as colunas "customers", "open", "promo_interval" e "month_map" foram desconsideradas para o modelo.
 
 - **Passo 04:** Análise exploratória de dados: Nesta fase, foi realizada uma análise minuciosa dos dados para extrair insights importantes sobre o comportamento das vendas em cada loja. Foram realizadas análises univariadas dos atributos numéricos e categóricos, bem como das vendas. Além disso, foram feitas análises bivariadas para validar cada uma das hipóteses propostas, sendo que gráficos foram utilizados para facilitar a visualização dos resultados.
Foi apresentado um resumo das hipóteses propostas, juntamente com a conclusão obtida e a relevância de cada hipótese. Também foram realizadas análises multivariadas dos atributos numéricos e categóricos para compreender melhor as relações entre as variáveis. 


- **Passo 05:** Preparação dos dados: Nesta fase, os dados foram preparados para que os modelos de Machine Learning pudessem aprender o comportamento específico dos dados. Foram realizadas transformações como rescaling usando os métodos RobustScaler() e MinMaxScaler(), já que não foram encontrados gráficos com distribuição normal entre as variáveis. Esses objetos foram salvos em formato pickle para uso futuro. Também foi feita a transformação usando encoding para as colunas state_holiday, store_type e assortment. Além disso, foi adicionado colunas com o seno e cosseno dos dias da semana, meses, dias e semana do ano, já que se tratam de dados cíclicos.


 - **Passo 06:** Seleção de features: Nesta etapa, foram selecionados os atributos mais significativos para treinar o modelo. Para isso, foram removidas colunas irrelevantes e os dados foram divididos em conjuntos de treinamento e teste. Adicionalmente, utilizou-se o método Boruta para identificar as features mais relevantes para o modelo.  
  
  
- **Passo 07:** Modelagem de Machine Learning: Diferentes modelos de Machine Learning foram testados, incluindo regressão linear, Lasso, Random Forest e XGBoost. Foi aplicada a técnica de cross-validation para avaliar o desempenho real de cada modelo. Para cada modelo, foram selecionadas as colunas de treinamento e teste que foram escolhidas pelo algoritmo Boruta. Além disso, foi criado um modelo de baseline (Average) para efeito de comparação. A performance dos modelos foi avaliada por meio de métricas como MAE, MAPE e RMSE, tanto para os modelos simples quanto para os modelos com cross-validation.

  O XGBoost foi o modelo escolhido para ser utilizado, devido à sua capacidade de lidar com dados complexos e heterogêneos, apesar de ter apresentado uma performance ligeiramente inferior à Random Forest. No entanto, considerou-se que a escolha do XGBoost foi a mais adequada para este projeto devido à sua exigência de processamento mais baixa em comparação com a Random Forest.


- **Passo 08:** Ajuste de hiperparâmetros: Foi realizada uma busca de hiperparâmetros para encontrar os melhores valores para cada parâmetro do modelo XGBoost, utilizando a técnica Random Search. O MAX_EVAL utilizado foi de 5, o que significa que o algoritmo foi executado em 5 conjuntos diferentes de valores de hiperparâmetros para encontrar a combinação ideal. Além disso, foram avaliados diversos parâmetros, como número de árvores, profundidade máxima da árvore, taxa de aprendizado entre outros. O objetivo foi obter o melhor desempenho possível do modelo. Após o ajuste de hiperparâmetros, o modelo final foi avaliado e comparado com os demais modelos testados anteriormente, utilizando métricas como MAE, MAPE e RMSE.


- **Passo 09:** Avaliação e interpretação de erros: Nesta etapa, foi realizada a avaliação do desempenho do modelo de Machine Learning, convertendo os resultados em métricas de negócio para avaliar sua eficácia na previsão das vendas por loja. Foram calculados indicadores como o erro absoluto médio (MAE) e o erro percentual absoluto médio (MAPE), além das prvisões de melhor e pior cenários. Além disso, foram gerados gráficos e visualizações para uma melhor interpretação dos erros e identificação de possíveis melhorias na performance do modelo.

- **Passo 10:** Implantação do modelo em produção:  O modelo selecionado foi publicado em um ambiente de nuvem para que outras pessoas ou serviços possam usar os resultados para melhorar a decisão de negócios. Além disso, um bot Telegram foi criado para fornecer acesso aos resultados do modelo em tempo real.


## 4. Coleta de dados

O conjunto de dados utilizado neste projeto foi obtido do Kaggle, que pode ser encontrado [aqui](https://www.kaggle.com/competitions/rossmann-store-sales) e compreende informações de vendas de 1.115 lojas Rossmann. É importante ressaltar que algumas lojas no conjunto de dados estavam temporariamente fechadas para reforma. 

O conjunto de dados contém 19 atributos, conforme listados abaixo:

| Atributo | Descrição |
|--|--|
|id  | identificador que representa um par (Store, Date) dentro do conjunto de testes  |
|store| identificador exclusivo para cada loja |
|day_of_week| dia da semana |
|date| data |
|sales| a receita para um determinado dia (isto é o que estamos prevendo) |
|customers| o número de clientes em um determinado dia |
|open| m indicador se a loja estava aberta: 0 = fechado, 1 = aberto |
|promo| indica se a loja está executando uma promoção naquele dia |
|state_holiday| indica um feriado estadual. Normalmente, todas as lojas, com poucas exceções, estão fechadas nos feriados estaduais. Observe que todas as escolas estão fechadas em feriados públicos e fins de semana. a = feriado público, b = feriado de Páscoa, c = Natal, 0 = Nenhum  |
|school_holiday| indica se (Store, Date) foi afetada pelo fechamento de escolas públicas  |
|store_type| diferencia entre 4 modelos de lojas diferentes: a, b, c, d  |
|assortment| descreve um nível de sortimento: a = básico, b = extra, c = estendido |
|competition_distance| distância em metros até a loja concorrente mais próxima |
|competition_open_since_month| dá o mês aproximado do tempo em que o concorrente mais próximo foi aberto|
|competition_open_since_year|dá o ano aproximado do tempo em que o concorrente mais próximo foi aberto  |
|promo2| é uma promoção contínua e consecutiva para algumas lojas: 0 = loja não está participando, 1 = loja está participando |
|promo2_since_week| descreve a semana do calendário em que a loja começou a participar da Promo2 |
|promo2_since_year|descreve o ano  em que a loja começou a participar da Promo2  |
|promo_interval| descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é iniciada novamente. Por exemplo, "Fev, Mai, Ago, Nov" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para essa loja. |

OBS:

 - Todas as linhas que não possuem a 'competition_distance' também não possuem a informação de 'competition_since_month/year'. 
 - Foi criada a coluna 'is_promo' para indicar se o dia está em promoção ou não.
 
 
##  5. Top 5 Insights de dados

### 5.1. Mapa mental de hipóteses 
Em conjunto com a equipa de negócios (marketing, vendas e produto), foi elaborado um mapa mental de hipóteses para identificar possíveis soluções para o problema em questão. Essa etapa é fundamental para buscar insights relevantes que possam auxiliar na busca pela melhor solução.


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/mind_map.png" alt="Ciclo do CRISP" width="800" height="500">
</p>


### 5.2. Insights
Das hipóteses levantadas, somente as que possuíam dados disponíveis foram consideradas. Hipóteses que envolviam informações sobre clientes ou localização não foram incluídas na análise. 

Através da análise de 12 hipóteses, foram identificados cinco insights importantes, que foram validados por meio de gráficos. Esses gráficos fornecem evidências concretas para embasar as conclusões obtidas na análise.

Os cinco insights identificados são:

**Insight 01 - Lojas próximas aos seus concorrentes têm um volume de vendas mais elevado.**

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/insight01.png" alt="Insight 01">
</p>


**Insight 02 - Lojas com concorrentes de longa data tendem a vender menos.**

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/insight02.png" alt="Insight 02">
</p>

**Insight 03 - Lojas que realizam promoções prolongadas têm um volume de vendas inferior.**

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/insight03.png" alt="Insight 03">
</p>

**Insight 04 - As lojas apresentam uma tendência de redução nas vendas anuais. Em 2014, o volume de vendas foi inferior ao registrado em 2013 e, até o momento, os dados preliminares indicam que o desempenho de vendas em 2015 é ainda menor. É importante destacar que os dados de 2015 ainda não estão completos, o que pode impactar nas conclusões finais.**


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/insight04.png" alt="Insight 04">
</p>

**Insight 05 - As lojas apresentam uma redução no volume de vendas no segundo semestre do ano, em comparação com o primeiro semestre, o que pode estar relacionado a fatores sazonais ou à diminuição geral do consumo nesse período.**


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/insight05.png" alt="Insight 05">
</p>

## 6. Modelo de Machine Learning aplicado

Após a codificação e transformação dos dados, aplicou-se o método Boruta para selecionar as variáveis mais relevantes para o modelo. Com base nos resultados obtidos, as seguintes variáveis foram selecionadas:

['store', 'promo', 'store_type', 'assortment', 'competition_distance', 'competition_open_since_month', 'competition_open_since_year', 'promo2', 'promo2_since_week', 'promo2_since_year', 'competition_time_month', 'promo_time_week', 'day_of_week_sin', 'day_of_week_cos', 'month_cos', 'day_sin', 'day_cos', 'week_of_year_cos']

Além disso, incluímos as variáveis 'month_sin' e 'week_of_year_sin', uma vez que estão relacionadas às suas respectivas variáveis cosseno. 

Para avaliar o desempenho dos modelos, foram testados cinco algoritmos: 

 - Average
 - Linear Regression
 - Lasso
 - Random Forest 
 - XGBoost
 
O modelo de Average foi utilizado como baseline para avaliar o desempenho dos outros modelos. Essa abordagem permitiu verificar se os resultados obtidos pelos demais modelos foram superiores ou inferiores ao resultado esperado com base na média.

Para avaliar o desempenho real dos modelos, foi adotado o método de cross validation. Devido à natureza do problema, que se baseia em séries temporais, não foi possível separar aleatoriamente as partes de treinamento e validação. Por isso, foram reservadas as seis últimas semanas de dados exclusivamente para teste, enquanto o restante dos dados foi utilizado na cross validation. O parâmetro K define o número de segmentos em que os dados de cross validation são divididos. É importante ressaltar que, ao aumentar o valor de K, mais semanas de dados são incluídas no treinamento e novas seis semanas são adicionadas à validação.


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/cross_validation.jpg" alt="Cross-validation">
</p> 


Os resultados da cross validation permitiram avaliar o desempenho real do modelo, que pode ser observado a seguir:


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/cross-validadion-comparacao.png" alt="Cross-validation comparacao">
</p>


Foi observado que o Modelo Average apresentou um desempenho superior aos modelos lineares, indicando que o fenômeno estudado é complexo e pode envolver padrões não-lineares e comportamentos sazonais e temporais difíceis de serem capturados por modelos lineares.

Em relação aos modelos baseados em árvores, o desempenho do Random Forest foi ligeiramente superior ao do XGBoost Regressor, mas optou-se por utilizar o XGBoost como modelo final. A justificativa para essa escolha foi que o modelo gerado pelo Random Forest era consideravelmente maior, o que poderia comprometer o desempenho em termos de uso de memória e processamento. Além disso, o ganho no desempenho com o Random Forest foi considerado insuficiente para justificar um aumento significativo no uso de recursos computacionais.

## 7. Performance do Modelo

Para realizar o fine tunning do modelo, escolhemos a técnica Random Search por ser eficiente em encontrar uma boa combinação de hiperparâmetros em um curto período de tempo. Essa abordagem foi selecionada porque seguimos a metodologia CRISP e nosso objetivo era entregar uma primeira versão da solução o mais rapidamente possível.

Após cinco iterações de busca aleatória, selecionamos o conjunto de parâmetros que apresentou o melhor desempenho em relação às métricas de avaliação para ser o modelo final. Esse processo permitiu obter um modelo com alto desempenho e boa generalização, além de explorar um espaço amplo e heterogêneo de hiperparâmetros.

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/param-tunned.png" alt="param tunned">
</p>


Em seguida, treinamos novamente o modelo com cross validation para obter seu desempenho final. O modelo foi salvo no formato pickle para ser implantado em produção posteriormente.

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/xgboost-pos-param-tunned.png" alt="param tunned XGBoost">
</p>


Para avaliar a performance do modelo de Machine Learning, criamos as colunas 'error', que determinam a diferença entre as vendas reais e as vendas previstas, e 'error_rate', que representa a taxa de erro nas vendas previstas em relação às vendas reais. Geramos um gráfico de dispersão para analisar mais detalhadamente os erros do modelo, como mostra a figura abaixo. Nesse gráfico, as vendas previstas estão no eixo x e a diferença entre as vendas previstas e as vendas reais (ou seja, o erro) está no eixo y. Assim, é possível observar se há algum padrão nos erros do modelo, como uma subestimação ou superestimação constante.

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/predictions-dispersion.png" alt="dispesao predicao">
</p>

Dessa forma, a avaliação dos resultados permitiu interpretar os erros e identificar possíveis melhorias em sua performance.



## 8. Resultados de Negócios

O desempenho do modelo de previsão de vendas da Rossmann foi avaliado utilizando métricas importantes como MAE (Erro Absoluto Médio) e MAPE (Erro Percentual Absoluto Médio). O MAE mede a diferença absoluta entre as previsões e os valores reais, enquanto o MAPE calcula a média das diferenças percentuais absolutas entre as previsões e os valores reais. Essas métricas fornecem uma compreensão mais completa do desempenho do modelo em diferentes perspectivas e ajudam a tomar decisões estratégicas para o negócio.

Para gerar informações precisas sobre o desempenho do modelo, um arquivo CSV foi criado contendo as previsões de vendas para cada loja, bem como os valores de melhor e pior cenário, MAE e MAPE. Esses dados foram calculados com base no desempenho do modelo treinado e permitem uma avaliação mais precisa do seu desempenho em diferentes perspectivas. Com essas informações, os responsáveis pelas decisões estratégicas podem tomar decisões mais informadas e embasadas, garantindo uma gestão mais eficiente e assertiva do negócio. Abaixo segue a imagem com algumas previsões, melhor e pior cenário:

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/prediction-table-all-stores.png" alt="all-stores-prediction">
</p>


A tabela completa em CSV com todas as previsões ser acessada [clicando aqui](https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/all_predictions.csv)



O gráfico abaixo apresenta a relação entre as vendas reais e as vendas previstas para cada loja.

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/realSales-prectionSales.png" alt="vendas/predicao">
</p>

O gráfico de dispersão apresenta como os valores de MAPE variam em relação a cada loja, destacando a relação entre as lojas e o MAPE. Essa informação é valiosa para identificar possíveis padrões ou tendências entre as lojas e o erro relativo do modelo.


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/dispersion-MAPE-stores.png" alt="MAPE lojas">
</p>


Para a avaliação da performance total, foram criadas três features: 'predictions', 'worst_scenario' e 'best_scenario'. A figura abaixo apresenta os valores totais obtidos.

<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/total-predictions-worts-best.png" alt="all predictions">
</p>



A análise dos resultados do modelo de previsão de vendas revelou que a implementação do modelo XGBoost gerou um aumento significativo nas vendas previstas em comparação com o modelo de referência (Baseline Model). Conforme demonstrado na tabela abaixo, o modelo XGBoost previu vendas totais de US$ 286.922.284,67, enquanto o modelo de referência previu vendas de US$ 276.978.801,43. Isso representa uma diferença de US$ 9.943.482,57 nas vendas previstas.

Além disso, comparando o modelo XGBoost com o modelo médio (Average Model), o modelo XGBoost também apresentou um desempenho superior, com uma diferença de US$ 2.649.466,00 nas vendas previstas. Isso demonstra a capacidade do modelo XGBoost em capturar as complexidades e nuances dos dados de vendas da Rossmann para fazer previsões mais precisas e úteis para a empresa.

A tabela abaixo resume os valores de vendas previstos pelos modelos e as vendas reais. Os valores da diferença entre as vendas dos modelos e as vendas reais para o modelo de referência e o modelo XGBoost também estão incluídos.


|            | Modelo de Referência | XGBoost Model   | Vendas Reais    |
|------------|----------------------|----------------|----------------|
| Total de vendas | $276,978,801.43     | $286,922,284.67 | $289,571,750.00 |
| Diferença entre as vendas do modelo | +$12,592,948.57 | +$2,649,466.00 | -               |


## 9. Deployment

Após a validação do modelo de previsão de vendas para a rede de lojas Rossmann, o próximo passo foi disponibilizá-lo para os usuários finais. Para isso, foi criada uma API usando o módulo Flask chamada 'handler.py', que permite aos usuários obter previsões de vendas precisas e atualizadas diariamente.

A API carrega o modelo de previsão de vendas treinado e a classe Rossmann, que é responsável por preparar e transformar os dados necessários para realizar as previsões de vendas. A arquitetura de implantação utilizada é ilustrada na figura abaixo.


<p align="center">
  <img src="https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/arquitetura-do-sistema.jpg" alt="arquitetura do sistema" width="80%">
</p>



Foi realizado o deploy do modelo de previsão de vendas na nuvem através da plataforma Render, o que permitiu a disponibilização das previsões através de uma API criada com o Flask e integrada ao modelo. Em seguida, desenvolveu-se um bot no Telegram que está integrado ao modelo previamente construído, garantindo que as previsões sejam atualizadas diariamente.

Com essa solução, o CFO pode acessar informações precisas sobre as vendas de qualquer loja a qualquer momento, de forma rápida e fácil, através do aplicativo Telegram. Isso agiliza o processo de tomada de decisão e torna a gestão de vendas mais eficiente e assertiva. Veja o funcionamento na demonstração abaixo:

![gif bot](https://github.com/raquelEllem/rossmann_store_sales/blob/main/rossmann_store_sales/img/gif-telegram.gif) 



## 10. Conclusão

Com base nos resultados deste projeto, conclui-se que o modelo treinado é uma ferramenta altamente precisa e confiável para prever as vendas diárias nas lojas Rossmann. Desenvolvido a partir da observação do fenômeno temporal e adaptado para o algoritmo XGBoost, o modelo apresentou um baixo RMSE de 958,72 após cross validation e fine tuning, demonstrando sua eficácia na previsão de vendas.

Além disso, o projeto evidenciou uma economia significativa de US$ 9.943.482,57 reforçando o potencial do modelo treinado como uma ferramenta valiosa para a equipe comercial e financeira da Rossmann.

Outro aspecto relevante é a obtenção de insights valiosos para outras melhorias, como as promoções estendidas, que podem ser aplicados em futuras decisões estratégicas da empresa, gerando melhorias adicionais e economias potenciais. Em resumo, este projeto demonstra como a análise de dados pode oferecer benefícios tangíveis e substanciais para empresas, possibilitando uma tomada de decisão mais eficiente e informada.

## 11. Próximos passos

-   Implementar a separação dos dados de treinamento e teste desde o início do projeto para garantir que não haja vazamento de informações.
-   Pesquisar por dados externos relevantes, como informações sobre o clima, eventos nacionais e indicadores macroeconômicos, para aprimorar a precisão do modelo.
-   Considerar agrupar as lojas por região para facilitar a análise e interpretação dos resultados.
-   Atualizar as informações de 'competition_open_since_year/month' para uma única data por loja, a fim de aprimorar a consistência dos dados.
-   Experimentar o método de pesquisa bayesiana durante o processo de fine tunning para otimizar o desempenho do modelo.
-   Incluir um gráfico diário das previsões no aplicativo Telegram, juntamente com outras informações relevantes. Isso permitirá uma visualização clara e rápida das previsões, facilitando a tomada de decisões pelos usuários do aplicativo.

## 12. Referências

-  Rossman Store Sales, Kaggle competition dataset, https://www.kaggle.com/c/rossmann-store-sales/data, Accessed [15/03/2023].
- Python. Python Software Foundation. https://www.python.org/.
- XGBoost: A Scalable Tree Boosting System. https://xgboost.readthedocs.io/en/latest/.
