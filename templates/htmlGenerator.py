#Generate HTML code for https://youthfuldream.github.io/
    #By Lucas Soohoo, Summer 2018
    #Last updated: 2019/01/08

print("\nYouthful Dream - HTML Generator")
print("Please enter the following:")
print("---------------------------------------")

title = input("Enter title:")

#Date
year = input("Enter date-year (yy):20")
month = input("Enter date-month (MM):")
day = input("Enter date-day (dd):")

#generate .html filename
htmlName = year + month + day + input("Enter short English name for HTML file (*****.html):") + ".html"

#category name (Chinese), folder name (English)
englishList=["reflectJournal","fiction","poems","prose","misc"]
chineseList=["反思&日志","小说","诗歌","散文","网络管理员"]
print("1:reflectJournal "+chineseList[0])
print("2:fiction "+chineseList[1])
print("3:poems "+chineseList[2])
print("4:prose "+chineseList[3])
print("5:misc "+chineseList[4])
list=99
while list>4 or list <0:
  list=int(input("Choose from list: type a number #1-5:"))-1
categHTML = englishList[list]
catg = chineseList[list]
print("\ncategHTML:"+categHTML)
print("catg:"+catg)

#article description/content placeholder
articleContent = "\nARTICLE_CONTENT\n"
print("Placeholder for article content (including <br><br>&emsp;&emsp;) will be marked as \"ARTICLE_CONTENT.\"")
articleDesc = input("\nEnter article description:")

#image information
    #determine the images folder name
imagesFolders=["imgReflectJournal","imgFiction","imgPoems","imgProse","imgMisc"]
imgFolderName = imagesFolders[list]

img ="images/"+ imgFolderName+ "/"+ input("Enter image file name with extension, no path (images/"+imgFolderName+ "/   *****.xxx   ):")
imgAlt = input("Enter image description:")
imgURL = input("Enter image URL:")
imgOwner = input("Enter photographer's name:")

# article html writer
#newFileLocation="../"+categHTML+"/"+htmlName
newFileLocation=htmlName;
newHtmlFile = open(newFileLocation,"x")
newHtmlFile = open(newFileLocation,"a")

# Article Code
print("Article HTML file generated under '" + htmlName + "'")
newHtmlFile.write("<!DOCTYPE HTML><!--	Binary by TEMPLATED	templated.co @templatedco	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)--><html><head>  <title>    " + title + " - 青春逐梦</title>")
newHtmlFile.write("<meta charset=\"utf-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" /><link rel=\"stylesheet\" href=\"../assets/css/main.css\" /></head><body><!-- Header --><header id=\"header\"><a href=\"../index.html\" class=\"logo\"><strong>青春逐梦</strong></a><nav><a href=\"#menu\">菜单</a></nav></header>")
newHtmlFile.write("<!-- Nav --><nav id=\"menu\">    <ul class=\"links\">      <li><a href=\"../index.html\">主页</a>      </li>      <li><a href=\"../about/about.html\">关于</a>      </li>      <li><a href=\"../reflectJournal/reflectJournal.html\">反思&日志</a>      </li>      <li><a href=\"../fiction/fiction.html\">小说</a>      </li>      <li><a href=\"../poems/poems.html\">诗歌</a>      </li>      <li><a href=\"../prose/prose.html\">散文</a>      </li>      <li><a href=\"../misc/misc.html\">网络管理员</a>      </li>    </ul>  </nav>")

newHtmlFile.write("<!-- Main -->  <section id=\"main\">    <div class=\"inner\">      <div class=\"row 50% uniform\">        <div class=\"6u\"><span class=\"image fit\"><img src=\"../" + img + "\" alt=\"" + imgAlt + "\" /></span>        </div>      </div>      <header>        <h1>" + title + "</h1>        <h4>" + month + "." + day + ".20" + year + " &ensp; 种类: <font color ='#1abc9c'><a href = '" + categHTML + ".html'>" + catg + "</a></font>.</h4>      </header>      <p>        <!--Start Article   <br><br>&emsp;&emsp;   -->             " + articleContent + "      <!--End Article -->      </p>    </div>  </section>")

newHtmlFile.write("<!-- Footer --><footer id=\"footer\">  <ul class=\"icons\">    <li><a href=\"https://github.com/YouthfulDream/YouthfulDream.github.io\" class=\"icon fa-github\"><span class=\"label\">GitHub</span></a>    </li>    <li><a href=\"https://www.facebook.com/profile.php?id=100005433241070\" class=\"icon fa-facebook\"><span class=\"label\">Facebook</span></a>    </li>    <li><a href=\"mailto:YouthfulDream18@gmail.com\" class=\"icon fa-envelope\"><span class=\"label\">Email</span></a>    </li>  </ul> <div class=\"copyright\">    &copy; <a href=\"/about/about.html\">陈杰</a>. 网络管理员: <a href=\"/about/webmaster.html\">Lucas Soohoo</a>. 设计: <a href=\"https://templated.co\">TEMPLATED</a>. <a href=\"/images/imageCredits.html\">图片来源</a>.  </div></footer>")

