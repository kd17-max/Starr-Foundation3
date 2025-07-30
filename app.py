from flask import Flask, render_template, url_for
from flask_ngrok import run_with_ngrok
import folium

app = Flask(__name__, static_folder='static', template_folder='templates')
run_with_ngrok(app)

app = Flask(__name__, static_folder='static', template_folder='templates')
run_with_ngrok(app)

app = Flask(__name__, static_folder='static', template_folder='templates')

locations = [
{
"name": "Port Richmond Library (75 Bennett St)",
"coords": [40.63757, -74.13101],
"images": ["rl1.png", "rl2.png"],
"summary": "The Starr Foundation played a key role in supporting the renovation of the children’s rooms and early childhood learning spaces at the Richmond Library — creating a more welcoming, educational environment for Staten Island families."
},
{
"name": "Dongan Hills Library (1617 Richmond Rd)",
"coords": [40.59049, -74.10112],
"images": ["dh1.png", "dh2.png", "dh3.png"],
"summary": "The Starr Foundation contributed funding toward the 2008 renovation of the Dongan Hills Library, improving public access and enhancing learning spaces for the local community."
},
{
"name": "Eger Adult Day Program (140 Meisner Ave)",
"coords": [40.57986, -74.12986],
"images": ["ef1.png", "ef2.png"],
"summary": "The Starr Foundation donated $325,000 to the Eger Foundation to support its general management operations, contributing to the continued care and services provided by the organization."
},
{
"name": "St. John Villa Academy (25 Landis Ave)",
"coords": [40.60083, -74.067833],
"images": ["sv1.png", "sv2.png"],
"summary": "A $250,000 gift from the Starr Foundation provided scholarships to St. John Villa Academy, supporting students in their pursuit of education in a nurturing academic environment."
},
{
"name": "Beacon of Hope House (90 Hancock St)",
"coords": [40.58843, -74.09613],
"images": ["hh1.png"],
"summary": "With a $120,000 donation, the Starr Foundation supported Beacon of Hope’s residential facilities for individuals living with mental illness, enhancing the quality of care and supportive services offered."
},
{
"name": "Wagner College (1 Campus Road)",
"coords": [40.615, -74.094],
"images": ["wc1.png"],
"summary": "The Starr Foundation gave $150,000 in scholarships to Wagner College, helping students from diverse backgrounds access higher education and reach their academic goals."
},
{
"name": "Snug Harbor Cultural Center (1000 Richmond Terrace)",
"coords": [40.6438, -74.1025],
"images": ["sh1.png", "sh2.png", "sh3.png"],
"summary": "The Starr Foundation contributed $555,000 toward the creation of the Aileen Pei Memorial and supported the Chinese Scholar’s Garden at Snug Harbor. This donation helped with preserving a beautiful and important cultural landmark and making it more accessible to the public."
},
{
"name": "Staten Island Children’s Museum (Snug Harbor)",
"coords": [40.6438, -74.1025],
"images": ["cm1.png"],
"summary": "With a $274,000 grant from the Starr Foundation, the Staten Island Children’s Museum received essential operating support. This funding helped keep their hands-on exhibits and educational programs accessible to young kids and families on Staten Island."
}

]

@app.route('/')
def index():
    m = folium.Map(location=[40.6, -74.1], zoom_start=12)

    for loc in locations:
        html = f"<h4>{loc['name']}</h4>"
        for img in loc['images']:
            img_url = url_for('static', filename=f'images/{img}', _external=True)
            html += (
                f'<a href="{img_url}" target="_blank" rel="noopener noreferrer">'
                f'<img src="{img_url}" width="200"></a><br>'
            )
        html += f"<p>{loc['summary']}</p>"

        iframe = folium.IFrame(
            html=html,
            width=240,
            height=260 + 100 * len(loc['images'])
        )
        popup = folium.Popup(iframe, max_width=300)
        folium.Marker(location=loc["coords"], popup=popup).add_to(m)

    return render_template("index.html", map_html=m._repr_html_())

if __name__ == '__main__':
    # local debugging
    app.run(debug=True)