app = app
from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Necklace", "price": "150 EGP", "image": "necklace.jpeg"},
    {"id": 2, "name": "Bracelet", "price": "100 EGP", "image": "bracelet.jpeg"},
    {"id": 3, "name": "Ring", "price": "100 EGP", "image": "ring.jpeg"},
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/checkout/<int:product_id>")
def checkout(product_id):
    # بيجيب المنتج اللي العميل اختاره بناء على الـ ID
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template("checkout.html", product=product)

@app.route("/confirm_order", methods=["POST"])
def confirm_order():
    # هنا بنستلم البيانات اللي العميل كتبها
    name = request.form.get("customer_name")
    address = request.form.get("address")
    phone = request.form.get("phone")
    product_name = request.form.get("product_name")
    
    # حالياً هنعرض رسالة نجاح، والخطوة الجاية هنخليها توصلك إيميل
    return f"<h3>شكراً يا {name}! طلبك لـ ({product_name}) وصل، وهنتصل بيك على رقم {phone} لتأكيد التوصيل لعنوانك: {address}.</h3>"

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0') # عشان يفتح من الموبايل
