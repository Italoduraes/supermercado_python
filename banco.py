from flask import Flask, request, render_template
from flaskext.mysql import MySQL

#Instanciando a app
banco = Flask(__name__)

# configurar BD
banco.config['MYSQL_DATABASE_USER'] = 'root'
banco.config['MYSQL_DATABASE_PASSWORD'] = 'root'
banco.config['MYSQL_DATABASE_BD'] = 'banco'

# instanciar BD
mysql = MySQL()
mysql.init_app(banco)

#rota para /
@banco.route('/')
def index():
    return render_template('form_login.html')



# Rota para /login
@banco.route('/login')
# metodo que responde /login
def login():
    #obtendo as parametros do formulario
    cpf_cliente = request.args.get('cpf_cliente')
    senha_cliente = request.args.get('senha_cliente')

    #criar conexao com BD
    cursor = mysql.connect().cursor()
    #submeter o comando SQL
    cursor.execute(f"SELECT nomecliente FROM banco.cliente WHERE cpfcliente ='{cpf_cliente}' AND senhacliente ='{senha_cliente}'")

    # recuperar os dados
    dados = cursor.fetchone()


    # imprimir nome
    return render_template('logado.html', nome_cliente=str(dados[0]))

  #executar
banco.run(debug=True)
