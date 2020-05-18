from flask import Flask, render_template, request
from main import get_ethnicities, read_into_data_structure, get_cities, get_indicator_disease, create_plot

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    This function generates
    the index default page.
    """
    data = read_into_data_structure()
    disease_list = get_indicator_disease(data)
    city_list = get_cities(data)
    ethnicities_list = get_ethnicities(data)
    return render_template('index.html', disease_list=disease_list, city_list=city_list,
                           ethnicities_list=ethnicities_list, graph=0)


@app.route("/indicator", methods=["GET", "POST"])
def need_input():
    if request.method == "POST":
        dis1 = request.form['disease1'][2:-2].split("', '")
        indicator1, disease1 = dis1[0], dis1[1]
        dis2 = request.form['disease2'][2:-2].split("', '")
        indicator2, disease2 = dis2[0], dis2[1]
        city1 = request.form['city1']
        city2 = request.form['city2']
        gender1 = request.form['gender1']
        gender2 = request.form['gender2']
        ethnicity1 = request.form['ethnicity1']
        ethnicity2 = request.form['ethnicity2']
        print(disease1, disease2)
        records = [(indicator1, disease1, city1, gender1, ethnicity1),
                   (indicator2, disease2, city2, gender2, ethnicity2)]
        data = read_into_data_structure()
        filename = create_plot(data, records)
        if filename is None:
            print("no data")
            return render_template('failure.html')
        disease_list = get_indicator_disease(data)
        city_list = get_cities(data)
        ethnicities_list = get_ethnicities(data)
        graph = filename
        return render_template('index.html', disease_list=disease_list, city_list=city_list,
                               ethnicities_list=ethnicities_list, graph=graph,
                               disease1=disease1, disease2=disease2,
                               city1=city1, city2=city2,
                               gender2=gender2, gender1=gender1,
                               ethnicity1=ethnicity1, ethnicity2=ethnicity2)


if __name__ == "__main__":
    app.run(debug=True)
