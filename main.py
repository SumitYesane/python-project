from flask import Flask, render_template

app = Flask(__name__)
songDetails = """
                        Tere Warga Taan Mainu
			Koyi Dissda Nai
			Main Taan Laya Bada Dil
			Kithe Lagda Nai

			Tere Rang Da Na Mileya
			Sitaara Ve Yaara
			Tere Bin Main Taan Saara
			Berang Sajna

			Maanda Nahi Yeh Dil
			Tere Liye Har Pal
			Teri Khair Mangda Rave

			Tu Jo Naina Ch Pilaya Ae
			Sharaabi Rang Laya
			Tere Ishq Ch Hoya Main
			Malang Sajna

			Teri Doriyan Nu Laike
			Dil Vaade Utte Behke
			Aaj Udd’da Ae Jaise Ki
			Patang Sajna

			Tu Jo Naina Ch Pilaya Ae
			Sharaabi Rang Laya
			Tere Ishq Ch Hoya Main
			Malang Sajna

			Ishq Pardo Se Jaise Ab
			Nikalne Laga Hai
			Yeh Toh Aayega Nazar Sareaam
			Hum Dono Ke Alawa Koyi Aur Nahi Hai
			Ishq Panno Pe Hai Tera Mera Naam

			Lakh Vaari Chhupa Le Chaahe Tu
			Ishq Behka Toh Nahi Chupna
			Ishq Pardo Se Jaise Ab
			Nikalne Laga Hai
			Yeh Toh Aayega Nazar Sareaam

			Tu Jo Naina Ch Pilaya Ae
			Sharaabi Rang Laya
			Tere Ishq Ch Hoya Main
			Malang Sajna

			Teri Doriyan Nu Laike
			Dil Vaade Utte Behke
			Aaj Udd’da Ae Jaise Ki
			Patang Sajna

			Tu Jo Naina Ch Pilaya Ae
			Sharaabi Rang Laya
			Tere Ishq Ch Hoya Main
			Malang Sajna

			Teri Doriyan Nu Laike
			Dil Vaade Utte Behke
			Aaj Udd’da Ae Jaise Ki
			Patang Sajna

			Tere Ishq Ch Hoya Main Malang Sajna"""


@app.route("/")
def hello():
  return render_template('home.html',
                         songs=songDetails,
                         SongName='Malang Sajna')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
