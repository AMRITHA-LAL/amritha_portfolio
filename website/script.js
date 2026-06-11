fetch("../projects.json")

.then(
response=>
response.json()
)

.then(
projects=>{

document
.getElementById(
"count"
)

.innerHTML=

`Total Projects:
${projects.length}`;

const container=

document
.getElementById(
"projects-container"
);

container.innerHTML="";

projects.forEach(

project=>{

const card=

document
.createElement(
"div"
);

card.className=

"project-card";

card.innerHTML=`

<h2>
${project.name}
</h2>

<p>

${
project.description
||
"No Description"
}

</p>

<a
href=
"${project.url}"

target=
"_blank"

>

Open Repository

</a>

`;

container
.appendChild(
card
);

}

);

}

);