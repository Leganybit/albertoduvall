from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def Firma():
		return render_template("/firma.html")
	@app.route("/carrera")
	def carrera():
		return render_template("/carrera.html")
	@app.route("/criticas")
	def criticas():
		return render_template("/criticas.html")

	@app.route("/realismo")
	def realismo():
		return render_template("/obras/realismo.html")
	@app.route("/realismo_onirico")
	def realismo_onirico():
		return render_template("/obras/realismo_onirico.html")
	@app.route("/suprarealismo")
	def suprarealismo():
		return render_template("/obras/suprarealismo.html")
	@app.route("/retrospectivo")
	def retrospectivo():
		return render_template("/obras/retrospectivo.html")
	@app.route("/retratos")
	def retratos():
		return render_template("/obras/retratos.html")

	@app.route("/contacto")
	def contacto():
		return render_template("/contacto.html")

	return app