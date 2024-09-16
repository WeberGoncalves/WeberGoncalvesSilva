# Desafio da Sprint 2
## Normalização do Banco de Dados concessionaria 
### **Passo 1: Analisar como a Tabela Atual**
**Havia apenas um tabela com todos os campo ou atributos da entidade tb_locacao**
**Analisando crie as entidades e separei os atributos.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/Edicao_Modelo_Dimensional-00.png)

 ### **Passo 2: Aplicar a 1NF**
 **Procure por dados duplicados ou colunas que não dependem completamente da chave primária.**
 **Criei Tabelas com Valores Atômicos: Certifiquei de que todas as colunas contêm valores únicos e não repetitivos, por isso usei BrModelo e fiz o modelo concetual**
 ![weber](/SPRINTS/SPRINT_2/DESAFIO/img/ModeloConceitual.png)

**Para continuar a analise criei com BrModelo o modelo lógico**
### **Passo 3: Aplicar a 2NF**
**Dividir Tabelas, verifique se tinha colunas que dependem apenas de parte da chave primária, mova-as para uma nova tabela.**
**Criar Relacionamentos: Use chaves estrangeiras para manter a relação entre as tabelas.**
 ![weber](/SPRINTS/SPRINT_2/DESAFIO/img/Modelo_Lógico_relacional.png)

 ### **Passo 4: Aplicar a 3NF**
 **Procurei Eliminai Dependências Transitivas: Se uma coluna não-chave depende de outra coluna não-chave, mova-a para outra tabela.**
**Revisei os Relacionamentos, para Mantenha manter as chaves estrangeiras para garantir a integridade referencial.**
**Transformei o modelo logico em modelo fisico**

![weber](/SPRINTS/SPRINT_2/DESAFIO/img/ModeloFísico1.png)
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/ModeloFísico2.png)

 ### **Usei inialmente DB Browser SQLite para visualiza a tabela original, mas ficou mais facil criar e migrar os dados para tabelas novas usando DBeaver, até para mudar o nome do Banco.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/NovaBD_Relacional_01.png)

**É possivel observa a criaçao das tabelas tb_cliente, tb_carro e tb_combustivel, e comamdo insert or replace into para migar os dados.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/NovaBD_Relacional_02.png)

**Depois exibi as novas tabelas, e também uni as tabelas com Join para realizar teste.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/NovaBD_Relacional_03.png)

## Transformado em modelo Dimensional
### **Foi necessario mudar ou adequadas para análise em um ambiente de data warehouse, sistema de gerenciamento de dados projetado para suportar atividades de business intelligence (BI) e análise avançada, para isso é necessario ter tabelas fato e dimensões.**
**Nesta imagem mostra diagrama onde Tabela de Fatos, que contém medidas quantitativas e chaves estrangeiras. Neste caso, a tabela de fatos pode ser fato_locacao.** 
**Foi criado tabelas de Dimensões,que contêm atributos descritivos. As tabelas de dimensões podem ser dim_vendedor, dim_cliente, dim_carro.**

![weber](/SPRINTS/SPRINT_2/DESAFIO/img/Modelo_Lógico_dimensional.png)

### **Nesta imagem mostra criação física das tabelas fato_locacao e dim_vendedor,e em seguida migrando os dados para novas tabelas, dentro BD já exixtente.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/Edicao_Modelo_Dimensional-01.png)

### **Nesta imagem mostra criação das tabelas dim_cliente e dim_carro, dentro  e migração dos dados para novas tabelas.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/Edicao_Modelo_Dimensional-02.png)


### **Nesta imagem mostra o teste realizado na novas tabelas para ver se estava exibindo os dados inesridos.**
![weber](/SPRINTS/SPRINT_2/DESAFIO/img/Edicao_Modelo_Dimensional-03.png)

### **Nesta imagem mostra a criação das Views, ou visões, são objetos de banco de dados que permitem a apresentação de dados de uma ou mais tabelas de forma virtual. Elas são essencialmente consultas armazenadas que podem ser tratadas como tabelas.** 
### ** View da fato_locacao**

![weber](/SPRINTS/SPRINT_2/DESAFIO/img/VIEW_v_fato_locacao.png)

### ** View da dim_vendedor**

![weber](/SPRINTS/SPRINT_2/DESAFIO/img/VIEW_v_dim_vendedor.png)

### ** View da dim_cliente**

![weber](/SPRINTS/SPRINT_2/DESAFIO/img/VIEW_v_dim_cliente.png)

### ** View da dim_carro**

![weber](/SPRINTS/SPRINT_2/DESAFIO/img/VIEW_v_dim_carro.png)