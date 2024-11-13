from flask import Flask, render_template, jsonify, redirect, request, url_for
from db import connect_database


app = Flask(__name__)


@app.route('/')
def index():
    conn = connect_database()

    try:
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos_db;")
            produtos = cursor.fetchall()

            cursor.close()
            conn.close()

            return render_template("index.html", produtos=produtos)
    except Exception as e:
        return jsonify({"Error": f"Falha ao conectar ao manco de dados erro: {str(e)}"})
    
    
@app.route("/add_produto", methods=["GET", "POST"])
def add_produto():
    conn = connect_database()

    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        codigo_barra = request.form["codigo_barra"]

        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos_db (nome, preco, codigo_barra) VALUES (%s, %s, %s)", (nome, preco, codigo_barra))
        cursor.close()
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add_produto.html")


@app.route("/update_produto/<int:id>", methods=["GET", "POST"])
def update_produto(id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos_db WHERE id = %s", (id,))
    produto = cursor.fetchone()

    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        codigo_barra = request.form["codigo_barra"]

        cursor = conn.cursor()
        cursor.execute("UPDATE produtos_db SET nome = %s, preco = %s, codigo_barra = %s WHERE id = %s", (nome, preco, codigo_barra, id))
        cursor.close()
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("update_produto.html", produto=produto)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos_db WHERE id = %s", (id,))
    cursor.close()
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)