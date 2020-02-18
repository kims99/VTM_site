from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Flask Server Home Page')

@app.route('/about')
def about():
     return render_template('about.html', pageTitle='About VTM')

@app.route('/kim', methods=['GET', 'POST'])
def kim():
    if request.method == 'POST':
        form = request.form
        radius = float(form['tankRad'])
        height = float(form['tankHt']) 

        print(radius)
        print(height)

        PI = 3.14
        MATERIALCOST = 25
        LABORCOST = 15
        
        topArea = PI * radius**2
        sideArea = (2 * (PI * (radius * height)))
        totalAreaSqFt = (topArea + sideArea)/144 #convert from square inches to square feet
        # print(topArea)
        # print(sideArea)
        # print(totalAreaSqFt)
        
        totalMaterialCost = totalAreaSqFt * MATERIALCOST
        totalLaborCost = totalAreaSqFt * LABORCOST
        # print(totalMaterialCost)
        # print(totalLaborCost)

        totalBidPrice = totalMaterialCost + totalLaborCost
        print(totalBidPrice)

    return render_template('kim.html', pageTitle='Tank Painting Estimate')

if __name__ == '__main__':
    app.run(debug=True)
