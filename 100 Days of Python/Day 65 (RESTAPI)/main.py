import random
from urllib import response
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random_cafe():
    data = db.session.execute(db.select(Cafe))
    all_cafes = data.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(
        Name= random_cafe.name,
        Location_link = random_cafe.map_url,
        Image= random_cafe.img_url,
        Location= random_cafe.location,
        Wall_sockets= random_cafe.has_sockets,
        Toilets = random_cafe.has_toilet,
        Wifi = random_cafe.has_wifi,
        Call = random_cafe.can_take_calls,
        Seats= random_cafe.seats,
        Price = random_cafe.coffee_price,
    )

@app.route("/all", methods=["GET"])
def all_cafe():
    data = db.session.execute(db.select(Cafe))
    all_cafes = data.scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def search_cafe():
    query_location = request.args.get("loc")
    data = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = data.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    
# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_record():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    ) # type: ignore
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added record'})
# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
# HTTP DELETE - Delete Record

@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == 'TopSecretAPIKey':
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key"})

if __name__ == '__main__':
    app.run(debug=True)
