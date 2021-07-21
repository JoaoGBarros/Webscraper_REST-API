from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ModeloLojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    pesquisa = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    classe_conteudo = db.Column(db.String(100), nullable=False)
    tag_conteudo = db.Column(db.String(11), nullable=False)
    classe_titulo = db.Column(db.String(100), nullable=False)
    tag_titulo = db.Column(db.String(11), nullable=False)
    classe_links = db.Column(db.String(100), nullable=False)
    tag_links = db.Column(db.String(11), nullable=False)
    classe_preco = db.Column(db.String(100), nullable=False)
    tag_preco = db.Column(db.String(11), nullable=False)
    classe_frete = db.Column(db.String(100), nullable=False)
    tag_frete = db.Column(db.String(11), nullable=False)
    classe_procura_prox_pag = db.Column(db.String(100), nullable=False)
    tag_procura_prox_pag = db.Column(db.String(11), nullable=False)
    classe_proxima = db.Column(db.String(100), nullable=False)
    tag_proxima = db.Column(db.String(11), nullable=False)
    titulo = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return f"Loja(nome = {nome}, pesquisa = {pesquisa}, link = {link})"


lojas_put_args = reqparse.RequestParser()
lojas_put_args.add_argument("nome", type=str, help="Nome da loja", required=True)
lojas_put_args.add_argument("pesquisa", type=str, help="Classe da barra de pesquisa", required=True)
lojas_put_args.add_argument("link", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_conteudo", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_conteudo", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_titulo", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_titulo", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_links", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_links", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_preco", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_preco", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_frete", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_frete", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_procura_prox_pag", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_procura_prox_pag", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("classe_proxima", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("tag_proxima", type=str, help="Link da loja", required=True)
lojas_put_args.add_argument("titulo", type=str, help="Link da loja", required=True)

db.create_all()

resource_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'pesquisa': fields.String,
    'link': fields.String,
    'classe_conteudo': fields.String,
    'tag_conteudo': fields.String,
    'classe_titulo': fields.String,
    'tag_titulo': fields.String,
    'classe_links': fields.String,
    'tag_links': fields.String,
    'classe_preco': fields.String,
    'tag_preco': fields.String,
    'classe_frete': fields.String,
    'tag_frete': fields.String,
    'classe_procura_prox_pag': fields.String,
    'tag_procura_prox_pag': fields.String,
    'classe_proxima': fields.String,
    'tag_proxima': fields.String,
    'titulo': fields.String
}


class Loja(Resource):
    @marshal_with(resource_fields)
    def get(self, id_loja):
        result = ModeloLojas.query.get(id_loja)
        return result

    @marshal_with(resource_fields)
    def put(self, id_loja):
        args = lojas_put_args.parse_args()
        loja = ModeloLojas(id=id_loja, nome=args['nome'], pesquisa=args['pesquisa'], link=args['link'], classe_conteudo=args['classe_conteudo'], tag_conteudo=args['tag_conteudo'], classe_titulo=args['classe_titulo'], tag_titulo=args['tag_titulo'], classe_links=args['classe_links'], tag_links=args['tag_links'], classe_preco=args['classe_preco'], tag_preco=args['tag_preco'],classe_frete=args['classe_frete'], tag_frete=args['tag_frete'],classe_procura_prox_pag=args['classe_procura_prox_pag'], tag_procura_prox_pag=args['tag_procura_prox_pag'], classe_proxima=args['classe_proxima'], tag_proxima=args['tag_proxima'], titulo=args['titulo'])

        db.session.add(loja)
        db.session.commit()
        return loja, 201

    def delete(self, id_loja):
        result = ModeloLojas.query.get(id_loja)
        db.session.delete(result)
        db.session.commit()


api.add_resource(Loja, "/loja/<int:id_loja>")

def IniciaBD():
    app.run(debug=True)


IniciaBD()