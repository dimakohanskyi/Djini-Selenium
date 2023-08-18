<h3>------------------------Description---------------------</h3>
<p>Using the modules which I described below,<br>
I created a program that will help to get the<br>
current information on the labor market for QA specialists.<br>
And sends the edited version to the email</p>
<br>


<h3>This project can help you to get current information:</h3>
<ul>
    <li>How many offers have been placed on Djini this week</li>
    <li>How many applicants on one position</li> 
    <li>How many candidates with QA qualification</li>
    <li>General salary statistics (Djini, Dou)</li>
    <li>Link in this project</li> 
</ul>

<br>
<h3>In this project I used such libraries as:</h3>
<ul>
    <li>Time</li> 
    <li>Selenium</li>
    <li>Web.driver</li>
    <li>SmtpLib</li>
    <li>dotenv</li>
    <li>os</li>
</ul>
<br>

<h3>The difficulties I faced:</h3>
<ul>
<li>I do not yet have good knowledge of the Selenium library and 
use one of the many methods of parsing the site, namely by XPATH</li>

<li>I faced into the problem of changing the value of progress-bar
which resulted in inaccurate salary data from the site dou.ua</li>

<li>The next problem is that I don't understand how you can pull,
for example, the entire list of vacancies, etc</li>
</ul>



<h3>Changes:</h3>
In the last version my script couldn't save any data from Djinni and Dou.<br>
So I changed this and now it supports sqlite3.<br> Each time when I run my code, all salary statistics
save in tables. I created 4 tables which consist salary statistics:
<ul>

<li>salary_qa_djinni</li>
<li>salary_qa_dou</li>
<li>salary_python_djinni</li>
<li>salary_python_dou</li>

</ul>
Also I add function which send email (with salary statistics) each Monday.



