@app.route("/delete", methods=["POST"])
def delete():
    p_id = request.form.get('p_id')

    deleteCartItem(p_id)

    return redirect(request.referrer)