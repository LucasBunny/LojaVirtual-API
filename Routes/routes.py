from flask import jsonify, make_response, request


def init_app(app, mycon):
    # Método GET
    @app.route("/api/produtos", methods=["GET"])
    def get_produtos():
        cursor = mycon.cursor()
        cursor.execute("select * from Produtos")
        get_produtos = cursor.fetchall()
        data = []
        for dado in get_produtos:
            data.append(
                {
                    "id": dado[0],
                    "codigoEAN": dado[1],
                    "descricao": dado[2],
                    "valor": dado[3],
                    "dataCadastro": dado[4],
                }
            )
        cursor.close()
        return make_response(jsonify(data))

    # Método GET por ID
    @app.route("/api/produtos/<int:id>", methods=["GET"])
    def get_produtos_id(id):
        cursor = mycon.cursor()
        cursor.execute(f"select * from Produtos where id = {id}")
        get_produtos = cursor.fetchall()
        data = []
        for dado in get_produtos:
            data.append(
                {
                    "id": dado[0],
                    "codigoEAN": dado[1],
                    "descricao": dado[2],
                    "valor": dado[3],
                    "dataCadastro": dado[4],
                }
            )
        cursor.close()
        return make_response(jsonify(data))

    # Método POST
    @app.route("/api/add_produtos", methods=["POST"])
    def post_produtos():
        prod = request.json
        cursor = mycon.cursor()
        sql_query = f"""
                insert into Produtos (codigoEAN, descricao, valor, dataCadastro) 
                values ({prod['codigoEAN']}, '{prod['descricao']}', {prod['valor']}, '{prod['dataCadastro']}');
                    """
        cursor.execute(sql_query)
        mycon.commit()
        cursor.close()
        return make_response(jsonify(prod), 201)

    # Método PUT
    @app.route("/api/update_produtos/<int:id>", methods=["PUT"])
    def atualizar_produtos(id):
        prod = request.json
        cursor = mycon.cursor()
        sql_query = f"""
                    UPDATE Produtos
                    SET codigoEAN = {prod['codigoEAN']}, descricao = "{prod['descricao']}", valor = {prod['valor']}, dataCadastro = "{prod['dataCadastro']}"
                    WHERE id = {id}
                    """
        cursor.execute(sql_query)
        mycon.commit()
        cursor.close()
        return make_response(jsonify(prod))

    # Método DELETE
    @app.route("/api/del_produtos/<int:id>", methods=["DELETE"])
    def excluir_produtos(id):
        cursor = mycon.cursor()
        cursor.execute(f"select * from Produtos where id = {id}")
        get_produtos = cursor.fetchall()
        data = []
        for dado in get_produtos:
            data.append(
                {
                    "id": dado[0],
                    "codigoEAN": dado[1],
                    "descricao": dado[2],
                    "valor": dado[3],
                    "dataCadastro": dado[4],
                }
            )
        cursor.execute(f"delete from Produtos where id = {id}")
        mycon.commit()
        cursor.close()
        return make_response(jsonify(data))
