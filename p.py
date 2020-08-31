import nltk
import bs4 as bs
import urllib
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
nltk.downloader.download('vader_lexicon')
# import webbrowser
# new = 2
def cyn(val):
	# mood = input("WELCOME TO MOODY NEWS! \n For ALL NEWS :o Enter A! \n For HAPPY NEWS :) Enter H! \n For SAD NEWS :( Enter S! \n")
	if 1:	
		source = urllib.request.urlopen("https://www.indiatoday.in/top-stories").read()
		soup = bs.BeautifulSoup(source, 'html.parser')
		news = []
		happy_news = []
		sad_news = []
		div = (soup.find_all("div", {"class" : "catagory-listing"}))
		for i in div:
			text0 =[]
			headline = i.find("h2").text
			matter = i.find("p").text
			text0.append(headline)
			text0.append(matter)
			news.append(text0)
		for info in news:
			sentiment_analyse(info, happy_news, sad_news)
		if val == 1:
			return print_happy_news(happy_news)
		if val == 2:
			return print_sad_news(sad_news)
		if val == 3:
			return print_all_news(news)

	

def sentiment_analyse(info, happy_news, sad_news):
	end_news = f"{info[0]} \n {info[1]}" 
	score = SentimentIntensityAnalyzer().polarity_scores(end_news)
	if score['neg'] < score['pos']:
		happy_news.append(info)
	if score['neg'] > score['pos']:
		sad_news.append(info)

def print_happy_news(news):
	file = "templates/h.html"
	l = open(file, "w")
	text = """
	<!DOCTYPE html>
	<html>
	<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	* {
	  box-sizing: border-box;
	}

	/* Add a gray background color with some padding */
	body {
	  font-family: "Trebuchet MS", Helvetica, sans-serif;
	  padding: 20px;
	  background: #f1f1f1;
	}

	/* Header/Blog Title */
	.header {
	  padding: 30px;
	  font-size: 40px;
	  text-align: center;
	  background: white;
	  border-radius: 10px
	}

	/* Create two unequal columns that floats next to each other */
	/* Left column */
	.leftcolumn {   
	  float: left;
	  width: 75%;
	}

	/* Right column */
	.rightcolumn {
	  float: left;
	  width: 25%;
	  padding-left: 20px;
	}

	.footer {
	  /*padding: 10px 10px;*/
	  font-size: 20px;
	  text-align: center;
	  color: #2d7535;
	  /*border-radius: 10px;*/
	  font-style: italic;
	}

	/* Add a card effect for articles */
	.card {
	   background-color: white;
	   padding: 20px;
	   margin-top: 20px;
	   border-radius: 10px
	}

	/* Clear floats after the columns */
	.row:after {
	  content: "";
	  display: table;
	  clear: both;
	}


	/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
	@media screen and (max-width: 800px) {
	  .leftcolumn, .rightcolumn {   
	    width: 100%;
	    padding: 0;
	  }
	}
	</style>
	</head>
	<body>

	<div class="header">
	  <h2>Top Happy Stories :)</h2>
	</div>

	<div class="row">
	</div>
	<div class="card">
	<div class="footer">
		<h>Developed by Sankalp Jaiswal</h>
	</div>
	</div>
	</body>
	</html>

	"""
	hahh = ""
	for info in news:
		content = f"""
		  <div class="card">
			<h2>{info[0]}</h2>
			<p>{info[1]}</p>
		  </div>"""
		hahh += content
	i = (text.find("""<div class="row">"""))
	alls = (str(text[:i + len("""<div class="row">""")]) + str(hahh) + str(text[i + len("""<div class="row">"""):]))
	l.write(alls)
	l.close()
	yes = "h.html"
	return yes
	# return file
	# url = "file:///home/sankalp/p1/h.html"
	# webbrowser.open(url,new=new)
