#By Lucas Soohoo, Summer 2018
print("Youthful Dream - Article HTML Generator\n")
print("Please enter the following:\n")
print("---------------------------------------\n")
title = input("Enter title:")

year = input("Enter date-year (yy):")
month = input("Enter date-month (MM):")
day = input("Enter date-day (dd):")

htmlName = year + month + day + input("Enter short English name for HTML file:") + ".html"

catg = input("Enter public category name (Ex. Reflections & Journal):")
categHTML = input("Enter category HTML file(without .html):")
articleContent = input("Enter article content including [<br><br>&emsp;&emsp;] :")
articleDesc = input("Enter article description:")

img = "images/" + input("Enter path to image: images/")
imgAlt = input("Enter image description:")
imgURL = input("Enter image URL:")
imgOwner = input("Enter photographer's name:")


newHtmlFile = open(htmlName,"x")
newHtmlFile = open(htmlName,"a")

## Article Code
print("\nArticle HTML file generated under " + htmlName)
newHtmlFile.write("<!DOCTYPE HTML><!--	Binary by TEMPLATED	templated.co @templatedco	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)--><html><head>  <title>    " + title + " - Youthful Dream</title>")
newHtmlFile.write("<meta charset=\"utf-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" /><link rel=\"stylesheet\" href=\"../assets/css/main.css\" /></head><body><!-- Header --><header id=\"header\"><a href=\"../index.html\" class=\"logo\"><strong>Youthful Dream</strong></a><nav><a href=\"#menu\">Menu</a></nav></header><!-- Nav --><nav id=\"menu\"><ul class=\"links\"><li><a href=\"../index.html\">Home</a></li><li><a href=\"../about/about.html\">About</a></li><li><a href=\"../reflectJournal/reflectJournal.html\">Reflections & Journal</a>     </li>      <li><a href=\"../fiction/fiction.html\">Fiction</a>      </li>      <li><a href=\"../poems/poems.html\">Poems</a>      </li>      <li><a href=\"../prose/prose.html\">Prose</a>      </li>      <li><a href=\"../misc/misc.html\">Miscellaneous</a>      </li>    </ul>  </nav>")
newHtmlFile.write("<!-- Main -->  <section id=\"main\">    <div class=\"inner\">      <div class=\"row 50% uniform\">        <div class=\"6u\"><span class=\"image fit\"><img src=\"../" + img + "\" alt=\"" + imgAlt + "\" /></span>        </div>      </div>      <header>        <h1>" + title + "</h1>        <h4>" + month + "." + day + ".20" + year + " &ensp; Filed under: <font color ='#1abc9c'><a href = '" + categHTML + ".html'>" + catg + "</a></font>.</h4>      </header>      <p>        <!--Start Article   <br><br>&emsp;&emsp;   -->             " + articleContent + "      <!--End Article -->      </p>    </div>  </section>")
newHtmlFile.write("<!-- Footer -->  <footer id=\"footer\">    <ul class=\"icons\">      <li><a href=\"https://github.com/YouthfulDream/YouthfulDream.github.io\" class=\"icon fa-github\"><span class=\"label\">GitHub</span></a>      </li>      <li><a href=\"https://www.facebook.com/profile.php?id=100005433241070\" class=\"icon fa-facebook\"><span class=\"label\">Facebook</span></a>      </li>      <li><a href=\"mailto:YouthfulDream18@gmail.com\" class=\"icon fa-envelope\"><span class=\"label\">Email</span></a>      </li>    </ul>    <div class=\"copyright\">      &copy; <a href=\"../about/about.html\">Jie Chen</a>. Webmaster: <a href=\"../about/webmaster.html\">Lucas Soohoo</a>. Design: <a href=\"https://templated.co\">TEMPLATED</a>. <a href=\"../images/imageCredits.html\">Image Credits</a>.    </div>  </footer>  <!-- Scripts -->  <script src=\"../assets/js/jquery.min.js\"></script>  <script src=\"../assets/js/jquery.scrolly.min.js\"></script>  <script src=\"../assets/js/skel.min.js\">")
newHtmlFile.write("</script>  <script scr=\"../assets/js/util.js\"></script>  <script src=\"../assets/js/main.js\"></script></body></html>")

copyHTMLName = "copy-"+htmlName
copyHTML = open(copyHTMLName,"x")
copyHTML = open(copyHTMLName,"a")
copyHTML.write("Copy info for "+htmlName)

## Photographer Credits
print("\nPhotographer credits generated under "+copyHTMLName)
copyHTML.write("Photographer Credits:\n")
copyHTML.write("- " + imgOwner + "\t\t(" + imgURL + ")" + "\t\t" + categHTML + "\\" + htmlName)

## Generate Featured Article content
copyHTML.write("\n'Featured' Article code\n")

numToEng = ["", "one", "two", "three", "four", "five", "menu"]
classes = ["", "post style1", "post invert style1 alt", "post style2", "post invert style2 alt", "post style3", "post invert style3 alt"]
num = int(0)
while num > 5 or num < 1:
  num = int(input("'Featured Article' # to replace:"))
print("\nGenerated 'Feature Article' code")

copyHTML.write("<!-- " + numToEng[num] + " -->")

copyHTML.write("<article id=\"" + numToEng[num] + "\" class=\"" + classes[num] + "\">")
copyHTML.write("  <div class=\"image\">    <img src=\"" + img + "\" alt=\"" + imgAlt + "\" data-position=\"75% center\" />")
copyHTML.write("  </div>  <div class=\"content\">    <div class=\"inner\">      <header>        <h2><a href=\"" + categHTML + "\\" + htmlName + "\">" + title + "</a></h2>")
copyHTML.write("      <p class=\"info\">" + month + "." + day + ".20" + year)
copyHTML.write(" &ensp; Filed under:    <font color='#1abc9c'><a href='" + categHTML + "\\" + categHTML + ".html'>" + catg+"</a></font>.")
copyHTML.write("        </p>      </header>      <p>         <!-- Feature Description goes here -->")
copyHTML.write(articleDesc)
copyHTML.write("              </p>      <ul class=\"actions\"> <li><a href=\"" + categHTML + "\\" + htmlName + "\" class=\"button alt\">Read More</a>        </li>      </ul>    </div>    <div class=\"postnav\">  ")
copyHTML.write("      <a href=\"#" + numToEng[num - 1] + "\" class=\"prev disabled\"><span class=\"icon fa-chevron-up\"></span></a>")
copyHTML.write("      <a href=\"#" + numToEng[num + 1] + "\" class=\"scrolly next\"><span class=\"icon fa-chevron-down\"></span></a>    </div>  </div></article>")


print("Generated code for "+categHTML+".html")
copyHTML.write("\nCode for "+categHTML+".html\n")
copyHTML.write("<tr><td><a href='"+htmlName+"'>"+title+"</a></td>")
copyHTML.write("<td>"+articleDesc+"</td><td>"+ month + "." + day + ".20" + year+"</td></tr>")