newHtmlFile.write("  <!-- Scripts -->  <script src=\"../assets/js/jquery.min.js\"></script>")
newHtmlFile.write("  <script src=\"../assets/js/jquery.scrolly.min.js\"></script>")
newHtmlFile.write("  <script src=\"../assets/js/skel.min.js\"></script>")
newHtmlFile.write("  <script src=\"../assets/js/util.js\"></script>")
newHtmlFile.write("  <script src=\"../assets/js/main.js\"></script>")
newHtmlFile.write("</body></html>")

#extraCode (copy and paste into index, image Credits) writer
copyHTMLName = "extraCode-"+htmlName
copyHTML = open(copyHTMLName,"x")
copyHTML = open(copyHTMLName,"a")
copyHTML.write("Extra HTML Code for:\t"+htmlName)
copyHTML.write("\n====================\n")


## Photographer Credits
print("\nPhotographer credits generated under "+copyHTMLName +"\n")
copyHTML.write("\n\nPhotographer Credits:\n\t\t/images/imageCredits.html\n--------------------\n")
copyHTML.write("<tr><td><a href =\""+imgURL+"\">"+imgOwner+"</a></td>")
copyHTML.write("<td><a href =\"../"+categHTML+"/"+htmlName+"\">"+title+"</a></td></tr>")

## Generate 'Featured Article' content
copyHTML.write("\n\n\n'Featured Article' code:\n\t\t/index.html\n")

#determine "Featured Article" number
numToEng = ["one", "two", "three", "four", "five", "six"]
classes = ["post style1", "post invert style1 alt", "post style2", "post invert style2 alt", "post style3", "post invert style3 alt"]
num = int(99)
while num > 6 or num < 1:
    #want 1-6 inclusive
    num = int(input("'Featured Article' # to replace (which is at the bottom)(int#1-6):"))

num -= 1
    #convert so 'num' can point to an index

#'previous' index
numMinusOne = num-1
if numMinusOne==-1:
    numMinusOne=5

#'next' index
numPlusOne = (num + 1)%6

#extra Code writer
print("\nGenerated 'Feature Article' code")
copyHTML.write("\tDelete the '" + numToEng[num]+ "' block from the bottom of index.html and paste the following after 'Begin Featured'\n")
copyHTML.write("\tDisable/Enable button: 'prev disabled' <==> 'scrolly prev'\n--------------------\n")
copyHTML.write("Don't forget to update the green button to go to the first article'\n--------------------\n")



copyHTML.write("<!-- Start " + numToEng[num] + " -->")

copyHTML.write("<article id=\"" + numToEng[num] + "\" class=\"" + classes[num] + "\">")
copyHTML.write("  <div class=\"image\">    <img src=\"" + img + "\" alt=\"" + imgAlt + "\" data-position=\"75% center\" />")
copyHTML.write("  </div>  <div class=\"content\">    <div class=\"inner\">      <header>        <h2><a href=\"" + categHTML + "\\" + htmlName + "\">" + title + "</a></h2>")
copyHTML.write("      <p class=\"info\">" + month + "." + day + ".20" + year)
copyHTML.write(" &ensp; 种类:    <font color='#1abc9c'><a href='" + categHTML + "\\" + categHTML + ".html'>" + catg+"</a></font>.")
copyHTML.write("        </p>      </header>      <p>         <!-- Feature Description goes here -->")
copyHTML.write(articleDesc)
copyHTML.write("              </p>      <ul class=\"actions\"> <li><a href=\"" + categHTML + "\\" + htmlName + "\" class=\"button alt\">阅读更多</a>        </li>      </ul>    </div>    <div class=\"postnav\">  ")
copyHTML.write("      <a href=\"#" + numToEng[numMinusOne] + "\" class=\"prev disabled\"><span class=\"icon fa-chevron-up\"></span></a>")
copyHTML.write("      <a href=\"#" + numToEng[numPlusOne] + "\" class=\"scrolly next\"><span class=\"icon fa-chevron-down\"></span></a>    </div>  </div></article>")
copyHTML.write("<!-- End " + numToEng[num] + " -->")

print("Generated code for "+categHTML+".html")
copyHTML.write("\n\n\nCategory Homepage code:\n\t\t"+categHTML+"\\"+categHTML+".html\n--------------------\n")

copyHTML.write("<tr><td><a href='"+htmlName+"'>"+title+"</a></td>")
copyHTML.write("<td>"+articleDesc+"</td><td>"+ month + "." + day + ".20" + year+"</td></tr>")

copyHTML.write("\n\n\n Article Content note:\n\t\t"+categHTML + "\\" + htmlName)
copyHTML.write("\n--------------------\nDon't forget to replace 'ARTICLE_CONTENT' with the actual article.\n<br><br>&emsp;&emsp;")

print("Finished.")