def print_sad_news(news):
	file = "templates/s.html"
	l = open(file, "w")
	text = """
	<!DOCTYPE html>
	<html>
	<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	* {
	  box-sizing: border-box;
	}

	/* Add a gray background color with some padding */
	body {
	  font-family: "Trebuchet MS", Helvetica, sans-serif;
	  padding: 20px;
	  background: #f1f1f1;
	}
	.footer {
	  /*padding: 10px 10px;*/
	  font-size: 20px;
	  text-align: center;
	  color: #2d7535;
	  /*border-radius: 10px;*/
	  font-style: italic;
	}
	/* Header/Blog Title */
	.header {
	  padding: 30px;
	  font-size: 40px;
	  text-align: center;
	  background: white;
	  border-radius: 10px
	}

	/* Create two unequal columns that floats next to each other */
	/* Left column */
	.leftcolumn {   
	  float: left;
	  width: 75%;
	}

	/* Right column */
	.rightcolumn {
	  float: left;
	  width: 25%;
	  padding-left: 20px;
	}



	/* Add a card effect for articles */
	.card {
	   background-color: white;
	   padding: 20px;
	   margin-top: 20px;
	   border-radius: 10px
	}

	/* Clear floats after the columns */
	.row:after {
	  content: "";
	  display: table;
	  clear: both;
	}


	/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
	@media screen and (max-width: 800px) {
	  .leftcolumn, .rightcolumn {   
	    width: 100%;
	    padding: 0;
	  }
	}
	</style>
	</head>
	<body>

	<div class="header">
	  <h2>Top Sad Stories :(</h2>
	</div>

	<div class="row">
	</div>
	<div class="card">
	<div class="footer">
		<h>Developed by Sankalp Jaiswal</h>
	</div>
	</div>
	</body>
	</html>

	"""
	hahh = ""
	for info in news:
		content = f"""
		  <div class="card">
			<h2>{info[0]}</h2>
			<p>{info[1]}</p>
		  </div>"""
		hahh += content
	i = (text.find("""<div class="row">"""))
	alls = (str(text[:i + len("""<div class="row">""")]) + str(hahh) + str(text[i + len("""<div class="row">"""):]))
	l.write(alls)
	l.close()
	yes = "s.html"
	# url = "file:///home/sankalp/p1/"
	# webbrowser.open(url,new=new)
	return yes
def print_all_news(news):
	file = "templates/n.html"
	if 1:
		l = open(file, "w")
		text = """
		<!DOCTYPE html>
		<html>
		<head>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<style>
		* {
		  box-sizing: border-box;
		}

		/* Add a gray background color with some padding */
		body {
		  font-family: "Trebuchet MS", Helvetica, sans-serif;
		  padding: 20px;
		  background: #f1f1f1;
		}
		.footer {
		  /*padding: 10px 10px;*/
		  font-size: 20px;
		  text-align: center;
		  color: #2d7535;
		  /*border-radius: 10px;*/
		  font-style: italic;
		}
		/* Header/Blog Title */
		.header {
		  padding: 30px;
		  font-size: 40px;
		  text-align: center;
		  background: white;
		  border-radius: 10px
		}

		/* Create two unequal columns that floats next to each other */
		/* Left column */
		.leftcolumn {   
		  float: left;
		  width: 75%;
		}

		/* Right column */
		.rightcolumn {
		  float: left;
		  width: 25%;
		  padding-left: 20px;
		}



		/* Add a card effect for articles */
		.card {
		   background-color: white;
		   padding: 20px;
		   margin-top: 20px;
		   border-radius: 10px
		}

		/* Clear floats after the columns */
		.row:after {
		  content: "";
		  display: table;
		  clear: both;
		}


		/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
		@media screen and (max-width: 800px) {
		  .leftcolumn, .rightcolumn {   
		    width: 100%;
		    padding: 0;
		  }
		}
		</style>
		</head>
		<body>

		<div class="header">
		  <h2>All Top Stories :o</h2>
		</div>

		<div class="row">
		</div>
		<div class="card">
		<div class="footer">
			<h>Developed by Sankalp Jaiswal</h>
		</div>
		</div>
		</body>
		</html>

		"""
		hahh = ""
		for info in news:
			content = f"""
			  <div class="card">
				<h2>{info[0]}</h2>
				<p>{info[1]}</p>
			  </div>"""
			hahh += content
		i = (text.find("""<div class="row">"""))
		alls = (str(text[:i + len("""<div class="row">""")]) + str(hahh) + str(text[i + len("""<div class="row">"""):]))
		l.write(alls)
		l.close()
	# url = "file:///home/sankalp/p1/"
	# webbrowser.open(url,new=new)
	yes = "n.html"
	return yes

