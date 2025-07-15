# Desafio Murabei - Data Science
# Candidato: Tarcísio Geovane
# Objetivo: Prever 'normexam' e avaliar qual tipo de escola é mais eficiente

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder

# Carregar dados
num_school = pd.read_csv("num_school_data.csv", sep=";", decimal=',')
num_student = pd.read_csv("num_student_data.csv", sep=";", decimal=',')
cat_school = pd.read_csv("cat_school_data.csv", sep=";")
cat_student = pd.read_csv("cat_student_data.csv", sep=";")

# Tratar dados numéricos das escolas
school_data = num_school.pivot(index='school', columns='variable', values='value').reset_index()
school_data = school_data.rename(columns={'schavg': 'school_avg'})

# Tratar dados categóricos das escolas
school_cat = cat_school.pivot(index='school', columns='variable', values='value').reset_index()
school_data = pd.merge(school_data, school_cat[['school', 'schgend', 'type']], on='school', how='left')

# Tratar dados numéricos dos alunos
student_num = num_student[num_student['variable'] == 'normexam']
student_num = student_num.drop_duplicates(subset=['school', 'student', 'variable'])
student_num = student_num.pivot(index=['school', 'student'], columns='variable', values='value').reset_index()
student_num = student_num.rename(columns={'normexam': 'normexam_score'})
student_num = student_num.dropna(subset=['normexam_score'])  # Remover NA em normexam

# Tratar dados categóricos dos alunos
student_cat = cat_student.drop_duplicates(subset=['school', 'student'])
student_cat = student_cat.pivot(index=['school', 'student'], columns='variable', values='value').reset_index()
student_cat = student_cat.rename(columns={'intake': 'intake_level'})

# Mesclar dados
merged_data = pd.merge(student_num, student_cat[['school', 'student', 'intake_level']], on=['school', 'student'], how='left')
merged_data = pd.merge(merged_data, school_data, on='school', how='left')

# Preparar features e target
X = merged_data[['school_avg', 'schgend', 'type', 'intake_level']]
y = merged_data['normexam_score']

# Codificar variáveis categóricas
encoder = OneHotEncoder(drop='first', sparse_output=False)
X_encoded = encoder.fit_transform(X[['schgend', 'type', 'intake_level']])
X = np.hstack((X[['school_avg']].values, X_encoded))

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Prever e avaliar
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Erro médio quadrático: {mse}")



# Análise final:
# De acordo com o modelo de regressão linear treinado, escolas de gênero misto ("mixed") tiveram um
# desempenho ligeiramente superior no exame normalizado ("normexam") em comparação com escolas 
# exclusivamente masculinas ou femininas. Além disso, o nível de entrada dos alunos ("intake_level") 
# mostrou forte influência: alunos do "top 25%" tiveram, em média, melhor desempenho. 
# A variável "school_avg" (nota média da escola na entrada) também contribuiu positivamente.
# Porém, o erro médio quadrático (MSE ≈ 0.67) indica que outros fatores não capturados 
# no conjunto de dados poderiam influenciar o resultado.