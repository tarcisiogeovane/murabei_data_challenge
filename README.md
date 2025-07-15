
# 📊 Murabei Data Challenge - Previsão de Desempenho Escolar

Este repositório contém a solução para o **Desafio de Data Science da Murabei**, cujo objetivo é prever o desempenho de alunos com base em dados escolares e individuais, e identificar qual tipo de escola é mais eficiente na formação dos estudantes.

---

## 📌 Objetivo

Desenvolver um modelo preditivo que estime a nota final normalizada (`normexam`) dos alunos, utilizando como base:

- Características da escola (tipo, gênero, média)
- Características dos alunos (nível de entrada)

Ao final, o modelo deve permitir responder:  
**"Qual tipo de escola (mista, só para meninos ou só para meninas) é mais eficiente?"**

---

## 🗂️ Estrutura do Projeto

```
.
├── data/
│   ├── cat_school_data.csv
│   ├── cat_student_data.csv
│   ├── num_school_data.csv
│   └── num_student_data.csv
├── tarcisio_murabei_modelagem.py
├── README.md
└── relatorio_word.docx  (opcional)
```

---

## 🧪 Tecnologias e Bibliotecas

- Python 3.8+
- Pandas
- NumPy
- scikit-learn

---

## ⚙️ Como Executar

1. Clone este repositório:

```
git clone https://github.com/seuusuario/murabei-data-challenge.git
cd murabei-data-challenge
```

2. Instale as dependências (recomenda-se ambiente virtual):

```
pip install -r requirements.txt
```

**Ou instale manualmente:**
```
pip install pandas numpy scikit-learn
```

3. Certifique-se de que os arquivos `.csv` estão na pasta `data/`.

4. Execute o script principal:

```
python tarcisio_murabei_modelagem.py
```

---

## 🔍 Resultado

- **Erro Médio Quadrático (MSE):** `0.673`

A performance do modelo foi razoável, considerando as variáveis disponíveis. A maior influência positiva no desempenho do aluno veio de:

- **Escolas de gênero misto**
- **Alunos classificados no top 25% na entrada**
- **Média geral da escola (school_avg)**

---

## 🧠 Conclusão

A análise indica que **escolas mistas** tendem a apresentar melhor desempenho médio no exame normalizado. O **nível de entrada do aluno** também se mostra altamente relevante.  

Apesar disso, o MSE de ~0.67 sugere que o modelo pode ser aprimorado com a inclusão de outras variáveis contextuais e socioeconômicas que não estavam disponíveis nos dados fornecidos.

---

## ✍️ Autor

Desenvolvido por **Tarcísio Geovane**  
Contato: [linkedin.com/in/tarcisio](https://linkedin.com/in/tarcisiogeovanecoding) 

