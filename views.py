from flask import Blueprint, render_template, request
import forms
views = Blueprint(__name__, "views")

@views.route("/")
#def home():
#    return render_template("index.html")

@views.route('/search', methods=["GET","POST"])
def search():
    search = forms.SearchByAddressForm(request.form)

    if request.method == 'POST':
        address = request.form["addressInput"]
        state = request.form["stateInput"]
        city = request.form["cityInput"]
        zipc = request.form["zipInput"]

        ownerInfo = forms.getOwnerData(address, city, state, zipc)
        priceInfo = forms.getPriceData(address, city, state, zipc)

        return render_template('results.html', form=search, address=address, city=city, state=state, zipC=zipc, ownerInfo=ownerInfo, priceInfo=priceInfo)
    return render_template('index.html', form=search)
